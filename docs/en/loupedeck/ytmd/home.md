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
    - With this action, you can play or pause the current track. It displays the current state like if paused or playing. It can also displays, depending on configuration, the current tracks state like duration, current time, etc. See the variables section for more information.
    ??? abstract "Settings"
        ![Play / Pause Track](/assets/images/guides/Loupedeck/YTMDesktop/play-pause.png)

        **1**{: .round-number } This is the name and is default to the Loupedeck software. This means, every action in every plugin has this. It's just to differentiate between multiple actions of the same type.

        **2**{: .round-number } The three different lines all support types of variables and attributes. Variables are the values that are displayed and attributes are the formatting of the variables. 
        The attributes are optional and can be left out. The attributes are separated by a colon ++colon++. The variables are replaced by the actual values.

        The following variables are available:
        - `{current}`: The current time of the track
        - `{duration}`: The duration of the track
        - `{remaining}`: The remaining time of the track

        The following attributes are available:
        - `S`: The time in seconds

        Example: Current Track is 2:30 long, the current time is 1:00, the remaining time is 1:30. The variables would be:

        - `{current}` = 1:00
        - `{current:S}` = 60
        - `{duration}` = 2:30
        - `{duration:S}` = 150
        - `{remaining}` = 1:30
        - `{remaining:S}` = 90

- Next Track
    - With this action, you can skip to the next track.
- Previous Track
    - With this action, you can go back to the previous track.
- Like Track
    - With this action, you can like the current track.
- Dislike Track
    - With this action, you can dislike the current track.
- Volume Control
    - With this action, you can control the volume of the YouTube Music Desktop App, like on a mixing console.
- Track Info
    - With this action, you can see the current track information like album, title, and author.
- Shuffle
    - With this action, you can toggle the shuffle mode.
- Repeat
    - With this action, you can toggle the repeat mode. The repeat modes are:
        - NONE
        - ALL
        - ONE
- Settings Profile
    - With this action, you can add a new settings profile. This is needed to authorize the plugin. See the [How to use it?](#5-how-to-use-it) section for more information.

## 5. How to use it?

1. Install the [YouTube Music Desktop App](https://github.com/ytmdesktop/ytmdesktop).
2. Install the Plugin from [Releases](https://github.com/XeroxDev/Loupedeck-plugin-YTMDesktop/releases) or from the official [Loupedeck Store](https://loupedeckmarketplace.com/asset/YTMDesktop).
3. Add a settings profile action, fill out everything and click save.

    ??? example "Show me!"
        ![Step 3.1](/assets/images/guides/Loupedeck/YTMDesktop/step3.1.png)

4. Make sure the YouTube Music Desktop App and the Companion Server is running
    - To start the companion server, click at the top right of YTMDesktop on the settings gear
    - Go on the left side on the "Integrations" tab
    - Enable the "Companion Server"

    ??? example "Show me!"
        ![Step 1](/assets/images/guides/YTMDesktop/step1.png)
        ![Step 2](/assets/images/guides/YTMDesktop/step2.png)
        ![Step 3](/assets/images/guides/YTMDesktop/step3.png)

5. Turn on "enable companion authorization" under the Companion Server

    ??? example "Show me!"
        ![Step 4](/assets/images/guides/YTMDesktop/step4.png)

6. Press the Profile button on your device
7. Compare the authorization code displaying by the plugin with the one displaying in the YouTube Music Desktop App and if they match, confirm the authorization in the YouTube Music Desktop App

    ??? example "Show me!"
        ![Step 7](/assets/images/guides/Loupedeck/YTMDesktop/step7.png)

8. If you've gotten no error and the plugin is now displayed in the "Authorized companions" list of YouTube Music Desktop, you can now use the plugin

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
