name: Compile Cyber-Sentinel APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Git Identity
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "GitHub Action"

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Setup Android SDK
        uses: android-actions/setup-android@v3

      - name: Install Buildozer and Cython
        run: |
          pip install --upgrade pip
          pip install Cython==0.29.36 buildozer

      - name: Build APK with Buildozer
        run: buildozer android debug

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: cybersentinel-release-apk
          path: bin/*.apk
