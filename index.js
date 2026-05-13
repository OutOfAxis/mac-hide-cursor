try {
  module.exports = require("./build/Release/cursor_hide.node")
} catch (e) {
  console.error("cursor_hide native addon failed to load:", e)
  module.exports = { hideCursor: () => {}, showCursor: () => {} }
}
