{
  "targets": [
    {
      "target_name": "cursor_hide",
      "sources": [ "cursor-hide.mm" ],
      "include_dirs": [ "<!@(node -p \"require('node-addon-api').include\")" ],
      "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
      "xcode_settings": {
        "OTHER_LDFLAGS": [ "-framework Cocoa", "-framework ApplicationServices" ],
        "MACOSX_DEPLOYMENT_TARGET": "10.13",
        "GCC_ENABLE_CPP_EXCEPTIONS": "NO",
        "CLANG_CXX_LIBRARY": "libc++"
      }
    }
  ]
}
