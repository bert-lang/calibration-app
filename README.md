# Calibration Calculator App

This is a Python + Kivy application for generating calibration tables
for horizontal cylindrical tanks.

## Features
- Tank diameter and length input
- Unit support: mm / cm / m
- Adjustable liter step
- Scrollable calibration table
- Android APK ready using Buildozer

## Files
- `main.py` – Kivy user interface
- `calibration.py` – Calibration math logic
- `requirements.txt` – Python dependencies

## Build APK (Linux / WSL)
```bash
buildozer android debug

