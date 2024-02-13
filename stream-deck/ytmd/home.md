---
title: YouTube Music Desktop
description: 
published: true
date: 2024-02-13T12:58:41.097Z
tags: plugin, extension, ytmd, elgato, streamdeck
editor: markdown
dateCreated: 2022-01-12T20:35:31.063Z
---

# 1. Badges
[![Forks](https://img.shields.io/github/forks/XeroxDev/YTMD-StreamDeck?color=blue&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/network/members) [![Stars](https://img.shields.io/github/stars/XeroxDev/YTMD-StreamDeck?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/stargazers) [![Watchers](https://img.shields.io/github/watchers/XeroxDev/YTMD-StreamDeck?color=lightgray&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/watchers) [![Contributors](https://img.shields.io/github/contributors/XeroxDev/YTMD-StreamDeck?color=green&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/graphs/contributors)

[![Issues](https://img.shields.io/github/issues/XeroxDev/YTMD-StreamDeck?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/issues) [![Issues closed](https://img.shields.io/github/issues-closed/XeroxDev/YTMD-StreamDeck?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/issues?q=is%3Aissue+is%3Aclosed)

[![Issues-pr](https://img.shields.io/github/issues-pr/XeroxDev/YTMD-StreamDeck?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/pulls) [![Issues-pr closed](https://img.shields.io/github/issues-pr-closed/XeroxDev/YTMD-StreamDeck?color=yellow&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/pulls?q=is%3Apr+is%3Aclosed) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/compare)

[![Release](https://img.shields.io/github/release/XeroxDev/YTMD-StreamDeck?color=black&style=for-the-badge)](https://github.com/XeroxDev/YTMD-StreamDeck/releases)

[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green?style=for-the-badge)](https://shields.io)

# 2. What is this Plugin?
This Stream Deck Plugin allows you to control the [YouTube Music Desktop App](https://github.com/ytmdesktop/ytmdesktop)

> **Note**
> We only support version 2.x.x and above, if you are using an older version, please update to the latest version.
{.is-warning}


# 3. Support / Feedback
You found a bug? You have a feature request? I would love to hear about it [here](https://github.com/XeroxDev/YTMD-StreamDeck/issues/new/choose) or click on the "Issues" tab here on the GitHub repositorie!

You can also join my discord [here](https://x.xeroxdev.de/s/discord)

# 4. Actions

- Play / Pause Track
- Next Track
- Previous Track
- Like Track
- Dislike Track
- Volume Mute
- Volume Down
- Volume Up
- Track Info
  - Shows a scrolling text for album, title and author
  - Shows the thumbnail of the track
- Shuffle
- Repeat
  - NONE
  - ALL
  - ONE

# 5. How to use it?

1. Install the [YouTube Music Desktop App](https://github.com/ytmdesktop/ytmdesktop).
2. Install the Plugin from [Releases](https://github.com/XeroxDev/YTMD-StreamDeck/releases) or from the official Stream Deck Store.
3. Add Play/Pause action
4. Insert, if not already correct, the settings to YTMDesktop (eg. Host and Port)
5. Make sure the YTMDesktop App and the Companion Server is running
   - To start the companion server, click at the top right of YTMDesktop on the settings gear
   - Go on the left side on the "Integrations" tab
   - Enable the "Companion Server"
6. Turn on "enable companion authorization" under the Companion Server
7. Press the Authorize button in the Play/Pause action settings
8. Compare the authorization code displaying by the plugin with the one displaying in the YTMDesktop App
9. If they match, confirm the authorization in the YTMDesktop App
10. You are ready to go! (Steps 6-9 are only needed once/when the plugin isn't authorized)

# 6. How to contribute?

Just fork the repository and create PR's.


> **Information**
> We're using [release-please](https://github.com/googleapis/release-please) to optimal release the plugin.
> release-please is following the [conventionalcommits](https://www.conventionalcommits.org) specification.
{.is-info}
