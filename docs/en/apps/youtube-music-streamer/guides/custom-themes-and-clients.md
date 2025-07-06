---
title: Creating Custom Themes and Clients
description: Learn how to create your own themes and clients for YouTube Music Streamer. (Very technical guide)
---

# Creating Custom Themes and Clients
YouTube Music Streamer allows you to create your own themes and clients (from now on, we only say "client") for the server. This is a very technical guide, so if you're not familiar with programming, or at least HTML, CSS and JavaScript, you might want to skip this guide.

!!! important "License for First-Party & Example Clients/Widgets"
    --8<-- "en/apps/youtube-music-streamer/license_notice.md"

## What is a Client?
A client is, very simple explained, anything that can communicate via WebSockets. It should (here comes the "theme" part) also be able to display something. For the first-party clients, this is a HTML file that can be embedded in the most streaming software programs (Browser Source). You can also create your own clients in any other way, with any language you like, as long as it can communicate via WebSockets. The possibilities are endless!

## Technical Information
The server communicates with the clients via WebSockets. It uses the DotNet `System.Net.HttpListener` class to create a simple HTTP server that listens for incoming WebSocket connections and is therefore very lightweight and minimalistic but this also means, the server is mostly in "send-only" mode (it doesn't listen for any incoming messages. Only for connections and disconnections).

To connect with it, you need to use the WebSocket protocol. The server listens on localhost:<port>. The port is the one you set in the server settings. For example `new WebSocket('ws://localhost:9876/`);`

The server sends multiple formats of messages in one single channel, depending on the type of message. It sends Song/Track Information and, if not disabled, Audio Data.

### Message Formats:
**Song/Track Information**: This is a JSON object that contains information about the currently playing song, such as title, artist, album, duration, and progress. It is sent every time the song changes or the progress updates.

`data` is [YTMDesktop CSharp Companion StateOutput][] from [YTMDesktop CSharp Companion][].

??? "minified example json"
    ```json5
    {
        "e": "TrackInfo",
        "data": {
            "Player": {
                "TrackState": 1,
                "VideoProgress": 198.46830118367325,
                "Volume": 10,
                "AdPlaying": false,
                "Queue": {
                    "Autoplay": true,
                    "Items": [],
                    "AutomixItems": [],
                    "IsGenerating": false,
                    "IsInfinite": false,
                    "RepeatMode": 0,
                    "SelectedItemIndex": 48
                }
            },
            "Video": {
                "Author": "London Elektricity",
                "ChannelId": "UCTyQFEG-Sr03fjZ4IY59Tiw",
                "Title": "Just One Second (Apex Remix)",
                "Album": "Sick Music",
                "AlbumId": "MPREb_sl4GScOhioX",
                "LikeStatus": 1,
                "Thumbnails": [
                    {
                        "Url": "https://lh3.googleusercontent.com/NuxLr-wv-zCR5u57iJP1JEsZJijWC0AR1m5S9lzjAudWKtdUpl2B98uK2aWpC1FwqCmaFgy5naD1sV1j=w60-h60-l90-rj",
                        "Width": 60,
                        "Height": 60
                    },
                    {
                        "Url": "https://lh3.googleusercontent.com/NuxLr-wv-zCR5u57iJP1JEsZJijWC0AR1m5S9lzjAudWKtdUpl2B98uK2aWpC1FwqCmaFgy5naD1sV1j=w120-h120-l90-rj",
                        "Width": 120,
                        "Height": 120
                    },
                    {
                        "Url": "https://lh3.googleusercontent.com/NuxLr-wv-zCR5u57iJP1JEsZJijWC0AR1m5S9lzjAudWKtdUpl2B98uK2aWpC1FwqCmaFgy5naD1sV1j=w180-h180-l90-rj",
                        "Width": 180,
                        "Height": 180
                    },
                    {
                        "Url": "https://lh3.googleusercontent.com/NuxLr-wv-zCR5u57iJP1JEsZJijWC0AR1m5S9lzjAudWKtdUpl2B98uK2aWpC1FwqCmaFgy5naD1sV1j=w226-h226-l90-rj",
                        "Width": 226,
                        "Height": 226
                    },
                    {
                        "Url": "https://lh3.googleusercontent.com/NuxLr-wv-zCR5u57iJP1JEsZJijWC0AR1m5S9lzjAudWKtdUpl2B98uK2aWpC1FwqCmaFgy5naD1sV1j=w302-h302-l90-rj",
                        "Width": 302,
                        "Height": 302
                    },
                    {
                        "Url": "https://lh3.googleusercontent.com/NuxLr-wv-zCR5u57iJP1JEsZJijWC0AR1m5S9lzjAudWKtdUpl2B98uK2aWpC1FwqCmaFgy5naD1sV1j=w544-h544-l90-rj",
                        "Width": 544,
                        "Height": 544
                    }
                ],
                "DurationSeconds": 378,
                "Id": "_YZD9PKeeDo"
            },
            "PlaylistId": "RDTMAK5uy_n_5IN6hzAOwdCnM8D8rzrs3vDl12UcZpA"
        }
    }
    ```

**Audio Data**: This is binary data (`byte[]`) that contains the audio stream of the currently playing song. It uses `NAudio`. It is sent every 33ms (about 30Hz) and can be used to visualize the audio in real-time. This is only sent if the "Allow Audio Stream" option is enabled in the server settings.
```json5
{
    "e": "AudioInfo",
    "data": {
        "SampleRate": 44100, // (1)!
        "BitsPerSample": 16, // (2)!
        "Channels": 2, // (3)!
        "Encoding": "Pcm" // (4)!
    }
}
```

1. integer - Sample rate of the audio stream (e.g., 44100Hz).
2. integer - Bits per sample (e.g., 16 bits).
3. integer - Number of channels (1 for mono, 2 for stereo, ...).
4. string - Encoding type of the audio stream (e.g., "Pcm", "Mp3", etc.). This is the `WaveFormatEncoding` from `NAudio`, as a string, so you can use it to determine how to decode the audio data.

## Creating a Client
For this, we concentrate only on the connection part etc. The "theme" part is not included here, because that has less to do with the application itself and more with the design and layout of a custom client. Below is a simple example of how to connect to the server and work with the data we receive. For the example, we're using JavaScript.

For an even more detailed example with visualizing, theming, etc., feel free to generate any of the clients in the server settings or use the copy of the "dev-widget" in [Example Client](#example-client). It is a good example of how to create a client that can display song information and visualize audio data.

```javascript
// connect to server
let ws = new WebSocket('ws://localhost:9876/');

