"""Isolated-Chromium checks of the page-side script against simulated Instagram layouts.
Run: python tests/browser_smoke.py   (set CHROMIUM_PATH if Chromium is not found automatically)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,os
ROOT=Path(__file__).resolve().parent.parent
checks=[]
URL='https://www.instagram.com/p/ABC123/'
NAV='<a href="/me/"><img alt="me\'s profile picture"></a>'
POST='<main><article><a href="/alice/">alice</a><section><button id="like"><svg aria-label="Like"></svg></button><button><svg aria-label="Comment"></svg></button></section><div><a href="/bob/">bob</a><span>Hello</span></div></article></main>'
PROFILE='<main><header><h2>alice</h2><button>Follow</button></header><a href="/p/AAA/">p</a><a href="/p/BBB/">p</a></main>'
MOCK='''window.data={job:{id:'test',status:'running'},receipts:{},history:[]};window.listeners=[];window.clicks=0;
window.chrome={runtime:{id:'extension',onMessage:{addListener:f=>listeners.push(f)},sendMessage:async()=>({ok:true}),getURL:p=>'https://fixture.test/'+p},storage:{local:{get:async()=>structuredClone(data),set:async x=>Object.assign(data,structuredClone(x))},onChanged:{addListener:()=>{}}}};
const nativeTimeout=window.setTimeout;window.setTimeout=(f,ms,...args)=>nativeTimeout(f,Math.min(ms,10),...args);
document.addEventListener('click',e=>{if(e.target.closest('main button'))clicks++});'''
with sync_playwright() as p:
 exe=os.environ.get('CHROMIUM_PATH') or next((x for x in ('/usr/bin/chromium','/opt/pw-browsers/chromium') if os.path.exists(x)),None)
 browser=p.chromium.launch(headless=True,args=['--no-sandbox'],**({'executable_path':exe} if exe else {}))
 context=browser.new_context()
 context.route('**/*',lambda r:r.fulfill(status=200,content_type='text/html',body='<html><body></body></html>'))
 page=context.new_page()
 def fixture(body,url=URL,actor=True):
  page.goto(url);page.set_content((NAV if actor else '')+body);page.add_script_tag(content=MOCK)
  for f in ['selectors.js','dom.js','content.js']:page.add_script_tag(path=str(ROOT/f))
 def step(action='like',dry=True,kind='engage',url=URL,**extra):
  c=dict(action=action,dry=dry,mode='posts',exclude=[],maxAge=0,videos=False,scanLimit=2,perUser=2,comment='Nice!');c.update(extra)
  return page.evaluate('''arg=>new Promise(resolve=>listeners[0]({action:'step',step:{kind:arg.kind,url:arg.url,username:'alice'},config:arg.c,jobId:'test'},{id:'extension'},resolve))''',dict(kind=kind,url=url,c=c))
 def check(name,condition):
  assert condition,name;checks.append(name)
 fixture(POST);r=step();check('like preview sends no clicks',r.get('preview') and page.evaluate('clicks')==0)
 fixture(POST);page.evaluate("document.querySelector('#like svg').setAttribute('aria-label','Unlike')");r=step();check('already liked post is skipped',not r.get('preview') and 'already liked' in r.get('message',''))
 fixture(POST);page.evaluate("()=>{const b=document.getElementById('like');b.onclick=()=>b.querySelector('svg').setAttribute('aria-label','Unlike')}");r=step(dry=False);check('live like is clicked once and confirmed',bool(r.get('performed')) and page.evaluate('clicks')==1)
 fixture(POST);r=step(dry=False,exclude=['alice']);check('excluded author is skipped',not r.get('performed') and 'excluded' in r.get('message',''))
 fixture(POST,actor=False);r=step(dry=False);check('live like without a signed-in user fails closed',bool(r.get('error')) and page.evaluate('clicks')==0)
 fixture(PROFILE,'https://www.instagram.com/alice/');r=step(action='follow',kind='account',url='https://www.instagram.com/alice/',mode='users');check('follow preview sends no clicks',r.get('preview') and page.evaluate('clicks')==0)
 for name,body,word in [('private profile','<main><header><h2>alice</h2></header><div>This account is private</div></main>','private'),('profile with no posts','<main><header><h2>alice</h2></header><div>No posts yet</div></main>','no posts'),('missing profile','<main><span>Sorry, this page isn\'t available.</span></main>','unavailable')]:
  fixture(body,'https://www.instagram.com/alice/');r=step(kind='posts',url='https://www.instagram.com/alice/',mode='users');check(name+' is skipped, not an error',not r.get('error') and r.get('posts')==[] and word in r.get('note',''))
 fixture(PROFILE,'https://www.instagram.com/alice/');r=step(kind='posts',url='https://www.instagram.com/alice/',mode='users');check('profile with posts still returns its posts',not r.get('error') and len(r.get('posts',[]))==2)
 fixture(POST.replace('<span>Hello','<span>Too many attempts, Action Blocked, Try Again Later'));r=step();check('warning words inside a comment do not stop the task',bool(r.get('preview')) and not r.get('error'))
 fixture(POST.replace('<main>','<main><div role="dialog">Try Again Later</div>'));r=step();check('warning shown in a dialog does stop the task',bool(r.get('error')) and 'verification' in r.get('error',''))
 fixture(POST);page.add_script_tag(path=str(ROOT/'content.js'));check('content script is safe to inject twice',page.evaluate('listeners.length')==1)
 fixture(POST);rep=page.evaluate('AuroraDiagnose()');check('page check reports what it found',('Post action bar found: ✓' in rep) and ('Like heart found: ✓' in rep) and 'Signed in: ✓' in rep)
 fixture(POST,actor=False);rep=page.evaluate('AuroraDiagnose()');check('page check flags a missing sign-in','Signed in: ✗' in rep)
 fixture(PROFILE,'https://www.instagram.com/alice/?hl=en');r=step(action='follow',kind='account',url='https://www.instagram.com/alice/',mode='users');check('profile with a tracking parameter is still recognised',not r.get('error'))
 for f in ('dashboard.html','popup.html'):
  html=(ROOT/f).read_text(encoding='utf-8');check(f+' preview defaults on','id="dry" checked' in html);check(f+' has the daily cap and banner','id="dailyCap"' in html and 'id="banner"' in html)
 browser.close()
print(json.dumps({'passed':len(checks),'checks':checks},indent=2))
