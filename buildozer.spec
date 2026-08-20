[app]

# (str) Title of your application
title = Cyber-Sentinel

# (str) Package name
package.name = cybersentinel

# (str) Package domain (needed for android packaging)
package.domain = org.cybersentinel

# (str) Source files to include (let it find python files)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET
