// node-gyp-build looks for a prebuilt N-API binary under
// `prebuilds/<platform>-<arch>/` first, and falls back to `build/Release/`
// if no matching prebuild is present.
try {
  module.exports = require("node-gyp-build")(__dirname)
} catch (e) {
  console.error("mac-hide-cursor native addon failed to load:", e)
  module.exports = { hideCursor: () => {}, showCursor: () => {} }
}
