import cv2

# 각 변수에 훈련된 얼굴인식 인공지능 xml파일을 넣음.
fece_xml = 'haarcascade_frontalface_default.xml'

# call 변수에 CascadeClassifier 함수를 사용하여 xml 변수에 있는 인공지능을 불러옴.
call_in_face = cv2.CascadeClassifier(fece_xml)

# 다운받은 이미지를 imread 함수를 사용하여 불러옴.
cap = cv2.VideoCapture(0)



while True:
    # Read the frame
    _, img = cap.read() # 캠으로 표시되는 실시간 이미지를 표시.

    img = cv2.flip(img, 2) # 호출된 이미지를 flip 함수를 사용해 뒤집어준다.

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 이미지를 흑백으로 만들어 주어서 노이즈를 제거하여 연산속도 개선.
    
    faces = call_in_face.detectMultiScale(    
        gray,               # 개선된 이미지를 호출.
        scaleFactor=1.05,   # 이미지 스케일 설정
        minNeighbors=5,     # 얼굴 인식 정확성 설정.
        minSize=(150, 150)) # 객체를 탐지할수 있는 범위 사이즈 설정.'

    for (x, y, w, h) in faces: # 캠에 표시되는 얼굴을 인식해 직사각형을 그려줌.
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) # cv2.rectangle(이미지, start_point, end_point, 색상, 두께)

    cv2.imshow('img', img)

    key = cv2.waitKey(33)

    if key != -1:
        key = chr(key)

        if key == 'e':
            print("종료")
            break

        elif key == 's':
            print("캡쳐")
            cv2.imwrite("save image z.jpg", img)

cap.release()

 
