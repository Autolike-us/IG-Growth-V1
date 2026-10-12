# Changelog

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
