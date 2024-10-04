---
title: YouTube Music Desktop
tags:

- plugin
- extension
- ytmd
- YouTube Music Desktop
- elgato
- streamdeck

---

# YouTube Music Desktop

![hero](https://raw.githubusercontent.com/XeroxDev/YTMD-StreamDeck/master/assets/thumbnail/ytmdc-thumbnail.png)

## 1. Badges

{{badges(repo='YTMD-StreamDeck')}}

## 2. What is this Plugin?

With this plugin, you can easily control nearly everything about the [YouTube Music Desktop App](https://github.com/ytmdesktop/ytmdesktop). You can play/pause, skip, go back, like, dislike, and more
from your Stream Deck, without having to switch windows.

!!! warning "Important"
    We only support version 2.x.x and above, if you are using an older version, please update to the latest version.

## 3. Support / Feedback

--8<-- "snippets/support-feedback.md"

## 4. Available Actions

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

## 5. How to use it?

<ol>
  <li>Install the <a href="https://github.com/ytmdesktop/ytmdesktop">YouTube Music Desktop App</a>.</li>
    <li>Install the Plugin from <a href="https://github.com/XeroxDev/YTMD-StreamDeck/releases">Releases</a> or from the official Stream Deck Store.</li>
    <li>
    Add Play/Pause action
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/StreamDeck/YTMDesktop/step3.png" alt="step3.png"/>
    </details>
  </li>
  <li>
    Click on the Play/Pause action and insert, if not already correct, the settings to YTMDesktop (eg. Host and Port)
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/StreamDeck/YTMDesktop/step4.png" alt="step4.png"/>
    </details>
  </li>
  <li>
    Make sure the YouTube Music Desktop App and the Companion Server is running
    <ul>
        <li>To start the companion server, click at the top right of YTMDesktop on the settings gear</li>
      <li>Go on the left side on the "Integrations" tab</li>
      <li>Enable the "Companion Server"</li>
    </ul>
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/YTMDesktop/step1.png" alt="step1.png"/><br/>
      <img src="/assets/images/guides/YTMDesktop/step2.png" alt="step2.png"/><br/>
      <img src="/assets/images/guides/YTMDesktop/step3.png" alt="step3.png"/>
    </details>
  </li>
  <li>
    Turn on "enable companion authorization" under the Companion Server
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/YTMDesktop/step4.png" alt="step6.png"/>
    </details>
  </li>
  <li>
    Press the Authorize button in the Play/Pause action settings
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/StreamDeck/YTMDesktop/step7.png" alt="step7.png"/>
    </details>
  </li>
  <li>
    Compare the authorization code displaying by the plugin with the one displaying in the YouTube Music Desktop App and if they match, confirm the authorization in the YouTube Music Desktop App
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/StreamDeck/YTMDesktop/step8.png" alt="step8.png"/>
    </details>
  </li>
  <li>
    If you got a <span style="color: green;">Authenticated</span> you are ready to go! (Steps 6-8 are only needed once/when the plugin isn't authorized)
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/StreamDeck/YTMDesktop/step9.png" alt="step9.png"/>
    </details>
  </li>
</ol>

!!! note
    Steps 6-8 are only needed once/when the plugin isn't authorized

## 6. Links

{{links_section('YTMD-StreamDeck', 'fun.shiro.ytmd.streamDeckPlugin')}}

## 7. How to contribute?

Just fork the repository and create PR's.

!!! info
    We're using [release-please](https://github.com/googleapis/release-please) to optimal release the plugin.
    release-please is following the [conventionalcommits](https://www.conventionalcommits.org) specification.
