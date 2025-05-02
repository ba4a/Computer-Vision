

import cv2
import numpy as np
import glob
import math
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import streamlit as st

# Define classes
class Enum(tuple): __getattr__ = tuple.index
Material = Enum(('Copper', 'Silver'))

# Histogram function
def get_histogram(image):
    mask = np.zeros(image.shape[:2], dtype="uint8")
    (width, height) = (int(image.shape[1] / 2), int(image.shape[0] / 2))
    cv2.circle(mask, (width, height), 60, 255, -1)
    hist = cv2.calcHist([image], [0, 1, 2], mask, [8, 8, 8],
                        [0, 256, 0, 256, 0, 256])
    return cv2.normalize(hist, hist).flatten()

def get_hist_from_file(file):
    img = cv2.imread(file)
    return get_histogram(img)

def get_material(clf, roi):
    hist = get_histogram(roi)
    s = clf.predict([hist])
    return Material[int(s)]

# Load training data
images_copper = glob.glob("Images/copper/*")
images_silver = glob.glob("Images/silver/*")
X = []
y = []

for i in images_copper:
    X.append(get_hist_from_file(i))
    y.append(Material.Copper)
for i in images_silver:
    X.append(get_hist_from_file(i))
    y.append(Material.Silver)

clf = MLPClassifier(solver="lbfgs")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf.fit(X_train, y_train)
print("Classifier trained.")

# Known diameters for classification
known_diameters = {
    '10 den': [19.25, 0.75, 'Silver', 10],
    '50 den': [21.45, 1.45, 'Silver', 50],
    '1 den': [17.95, 1.25, 'Copper', 1],
    '2 den': [20.45, 1.25, 'Copper', 2],
    '5 den': [22.95, 2.5, 'Copper', 5]
}

def process_image(input_image):
    image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)

    d = 1024 / image.shape[1]
    dim = (1024, int(image.shape[0] * d))
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    output = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=2.2, minDist=100,
                               param1=200, param2=100, minRadius=50, maxRadius=120)

    diameter = []
    materials = []
    coordinates = []
    count = 0

    if circles is not None:
        for (x, y, r) in circles[0, :]:
            diameter.append(r)
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, d) in circles:
            count += 1
            coordinates.append((x, y))
            roi = image[y - d:y + d, x - d:x + d]
            material = get_material(clf, roi)
            materials.append(material)
            cv2.circle(output, (x, y), d, (187, 255, 0), 2)
            cv2.putText(output, material, (x - 40, y), cv2.FONT_HERSHEY_PLAIN,
                        1.5, (187, 255, 0), 2, cv2.LINE_AA)

        biggest = max(diameter)
        i = diameter.index(biggest)

        if materials[i] == "Silver":
            diameter = [x / biggest * 19.45 for x in diameter]
            scaledTo = "Scaled to 50 denars"
        elif materials[i] == "Copper":
            diameter = [x / biggest * 21.95 for x in diameter]
            scaledTo = "Scaled to 5 denars"
        else:
            scaledTo = "unable to scale.."

        i = 0
        total = 0
        while i < len(diameter):
            d = diameter[i]
            m = materials[i]
            (x, y) = coordinates[i]
            t = "Unknown"

            for key in known_diameters:
                if math.isclose(d, known_diameters[key][0], abs_tol=known_diameters[key][1]) and m == known_diameters[key][2]:
                    t = key
                    total += known_diameters[key][3]

            cv2.putText(output, t, (x - 40, y + 22), cv2.FONT_HERSHEY_PLAIN,
                        1.5, (3, 186, 252), 2, cv2.LINE_AA)
            i += 1

        output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        return output_rgb, f"Coins detected: {count}, Total: MKD {total}, {scaledTo}"
    else:
        return input_image, "No coins detected"



    st.title("Coin Detector & Classifier")
st.write("Upload a coin image to detect and classify its value")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image_rgb, caption='Uploaded Image.', use_container_width=True)
    st.write("")
    st.write("Classifying...")

    output_image, summary = process_image(image_rgb)
    st.image(output_image, caption='Processed Image.', use_container_width=True)
    st.write(summary)

