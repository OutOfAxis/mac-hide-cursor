#include <napi.h>
#import <Cocoa/Cocoa.h>
#import <ApplicationServices/ApplicationServices.h>

// CGDisplayHideCursor is reference-counted per process; call once at app
// startup and once on every focus event to keep the count > 0 across
// macOS's automatic reset on app deactivation. No Accessibility (TCC)
// permission is required for this API.
static Napi::Value HideCursor(const Napi::CallbackInfo& info) {
  CGDisplayHideCursor(kCGDirectMainDisplay);
  return info.Env().Undefined();
}

static Napi::Value ShowCursor(const Napi::CallbackInfo& info) {
  CGDisplayShowCursor(kCGDirectMainDisplay);
  return info.Env().Undefined();
}

static Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set("hideCursor", Napi::Function::New(env, HideCursor));
  exports.Set("showCursor", Napi::Function::New(env, ShowCursor));
  return exports;
}

NODE_API_MODULE(cursor_hide, Init)
