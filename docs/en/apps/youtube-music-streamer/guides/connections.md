---
title: Connections
description: Check your connection status and manage your connections to Twitch and YTMDesktop.
---

# Connections

Here you can manage your connections to Twitch and YTMDesktop. You can see if you're connected, and if not, you can connect to them very easily.

On the left side, you see the connection to Twitch. Choose below between the "Not connected" and the "Connected" state to see more information about each state.

=== "Not connected"
    
    ![logged-out.png](/assets/images/youtube-music-streamer/guides/connections/logged-out.png)

    If you're not connected yet, you can very simply connect your Twitch Account to the application. To do this, press the <button class="tw-bg-[#ad6dfd] tw-px-3 tw-py-2 tw-rounded">:simple-twitch: Login with Twitch</button> button. This should open a so called "OAuth" window, where you can login with your account and you see all permissions the app asks you for.

    !!! warning "Important"
        Please read the message from Twitch carefully, as it explains what permissions the app asks for. If you don't agree with them, you can simply close the window and the app will not be connected to your Twitch Account.

    
=== "Connected"
    
    ![logged-in.png](/assets/images/youtube-music-streamer/guides/connections/logged-in.png)

    If you're connected, you can see your Twitch username and profile picture.

    If you're connected to the wrong account or just simply want to connect to another Twitch Account, just press the text saying "<span class="tw-text-[#75ffff]">Log out</span>"

On the right side, you can connect to your YTMDesktop app. To do this, you've to follow a few steps.

1. Make sure the YTMDesktop App and the Companion Server is running
    - To start the companion server, click at the top right of YTMDesktop on the settings gear
    - Go on the left side on the "Integrations" tab
    - Enable the "Companion Server"

    ??? example "Show me!"
        ![Step 1](/assets/images/guides/YTMDesktop/step1.png)
        ![Step 2](/assets/images/guides/YTMDesktop/step2.png)
        ![Step 3](/assets/images/guides/YTMDesktop/step3.png)

2. Turn on "enable companion authorization" under the Companion Server

    ??? example "Show me!"
        ![Step 4](/assets/images/guides/YTMDesktop/step4.png)

3. Now, in YouTube Music Streamer, fill out the host and the port
4. Press the Button below the inputs
5. Now YouTube Music Streamer should show a code, also, YTMDesktop should open a new Window (if not, look in the Taskbar, there should something be blinking) with a code as well. Compare the codes and if they match, confirm the authorization in the YTMDesktop App by pressing on the "Allow" button on the right side.
6. If you've gotten no error and YouTube Music Streamer is now displayed in the "Authorized companions" list of YTMDesktop, the connection was successfully established.
