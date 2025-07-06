---
title: Twitch
description: Learn how to set up and use YouTube Music Streamer with Twitch for your streams.
---

# Twitch
YouTube Music Streamer can be used with Twitch to enhance your streams by allowing you to display the currently playing song and interact with your viewers.

You have two type of tabs, "Global" and "Commands".

=== ":material-earth: Global"
    ![global.png](/assets/images/youtube-music-streamer/guides/twitch/global.png)
    
    In the "Global" tab, you can set up the global settings for Twitch.

    <h2>Command Prefix</h2>
    This is the prefix that viewers need to use to trigger commands in your Twitch chat. For example, if you set the prefix to `!` (default), viewers can type `!info` to see the currently playing song.

    Below is also a small preview of how the commands will look like in your Twitch chat.

    !!! tip
        You can change the command prefix to any character or string you prefer, such as `?`, `/`, or even custom words. 
        You can also use spaces like in the example in the image above <code>music </code>. This would result in `music info` or `music request` which could be useful if you want a more "natural" feeling.

    <h2>Send Message on Connect</h2>
    This option allows you to send a message to your Twitch chat when YouTube Music Streamer connects to your Twitch account. This can be useful to inform your viewers that the bot is online and ready to interact.

    <h2>Connect Message</h2>
    This is the message that will be sent to your Twitch chat when the bot connects. You can customize this message to your liking, but it would be awesome if you could keep the application name in the message, so your viewers know what bot is connected.

=== ":material-code-tags: Commands"
    ![command.png](/assets/images/youtube-music-streamer/guides/twitch/command.png)

    In the "Commands" tab, you can manage the commands that viewers can use in your Twitch chat.

    You can expand and collapse the commands by clicking on them. This will show or hide the settings of the command.

    All the command settings have the same layout:

    <h2>Command Status</h2>
    This toggle allows you to enable or disable the command. If the command is disabled, it will not respond to any chat messages.

    <h2>Trigger</h2>
    This is the command that viewers need to type in the chat to trigger the command. For example, if you set the trigger to `info`, viewers can type `!info` (or whatever prefix you set) to see the currently playing song. You can also see the prefix you set in the "Global" tab.

    <h2>Auto Response</h2>
    This allows you to set a custom response that the bot will send to the chat when the command is triggered. Each command has their own specific placeholders that are being replaced with the specific values. For example `{username}` will be replaced with the username of the viewer who triggered the command.
    
    All the available placeholders are listed below the input with a short description of what they do.

    <h2>Cooldown</h2>
    This is the global cooldown for the command. It prevents the command from being triggered too frequently. The cooldown is in seconds, so if you set it to `10`, viewers can only trigger the command once every 10 seconds.

    <h2>Required Bits</h2>
    This is the amount of bits that viewers need to donate to trigger the command. If you set it to `0`, the command can be triggered for free. If you set it to a positive number, viewers need to donate that amount of bits to trigger the command.

    <h2>Twitch Reward</h2>
    This allows you to bind the command to a Twitch channel point reward (if eligible). The dropdown will show you all the available channel point rewards that you have created on your Twitch channel. If you select a reward, viewers can trigger the command by redeeming that reward instead of typing it in the chat.

    You created a new reward and it doesn't show up in the dropdown? Just hit the <button class="tw-bg-[#c25] tw-px-3 tw-py-2 tw-rounded">Reload</button> button next to the dropdown to refresh the list of rewards.

    Choose "Disabled" if you don't want to bind the command to a channel point reward.

    !!! warning
        If you choose a command that requires a value (e.g. the `request` command), you need to make sure that the channel point reward also requires a value to be redeemed. Otherwise, the command will not work as expected (or at all), because the user could not provide a value for the command.

    <h2>Available Commands</h2>

    - **Info**: Send information about the current song.
    - **Next**: Triggers the next command in YTMDesktop - This means it skips the current song and plays the next one.
    - **Prev**: Triggers the previous command in YTMDesktop - This means it either restarts the current song or plays the previous song in the queue.
    - **RandomVolume**: Sets a random volume between 0 and 100.
    - **Request**: Allows viewers to request a song by providing a YouTube (Music) link. This command requires a value to be provided! Requested songs will be added to the [queue](queue.md).
    - **Start**: Forcefully starts playing the song provided by the user. This command requires a value to be provided!
    - **Volume**: Sets the volume to a specific value between 0 and 100. This command requires a value to be provided!
