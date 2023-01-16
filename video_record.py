import datetime
import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    
    ret, frame = capture.read()
    img = cv2.flip(frame, 2) # x축 혹은 y축을 기준으로 이미지를 뒤집을 수 있고 둘 다 기준으로 이미지를 뒤집을 수 있음 2번째 인자 값에 따라 달라짐.
    cv2.imshow("VideoFrame", img)

    faces = face_cascade.detectMultiScale(    
        img,               # 개선된 이미지를 호출.
        scaleFactor=1.05,   # 이미지 스케일 설정
        minNeighbors=5,     # 얼굴 인식 정확성 설정.
        minSize=(150, 150)) # 객체를 탐지할수 있는 범위 사이즈 설정.'

    for (x, y, w, h) in faces: # 캠에 표시되는 얼굴을 인식해 직사각형을 그려줌.
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) # cv2.rectangle(이미지, start_point, end_point, 색상, 두께)

    cv2.imshow('img', img)
 
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")

    key = cv2.waitKeyEx(33)

    if key != -1:
        key = chr(key)
        
        if key == "q":
            print("캡쳐")
            cv2.imwrite("./didtpals/" + str(now) + ".png", img)
        elif key == "r":
            print("녹화 시작")
            record = True
            video = cv2.VideoWriter("./didtpals/" + str(now) + ".avi", fourcc, 20.0, (img.shape[1], img.shape[0]))
        elif key == "e":
            print("녹화 중지")
            record = False
            video.release()
        elif key == "w":
            print("종료")
            break
    if record == True:
        print("녹화 중..")
        video.write(img)

capture.release()
cv2.destroyAllWindows()


