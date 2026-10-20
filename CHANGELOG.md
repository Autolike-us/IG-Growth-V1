# Changelog

## 1.2.2 — Home feed fix
- Fixed: with "Your home feed", Aurora only saw the first post on the page. It now reads the whole feed, keeps scrolling to load more, and counts each post once (a reel and its post link are the same post).

## 1.2.1 — Profiles without a Next arrow
- Fixed: when Instagram opens a post as a plain page (no left/right arrow), Aurora used to stop after the first post. It now closes the post, opens the next picture on the profile grid, and continues until your posts-per-profile number is reached.

## 1.2.0 — Follow + like, home feed, different comments
- **Follow + like**: a new action. For profiles it follows each account and then likes its posts; for a hashtag, place, home feed or post links it likes each post and follows its author. Both actions count toward the task limit and the daily cap.
- **Your home feed** is a new source: Aurora scrolls your own feed and uses the posts it finds, up to the discovery limit. No target needed.
- **A different comment on each post**: write one comment per line and tick the new box; Aurora picks one at random for each post and does not repeat a comment until all have been used.
- Instagram's own "Something went wrong" page is now recognised: Aurora reloads it (and tries the other form of a hashtag address) instead of reading an empty page, and says clearly when the problem comes from Instagram.

## 1.1.0 — New popup and a fresher dashboard
- The toolbar popup is now a small status card: what is running, Pause / Stop, today's count against your daily limit, your license, and **Open dashboard**. It cannot start or resume anything.
- Everything else (new tasks, saved setups, history, debug log) lives in the full dashboard tab, which opens from the popup. It re-uses the tab if it is already open.
- The dashboard has a calmer look in light and dark, a fourth **Today** card and a Help & support link.
- Nothing about how tasks run has changed: previews, confirmations, pacing, receipts and pause-on-problems are exactly as in 1.0.1.

## 1.0.1
- New: Telegram channel "Aurora Studios Report" for bug reports, feature requests and ideas — linked in the footer of the studio and the toolbar popup (next to Report an issue and Contact us).

## 1.0.0
- Pace floor lowered to 5 seconds between steps (default 20).
- Preview works without a license; only live tasks need a key. The trial (3 days, no subscription or payment method) is advertised in the License box.
- "Report an issue" and "Contact us" open an email to support@getaurorastudios.com (the issue report copies the diagnostic report for you to paste).
- First public release, sold through getaurorastudios.com. Version numbering restarts at 1.0.0; everything listed below is included. The studio now enforces the license (3-day free trial, then a subscription) against https://getaurorastudios.com.

## 2.9.0
- License system (for selling Aurora): a License box in the studio/popup where the customer pastes their key; live tasks (Start/Resume/every step) are blocked without a valid trial or subscription, while Preview works without a key. License tokens are signed (ES256) by the Aurora website and checked offline; they refresh every 12 hours and work for up to 72 hours offline. Builds stay unlocked until you run `node scripts/configure-license.cjs --api https://your-site --jwk '{…public key…}'`, and `npm run package` refuses to build an unlocked zip (use `--dev` for a test build).

## 2.8.0
- The panel and the Live session card show the same progress line on every site: "Target 2 of 5 · @name · post 2/3 · next post in 24s · 1/9 done", a finished/current/upcoming target list, and a "Skip this target & continue" button when paused.
- The studio, popup and on-page panel now open in the light theme by default (the theme switch still remembers your choice).

## 2.7.2
- The countdown is back during a profile walk: after each like the panel and studio show "Next post in Ns" counting down to the next post.

## 2.7.1
- While a profile walk is running, the panel and studio now show live progress (current post, likes done so far, the waiting pause) and count each like as it happens, instead of staying at 0/N until the whole profile finishes.

## 2.7.0
- Like (and comment) now work the way you would by hand: Aurora opens the first post of a profile in its popup, acts, presses the popup's Next arrow and repeats until the posts-per-profile / task limit, then closes the popup. No more loading each post by URL, so Instagram redirects can no longer stop the task. Already-liked posts are skipped, the last post ends the walk, photo-carousel arrows are ignored, and previews walk without clicking.
- Hashtag/location sources and direct post links still open posts by URL.

