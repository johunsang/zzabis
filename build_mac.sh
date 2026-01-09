#!/bin/bash
# ZZABIS macOS 빌드 스크립트

echo "==================================="
echo "  ZZABIS macOS 빌드"
echo "==================================="

# 가상환경 활성화
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# PyInstaller 설치
pip install pyinstaller

# 이전 빌드 정리
rm -rf build dist *.spec

# 빌드 (onedir 모드 사용)
pyinstaller --name "ZZABIS" \
    --windowed \
    --hidden-import "PyQt6" \
    --hidden-import "PyQt6.QtCore" \
    --hidden-import "PyQt6.QtGui" \
    --hidden-import "PyQt6.QtWidgets" \
    --hidden-import "pynput" \
    --hidden-import "pynput.keyboard" \
    --hidden-import "pynput.mouse" \
    --hidden-import "sounddevice" \
    --hidden-import "numpy" \
    --hidden-import "openai" \
    --hidden-import "pyperclip" \
    --hidden-import "pyautogui" \
    --osx-bundle-identifier "com.zzabis.app" \
    main.py

echo ""
echo "빌드 완료!"
echo "결과물: dist/ZZABIS.app"
