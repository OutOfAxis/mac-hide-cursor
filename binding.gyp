{
  "targets": [
    {
      "target_name": "cursor_hide",
      "include_dirs": [ "<!@(node -p \"require('node-addon-api').include\")" ],
      "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
      "conditions": [
        [ "OS=='mac'", {
          "sources": [ "cursor-hide.mm" ],
          "xcode_settings": {
            "OTHER_LDFLAGS": [ "-framework Cocoa", "-framework ApplicationServices" ],
            "MACOSX_DEPLOYMENT_TARGET": "10.13",
            "GCC_ENABLE_CPP_EXCEPTIONS": "NO",
            "CLANG_CXX_LIBRARY": "libc++"
          }
        } ],
        [ "OS!='mac'", {
          "sources": [ "cursor-hide-stub.cc" ]
        } ]
      ]
    }
  ]
}
