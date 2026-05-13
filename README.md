# mac-hide-cursor

Tiny Node native addon that hides the macOS OS cursor without requiring Accessibility (TCC) permission.

On macOS it calls `CGDisplayHideCursor(kCGDirectMainDisplay)` / `CGDisplayShowCursor(kCGDirectMainDisplay)`. The cursor is hidden while the calling app is the foreground app — exactly what a kiosk wants.

macOS only. The package's `os` field restricts npm install to Darwin; on Windows or Linux npm will skip it entirely (no native build attempted).

## Install

```
npm install OutOfAxis/mac-hide-cursor
```

The package ships prebuilt N-API binaries under `prebuilds/darwin-arm64/` and `prebuilds/darwin-x64/`, so no compilation or `electron-rebuild` is needed on the consumer side. N-API binaries are ABI-stable across Node and Electron versions.

If prebuilds are missing for some reason, the `install` script falls back to building from source via `node-gyp-build`.

## Building prebuilds (maintainers only)

Run on macOS — Xcode toolchain can cross-compile to both arches:

```
npm install
npm run prebuild
```

This produces:

- `prebuilds/darwin-arm64/<name>.node`
- `prebuilds/darwin-x64/<name>.node`

Commit and push:

```
git add prebuilds/
git commit -m "Rebuild prebuilds"
git push
```

Consumers pulling the package via `npm install` will then pick up the prebuilt binary for their arch — no native build needed.

## Usage

```js
const { hideCursor, showCursor } = require("mac-hide-cursor")

hideCursor()  // CGDisplayHideCursor
showCursor()  // CGDisplayShowCursor
```

`CGDisplayHideCursor` is reference-counted per process and reset on app deactivation. For a kiosk, call `hideCursor()` once at startup and again on every window `focus` / `show` event.

## Why not nut-js / robotjs?

Both move the cursor via `CGEventPost`, which requires the user to grant Accessibility permission in *System Settings → Privacy & Security → Accessibility*. `CGDisplayHideCursor` does not — it only hides the cursor while the app is foreground, with no permission prompt.

## License

MIT
