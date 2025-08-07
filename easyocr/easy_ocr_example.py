import easyocr
import os

# 한국어 및 영어 언어에 대한 EasyOCR Reader 인스턴스 생성
# GPU 사용을 원하시면 'gpu=True' 옵션을 추가하세요.
reader = easyocr.Reader(['ko', 'en'])

# 이미지 파일 경로 설정
# 중요: 아래 파일 경로는 예시이므로, 실제 이미지 파일 경로로 수정해야 합니다.
image_path = 'image.png' 

# 파일 존재 여부 확인
if not os.path.exists(image_path):
    print(f"오류: 이미지 파일이 '{image_path}' 경로에 없습니다. 파일을 확인해주세요.")
else:
    # 이미지에서 텍스트 인식
    # detail=0 을 사용하면 인식된 텍스트만 반환합니다.
    results = reader.readtext(image_path, detail=0)

    # 인식된 텍스트 출력
    if results:
        print("인식된 텍스트:")
        for text in results:
            print(text)
    else:
        print("이미지에서 텍스트를 찾을 수 없습니다.")