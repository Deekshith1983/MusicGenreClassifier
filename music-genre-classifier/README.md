# 🎵 Music Genre Classifier - Web App

A beautiful, interactive web application for classifying music genres using deep learning!

![Music Genre Classifier](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange.svg)

## ✨ Features

- 🎨 **Beautiful Gradient UI** - Eye-catching purple gradient design
- 🎯 **Real-time Classification** - Instant genre prediction
- 📊 **Interactive Visualizations** - Waveform & spectrogram plots
- 🎼 **Audio Feature Analysis** - Tempo, brightness, energy metrics
- 📈 **Confidence Scores** - See prediction probabilities for all genres
- 🎧 **Audio Preview** - Listen to your uploaded music
- 🏆 **Top 3 Predictions** - View alternative genre possibilities

## 🎭 Supported Genres

- 🎸 Blues
- 🎻 Classical
- 🤠 Country
- 🕺 Disco
- 🎤 Hip Hop
- 🎷 Jazz
- 🤘 Metal
- 🎵 Pop
- 🏝️ Reggae
- 🎸 Rock

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Trained model files:
  - `music_genre_classifier_model.h5`
  - `label_encoder.pkl`

### Installation

1. **Clone or navigate to the directory:**
   ```bash
   cd music-genre-classifier
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements_app.txt
   ```

3. **Ensure model files are present:**
   ```
   music-genre-classifier/
   ├── app.py
   ├── music_genre_classifier_model.h5  ← Required
   ├── label_encoder.pkl                 ← Required
   └── requirements_app.txt
   ```

### Running the App

1. **Start the Streamlit server:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser:**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in terminal

3. **Upload and classify:**
   - Click "Browse files" or drag & drop an audio file
   - Supported formats: `.wav`, `.mp3`, `.ogg`, `.flac`
   - Click "🎯 Classify Genre" button
   - View predictions and visualizations!

## 📸 Screenshots

### Main Interface
- Beautiful purple gradient background
- Drag & drop file upload
- Real-time audio preview

### Prediction Results
- Large, bold genre prediction
- Confidence percentage
- Interactive confidence chart for all genres

### Audio Analysis
- Waveform visualization
- Mel spectrogram heatmap
- Audio feature metrics (Tempo, Brightness, Energy, etc.)

## 🎯 How It Works

1. **Upload Audio** - User uploads a music file
2. **Feature Extraction** - Extract mel-spectrogram features using librosa
3. **Deep Learning Prediction** - LSTM with Attention model processes features
4. **Results Display** - Show predicted genre with confidence scores
5. **Visualizations** - Display waveforms, spectrograms, and audio metrics

## 🧠 Model Architecture

- **Type:** Bidirectional LSTM with Attention Mechanism
- **Input:** Mel-spectrogram features (128 x 174)
- **Layers:**
  - 3 Bidirectional LSTM layers (256, 128, 64 units)
  - Custom attention mechanism
  - Batch normalization
  - Dropout regularization
- **Output:** 10 genre probabilities
- **Accuracy:** ~75-85% on test set

## 📊 Audio Features Displayed

| Feature | Description |
|---------|-------------|
| **Tempo** | Beats per minute (BPM) |
| **Brightness** | Spectral centroid (Hz) |
| **Rolloff** | Spectral rolloff frequency (Hz) |
| **ZCR** | Zero crossing rate |
| **Energy** | RMS energy level |

## 🎨 UI Features

### Color Scheme
- Primary: Purple gradient (`#667eea` to `#764ba2`)
- Accent: Pink gradient for predictions
- Genre colors: Each genre has unique color

### Interactive Elements
- Hover effects on buttons
- Animated transitions
- Responsive design
- Dark theme charts

### Customization
You can customize the UI by modifying the CSS in `app.py`:
- Change gradient colors
- Adjust card styles
- Modify chart themes

## 📁 Project Structure

```
music-genre-classifier/
├── app.py                              # Streamlit web application
├── music_genre_classifier_model.h5     # Trained LSTM model
├── label_encoder.pkl                   # Genre label encoder
├── requirements_app.txt                # Python dependencies
├── README_APP.md                       # This file
└── sample_music/                       # (Optional) Sample audio files
```