## 2.6.2
- The Live session card and the on-page Aurora panel show a running counter again: actions done / limit, steps left and a countdown to the next step.

## 2.6.1
- Reels: `/reels/<id>/` links count as the same reel as `/reel/<id>/`, so an Instagram redirect between them no longer pauses the task; reel pages and post popups without an article/main wrapper are now found.

## 2.6.0
- Studio refresh (interface only; automation unchanged): always-visible PREVIEW/LIVE bar (LIVE tucks away after 2 s), the Live choice stays on until the task finishes or is stopped, fields the chosen action does not use are hidden, collapsible Pace & limits and Advanced sections, a one-line summary above Start, sidebar badges, activity filters and search, Saved setups under the Live session card, a real factory reset, a first-run checklist, Ctrl+Enter to start, a single scrollbar and no pinned bars in the popup, and a redesigned on-page Aurora panel.

## 2.5.2
- The popup closes and the on-page panel folds away once a task starts running.

## 2.5.1
- Starting a task now reuses the Instagram tab you already have open instead of opening a new one.

## 2.5.0
- New: the form is remembered when the popup closes, a Reset to defaults button, and named saved setups (save, load, rename, delete).

## 2.4.1
- Fix: comments now wait for the post page to finish loading before typing, restore text if Instagram resets the box while typing, and reuse leftover text from an interrupted attempt instead of stopping.

## 2.4.0
- **Human-like typing.** Comments are typed one character at a time with an uneven rhythm and thinking pauses (capped at about 90 seconds) instead of being pasted in one go; line breaks become spaces; typing is checked before Post is pressed.
- A human-length pause (about 1–2.5 s) before every action.
- **Captcha handling.** A captcha, verification page or "try again later" dialog is reported clearly; for captchas Aurora brings the Instagram tab to the front, notifies you and continues by itself once it is solved. Identity checks and "try again later" warnings need a manual Resume.

## 2.3.1
- **Fixed: false "verification requested" stops.** A captcha now counts only when it is actually on screen with a real size and content; empty captcha placeholders that the page keeps around no longer stop the task. When a warning does stop a task, the debug log names the element that triggered it.

## 2.3.0
- **Faster start.** The pacing wait now applies after each action, not after reading a profile or skipping a post, so the first action begins about 10 seconds after you press Start instead of waiting a full delay first. The wait between actions is unchanged (never shorter than your setting, plus the random extra).

## 2.2.2
- **Your own posts are never liked or commented on**; they are skipped with a message (parity with the TikTok build).

## 2.2.1
- **Fixed: comment steps stopped with `Cannot read properties of null (reading 'querySelectorAll')`.** Instagram can replace the comment box while text is typed; Aurora now looks the box up fresh each time instead of holding on to one element, and confirms the comment against the live page. Nothing was ever submitted when this error occurred.
- Page helpers no longer throw when an element disappears mid-step; the debug log now includes the page-side error stack.

## 2.2.0
- **Debug log**: a rolling activity log with a one-click **Copy report** (studio tab, paused banner and on-page panel). Failed steps record a page trace and the Check page report automatically.
- Instagram posts, carousels and reels were already supported through `/p/` and `/reel/` links.

## 2.1.0
- Parity with the TikTok build: finish immediately at the action limit; wait never shorter than the setting plus 0–40% random extra; optional daily action cap.
- Interrupted live actions are detected and never re-sent; page-load errors retry up to 3 times (nothing that could have clicked is retried).
- Alerts: one status notification (replaced, not stacked) with one-click **Resume** for load-type pauses; badge; banner; pulsing on-page button.
- The page-warning scan only looks at dialogs, alerts and captcha widgets, at most every 1.5 s.
- Content script is re-attached automatically after an extension reload.
- Profile links with tracking parameters (e.g. `?hl=en`) are recognised as the same profile.
- **Check page** report, progress line, **Clear history**, history capped at 5,000, receipts pruned after 90 days (comments kept), CSV export protected against formulas.
- Removed stray byte-order marks from two scripts.
- Tests (previously none) and a GitHub Action; `npm run package` builds an installable zip.

## 2.0.0
- Instagram-themed studio, icons, inline live confirmation (no browser dialog), skip private/empty profiles.
