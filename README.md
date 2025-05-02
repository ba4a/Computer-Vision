

---

```markdown
# 🪙 Coin Detector & Classifier Web App

This is a Streamlit-based web application for detecting and classifying coins from images. The app uses image processing (via OpenCV) and machine learning (via `sklearn`'s MLPClassifier) to identify coin materials and values based on shape and color features.

## 📦 Features

- Detects circular coins using Hough Circle Transform
- Classifies coin material: **Copper** or **Silver**
- Estimates coin denomination based on diameter and material
- Provides a GUI for uploading and analyzing images
- Displays annotated output with classification and total value in MKD

## 🖼️ Folder Structure

Before running, make sure you have the following structure:

```

project/
│
├── Images/
│   ├── copper/
│   │   ├── image1.jpg
│   │   └── ...
│   └── silver/
│       ├── image1.jpg
│       └── ...
├── app.py
└── README.md

````

## 🔧 Installation

Install all required packages using:

```bash
pip install streamlit opencv-python==4.8.0.76 numpy==1.24.4 scikit-learn==1.3.2 ipykernel==6.29.3 matplotlib==3.7.3
````

Alternatively:

```bash
pip install streamlit opencv-python-headless scikit-learn numpy
```

## 🚀 Running the App

To start the Streamlit app:

```bash
streamlit run app.py
```

Make sure your working directory contains the `Images/` folder for training data.

## 🧠 How It Works

1. **Training Phase**:

   * Extracts color histograms from training images of copper and silver coins.
   * Trains a Multi-layer Perceptron (MLP) classifier.

2. **Prediction Phase**:

   * Upload an image via the Streamlit interface.
   * Detects coins using Hough Circle Transform.
   * Classifies material using the trained model.
   * Estimates value using measured diameters and predefined known dimensions.

## 📌 Dependencies

* `streamlit`
* `opencv-python==4.8.0.76` *(or `opencv-python-headless`)*
* `numpy==1.24.4`
* `scikit-learn==1.3.2`
* `ipykernel==6.29.3`
* `matplotlib==3.7.3`

## 📷 Example

Upload an image containing coins and the app will return the processed image with:

* Coin material (Copper/Silver)
* Estimated denomination
* Total value in MKD

## 🛠 Notes

* Training happens every time the app is launched. For large datasets, consider persisting the trained model.
* Coins should be placed flat and clearly visible for best accuracy.

## 📃 License

This project is provided for educational purposes.

---

```

Let me know if you'd like a `requirements.txt` file or a `Dockerfile` as well.
```


```markdown
# 🪙 Coin Detector & Classifier Web App

This is a Streamlit-based web application for detecting and classifying coins from images. The app uses image processing (via OpenCV) and machine learning (via `sklearn`'s MLPClassifier) to identify coin materials and values based on shape and color features.

## 📦 Features

- Detects circular coins using Hough Circle Transform
- Classifies coin material: **Copper** or **Silver**
- Estimates coin denomination based on diameter and material
- Provides a GUI for uploading and analyzing images
- Displays annotated output with classification and total value in MKD





## 🔧 Installation

Install all required packages using:

```bash
pip install streamlit opencv-python==4.8.0.76 numpy==1.24.4 scikit-learn==1.3.2 ipykernel==6.29.3 matplotlib==3.7.3
````

Alternatively:

```bash
pip install streamlit opencv-python-headless scikit-learn numpy
```

## 🚀 Running the App

To start the Streamlit app:

```bash
streamlit run app.py
```

Make sure your working directory contains the `Images/` folder for training data.

## 🧠 How It Works

1. **Training Phase**:

   * Extracts color histograms from training images of copper and silver coins.
   * Trains a Multi-layer Perceptron (MLP) classifier.

2. **Prediction Phase**:

   * Upload an image via the Streamlit interface.
   * Detects coins using Hough Circle Transform.
   * Classifies material using the trained model.
   * Estimates value using measured diameters and predefined known dimensions.

## 📌 Dependencies

* `streamlit`
* `opencv-python==4.8.0.76` *(or `opencv-python-headless`)*
* `numpy==1.24.4`
* `scikit-learn==1.3.2`
* `ipykernel==6.29.3`
* `matplotlib==3.7.3`

## 📷 Example

Upload an image containing coins and the app will return the processed image with:

* Coin material (Copper/Silver)
* Estimated denomination
* Total value in MKD

## 🛠 Notes

* Training happens every time the app is launched. For large datasets, consider persisting the trained model.
* Coins should be placed flat and clearly visible for best accuracy.



