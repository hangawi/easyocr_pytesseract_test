
import pytesseract

# Tesseract 설치 경로를 지정합니다.
# Windows의 경우, 보통 'C:\Program Files\Tesseract-OCR\tesseract.exe' 와 같은 경로입니다.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def extract_text_from_image(image_path, lang='kor'):
    """
    이미지 파일에서 텍스트를 추출합니다.

    :param image_path: 텍스트를 추출할 이미지 파일의 경로
    :param lang: 추출할 언어 (기본값: 'kor' - 한국어)
    :return: 추출된 텍스트 문자열
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang=lang)
        return text
    except FileNotFoundError:
        return f"오류: 파일을 찾을 수 없습니다 - {image_path}"
    except Exception as e:
        return f"오류가 발생했습니다: {e}"

if __name__ == "__main__":
    # 여기에 이미지 파일 경로를 입력하세요.
    # 예: image_file = 'sample.png'
    image_file = 'image.png'
    
    extracted_text = extract_text_from_image(image_file)
    
    print("--- 추출된 텍스트 ---")
    print(extracted_text)
    print("--------------------")
