[app]

# (str) Title of your application
title = Cyber-Sentinel

# (str) Package name
package.name = cybersentinel

# (str) Package domain (needed for android packaging)
package.domain = org.cybersentinel

# (str) Source files where the app lives (relative to .spec file)
source.dir = .

# (list) Source files to include (let it catch python files, images, etc.)
source.include_exts = py,png,jpg,kv,atlas
main.filename = main.py

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add your app dependencies here (e.g., python3, kivy, requests)
requirements = python3,kivy

# (str) Supported orientations (portrait, landscape, all)
orientation = portrait

# (bool) Indicate if the application should be full screen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# Explicit Android SDK / NDK configurations for GitHub Actions compatibility
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

# Increase log level for debugging build output
log_level = 2

