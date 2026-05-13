#include <napi.h>

static Napi::Value Noop(const Napi::CallbackInfo& info) {
  return info.Env().Undefined();
}

static Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set("hideCursor", Napi::Function::New(env, Noop));
  exports.Set("showCursor", Napi::Function::New(env, Noop));
  return exports;
}

NODE_API_MODULE(cursor_hide, Init)
