#!/usr/bin/env sh
# Downloads the MediaPipe Face Landmarker into ./vendor so the nostril act works offline.
# Run once from this folder while you still have internet:  sh get-face-lib.sh
set -e
V=0.10.14
CDN="https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@$V"
mkdir -p vendor/mediapipe/wasm
curl -fL "$CDN/vision_bundle.mjs" -o vendor/mediapipe/vision_bundle.mjs
for f in vision_wasm_internal.js vision_wasm_internal.wasm vision_wasm_nosimd_internal.js vision_wasm_nosimd_internal.wasm; do
  curl -fL "$CDN/wasm/$f" -o "vendor/mediapipe/wasm/$f"
done
curl -fL "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task" -o vendor/mediapipe/face_landmarker.task
echo "Done. Serve this folder over http (python3 -m http.server 8000) to use the local copy."
