---
title: YouTube Music Desktop
tags:

- plugin
- extension
- ytmd
- YouTube Music Desktop
- loupedeck

---

# YouTube Music Desktop

## 1. Badges

{{badges(repo='Loupedeck-plugin-YTMDesktop', loupedeck='YTMDesktop')}}

## 2. What is this Plugin?

With this plugin, you can easily control nearly everything about the [YouTube Music Desktop App](https://github.com/ytmdesktop/ytmdesktop). 
You can play/pause, skip, go back, like, dislike, and more from your Loupedeck, without having to switch windows.

!!! warning "Important"
    We only support version 2.x.x and above, if you are using an older version, please update to the latest version.

## 3. Support / Feedback

{{feedback_section('Loupedeck-plugin-YTMDesktop')}}

## 4. Available Actions

- Play / Pause Track
- Next Track
- Previous Track
- Like Track
- Dislike Track
- Volume Control
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
    <li>Install the Plugin from <a href="https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/releases">Releases</a> or from the official Loupedeck Store.</li>
    <li>
    Add a settings profile action, fill out everything and click save.
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/Loupedeck/YTMDesktop/step3.1.png" alt="step3.1.png"/>
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
  <li>Press the Profile button on your device</li>
  <li>
    Compare the authorization code displaying by the plugin with the one displaying in the YouTube Music Desktop App and if they match, confirm the authorization in the YouTube Music Desktop App
    <details class="example">
      <summary>Show me!</summary>
      <img src="/assets/images/guides/Loupedeck/YTMDesktop/step7.png" alt="step8.png"/>
    </details>
  </li>
  <li>If you've gotten no error and the plugin is now displayed in the "Authorized companions" list of YouTube Music Desktop, you can now use the plugin</li>
</ol>

!!! note
    The authorization steps are only needed once/when the plugin isn't authorized or you wish to change it.

## 6. FAQ

- **I can't find the stated / required options (e.g. Companion Server)**
    - Make sure you are using the latest version of the YouTube Music Desktop App and have not accidentally installed the official PWA (progressive web app) version. It has to be YTMDesktop (YouTube Music Desktop App) from github mentioned in the first step.
- **Loupedeck started before YouTube Music Desktop App [...]**
    - The Plugin, if authorized, will automatically try to connect to the Companion Server. If it can't connect but it was connected previously, it will retry every 5 seconds.
    - It can happen, that it only shows "Paused" even if the music is playing, just press the play button **twice** on your Loupedeck and it should work again.
- **Playlist feature [...]**
    - YTMDesktop already supports this feature natively using a custom "URI scheme". To use this, you just have to create an action that opens the following URL: `ytmd://play/<VideoID>/<PlaylistID>`
        - `<VideoID>` is your desired video id
        - `<PlaylistID>` is the playlist id.
        - As example, see this youtube link: `https://music.youtube.com/watch?v=abcdef&list=ghijkl`
            - In this example, the `abcdef` is the `<VideoID>` and the `ghijkl` is the `<PlaylistID>`

## 7. Links

{{links_section('Loupedeck-plugin-YTMDesktop', 'YTMDesktopPlugin.lplug4', 'YTMDesktop')}}

## 8. How to contribute?

Just fork the repository and create PR's.

!!! info
    We're using [release-please](https://github.com/googleapis/release-please) to optimal release the plugin.
    release-please is following the [conventionalcommits](https://www.conventionalcommits.org) specification.
