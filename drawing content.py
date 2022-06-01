import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (0, 0), (150, 30), (255, 0, 0), -1)
    cv2.putText(frame, 'Web Cam: 0', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()