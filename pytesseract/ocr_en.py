from PIL import Image
import pytesseract
import os

# Tesseract 실행 파일 경로 설정 (필요에 따라 수정)
# pytesseract.pytesseract.tesseract_cmd = r'C:\ Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image_english(image_path):
    """
    주어진 이미지 파일에서 영어 텍스트를 추출합니다.
    """
    if not os.path.exists(image_path):
        print(f"오류: 파일을 찾을 수 없습니다 - {image_path}")
        return None

    try:
        # 이미지 열기
        img = Image.open(image_path)

        # 영어(eng) 언어 팩을 사용하여 OCR 수행
        text = pytesseract.image_to_string(img, lang='eng')

        return text
    except Exception as e:
        print(f"OCR 처리 중 오류 발생: {e}")
        return None

if __name__ == "__main__":
    # OCR을 수행할 이미지 파일 경로 (예시: 1.jpeg 또는 다른 영어 텍스트 이미지)
    # 이 부분을 실제 영어 텍스트가 있는 이미지 파일 경로로 변경하세요.
    image_file = "image.png"

    print(f"'{image_file}' 파일에서 영어 텍스트를 추출합니다...")
    extracted_text = ocr_image_english(image_file)

    if extracted_text:
        print("\n--- 추출된 영어 텍스트 ---")
        print(extracted_text)
        print("--------------------------")
    else:
        print("\n영어 텍스트 추출에 실패했습니다.")
