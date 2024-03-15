---
title: YouTube Music Desktop
description: 
published: true
date: 2024-03-15T20:26:28.091Z
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

<ol>
  <li>Install the <a rel="noreferrer" target="_blank" href="https://github.com/ytmdesktop/ytmdesktop" class="is-external-link">YouTube Music Desktop App</a>.</li>
	<li>Install the Plugin from <a rel="noreferrer" target="_blank" href="https://github.com/XeroxDev/YTMD-StreamDeck/releases" class="is-external-link">Releases</a> or from the official Stream Deck Store.</li>
	<li>
    Add Play/Pause action
    <details>
      <summary>Show me!</summary>
      <img src="/assets/guides/streamdeck/ytmdesktop/step3.png" alt="step3.png"/>
    </details>
  </li>
  <li>
    Click on the Play/Pause action and insert, if not already correct, the settings to YTMDesktop (eg. Host and Port)
    <details>
      <summary>Show me!</summary>
      <img src="/assets/guides/streamdeck/ytmdesktop/step4.png" alt="step4.png"/>
    </details>
  </li>
  <li>
    Make sure the YTMDesktop App and the Companion Server is running
    <ul>
    	<li>To start the companion server, click at the top right of YTMDesktop on the settings gear</li>
      <li>Go on the left side on the "Integrations" tab</li>
      <li>Enable the "Companion Server"</li>
    </ul>
    <details>
      <summary>Show me!</summary>
      <img src="/assets/guides/streamdeck/ytmdesktop/step5.1.png" alt="step5.1.png"/><br/>
      <img src="/assets/guides/streamdeck/ytmdesktop/step5.2.png" alt="step5.2.png"/><br/>
      <img src="/assets/guides/streamdeck/ytmdesktop/step5.3.png" alt="step5.3.png"/>
    </details>
  </li>
  <li>
    Turn on "enable companion authorization" under the Companion Server
    <details>
      <summary>Show me!</summary>
      <img src="/assets/guides/streamdeck/ytmdesktop/step6.png" alt="step6.png"/>
    </details>
  </li>
  <li>
    Press the Authorize button in the Play/Pause action settings
    <details>
      <summary>Show me!</summary>
      <img src="/assets/guides/streamdeck/ytmdesktop/step7.png" alt="step7.png"/>
    </details>
  </li>
  <li>
    Compare the authorization code displaying by the plugin with the one displaying in the YTMDesktop App and if they match, confirm the authorization in the YTMDesktop App
    <details>
      <summary>Show me!</summary>
      <img src="/assets/guides/streamdeck/ytmdesktop/step8.png" alt="step8.png"/>
    </details>
  </li>
  <li>
    If you got a <span style="color: green;">Authenticated</span> you are ready to go! (Steps 6-8 are only needed once/when the plugin isn't authorized)
    <details>
      <summary>Show me!</summary>
      <img src="/assets/guides/streamdeck/ytmdesktop/step9.png" alt="step9.png"/>
    </details>
  </li>
</ol>

# 6. How to contribute?

Just fork the repository and create PR's.


> **Information**
> We're using [release-please](https://github.com/googleapis/release-please) to optimal release the plugin.
> release-please is following the [conventionalcommits](https://www.conventionalcommits.org) specification.
{.is-info}