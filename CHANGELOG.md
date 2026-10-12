# Changelog

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
