# Aurora 2.0.0

## Update
1. Stop the old Aurora task.
2. Extract this ZIP. Copy ALL files from aurora-ig into your original unpacked extension folder, replacing existing files. This preserves history/settings.
3. Open chrome://extensions, click Reload, verify version 2.0.0.
4. Refresh Instagram tabs. Stop any old-version task and create a new one.
5. Floating Aurora button > Open full studio > choose Action and Find targets from.
6. Begin with Preview only and an action limit of 1. Preview never likes, follows, unfollows, or types/posts comments.
7. To act, uncheck Preview only and review the live-task confirmation.

Preview resets ON when the studio opens or action changes. The floating panel offers a quick profile/like preview; full options are in the studio.

## Alerts when a task stops

When a task pauses (sign-in, verification, Instagram layout problem, restart) Aurora shows a desktop notification, turns the toolbar icon badge red (`!`), pops open the on-page panel with a pulsing red button, and shows a **Resume / Stop** banner in the studio and popup. A green `ON` badge means a task is running and `✓` means it finished. Starting a live task now asks for an inline two-step confirmation instead of a browser `confirm()` dialog.

## Actions
- Like: the post itself, not its comments.
- Follow: explicit/discovered accounts, or authors of discovered posts. Already-followed/requested accounts are skipped.
- Unfollow: only usernames explicitly entered in Profiles / custom user list. Other discovery sources are disabled. Pending requests are not canceled.
- Comment: uses your exact entered text. At most one Aurora comment attempt per post per signed-in account; local receipts prevent duplicate retries. Uncertain submission pauses the task. Check Instagram manually; it will not automatically resend.

One action per task. Post age/video filters apply to post likes/comments. Posts per profile controls profile discovery. Discovery limit caps each discovery step; scans also stop after 20 scroll attempts or 3 scans without new results. Action limit counts confirmed actions or eligible previews, not skips/discovery steps.

## Inputs
- Profiles: usernames, @usernames or profile URLs separated by commas/whitespace.
- Followers / following: one username; loads the appropriate dialog.
- Commenters / likers: one post/reel URL; uses comment rows or the post likes dialog.
- Hashtag: #travel, travel, a hashtag URL or Instagram hashtag search URL. Search redirects no longer cause a navigation loop.
- Location: a specific place URL containing a numeric ID, or the ID alone. Example: https://www.instagram.com/explore/locations/114897945188014/mexico-city-mexico/
  Use Find a location to browse country, city, then a particular place. Directory URLs and plain place names are not post-feed targets.
- Direct posts: post/reel URLs separated by commas/whitespace. Both /p/ID/ and /username/p/ID/ work.

## Verification
34 planning tests and 16 isolated browser checks passed. Worker tests cover sender validation, redirects, limits/counts and completion. Dashboard form checks and JavaScript syntax checks passed.
Live Instagram inspection verified hashtag redirects, location post links, likes/following dialogs and the unfollow menu. No live comments, follows or unfollows were submitted during development.
This ZIP has not yet been tested end to end as an installed extension. Start with a one-target preview, then one live action you intend to perform.

## Limits
Use Instagram in English, signed in, with the task tab open. Discovery uses rendered website content with bounded scrolling; it cannot guarantee all posts/accounts or access hidden content. Instagram changes can break selectors. Tasks pause on errors, sign-in/verification requests and detected restrictions. A click already sent may finish after pause/stop.
All extension data stays in local storage. No passwords/cookies are collected. No subscription/license checks, analytics or external servers. Existing extension permissions are unchanged.