// On close, very simple reconnect
ws.onclose = (event) => {
    ws = new WebSocket(event.target.url);
    ws.onclose = event.target.onclose;
    ws.onmessage = event.target.onmessage;
}

// listen for messages
ws.onmessage = async (event) => {
    // first check, if it's json data or binary data
    if (typeof event.data === 'string') {
        const data = JSON.parse(event.data);
        
        // if it's json data, check if it's track info or audio info
        switch (data.e) {
            case 'TrackInfo':
                // If it's track info, do something to visualize it, here comes theming into play
            case 'AudioInfo':
                // If it's audio info, use those as metadata to work better with the binary audio data
        }
    } else {
        // Binary message (Blob) with raw audio data. It's recommended to first wait for the metadata (AudioInfo)
        if (!audioInfo) {
            console.error("Audio metadata not received yet!");
            return;
        }
        
        // Do something with the binary data (make an audio visualizer, etc). Here's a small extended example on how you could work with it.
        
        // Convert it to a float 32 array
        const arrayBuffer = await event.data.arrayBuffer();
        const floatData = new Float32Array(arrayBuffer);

        // check if it's mono or stereo based on the channels
        let monoData;
        if (audioInfo.Channels === 2) {
            // For stereo data, average the left and right channels
            const numSamples = floatData.length / 2;
            monoData = new Float32Array(numSamples);
            for (let i = 0; i < numSamples; i++) {
                // Assuming interleaved stereo: left at index 2*i, right at index 2*i+1
                monoData[i] = (floatData[2 * i] + floatData[2 * i + 1]) / 2;
            }
        } else {
            // If mono, no need to process further
            monoData = floatData;
        }
        
        // save it for for visualization
        latestAudioData = monoData;
    }
}
```

## Example Client

??? dev-widget
    ``` { .html .copy }
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Modern</title>
        <style>
            html, body {
                margin: 0;
                padding: 0;
                overflow: hidden;
                width: 100vw;
                height: 100vh;
                font-size: min(3vw, 9vh);
            }
    
            body {
                background: #111;
                color: white;
                font-family: 'Segoe UI', sans-serif;
            }
    
            *, *::before, *::after {
                box-sizing: border-box;
                padding: 0;
                margin: 0;
                overflow: hidden;
            }
    
            h1, h2, p {
                white-space: nowrap;
                overflow: hidden;
                width: 100%;
                max-width: 100%;
            }
    
            .widget {
                width: min(100vw, calc(3 * 100vh));
                height: min(100vh, calc(100vw / 3));
                display: flex;
                gap: 1rem;
            }
    
            .image-container {
                height: 100%;
                aspect-ratio: 1 / 1;
                flex-shrink: 0;
                overflow: hidden;
                border-radius: 1rem;
            }
    
            .image-container img {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }
    
            .info {
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }
    
            .card {
                background: #333333bb;
                padding: 0.75rem;
                position: relative;
            }
    
            .card:first-child {
                border-top-left-radius: 1rem;
                border-top-right-radius: 1rem;
            }
    
            .card:last-child {
                border-bottom-left-radius: 1rem;
                border-bottom-right-radius: 1rem;
            }
    
            .quote {
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }
    
            .quote-text {
                display: flex;
                flex-direction: column;
                border-left: 0.25rem solid #c25;
                padding-left: 0.5rem;
            }
    
            .quote-author {
                font-size: 1.25rem;
                position: relative;
                padding-left: 1.5rem;
                font-weight: bold;
                font-style: italic;
            }
    
            .quote-author::before {
                content: '— ';
                position: absolute;
                left: 0;
            }
    
            #title {
                font-size: 1.75rem;
            }
    
            #album {
                font-size: 1.25rem;
                font-weight: normal;
            }
    
            #track-state {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 1rem;
                position: relative;
            }
    
            .timer {
                flex-shrink: 0;
            }
    
            #visualizer {
                position: absolute;
                left: 15%;
                width: 70%;
                height: 2rem;
            }
    
            #progress {
                --value: 0%;
    
                position: absolute;
                height: 0.2rem;
                background: #333;
                overflow: hidden;
                left: 0;
                right: 0;
                top: 0;
            }
    
            #progress::before {
                content: '';
                display: block;
                height: 100%;
                background: #c25;
                width: var(--value, 0%);
                transition: width 0.5s;
            }
    
            .marquee-container {
                display: inline-flex;
                white-space: nowrap;
            }
    
            .marquee-container.scroll {
                animation: marquee linear infinite;
            }
    
            .marquee-text {
                flex-shrink: 0;
                margin-right: 1rem;
            }
    
            @keyframes marquee {
                0% {
                    transform: translateX(0);
                }
                100% {
                    transform: translateX(-50%);
                }
            }
        </style>
    </head>
    <body>
    <div class="widget">
        <div class="image-container">
            <img id="image" src="https://placehold.co/544?text=No%20Image" alt="Placeholder image" referrerpolicy="no-referrer">
        </div>
    
        <div class="info">
            <div class="card">
                <div class="quote">
                    <div class="quote-text">
                        <h1 id="title"></h1>
                        <h2 id="album"></h2>
                    </div>
                    <div class="quote-author">
                        <p id="author"></p>
                    </div>
                </div>
            </div>
    
            <div class="card">
                <div id="progress" data-value="50"></div>
                <div id="track-state">
                    <span class="timer" id="current">00:00</span>
                    <canvas id="visualizer"></canvas>
                    <span class="timer" id="duration">00:00</span>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const isDebug = true;
            let ws = new WebSocket('ws://localhost:9876/');
    
            ws.onclose = (event) => {
                ws = new WebSocket(event.target.url);
                ws.onerror = event.target.onerror;
                ws.onclose = event.target.onclose;
                ws.onmessage = event.target.onmessage;
            };
            
            ws.onmessage = async (event) => {
                if (typeof event.data === 'string') {
                    const data = JSON.parse(event.data);
                    switch (data.e) {
                        case 'TrackInfo':
                            return updateWidget(data.data);
                        case 'AudioInfo':
                            audioInfo = data.data;
                            console.log('Audio metadata received:', audioInfo);
                            break;
                    }
                } else {
                    // Binary message (Blob) with raw audio data
                    if (!audioInfo) {
                        console.error("Audio metadata not received yet!");
                        return;
                    }
                    const arrayBuffer = await event.data.arrayBuffer();
                    const floatData = new Float32Array(arrayBuffer);
    
                    let monoData;
                    if (audioInfo.Channels === 2) {
                        // For stereo data, average the left and right channels
                        const numSamples = floatData.length / 2;
                        monoData = new Float32Array(numSamples);
                        for (let i = 0; i < numSamples; i++) {
                            // Assuming interleaved stereo: left at index 2*i, right at index 2*i+1
                            monoData[i] = (floatData[2 * i] + floatData[2 * i + 1]) / 2;
                        }
                    } else {
                        // If mono, no need to process further
                        monoData = floatData;
                    }
                    latestAudioData = monoData;
                }
            }
    
            function updateWidget(data) {
                const imageElement = document.getElementById('image');
                const titleElement = document.getElementById('title');
                const authorElement = document.getElementById('author');
                const albumElement = document.getElementById('album');
                const progressElement = document.getElementById('progress');
                const currentElement = document.getElementById('current');
                const durationElement = document.getElementById('duration');
    
                const updateInnerText = (element, text) => {
                    if (!element || element.dataset.lastText === text || !text) {
                        return;
                    }
    
                    element.dataset.lastText = text;
    
                    element.innerText = text;
    
                    if (element.scrollWidth <= element.clientWidth) {
                        return;
                    }
    
                    element.innerHTML = '';
    
                    const marqueeContainer = document.createElement('div');
                    marqueeContainer.classList.add('marquee-container');
    
                    const span1 = document.createElement('span');
                    span1.classList.add('marquee-text');
                    span1.innerText = text;
    
                    const span2 = document.createElement('span');
                    span2.classList.add('marquee-text');
                    span2.innerText = text;
    
                    marqueeContainer.appendChild(span1);
                    marqueeContainer.appendChild(span2);
                    element.appendChild(marqueeContainer);
    
                    requestAnimationFrame(() => {
                        if (span1.scrollWidth > element.clientWidth) {
                            marqueeContainer.classList.add('scroll');
                            const duration = span1.scrollWidth / 50;
                            marqueeContainer.style.animationDuration = `${duration}s`;
                        }
                    });
                };
    
                const updateImage = (element, url) => {
                    if (typeof isDebug !== 'undefined' && isDebug) url = 'https://placehold.co/544?text=No%20Image';
                    if (element.src === url || !url) {
                        return;
                    }
                    element.src = url;
                };
    
                const updateTimer = (element, seconds) => {
                    const minutes = Math.floor(seconds / 60);
                    const remainingSeconds = Math.floor(seconds % 60);
    
                    const formattedMinutes = minutes.toString().padStart(2, '0');
                    const formattedSeconds = remainingSeconds.toString().padStart(2, '0');
    
                    updateInnerText(element, `${formattedMinutes}:${formattedSeconds}`);
                };
    
                const updateProgress = (element, value) => {
                    element.style.setProperty('--value', `${value}%`);
                };
    
                if (typeof isDebug !== 'undefined' && isDebug) console.log(data);
    
                if (!data.Video || !data.Player) return;
    
                const thumbnail = data.Video.Thumbnails.reduce((prev, current) => {
                    return (prev.Width > current.Width) ? prev : current
                });
    
                if (thumbnail) {
                    updateImage(imageElement, thumbnail.Url);
                }
    
                updateInnerText(titleElement, data.Video.Title);
                updateInnerText(authorElement, data.Video.Author);
                updateInnerText(albumElement, data.Video.Album);
    
                const durationInSeconds = data.Video.DurationSeconds;
                const progressInSeconds = data.Player.VideoProgress;
    
                updateProgress(progressElement, (progressInSeconds / durationInSeconds) * 100);
                updateTimer(currentElement, progressInSeconds);
                updateTimer(durationElement, durationInSeconds);
            }
    
            let audioInfo = null;
            let latestAudioData = null;
            const amplitudeMultiplier = 1;
            const FFT_SIZE = 1024; // Use a power-of-2 FFT size.
    
            // Helper: Resize the canvas for high-DPI displays.
            function resizeCanvasToDisplaySize(canvas) {
                const width = canvas.clientWidth;
                const height = canvas.clientHeight;
                if (canvas.width !== width || canvas.height !== height) {
                    canvas.width = width;
                    canvas.height = height;
                }
                return 1;
            }
    
            function fft(re, im) {
                const n = re.length;
                if (n <= 1) return;
    
                const half = n >> 1;
                const evenRe = new Array(half),
                    evenIm = new Array(half);
                const oddRe = new Array(half),
                    oddIm = new Array(half);
    
                for (let i = 0; i < half; i++) {
                    evenRe[i] = re[2 * i];
                    evenIm[i] = im[2 * i];
                    oddRe[i] = re[2 * i + 1];
                    oddIm[i] = im[2 * i + 1];
                }
    
                fft(evenRe, evenIm);
                fft(oddRe, oddIm);
    
                for (let k = 0; k < half; k++) {
                    const t = (-2 * Math.PI * k) / n;
                    const cos = Math.cos(t);
                    const sin = Math.sin(t);
                    const oddReTemp = cos * oddRe[k] - sin * oddIm[k];
                    const oddImTemp = sin * oddRe[k] + cos * oddIm[k];
    
                    re[k] = evenRe[k] + oddReTemp;
                    im[k] = evenIm[k] + oddImTemp;
                    re[k + half] = evenRe[k] - oddReTemp;
                    im[k + half] = evenIm[k] - oddImTemp;
                }
            }
            function computeFFT(samples) {
                const data = new Float32Array(FFT_SIZE);
                const len = Math.min(samples.length, FFT_SIZE);
                data.set(samples.subarray(0, len));
    
                const N = FFT_SIZE;
                const re = Array.from(data);
                const im = new Array(N).fill(0);
    
                fft(re, im);
    
                const half = N / 2;
                const magnitudes = new Array(half);
                for (let i = 0; i < half; i++) {
                    magnitudes[i] = Math.sqrt(re[i] * re[i] + im[i] * im[i]);
                }
                return magnitudes;
            }
    
            function drawFrequencyBarsVisualizer() {
                const canvas = document.getElementById("visualizer");
                const ctx = canvas.getContext("2d");
    
                // Resize and clear the canvas.
                const dpr = resizeCanvasToDisplaySize(canvas);
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();
                ctx.scale(dpr, dpr);
    
                if (latestAudioData) {
                    // Compute the frequency spectrum from the latest audio data.
                    const spectrum = computeFFT(latestAudioData);
    
                    const width = canvas.clientWidth;
                    const height = canvas.clientHeight;
                    const barCount = 64; // Typical count (change to 16 if desired)
                    const barWidth = width / barCount;
                    const groupSize = Math.floor(spectrum.length / barCount);
    
                    // Define non-linear EQ parameters.
                    // Left-most bar will be scaled by minEQ (shrunken down),
                    // right-most bar by maxEQ (boosted more).
                    const minEQ = 0.05;   // Left side scale factor
                    const maxEQ = 6.0;    // Right side scale factor
                    const exponent = 2;   // Use a quadratic mapping for a non-linear transition
    
                    for (let i = 0; i < barCount; i++) {
                        let sum = 0;
                        let count = 0;
                        const start = i * groupSize;
                        const end = start + groupSize;
                        for (let j = start; j < end && j < spectrum.length; j++) {
                            sum += spectrum[j];
                            count++;
                        }
                        const avgAmplitude = count > 0 ? sum / count : 0;
                        // Compute a non-linear EQ factor: lower on the left, higher on the right.
                        const eqFactor = minEQ + (maxEQ - minEQ) * Math.pow(i / (barCount - 1), exponent);
                        let amplitude = avgAmplitude * amplitudeMultiplier * eqFactor;
                        // Convert amplitude to a bar height.
                        let barHeight = amplitude * height;
                        // Ensure bars are always visible (minimum 5% of the canvas height).
                        barHeight = Math.max(barHeight, height * 0.05);
                        if (barHeight > height) barHeight = height;
    
                        // Draw the bar centered vertically.
                        const centerY = height / 2;
                        const y = centerY - barHeight / 2;
                        const x = i * barWidth;
                        ctx.fillStyle = "#C25";
                        // Use 80% of the available bar width to leave a gap between bars.
                        ctx.fillRect(x, y, barWidth * 0.8, barHeight);
                    }
                }
    
                ctx.restore();
                requestAnimationFrame(drawFrequencyBarsVisualizer);
            }
    
            // Start the frequency bars visualizer loop.
            requestAnimationFrame(drawFrequencyBarsVisualizer);
        });
    </script>
    </body>
    </html>
    ```

## Recommendations

We recommend that your custom client:

- **Use the Canvas API and `requestAnimationFrame`**
    - Leverage the [Canvas API][] together with [requestAnimationFrame][] for smooth, high-performance audio visualizations (waveforms, spectrograms, etc.).

- **Keep it lightweight**
    - Minimize dependencies and bundle size: tree-shake and lazy-load assets.
    - Defer non-essential scripts and styles to speed up initial load.

- **Ensure full responsiveness**
    - Use fluid units (`vw`/`vh`, `%`) and CSS functions (`min()`, `max()`, `clamp()`).
    - Define an explicit `aspect-ratio` on your root container so OBS and other streaming tools can size the widget correctly.
    - Auto-scroll long text only when overflow is detected (e.g., marquee or CSS scroll).

- **Provide clear fallbacks**
    - Detect feature support (e.g., OffscreenCanvas, Web Audio) and gracefully degrade.
    - Show a static thumbnail or simple text view if real-time audio data isn’t available.

- **Keep theming flexible**
    - Expose CSS variables (e.g., `--primary-color`, `--font-size`) for easy overrides.
    - Structure your HTML with semantic classes so users can swap out layouts without touching core logic.
