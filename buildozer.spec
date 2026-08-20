[app]
title = NSS Cyber-Sentinel
package.name = cybersentinel
package.domain = com.nss.sentinel

# Source directory and version fix
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3,flet,requests
android.permissions = INTERNET,ACCESS_WIFI_STATE,ACCESS_FINE_LOCATION
android.archs = arm64-v8a
fullscreen = 0
orientation = portrait
