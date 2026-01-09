#!/usr/bin/env python3
"""ZZABIS 앱 아이콘 생성"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    # 1024x1024 크기로 생성 (macOS 권장 크기)
    size = 1024
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 배경 원 (그라데이션 효과를 위해 여러 원)
    center = size // 2
    
    # 외곽 그림자
    for i in range(20):
        offset = 20 - i
        alpha = int(255 * (i / 20) * 0.3)
        draw.ellipse(
            [50 + offset, 50 + offset, size - 50 + offset, size - 50 + offset],
            fill=(0, 0, 0, alpha)
        )
    
    # 메인 원 (보라색 그라데이션)
    # 바깥쪽 진한 보라
    draw.ellipse([50, 50, size - 50, size - 50], fill='#6B21A8')
    # 안쪽 밝은 보라
    draw.ellipse([100, 100, size - 100, size - 100], fill='#7C3AED')
    # 중심 더 밝은 보라
    draw.ellipse([150, 150, size - 150, size - 150], fill='#8B5CF6')
    
    # 마이크 아이콘 그리기
    mic_width = 180
    mic_height = 280
    mic_x = center - mic_width // 2
    mic_y = center - 180
    
    # 마이크 본체 (흰색)
    draw.rounded_rectangle(
        [mic_x, mic_y, mic_x + mic_width, mic_y + mic_height],
        radius=90,
        fill='white'
    )
    
    # 마이크 안쪽 선
    line_y_start = mic_y + 80
    for i in range(3):
        y = line_y_start + i * 50
        draw.rounded_rectangle(
            [mic_x + 40, y, mic_x + mic_width - 40, y + 20],
            radius=10,
            fill='#8B5CF6'
        )
    
    # 마이크 스탠드 (U자형)
    stand_width = 280
    stand_x = center - stand_width // 2
    stand_y = mic_y + mic_height - 60
    
    # U자형 곡선
    draw.arc(
        [stand_x, stand_y, stand_x + stand_width, stand_y + 200],
        start=0, end=180,
        fill='white',
        width=30
    )
    
    # 세로 줄기
    draw.rectangle(
        [center - 15, stand_y + 200, center + 15, stand_y + 280],
        fill='white'
    )
    
    # 받침대
    draw.rounded_rectangle(
        [center - 80, stand_y + 260, center + 80, stand_y + 300],
        radius=15,
        fill='white'
    )
    
    # "Z" 문자 추가 (오른쪽 위)
    try:
        # 시스템 폰트 사용 시도
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 200)
    except:
        font = ImageFont.load_default()
    
    # Z 문자 배경 원
    z_center_x = size - 200
    z_center_y = 200
    draw.ellipse(
        [z_center_x - 100, z_center_y - 100, z_center_x + 100, z_center_y + 100],
        fill='#EC4899'
    )
    
    # Z 문자
    draw.text(
        (z_center_x - 55, z_center_y - 110),
        "Z",
        font=font,
        fill='white'
    )
    
    # PNG로 저장
    png_path = '/Users/hunsangjo/Documents/projects/macvoice/icon.png'
    img.save(png_path, 'PNG')
    print(f"PNG 아이콘 생성: {png_path}")
    
    return png_path

if __name__ == '__main__':
    create_icon()
