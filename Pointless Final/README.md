# Phone Number (Please Hold)

**The world's least efficient phone number form: your digits fall through a pachinko board into random slots, the volume knob escapes and bounces around the screen forever, and then the site checks your identity by putting cartoon slime on your nostrils.**

Built for a "most pointless project" hackathon. Everything is in one file, `index.html`: vanilla JS, a homemade physics engine (gravity, collisions, bounce), and sounds made with Web Audio (no audio files). The only external dependency is MediaPipe Face Landmarker, used for the nostril act.

## How to run

Recommended (camera permission is remembered, and the local face-library fallback works):

```sh
cd "Pointless Final"
python3 -m http.server 8000
# open http://localhost:8000
```

Quick option: double-click `index.html`. Everything works from `file://` except the *local* face-library fallback, because browsers refuse to load ES modules from `file://`. The CDN copy still works if you are online.

Use Chrome or Edge for the best results. Firefox and Safari work too, but their speech voices sound different.

## Presenter shortcuts

| Key | Action |
| --- | --- |
| `R` | Reset everything instantly |
| `V` | Force the volume ball to escape |
| `N` | Jump straight to the nostril act (press again to skip the countdown) |
| `M` | Mute (the real mute; the status-bar **Mute** button does the same) |
| `0`-`9` | Drop a digit |
| `Esc` | Close the camera |

## Face library: CDN plus a local fallback

Load order, set in `CONFIG.faceLib` at the top of the script:

1. **CDN** (default): `@mediapipe/tasks-vision@0.10.14` from jsDelivr, with the model from `storage.googleapis.com`. The page starts loading it in the background about 1.5 s after it opens.
2. **Local**: `./vendor/mediapipe/…`. To set it up, run this once while you are online:
   ```sh
   sh get-face-lib.sh
   ```
   This downloads `vision_bundle.mjs`, the `wasm/` files and `face_landmarker.task` (about 15 MB) into `vendor/mediapipe/`. Then serve the folder over http.
3. **Stock face**: if both fail, or the camera is denied, or no face is found within 5 s, a cartoon avatar appears with the same slime and the message "No face found. Using a stock face." The demo still works.

URL overrides: `?face=local` (local only), `?face=cdn` (CDN only), `?face=off` (skip the library and always use the stock face).

Privacy: the camera feed never leaves the browser. **Snap a photo** builds a PNG on a canvas and downloads it directly. Nothing is uploaded.

See `DEMO.md` for the 45-second stage script and the pre-demo checklist.
