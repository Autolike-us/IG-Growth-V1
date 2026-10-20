// Offline check of the in-place profile walk: open the first post popup, like, press Next, repeat, close.
const {chromium}=require('playwright'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const ROOT=path.join(__dirname,'..'),read=n=>fs.readFileSync(path.join(ROOT,n),'utf8');let passed=0;const check=(n,v)=>{assert(v,n);passed++;console.log('PASS '+n);};
const MOCK=`window.data={job:{id:'test',status:'running'},receipts:{},history:[]};window.listeners=[];
window.chrome={runtime:{id:'extension',onMessage:{addListener:f=>listeners.push(f)},sendMessage:async()=>({ok:true})},storage:{local:{get:async()=>structuredClone(data),set:async x=>Object.assign(data,structuredClone(x)),remove:async()=>{}},onChanged:{addListener:()=>{}}}};
const nt=window.setTimeout;window.setTimeout=(f,ms,...a)=>nt(f,Math.min(ms||0,10),...a);`;
const PAGE=`<html lang="en"><body><main><div data-pagelet="story_tray"><ul><li><div role="button" aria-label="Story by x"><span role="link"><img alt="x"></span></div></li></ul></div>
<article><header><a href="/morenita_poblana/">morenita_poblana</a><time>2d</time></header><a href="https://www.instagram.com/p/DenH7N6DnXF/"><time>2d</time></a><a href="https://www.instagram.com/reels/DenH7N6DnXF/"><div></div></a><section><div role="button"><svg aria-label="Like"></svg></div><div role="button"><svg aria-label="Comment"></svg></div></section></article>
<article><a href="/mercinazz/">mercinazz</a><a href="https://www.instagram.com/p/Deb036EpfN5/"><time>6d</time></a><section><div role="button"><svg aria-label="Like"></svg></div></section></article>
</main><script>
var n=0;window.addEventListener('scroll',()=>{});window.scrollBy=()=>{if(n++===0){var m=document.querySelector('main'),a=document.createElement('article');a.innerHTML='<a href="https://www.instagram.com/p/Dxx333/"><time>9d</time></a><section><div role="button"><svg aria-label="Like"></svg></div></section>';m.append(a);}};
</script></body></html>`;
(async()=>{const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
try{const pg=await browser.newPage();pg.on('pageerror',e=>{throw e;});await pg.setContent(PAGE);await pg.addScriptTag({content:MOCK});await pg.addScriptTag({content:read('selectors.js')});await pg.addScriptTag({content:'{const location={href:"https://www.instagram.com/",pathname:"/"};'+read('dom.js')+'\n'+read('content.js')+'}'});
 const r=await pg.evaluate(()=>new Promise(r=>listeners[0]({action:'step',step:{kind:'posts',url:'https://www.instagram.com/',label:'your home feed'},config:{action:'like',dry:true,mode:'feed',perUser:3,limit:10,delay:30,exclude:[],maxAge:0,videos:false,scanLimit:3,comment:'x'},jobId:'test'},{id:'extension'},r)));
 const codes=(r.posts||[]).map(u=>u.match(/\/p\/([^/]+)/)?.[1]);
 check('home feed: collects every post in the feed column (not just the first article)',codes.includes('DenH7N6DnXF')&&codes.includes('Deb036EpfN5'));
 check('home feed: keeps scrolling to load more posts up to the scan limit',codes.length===3&&codes.includes('Dxx333'));
 console.log('\n'+passed+' feed checks passed');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1);});
