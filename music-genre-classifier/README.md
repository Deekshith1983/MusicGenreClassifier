# 🎵 Music Genre Classification using CNN

A deep learning project that classifies music into 10 different genres using Convolutional Neural Networks (CNN) trained on mel-spectrogram features.

## 📋 Project Overview

This project implements a music genre classifier using:
- **Deep Learning**: CNN architecture with 4 convolutional blocks
- **Audio Processing**: Mel-spectrogram feature extraction using librosa
- **Dataset**: GTZAN Dataset (1000 audio files, 10 genres)
- **Interface**: Interactive Streamlit web application

## 🎯 Genres Supported

The model classifies music into 10 genres:
- Blues
- Classical
- Country
- Disco
- Hip-hop
- Jazz
- Metal
- Pop
- Reggae
- Rock

## 🏗️ Model Architecture

### CNN Structure:
```
Input (128 x 1293 x 1) - Mel-spectrogram
    ↓
Conv2D(32) → BatchNorm → ReLU → MaxPool → Dropout(0.25)
    ↓
Conv2D(64) → BatchNorm → ReLU → MaxPool → Dropout(0.25)
    ↓
Conv2D(128) → BatchNorm → ReLU → MaxPool → Dropout(0.25)
    ↓
Conv2D(256) → BatchNorm → ReLU → MaxPool → Dropout(0.3)
    ↓
Flatten → Dense(256) → Dropout(0.5)
    ↓
Dense(128) → Dropout(0.4)
    ↓
Dense(10, softmax) - Output
```

### Training Details:
- **Optimizer**: Adam (lr=0.001)
- **Loss**: Categorical Crossentropy
- **Batch Size**: 32
- **Epochs**: 50 (with early stopping)
- **Data Split**: 70% train, 15% validation, 15% test

## 📁 Project Structure

```
music-genre-classifier/
│
├── ModelTraining.ipynb          # Complete training pipeline
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
│
├── data/                         # Dataset directory
│   └── (GTZAN dataset goes here)
│
├── models/                       # Saved models
│   ├── music_genre_cnn.h5       # Trained model
│   └── label_encoder.npy        # Label encoder
│
└── utils/                        # Utility scripts
```

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- numpy
- librosa
- tensorflow
- scikit-learn
- matplotlib
- streamlit
- soundfile
- pandas
- seaborn

### 2. Download Dataset

Download the GTZAN dataset from Kaggle:

**Option 1: Using Kaggle API**
```bash
# Install Kaggle CLI
pip install kaggle

# Download dataset
kaggle datasets download -d andradaolteanu/gtzan-dataset-music-genre-classification

# Unzip to project directory
unzip gtzan-dataset-music-genre-classification.zip -d data/
```

**Option 2: Manual Download**
1. Visit: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification
2. Download and extract to `data/` folder

### 3. Train the Model

Open and run the Jupyter notebook:

```bash
jupyter notebook ModelTraining.ipynb
```

**Training steps in the notebook:**
1. Import libraries
2. Load and explore dataset
3. Extract mel-spectrogram features
4. Build CNN model
5. Train with callbacks (early stopping, model checkpoint)
6. Evaluate performance
7. Visualize results (confusion matrix, accuracy plots)

**Expected training time:** 15-30 minutes (depends on hardware)

### 4. Run the Web Application

```bash
streamlit run app.py
```

This will launch an interactive web interface where you can:
- Upload audio files (WAV, MP3, OGG, FLAC)
- Get instant genre predictions
- View confidence scores for all genres
- Visualize mel-spectrogram

## 📊 Feature Extraction

The model uses **mel-spectrograms** as input features:

- **Mel-spectrogram**: Represents audio frequency content over time
- **Dimensions**: 128 mel bands × 1293 time frames
- **Normalization**: Scaled to [0, 1] range
- **Advantages**: Captures both temporal and spectral information

## 🎯 Model Performance

Expected performance metrics:
- **Test Accuracy**: ~75-85% (typical for GTZAN)
- **Training Time**: 15-30 minutes
- **Inference Time**: <1 second per audio file

Performance varies by genre:
- High accuracy: Classical, Metal, Jazz
- Challenging: Rock vs Metal, Pop vs Disco

## 🔧 Customization

### Modify Model Architecture
Edit the `build_cnn_model()` function in the notebook:
```python
def build_cnn_model(input_shape, num_classes):
    # Add/remove layers
    # Change filter sizes
    # Adjust dropout rates
```

### Change Audio Parameters
```python
SAMPLE_RATE = 22050  # Audio sampling rate
DURATION = 30        # Audio duration in seconds
N_MELS = 128        # Number of mel bands
```

### Adjust Training Settings
```python
EPOCHS = 50
BATCH_SIZE = 32
LEARNING_RATE = 0.001
```

## 📈 Results Visualization

The notebook includes:
1. **Training History Plots**: Accuracy and loss over epochs
2. **Confusion Matrix**: Shows prediction patterns
3. **Per-Genre Accuracy**: Individual genre performance
4. **Sample Predictions**: Test on specific audio files

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Audio signal processing with librosa
- ✅ CNN architecture for time-series data
- ✅ Transfer learning concepts (spectrograms as images)
- ✅ Model evaluation and visualization
- ✅ Deployment with Streamlit
- ✅ End-to-end ML pipeline (data → model → deployment)

## 🛠️ Troubleshooting

**Issue**: Low accuracy
- Solution: Train for more epochs, increase model capacity, or use data augmentation

**Issue**: Overfitting
- Solution: Increase dropout rates, add more data, or use regularization

**Issue**: Audio loading errors
- Solution: Ensure librosa and soundfile are properly installed

**Issue**: GPU not detected
- Solution: Install tensorflow-gpu or use CPU (slower but works)

## 📚 Dataset Information

**GTZAN Dataset:**
- **Size**: ~1.2 GB
- **Format**: WAV files (mono, 22050 Hz)
- **Duration**: 30 seconds per track
- **Total tracks**: 1000 (100 per genre)
- **Source**: Collected by George Tzanetakis

## 🚀 Future Improvements

Potential enhancements:
- [ ] Data augmentation (pitch shift, time stretch)
- [ ] Use MFCCs alongside mel-spectrograms
- [ ] Try recurrent layers (LSTM/GRU)
- [ ] Implement attention mechanisms
- [ ] Test on other datasets (FMA, Million Song Dataset)
- [ ] Real-time audio streaming classification
- [ ] Mobile app deployment

## 📝 Requirements

```
Python 3.8+
TensorFlow 2.x
librosa
scikit-learn
matplotlib
streamlit
```

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Improve documentation
- Optimize model architecture

## 📄 License

This project uses the GTZAN dataset for educational purposes.

## 🙏 Acknowledgments

- GTZAN Dataset: George Tzanetakis
- Librosa: Audio processing library
- TensorFlow/Keras: Deep learning framework

---

**Built with ❤️ using TensorFlow and Librosa**

⭐ Star this project if you found it helpful!
