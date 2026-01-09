# ZZABIS - AI 음성 타이핑 도우미

macOS/Windows용 AI 음성 타이핑 앱입니다. 핫키를 누르고 말하면 AI가 음성을 인식하여 텍스트로 변환하고, 선택한 말투 스타일로 자동 입력합니다.

## 주요 기능

- **음성 인식**: OpenAI Whisper API를 통한 정확한 한국어 음성 인식
- **스타일 변환**: GPT-4o-mini를 활용한 10가지 말투 스타일 변환
- **자동 타이핑**: 음성을 텍스트로 변환하여 현재 커서 위치에 자동 입력
- **맞춤법 수정**: AI 기반 자동 맞춤법 교정
- **Push-to-Talk**: 핫키를 누르고 있는 동안만 녹음

## 스타일 모드 (10가지)

| 모드 | 설명 | 예시 |
|------|------|------|
| 그대로 | 맞춤법만 수정 | 원본 유지 |
| 공적 | 격식체 존댓말 | ~습니다, ~합니다 |
| 정중 | 공손한 존댓말 | ~해요, ~세요 |
| 반말 | 친구끼리 반말 | ~야, ~어, ~지 |
| 귀엽게 | 귀여운 말투 | ~용, ~당, ~해용 |
| 애교 | 애교 섞인 말투 | ~잉, ~쪄, ~행 |
| 다정 | 따뜻한 말투 | ~해줄게, ~고 싶어 |
| 쿨하게 | 담담한 말투 | ~임, ㅇㅇ |
| 유머 | 재미있게 | 드립/재치 추가 |
| 비즈니스 | 전문가 말투 | ~드립니다 |

---

## 🚀 초보자를 위한 상세 설치 가이드

### 1단계: Python 설치하기

#### macOS
1. 터미널을 엽니다 (Spotlight에서 "터미널" 검색)
2. Homebrew가 없다면 먼저 설치합니다:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Python 설치:
   ```bash
   brew install python
   ```

#### Windows
1. https://www.python.org/downloads/ 에서 Python 다운로드
2. 설치 시 **"Add Python to PATH"** 체크박스를 반드시 체크!
3. 설치 완료 후 명령 프롬프트(cmd)를 열고 확인:
   ```
   python --version
   ```

### 2단계: 프로젝트 다운로드

#### 방법 1: Git 사용 (추천)
```bash
git clone https://github.com/johunsang/zzabis.git
cd zzabis
```

#### 방법 2: ZIP 다운로드
1. https://github.com/johunsang/zzabis 접속
2. 녹색 "Code" 버튼 클릭
3. "Download ZIP" 클릭
4. 압축 해제 후 폴더로 이동

### 3단계: 가상환경 만들기

