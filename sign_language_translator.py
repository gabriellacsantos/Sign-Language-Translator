import cv2
import numpy as np
from tensorflow.keras.models import load_model
from google.colab.patches import cv2_imshow

# Load the pre-trained model
model = load_model('sign_language_model.h5')

# Define the dictionary for letters
letters = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

# Function to capture video from the webcam
def video_capture():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Define the region of interest (ROI)
        x1, y1, x2, y2 = 100, 100, 300, 300
        roi = frame[y1:y2, x1:x2]

        # Preprocess the ROI
        roi = cv2.resize(roi, (64, 64))
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        roi = np.expand_dims(roi, axis=2)
        roi = np.expand_dims(roi, axis=0)

        # Make a prediction
        pred = model.predict(roi)
        letter = letters[np.argmax(pred)]

        # Display the resulting frame with the prediction
        cv2.putText(frame, letter, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2_imshow(frame)  # Use cv2_imshow in Colab
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Start video capture
video_capture()