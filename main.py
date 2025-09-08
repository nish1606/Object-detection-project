from ultralytics import YOLO
import cvzone
import cv2

model = YOLO('yolov10n.pt')

# live webcam
cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    results = model(image, stream=True)

    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype('int32')
            confidence = int(box.conf[0].cpu().numpy() * 100)
            class_detected_number = int(box.cls[0].cpu().numpy())
            class_detected_name = model.names[class_detected_number]

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
            cvzone.putTextRect(image, f'{class_detected_name} {confidence}%', (x1 + 8, y1 - 10), scale=0.5, thickness=1, border=1,colorT=(0, 0, 0), colorR=(255, 255, 255), colorB=(0, 255, 255) )

    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()