# mac-hide-cursor

Tiny Node native addon that hides the macOS OS cursor without requiring Accessibility (TCC) permission.

On macOS it calls `CGDisplayHideCursor(kCGDirectMainDisplay)` / `CGDisplayShowCursor(kCGDirectMainDisplay)`. The cursor is hidden while the calling app is the foreground app — exactly what a kiosk wants.

macOS only. The package's `os` field restricts npm install to Darwin; on Windows or Linux npm will skip it entirely (no native build attempted).

## Install

```
npm install OutOfAxis/mac-hide-cursor
```

For Electron projects, rebuild against Electron's V8 ABI after install:

```
npx electron-rebuild -m node_modules/mac-hide-cursor
```

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
