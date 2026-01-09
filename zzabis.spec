# -*- mode: python ; coding: utf-8 -*-
import os

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PyQt6',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
        'PyQt6.sip',
        'pynput',
        'pynput.keyboard',
        'pynput.mouse',
        'pynput.keyboard._darwin',
        'pynput.mouse._darwin',
        'sounddevice',
        'numpy',
        'openai',
        'pyperclip',
        'pyautogui',
        'certifi',
        'httpx',
        'httpcore',
        'anyio',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'PIL', 'matplotlib'],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ZZABIS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='ZZABIS',
)

app = BUNDLE(
    coll,
    name='ZZABIS.app',
    icon='icon.icns' if os.path.exists('icon.icns') else None,
    bundle_identifier='com.zzabis.app',
    info_plist={
        'CFBundleName': 'ZZABIS',
        'CFBundleDisplayName': 'ZZABIS',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSMicrophoneUsageDescription': '음성 인식을 위해 마이크 접근이 필요합니다.',
        'NSAppleEventsUsageDescription': '키보드 입력을 위해 접근성 권한이 필요합니다.',
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.15.0',
    },
)