## 🔧 Configuration

### Sidebar Settings
- **Show Visualizations** - Toggle waveform/spectrogram plots
- **Show Audio Features** - Toggle feature metrics display

### Model Parameters
To use a different model:
1. Update model path in `load_model_and_encoder()` function
2. Ensure label encoder matches model classes

## 🐛 Troubleshooting

### Common Issues

**❌ "Error loading model"**
- Ensure `music_genre_classifier_model.h5` is in the same directory as `app.py`
- Check file permissions

**❌ "Error extracting features"**
- Verify audio file is not corrupted
- Try converting to .wav format
- Ensure file duration is at least 3 seconds

**❌ "Module not found"**
- Run: `pip install -r requirements_app.txt`
- Ensure you're in the correct Python environment

**❌ App loads slowly**
- First load caches the model (takes ~5-10 seconds)
- Subsequent predictions are fast

### Performance Tips

1. **Use GPU:** If available, TensorFlow will automatically use GPU
2. **File Size:** Smaller files (<10MB) process faster
3. **Format:** WAV files process slightly faster than MP3

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add web app"
   git push
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Select `app.py` as main file
   - Deploy!

3. **Important:** Upload model files to GitHub LFS or use cloud storage

### Deploy Locally with ngrok

```bash
# Install ngrok
pip install pyngrok

# Run app with public URL
streamlit run app.py & ngrok http 8501
```

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.29.0 | Web framework |
| tensorflow | 2.15.0 | Model inference |
| librosa | 0.10.1 | Audio processing |
| plotly | 5.18.0 | Interactive charts |
| numpy | 1.24.3 | Numerical operations |
| pandas | 2.1.4 | Data handling |
| scikit-learn | 1.3.2 | Label encoding |

## 🎓 Usage Examples

### Example 1: Classify a Song
```bash
# Start app
streamlit run app.py

# In browser:
1. Upload "jazz_song.wav"
2. Click "Classify Genre"
3. See result: "🎷 JAZZ" with 87.3% confidence
```

### Example 2: Compare Genres
```bash
# Upload multiple files in succession
# Compare prediction confidence charts
# Analyze audio features side-by-side
```

## 🚀 Advanced Features

### Custom Model
Replace the model with your own:
```python
# In app.py, modify:
model = tf.keras.models.load_model('your_model.h5')
```

### Add New Genres
Update genre mappings:
```python
GENRE_EMOJIS = {
    'your_genre': '🎵',
    # ... existing genres
}
```

### Export Results
Add export functionality:
```python
# Export predictions to CSV
results_df.to_csv('predictions.csv')
```

## 📈 Performance

- **Prediction Time:** ~1-2 seconds per file
- **Supported File Size:** Up to 50 MB
- **Concurrent Users:** Depends on hosting
- **Model Accuracy:** ~75-85%

## 🔒 Security Notes

- Temporary files are automatically deleted
- No data is stored permanently
- Upload files are processed in memory
- Model runs locally (no external API calls)

## 🤝 Contributing

Want to improve the app? Here are some ideas:

- [ ] Add batch processing for multiple files
- [ ] Export predictions to CSV/JSON
- [ ] Add more audio visualizations
- [ ] Implement genre comparison mode
- [ ] Add dark/light theme toggle
- [ ] Support for longer audio files
- [ ] Add confidence threshold settings

## 📝 License

This project uses the GTZAN dataset and is for educational purposes.

## 🙏 Acknowledgments

- **GTZAN Dataset** - Music genre classification dataset
- **Streamlit** - Amazing web framework
- **TensorFlow** - Deep learning library
- **Librosa** - Audio processing library

## 📞 Support

Having issues? Try these:
1. Check the troubleshooting section above
2. Ensure all dependencies are installed
3. Verify model files are present
4. Check Python version (3.8+)

## 🎉 Enjoy!

Upload your favorite songs and discover their genres with AI! 🎵🤖

---

**Made with ❤️ using Streamlit & TensorFlow**

*Last Updated: December 6, 2025*
