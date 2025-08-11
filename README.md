# OCR 프로젝트: easyocr vs. pytesseract

이 프로젝트는 Python의 두 가지 대표적인 OCR(광학 문자 인식) 라이브러리인 `easyocr`과 `pytesseract`를 사용하여 이미지에서 텍스트를 추출하는 방법을 비교하고 기록하기 위해 만들어졌습니다.

## 📖 프로젝트 개요

`image.png` 파일에 포함된 영어와 한국어 텍스트를 `easyocr`과 `pytesseract`를 이용해 각각 추출하고, 그 과정과 결과를 비교 분석합니다. 이를 통해 각 라이브러리의 장단점과 사용법을 익힙니다.

## 📚 사용한 라이브러리

-  **easyocr**: GPU를 활용할 수 있으며, 다국어 지원이 강력한 사용자 친화적인 OCR 라이브러리입니다.
-  **pytesseract**: Google의 Tesseract OCR 엔진을 Python에서 사용할 수 있도록 하는 래퍼(wrapper) 라이브러리입니다.

## ⚙️ 설치 및 설정 과정

### Python 라이브러리 설치

프로젝트에 필요한 Python 라이브러리들을 설치합니다. 가상 환경을 사용하는 것을 권장합니다.

```bash
# 가상 환경 생성 (선택 사항이지만 권장)
python -m venv venv
# 가상 환경 활성화 (Windows)
.\venv\Scripts\activate
# 가상 환경 활성화 (macOS/Linux)
source venv/bin/activate

# easyocr과 의존성 라이브러리 설치
pip install easyocr

# pytesseract 설치
pip install pytesseract
```

### Tesseract-OCR 엔진 설치 (pytesseract 사용 시 필수)

`pytesseract`는 Tesseract 엔진이 시스템에 별도로 설치되어 있어야 합니다.

-  **Windows:** [Tesseract 공식 설치 프로그램](https://github.com/UB-Mannheim/tesseract/wiki)을 다운로드하여 설치합니다.
   -  설치 과정에서 **"Add Tesseract to the system PATH"** 옵션을 반드시 체크하는 것이 좋습니다. 이렇게 하면 스크립트에서 Tesseract 실행 파일의 경로를 직접 지정할 필요가 없어집니다.
   -  만약 PATH에 추가하지 않았다면, Python 스크립트 상단에 다음과 같이 경로를 명시해야 합니다.
      ```python
      import pytesseract
      pytesseract.pytesseract.tesseract_cmd = r'C:\ Program Files\Tesseract-OCR\tesseract.exe'
      ```
-  **macOS (Homebrew 사용):**
   ```bash
   brew install tesseract
   brew install tesseract-lang
   ```
-  **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr
   sudo apt install tesseract-ocr-kor tesseract-ocr-eng # 한국어, 영어 언어팩 설치
   ```

### 설치 과정에서 발생할 수 있는 문제 및 해결

1. **`pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH` 오류:**

   -  **원인:** Tesseract OCR 엔진이 설치되지 않았거나, 설치되었더라도 시스템 PATH에 등록되지 않아 `pytesseract` 라이브러리가 Tesseract 실행 파일을 찾지 못하는 경우입니다.
   -  **해결:** 위 "Tesseract-OCR 엔진 설치" 섹션을 참조하여 Tesseract를 올바르게 설치하고, PATH에 추가되었는지 확인합니다. Windows의 경우 설치 시 "Add Tesseract to the system PATH" 옵션을 체크하거나, 수동으로 환경 변수를 설정해야 합니다. 또는 `pytesseract.pytesseract.tesseract_cmd`에 Tesseract 실행 파일의 절대 경로를 직접 지정해 줍니다.

2. **`ModuleNotFoundError: No module named 'easyocr'` 또는 `No module named 'pytesseract'` 오류:**

   -  **원인:** 해당 Python 라이브러리가 현재 활성화된 Python 환경에 설치되지 않은 경우입니다.
   -  **해결:** `pip install easyocr` 또는 `pip install pytesseract` 명령어를 사용하여 라이브러리를 설치합니다. 가상 환경을 사용 중이라면, 가상 환경이 올바르게 활성화되었는지 확인한 후 설치를 진행합니다.

3. **OCR 결과가 제대로 나오지 않는 경우 (언어팩 문제):**
   -  **원인:** Tesseract의 경우, 인식하려는 언어에 해당하는 언어팩이 설치되지 않았거나, 코드에서 올바른 언어 코드를 지정하지 않은 경우입니다.
   -  **해결:** Tesseract의 경우 `tesseract-ocr-kor` (한국어), `tesseract-ocr-eng` (영어) 등 필요한 언어팩을 설치했는지 확인합니다. 코드에서 `lang='kor'` 또는 `lang='eng'`와 같이 올바른 언어 코드를 사용했는지 확인합니다.

## ▶️ 실행 방법

각 스크립트는 터미널에서 다음 명령어를 통해 실행할 수 있습니다. (프로젝트 루트 디렉토리에서 실행한다고 가정)

```bash
# easyocr 예제 실행
python easyocr/easy_ocr_example.py

# pytesseract 한국어 예제 실행
python pytesseract/ocr.py

# pytesseract 영어 예제 실행
python pytesseract/ocr_en.py
```


## 📎 첨부 파일

더 자세한 프로젝트 설명 및 분석 내용은 다음 파일을 참조하십시오:

-   [프로젝트 상세 설명 (PDF)](images/1.pdf)