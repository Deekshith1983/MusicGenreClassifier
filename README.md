# 🎵 Music Genre Classifier

A deep learning project that classifies music into 10 different genres using a CNN/LSTM model with an interactive Streamlit web interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)

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
- Click "Code" → "Download ZIP" on GitHub
- Extract the ZIP file
- Open terminal/command prompt in the `music-genre-classifier` folder

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

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

**Installation takes 5-10 minutes depending on your internet speed.**

---

## 🎯 Running the Project

### Option 1: Run the Web App (Quick Start)

1. **Navigate to project folder:**
   ```bash
   cd music-genre-classifier
   ```

2. **Activate virtual environment** (if not already active):
   ```bash
   # Windows
   .\venv\Scripts\Activate.ps1
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Start the app:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   - App automatically opens at `http://localhost:8501`
   - If not, manually visit the URL shown in terminal

5. **Use the app:**
   - Click "Browse files" to upload music file (`.wav`, `.mp3`, `.ogg`, `.flac`)
   - Click "🎯 Classify Genre" button
   - See prediction results with confidence scores!

### Option 2: Train Your Own Model

1. **Open Google Colab:**
   - Go to [Google Colab](https://colab.research.google.com)
   - Upload `music-genre-classification.ipynb`

2. **Enable GPU:**
   - Runtime → Change runtime type → Hardware accelerator → GPU

3. **Upload Kaggle API Key:**
   - When prompted, upload your `kaggle.json` file
   - Notebook will auto-download GTZAN dataset

4. **Run All Cells:**
   - Click Runtime → Run all
   - Training takes ~20-30 minutes on GPU

5. **Download Model:**
   - Download `music_genre_classifier_model.h5`
   - Download `label_encoder.pkl`
   - Place both files in `music-genre-classifier/` folder

---

## 📁 Project Structure

```
music-genre-classifier/
├── app.py                              # Streamlit web application
├── music-genre-classification.ipynb    # Training notebook (Google Colab ready)
├── music_genre_classifier_model.h5     # Pre-trained model
├── label_encoder.pkl                   # Genre label encoder
├── requirements_app.txt                # Python dependencies
├── model_summary.txt                   # Model architecture details
├── README.md                           # This file
├── README_APP.md                       # Detailed app documentation
└── USER_GUIDE.md                       # User guide
```

---

## 🎨 Features

### Web Application
- 🎨 Beautiful purple gradient UI
- 🎯 Real-time genre classification
- 📊 Interactive confidence charts
- 🎵 Audio player to preview uploaded songs
- 📈 Waveform and spectrogram visualizations
- 🏆 Top 3 genre predictions with percentages
- 🎼 Audio feature analysis (tempo, brightness, energy)

### Model
- **Architecture:** Bidirectional LSTM with Attention
- **Input:** 58 audio features (MFCCs, spectral features, tempo, etc.)
- **Output:** 10 genre probabilities
- **Accuracy:** ~75-85% on test set
- **Inference Time:** 1-2 seconds per song

---

## 🐛 Troubleshooting

### Common Issues

**Problem:** `pip install` fails
- **Solution:** Upgrade pip: `python -m pip install --upgrade pip`

**Problem:** "No module named 'streamlit'"
- **Solution:** Activate virtual environment and reinstall: `pip install -r requirements_app.txt`

**Problem:** "Error loading model"
- **Solution:** Ensure `music_genre_classifier_model.h5` is in the same folder as `app.py`

**Problem:** App doesn't open in browser
- **Solution:** Manually open `http://localhost:8501` in your browser

**Problem:** Execution policy error (Windows)
- **Solution:** Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Problem:** Audio file not working
- **Solution:** Convert to `.wav` format or ensure file is not corrupted

---

## 📚 Additional Resources

- **Detailed App Guide:** See `README_APP.md`
- **User Manual:** See `USER_GUIDE.md`
- **Model Details:** See `model_summary.txt`

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation
- Add new genres

---

## 📄 License

This project is for educational purposes. GTZAN dataset credit to original creators.

---

## 🙏 Acknowledgments

- **GTZAN Dataset** - Music genre classification dataset
- **TensorFlow** - Deep learning framework
- **Streamlit** - Web application framework
- **Librosa** - Audio processing library

---


