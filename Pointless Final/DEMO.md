# 45-second stage demo

Before you start: the page should be freshly reset (`R`), **Master: 100%**, the laptop volume loud, and the browser fullscreen (`F11`). Click once anywhere on the page so audio is unlocked.

| Time | You say | You do |
| --- | --- | --- |
| 0:00 | "Every website asks for your phone number. We made it… secure." | Point at the calm, corporate-looking form. |
| 0:04 | "Let's type my number. Nine…" | Click **9**. A quack plays and the duck pops up. The digit falls from the top of the screen and bounces through the pegs. |
| 0:08 | "…eight, seven, six…" *(speed up)* | Click 8 to 0 quickly. Digits pile up, slots that are already taken spit digits back out ("TAKEN!"), and every click quacks. |
| 0:16 | "Shuffled. For your security." | Wait for **Number accepted!**. The robot voice reads the scrambled number with DTMF tones. |
| 0:22 | *(deadpan)* "…It connected me to a confused pigeon." | Let the joke land. Click **Hang up & redial**: the digits drop into a pile at the bottom of the screen and get flushed. |
| 0:28 | "Bit loud. Let me turn it down… wait, *up*." | Drag the volume knob slowly to the right. It trembles ("Please don't."). Drag it to 100%. |
| 0:31 | "Oh no." | The ball escapes and bounces off every edge: BOING, PBBT, BONK, AAAAH. Flick it once with the mouse. |
| 0:35 | "And finally, for your safety…" | The face check opens by itself 2 s after the escape. Click **Allow camera, but sadly**. |
| 0:39 | "…it locates my nostrils." | Face the camera. Crosshairs appear, then the slime starts dripping. Turn your head so the slime follows it. |
| 0:43 | "And *that* is what your phone number costs." | Click **Snap a photo** for the "Certified Nostril Verified™" frame. Bow. |

If you are short on time: press `V` to skip Act 1, or `N` to go straight to the nostril act. Press `R` before taking questions.

# Pre-demo checklist

**Camera and permissions**
- [ ] Serve the folder over `http://localhost` (not `file://`) so Chrome remembers the camera permission.
- [ ] Press `N`, allow the camera, and confirm that crosshairs appear on your nostrils and the slime follows your head. Then press `R`.
- [ ] Test it in the venue lighting. If tracking is jumpy, add a light in front of your face.
- [ ] Make sure no other app (Zoom, Teams, OBS) is using the camera.

**Projector**
- [ ] Mirror the displays, and check the layout at the projector's resolution (it is designed for 1366×768 and 1920×1080).
- [ ] Set browser zoom to 100%, go fullscreen with `F11`, and hide the bookmarks bar.
- [ ] Check that the volume knob, digits and status bar are readable from the back of the room.
- [ ] Audio: confirm that HDMI or the venue speakers play the quack. Know where the **Mute** button and the `M` key are.

**Backups**
- [ ] Copy the whole `Pointless Final` folder (including `vendor/` if you downloaded it) to a USB stick and to a second laptop.
- [ ] Have a screen recording of a full run ready in case the machine dies.

**Offline fallback**
- [ ] Run `sh get-face-lib.sh` while online, then turn Wi-Fi off and reload `http://localhost:8000`. Confirm the nostril act still tracks your face (it uses the local copy).
- [ ] With Wi-Fi off, open `?face=off` and confirm the stock face and slime appear.
- [ ] Deny camera permission once and confirm you see "No face found. Using a stock face."
- [ ] Press `R` and check that everything resets instantly.
