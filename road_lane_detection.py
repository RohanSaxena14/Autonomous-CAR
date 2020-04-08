import cv2
import numpy as np

def nothing(pos):
    print(pos)

def region_of_interest(frame, vertices):
    mask = np.zeros_like(frame)
    channel_count = frame.shape[2]
    #match_mask_color = (255,) * channel_count
    match_mask_color = (255,255,255)
    cv2.fillPoly(mask, np.array([vertices], np.int32), match_mask_color)
    masked_image = cv2.bitwise_and(frame, mask)
    return masked_image

#img = cv2.imread("lane.jpg")
cv2.namedWindow("road")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cap = cv2.VideoCapture("road.mp4")
_, frame = cap.read()

vertices = [(0, 300), (int(frame.shape[1]/2), int(3*frame.shape[0]/4)), (1000, 375), (frame.shape[1], frame.shape[0]), (0, frame.shape[0])]

#cv2.createTrackbar("min", "image", 0, 200, nothing)
#cv2.createTrackbar("max", "image", 0, 400, nothing)

while cap.isOpened():
    _, frame = cap.read()
    frame_roc = region_of_interest(frame, vertices)
    #frame_roc = cv2.cvtColor(frame_roc, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(frame_roc, 50, 200)
    #a = cv2.getTrackbarPos("min", "image")
    #b = cv2.getTrackbarPos("max", "image")
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=100)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("road", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()