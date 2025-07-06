---
title: YTMDesktop
description: Learn how to display the currently playing song in YTMDesktop and maintain a blacklist of songs for your Twitch stream.
---

# YTMDesktop
YouTube Music Streamer can be used to display widgets of the currently playing song in YTMDesktop as well as maintaining a blacklist of songs that you don't want your users to request.

You have two type of tabs, "Server" and "Blacklist".

=== ":material-server-outline: Server"
    ![server.png](/assets/images/youtube-music-streamer/guides/ytmd/server.png)
    
    In the "Server" tab, you can set up a locally running server which will allow clients to fetch song, track and audio information. This is used for the widgets to display all important information like song title, duration, progress and to visualize audio.

    <h2>Auto Start</h2>
    This option allows you to automatically start the server when YTMDesktop starts. If enabled, the server will start running in the background without needing to manually start it each time.

    <h2>Server Port</h2>
    This is the port that the server will listen on. You can change it to any other port if needed. Make sure that the port is not being used by another application.

    <h2>Client Theme</h2>
    Here you can choose and generate a client (widget) with first-party themes. You can select from any of the available themes. If you're happy with your choice, press the <button class="tw-bg-[#c25] tw-px-3 tw-py-2 tw-rounded">Generate Client</button> button to generate the client.

    This client is just a HTML file you can embed in your streaming software. For example in OBS Studio, you would embed it using the "Browser" source type. You can also use it in other streaming software that supports HTML embedding.

    Feel free to use the themes and clients as a starting point and customize them to your liking. (1) You can also create your own themes and clients if you want to. I would love if you could share them with the community, so I can see all your awesome creations!
    { .annotate }

    1. 
        --8<-- "en/apps/youtube-music-streamer/license_notice.md"

    To learn how to create your own themes and clients in more detail, jump to the [Creating Custom Themes and Clients](custom-themes-and-clients.md) guide.

    **Available Clients**
    === "Minimal"
        ![minimal.gif](/assets/images/youtube-music-streamer/guides/ytmd/clients/minimal.gif)

    === "Minimal Progressive"
        ![minimal-progressive.gif](/assets/images/youtube-music-streamer/guides/ytmd/clients/minimal-progressive.gif)

    === "Modern"
        ![modern.gif](/assets/images/youtube-music-streamer/guides/ytmd/clients/modern.gif)

    <h2>Preview</h2>
    This is a preview of the client that you have selected. It will show you how the client could look like in your streaming software. Below the preview, you can see a recommended aspect ratio that shows if you insert them as a browser source in your streaming software. This is just a recommendation, you can use any aspect ratio you like, but the recommended one will fit best with the client design.

    The aspect ratio is in the format of `width:height`, so for example `3:1` means that the width is three times the height. In pixels, this would be `300:100` or `600:200`, etc. You can use any resolution that fits your needs as long as you keep the aspect ratio in mind.

    <h2>Allow Audio Stream</h2>
    This option allows you to enable or disable the audio stream. If enabled, the server will also stream the audio of your selected audio device. This is used in some clients to visualize the audio in real-time, such as the [Modern](#modern) client.

    <h2>Audio Device</h2>
    This is the audio device that the server will use to stream the audio. You can select any audio device that is available on your system.

=== ":material-format-list-bulleted: Blacklist"
    ![blacklist.png](/assets/images/youtube-music-streamer/guides/ytmd/blacklist.png)

    In the "Blacklist" tab, you can manage the blacklist of songs that you don't want your users to request. This is useful if you want to prevent certain songs from being requested.

    To add a song to the blacklist, just insert the URL into the URL input and, optionally, a small description so you can remember why you blacklisted the song, then press the <button class="tw-bg-[#c25] tw-px-3 tw-py-2 tw-rounded">:material-plus: Add</button> button. The song will be added to the blacklist and will not be available for requests.

    If you want to remove a song from the blacklist, just click on the <button class="tw-bg-[#fb453a] tw-p-2 tw-rounded tw-text-black">:material-trash-can-outline:</button> button next to the song. This will remove the song from the blacklist and it will be available for requests again.
    
