[app]
title = Calibration App
package.name = calibration
package.domain = org.example
version = 1.0

source.dir = .
source.include_exts = py

requirements = python3,kivy

orientation = portrait

android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.archs = arm64-v8a

fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
