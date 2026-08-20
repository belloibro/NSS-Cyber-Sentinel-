[app]

# (str) Title of your application
title = Cyber-Sentinel

# (str) Package name
package.name = cybersentinel

# (str) Package domain (needed for android packaging)
package.domain = org.cybersentinel

# (str) Source code where the main.py lives
source.dir = .

# (str) Source files where the *.py file resides
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pillow

# (list) Supported orientations
orientation = portrait

# (list) The permissions for your application
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Fullscreen
fullscreen = 0


[buildozer]

# (int) Log level
log_level = 2

# (str) Path to build artifact, storage, etc.
bin_dir = ./bin

# (bool) Accept Android SDK licenses automatically
android.accept_sdk_license = True