#### macOS/Linux
```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

#### Windows
```batch
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate
```

> 💡 가상환경이 활성화되면 터미널 앞에 `(venv)`가 표시됩니다.

### 4단계: 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

설치되는 패키지:
- PyQt6: UI 프레임워크
- pynput: 키보드/마우스 감지
- pyaudio: 오디오 처리
- numpy: 수치 계산
- openai: OpenAI API
- sounddevice: 마이크 입력

### 5단계: OpenAI API 키 발급받기

1. https://platform.openai.com 접속
2. 계정이 없으면 회원가입
3. 우측 상단 프로필 → "API keys" 클릭
4. "Create new secret key" 클릭
5. 생성된 키를 복사 (sk-로 시작하는 긴 문자열)

> ⚠️ **중요**: API 키는 한 번만 표시됩니다! 반드시 안전한 곳에 저장하세요.

### 6단계: 앱 실행하기

```bash
python main.py
```

처음 실행 시:
1. API 키 입력창이 나타납니다
2. 5단계에서 복사한 키를 붙여넣기
3. "확인" 클릭

---

## 🎙️ 사용 방법

### 기본 사용법

1. **앱 실행**: `python main.py`
2. **스타일 선택**: 상단의 스타일 버튼 클릭 (그대로, 공적, 귀엽게 등)
3. **음성 입력**:
   - 핫키를 **누른 상태**로 말하기
   - 핫키를 떼면 자동으로 인식 → 변환 → 입력
4. **결과 확인**: 현재 커서 위치에 텍스트가 자동 입력됨

### 핫키 설정

기본 핫키: **Ctrl+Alt+Z** (또는 마우스 사이드 버튼)

핫키 변경 방법:
1. 우측 상단 ⚙ (설정) 버튼 클릭
2. "키보드 설정" 또는 "마우스 사이드" 버튼 클릭
3. 원하는 키 조합 입력

### 마이크 설정

1. ⚙ 설정 버튼 클릭
2. "마이크" 드롭다운에서 사용할 마이크 선택
3. 설정은 자동 저장됨

---

## 🔧 macOS 권한 설정 (필수!)

핫키가 작동하려면 **두 가지 권한**이 필요합니다.

### 1. 마이크 권한
1. 시스템 설정 → 개인 정보 보호 및 보안 → **마이크**
2. 터미널 (또는 사용 중인 터미널 앱) 체크

### 2. 입력 모니터링 권한 ⚠️ 중요!

키보드/마우스 단축키 감지를 위해 **입력 모니터링** 권한이 필요합니다.

1. 시스템 설정 → 개인 정보 보호 및 보안 → **입력 모니터링**
2. 좌측 하단 자물쇠 클릭 → 잠금 해제
3. **+** 버튼 클릭
4. 실행 방법에 따라 다음 앱 추가:

| 실행 방법 | 권한 줄 앱 |
|-----------|-----------|
| 터미널에서 `python main.py` | 터미널.app |
| `ZZABIS.command` 더블클릭 | 터미널.app |
| `ZZABIS.app` 더블클릭 | ZZABIS.app |

5. 체크박스 켜기

> ⚠️ **주의**: "접근성"이 아닌 **"입력 모니터링"** 권한이 필요합니다!
>
> 💡 권한 변경 후 **터미널/앱을 완전히 종료**하고 다시 열어야 적용됩니다.

---

## ❓ 자주 묻는 질문

### Q: "API 키가 올바르지 않습니다" 오류
- API 키가 `sk-`로 시작하는지 확인
- 키를 다시 복사해서 붙여넣기
- OpenAI 계정에 결제 수단이 등록되어 있는지 확인

### Q: 핫키가 작동하지 않아요
- macOS: **입력 모니터링** 권한 확인 (접근성 아님!)
- 시스템 설정 → 개인 정보 보호 및 보안 → 입력 모니터링 → 터미널 추가
- 권한 추가 후 터미널 완전 종료 → 재시작
- 다른 앱과 핫키가 충돌하는지 확인
- 설정에서 다른 핫키로 변경

### Q: 음성이 인식되지 않아요
- 마이크 권한 확인
- 설정에서 올바른 마이크 선택
- 마이크가 음소거되어 있지 않은지 확인

### Q: 한글이 깨져서 입력돼요
- 한글 입력기(한국어 키보드)가 활성화되어 있는지 확인
- 입력할 앱에서 한글 입력이 가능한지 확인

---

## 📁 파일 구조

```
zzabis/
├── main.py              # 메인 앱 진입점
├── ui.py                # PyQt6 UI 컴포넌트
├── ai_agent.py          # GPT-4o-mini 스타일 변환
├── speech_openai.py     # OpenAI Whisper 음성 인식
├── commands.py          # 키보드/마우스 명령 실행
├── config.py            # 설정 관리
├── settings_dialog.py   # 설정 다이얼로그
├── requirements.txt     # Python 의존성
├── build_mac.sh         # macOS 빌드 스크립트
├── build_windows.bat    # Windows 빌드 스크립트
└── zzabis.spec          # PyInstaller 설정
```

---

## 🏗️ 빌드 (배포용 실행 파일 생성)

### macOS (.app 파일 생성)

```bash
chmod +x build_mac.sh
./build_mac.sh
```
결과물: `dist/ZZABIS.app`

### Windows (.exe 파일 생성)

```batch
build_windows.bat
```
결과물: `dist/ZZABIS.exe`

### PyInstaller 직접 사용

```bash
pip install pyinstaller
pyinstaller zzabis.spec
```

---

## 시스템 요구사항

- macOS 10.15 (Catalina) 이상 또는 Windows 10 이상
- Python 3.9 이상
- 인터넷 연결 (OpenAI API 통신용)
- 마이크

## 라이선스

MIT License
