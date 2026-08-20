[app]

# (str) Title of your application
title = Cyber-Sentinel

# (str) Package name
package.name = cybersentinel

# (str) Package domain (needed for android packaging)
package.domain = org.cybersentinel

# (str) Source files where the *.py file resides
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Source files to include (let it blank to include all files)
source.include_patterns = assets/*,images/*

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pillow

# (str) Customized icon
#icon.filename = %(source.dir)s/data/icon.png

# (str) Customized presplash
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Supported orientations
orientation = portrait

# (list) The permissions for your application
# e.g. android.permissions = INTERNET,CAMERA
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color
#android.presplash_color = #FFFFFF


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact, storage, etc.
bin_dir = ./bin

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True
