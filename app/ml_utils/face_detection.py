import cv2 as cv
def face_detection(image):
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + '/haarcascade_frontalface_default.xml')

    image = image

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.01,
        minNeighbors=10,
        minSize=(100, 100),
        flags = cv.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image, len(faces)