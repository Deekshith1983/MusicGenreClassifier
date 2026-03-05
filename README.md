# 🎵 Music Genre Classifier

A deep learning project that classifies music into 10 different genres using a CNN/LSTM model with an interactive Streamlit web interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)

---

# 🌐 View Application

🚀 **Try the Live Application**

👉 **[View Application](https://musicgenreclassifier99.streamlit.app/)**

Upload any music file and instantly classify its genre using the trained deep learning model.

---

## 📖 Project Overview

This project uses deep learning to automatically identify music genres. It includes:

- **Training Notebook**: Train your own model using the GTZAN dataset (1000 songs across 10 genres)
- **Pre-trained Model**: Ready-to-use model with ~75-85% accuracy
- **Web Application**: Beautiful Streamlit interface to classify any music file
- **Real-time Predictions**: Upload a song and get instant genre classification

**Supported Genres:** Blues, Classical, Country, Disco, Hip Hop, Jazz, Metal, Pop, Reggae, Rock

---

## 📋 Prerequisites

Before starting, make sure you have:

### 1. System Requirements
- **Operating System:** Windows, macOS, or Linux
- **RAM:** Minimum 8 GB (16 GB recommended for training)
- **Storage:** ~5 GB free space for dataset and model
- **Internet Connection:** For downloading dataset and dependencies

### 2. Software Requirements
- **Python:** Version 3.8 or higher ([Download Python](https://www.python.org/downloads/))
- **pip:** Python package manager (comes with Python)
- **Git:** (Optional) For cloning repository ([Download Git](https://git-scm.com/downloads))

### 3. Dataset (For Training)
- **GTZAN Dataset:** Available on Kaggle
  - Create account at [kaggle.com](https://www.kaggle.com)
  - Get API token: Account → Settings → API → "Create New API Token"
  - Dataset auto-downloads in the notebook

### 4. Model Files (For Web App)

The repository includes:

- `music_genre_classifier_model.h5` - Pre-trained model  
- `label_encoder.pkl` - Label encoder for genres

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

**Option A: Using Git**

```bash
git clone https://github.com/Deekshith1983/MusicGenreClassifier.git
cd MusicGenreClassifier/music-genre-classifier
```

**Option B: Download ZIP**

- Click **Code → Download ZIP** on GitHub
- Extract the ZIP file
- Open terminal/command prompt in the `music-genre-classifier` folder

---

### Step 2: Create Virtual Environment (Recommended)

**Windows**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements_app.txt
```

This installs all required packages:

- Streamlit (web interface)
- TensorFlow (deep learning)
- Librosa (audio processing)
- Plotly (visualizations)
- And other dependencies

**Installation takes 5–10 minutes depending on your internet speed.**

---

# 🎯 Running the Project

## Option 1: Run the Web App (Quick Start)

1️⃣ **Navigate to project folder**

```bash
cd music-genre-classifier
```

2️⃣ **Activate virtual environment**

Windows

```bash
.\venv\Scripts\Activate.ps1
```

macOS/Linux

```bash
source venv/bin/activate
```

3️⃣ **Start the app**

```bash
streamlit run app.py
```

4️⃣ **Open in browser**

The app automatically opens at:

```
http://localhost:8501
```

5️⃣ **Use the app**

- Upload music file (`.wav`, `.mp3`, `.ogg`, `.flac`)
- Click **🎯 Classify Genre**
- See prediction results instantly

---

## Option 2: Train Your Own Model

1️⃣ Open **Google Colab**

https://colab.research.google.com

Upload:

```
music-genre-classification.ipynb
```

2️⃣ Enable GPU

Runtime → Change Runtime Type → GPU

3️⃣ Upload Kaggle API Key

Upload `kaggle.json` when prompted.

4️⃣ Run All Cells

Training takes **~20–30 minutes**.

5️⃣ Download Model Files

```
music_genre_classifier_model.h5
label_encoder.pkl
```

Place them in:

```
music-genre-classifier/
```

---

# 📁 Project Structure

```
music-genre-classifier/
│
├── app.py
├── music-genre-classification.ipynb
├── music_genre_classifier_model.h5
├── label_encoder.pkl
├── requirements_app.txt
├── model_summary.txt
├── README.md
├── README_APP.md
└── USER_GUIDE.md
```

---

# 🎨 Features

### Web Application

- 🎨 Modern purple gradient UI
- 🎯 Real-time genre classification
- 📊 Interactive confidence charts
- 🎵 Audio preview player
- 📈 Waveform & spectrogram visualization
- 🏆 Top 3 genre predictions
- 🎼 Audio feature analysis

---

### Model

- **Architecture:** Bidirectional LSTM + Attention
- **Input Features:** 58 audio features
- **Output:** 10 genre probabilities
- **Accuracy:** ~75–85%
- **Inference Time:** 1–2 seconds

---

# 🐛 Troubleshooting

### pip install fails

```bash
python -m pip install --upgrade pip
```

---

### Streamlit module error

```bash
pip install -r requirements_app.txt
```

---

### Model loading error

Ensure these files exist:

```
music_genre_classifier_model.h5
label_encoder.pkl
```

---

### App not opening

Open manually:

```
http://localhost:8501
```

---

### Windows Execution Policy Error

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Audio file issue

Convert to `.wav` format.

---

# 📚 Additional Resources

- `README_APP.md` → Detailed app documentation  
- `USER_GUIDE.md` → User guide  
- `model_summary.txt` → Model architecture

---

# 🤝 Contributing

Contributions are welcome!

You can:

- Report bugs
- Improve UI
- Add new music genres
- Enhance model accuracy

---

# 📄 License

This project is for **educational purposes**.

GTZAN dataset credit goes to the original creators.

---

# 🙏 Acknowledgments

- **GTZAN Dataset**
- **TensorFlow**
- **Streamlit**
- **Librosa**

---
