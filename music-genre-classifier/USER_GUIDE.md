# 🎵 Music Genre Classifier App - Complete Guide

## 📋 Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Using the App](#using-the-app)
4. [Features Guide](#features-guide)
5. [Troubleshooting](#troubleshooting)

---

## 🚀 Installation

### Step 1: Verify Files

Make sure you have these files in your `music-genre-classifier` folder:

```
music-genre-classifier/
├── app.py                              ✅ Main application
├── music_genre_classifier_model.h5     ✅ Trained model (download from Colab)
├── label_encoder.pkl                   ✅ Label encoder (download from Colab)
├── requirements_app.txt                ✅ Dependencies
├── run_app.ps1                         ✅ Quick start script
└── test_setup.py                       ✅ Setup verification
```

### Step 2: Install Dependencies

**Option A - Use PowerShell Script (Recommended):**
```powershell
.\run_app.ps1
```
This will automatically install everything and start the app!

**Option B - Manual Installation:**
```bash
# Create virtual environment (optional but recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements_app.txt
```

### Step 3: Verify Setup

Run the verification script:
```bash
python test_setup.py
```

You should see all ✅ checkmarks if everything is ready!

---

## 🎯 Quick Start

### Method 1: PowerShell Script (Easiest)
```powershell
.\run_app.ps1
```

### Method 2: Manual Start
```bash
streamlit run app.py
```

### What Happens Next:
1. Browser opens automatically to `http://localhost:8501`
2. You'll see the beautiful purple gradient interface
3. Ready to upload and classify music! 🎵

---

## 🎨 Using the App

### Interface Overview

```
┌─────────────────────────────────────────────┐
│     🎵 Music Genre Classifier               │
│     Powered by Deep Learning                │
├─────────────────────────────────────────────┤
│                                             │
│         📤 Upload your music file           │
│         [Drag & Drop or Click]              │
│                                             │
├─────────────────────────────────────────────┤
│  📁 File Name  │ 📦 Size  │ 🎼 Format      │
├─────────────────────────────────────────────┤
│         🎧 Preview Your Music               │
│         [Audio Player]                      │
├─────────────────────────────────────────────┤
│           🎯 Classify Genre                 │
│              [Button]                       │
└─────────────────────────────────────────────┘
```

### Step-by-Step Usage

#### 1. **Upload Audio File**
   - Click "Browse files" or drag & drop
   - Supported formats: `.wav`, `.mp3`, `.ogg`, `.flac`
   - File size: Up to 50 MB
   - Duration: Any (will process first 30 seconds)

#### 2. **Preview Your Music**
   - Audio player appears automatically
   - Listen to your uploaded track
   - Verify it's the correct file

#### 3. **Click "Classify Genre"**
   - Purple button in the center
   - Processing takes 1-2 seconds
   - Watch for the loading animation

#### 4. **View Results**
   - **Big Prediction Box:** Shows the predicted genre with emoji
   - **Confidence Score:** Percentage certainty
   - **Confidence Chart:** Bar chart of all genre probabilities
   - **Top 3 Predictions:** Alternative genre possibilities

---

## 🎨 Features Guide

### 1. Genre Prediction

**Main Prediction Display:**
```
┌─────────────────────────────────────┐
│     🎷 JAZZ 🎷                      │
│     Confidence: 87.3%               │
└─────────────────────────────────────┘
```

- Large, colorful gradient box
- Genre name in uppercase
- Matching emoji (e.g., 🎷 for Jazz)
- Confidence percentage

### 2. Confidence Chart

**Interactive Bar Chart:**
- All 10 genres ranked by probability
- Color-coded bars (each genre has unique color)
- Hover to see exact percentages
- Helps you see how "close" other genres are

**Example:**
```
Jazz     ████████████████████ 87.3%
Blues    ████████░░░░░░░░░░░ 6.2%
Classical ███░░░░░░░░░░░░░░░ 2.1%
...
```

### 3. Top 3 Predictions

**Three Cards Showing:**
```
┌──────────┐  ┌──────────┐  ┌──────────┐
│    🎷    │  │    🎸    │  │    🎻    │
│   Jazz   │  │   Blues  │  │ Classical│
│  87.3%   │  │   6.2%   │  │   2.1%   │
└──────────┘  └──────────┘  └──────────┘
```

- Visual cards with emojis
- Genre name and confidence
- Great for seeing alternatives

### 4. Audio Visualizations

#### **Waveform Plot**
```
🎵 Audio Waveform
─────────────────────────────
  ╱╲    ╱╲    ╱╲
 ╱  ╲  ╱  ╲  ╱  ╲
╱    ╲╱    ╲╱    ╲
```

- Shows amplitude over time
- Interactive plot (zoom, pan)
- Blue gradient fill
- X-axis: Time (seconds)
- Y-axis: Amplitude

#### **Mel Spectrogram**
```
🎨 Mel Spectrogram
─────────────────────────────
High ▓▓░░▓▓░░▓▓  Frequency
     ▓▓▓▓▓▓▓▓▓▓
Low  ░░▓▓░░▓▓░░
     ────────────→ Time
```

- Heat map of frequencies
- Viridis color scale
- Shows how sound changes over time
- Interactive (hover for values)

### 5. Audio Features

Five key metrics displayed:

| Metric | Icon | Description | Typical Range |
|--------|------|-------------|---------------|
| **Tempo** | 🥁 | Beats per minute | 60-180 BPM |
| **Brightness** | ✨ | Spectral centroid (Hz) | 1000-4000 Hz |
| **Rolloff** | 📈 | Spectral rolloff (Hz) | 2000-8000 Hz |
| **ZCR** | 〰️ | Zero crossing rate | 0.01-0.30 |
| **Energy** | 🔊 | RMS energy level | 0.01-0.50 |

**What They Mean:**

- **Tempo:** How fast the music is
  - Slow: 60-90 BPM (ballads)
  - Medium: 90-120 BPM (pop)
  - Fast: 120-180+ BPM (dance, metal)

- **Brightness:** How "bright" or "sharp" the sound is
  - Low: Darker, bass-heavy (blues, jazz)
  - High: Brighter, treble-heavy (pop, disco)

- **Rolloff:** Frequency where most energy is below
  - Shows the "edge" of the sound spectrum

- **ZCR:** How often the signal crosses zero
  - High: Noisy/percussive (metal, hiphop)
  - Low: Smooth/tonal (classical, jazz)

- **Energy:** Overall loudness/intensity
  - High: Loud and energetic
  - Low: Soft and mellow

### 6. Sidebar Settings

**Toggle Features:**
- ✅ Show Visualizations (waveform & spectrogram)
- ✅ Show Audio Features (metrics)

**About Section:**
- Model information
- Accuracy stats
- Supported genres list

**Instructions:**
- Quick how-to guide
- Always visible for reference

---

## 🎭 Genre Examples

### What Each Genre Sounds Like:

| Genre | Emoji | Characteristics | Example Features |
|-------|-------|-----------------|------------------|
| **Blues** | 🎸 | Soulful, 12-bar structure | Medium tempo, smooth |
| **Classical** | 🎻 | Orchestral, complex | Variable tempo, high brightness |
| **Country** | 🤠 | Guitars, storytelling | Medium tempo, bright |
| **Disco** | 🕺 | Dance beats, 4/4 time | Fast tempo, high energy |
| **Hip Hop** | 🎤 | Rap, beats, samples | Medium-fast, high ZCR |
| **Jazz** | 🎷 | Improvisation, swing | Variable tempo, complex |
| **Metal** | 🤘 | Heavy guitars, drums | Fast tempo, high energy |
| **Pop** | 🎵 | Catchy, mainstream | Medium-fast, bright |
| **Reggae** | 🏝️ | Offbeat rhythm, bass | Medium tempo, rhythmic |
| **Rock** | 🎸 | Guitars, drums, energy | Medium-fast, energetic |

---

## 🔧 Advanced Usage

### Testing Different Songs

**Try uploading:**
1. A song you know the genre of
2. Songs from different eras
3. Genre-blending music
4. Instrumental vs. vocal tracks
5. Live recordings vs. studio

### Understanding Misclassifications

**Common confusions:**
- **Blues ↔ Jazz:** Similar instruments and feel
- **Rock ↔ Metal:** Intensity differences
- **Pop ↔ Disco:** Both have dance elements
- **Country ↔ Rock:** Shared guitar elements

**Why it happens:**
- Genre boundaries are fuzzy
- Some songs blend multiple genres
- Model trained on specific examples

### Maximizing Accuracy

**Best results with:**
- ✅ Clear, high-quality audio
- ✅ Full band/ensemble recordings
- ✅ Typical genre examples
- ✅ WAV format (less compression)

**May struggle with:**
- ❌ Very short clips (<10 seconds)
- ❌ Heavy noise/distortion
- ❌ Acoustic solo performances
- ❌ Experimental/fusion genres

---

## 🚨 Troubleshooting

### App Won't Start

**Error: "Model file not found"**
```
Solution:
1. Check file exists: music_genre_classifier_model.h5
2. Ensure it's in the same folder as app.py
3. Re-download from Google Colab if missing
```

**Error: "Module not found"**
```
Solution:
1. Install requirements: pip install -r requirements_app.txt
2. Activate virtual environment if using one
3. Check Python version (need 3.8+)
```

**Port already in use**
```
Solution:
1. Stop other Streamlit apps
2. Or use different port: streamlit run app.py --server.port 8502
```

### Upload Issues

**File won't upload**
```
Solutions:
- Check file format (wav, mp3, ogg, flac only)
- Reduce file size if very large (>50MB)
- Try different browser
- Check file isn't corrupted
```

**Upload stuck/frozen**
```
Solutions:
- Refresh the page
- Clear browser cache
- Try smaller file
- Check internet connection
```

### Prediction Issues

**Error during classification**
```
Solutions:
- Ensure audio file is valid
- Try converting to WAV format
- Check file isn't too short (<3 seconds)
- Restart the app
```

**Weird predictions**
```
This might be normal if:
- Song blends multiple genres
- Unusual instruments/style
- Poor audio quality
- Very short or repetitive clip
```

### Performance Issues

**App running slow**
```
Solutions:
- Close other applications
- Use smaller audio files
- Disable visualizations in sidebar
- Restart browser
- Check system resources
```

**First prediction is slow**
```
This is normal:
- Model loads on first use (~5-10 seconds)
- Subsequent predictions are much faster
- Model is cached after first load
```

---

## 💡 Tips & Tricks

### 1. Best Practices

- **File Format:** WAV for best quality
- **File Size:** 5-20 MB is ideal
- **Duration:** 30 seconds is optimal (full analysis)
- **Quality:** 128+ kbps for MP3

### 2. Keyboard Shortcuts

```
F5         - Refresh app
Ctrl + R   - Reload page
Ctrl + W   - Close tab
```

### 3. Saving Results

**Screenshot predictions:**
- Windows: Win + Shift + S
- Mac: Cmd + Shift + 4

**Export data:** (Coming soon!)
- CSV export of predictions
- Batch processing mode

### 4. Comparing Songs

**Process:**
1. Upload Song A
2. Note predictions
3. Upload Song B
4. Compare confidence charts
5. Analyze feature differences

---

## 📊 Understanding the Output

### Confidence Scores

**What they mean:**

| Score | Interpretation |
|-------|----------------|
| >80% | Very confident - likely correct |
| 60-80% | Confident - probably correct |
| 40-60% | Uncertain - could be close call |
| <40% | Low confidence - check alternatives |

**Multiple high scores:**
- Song may blend genres
- Check top 3 predictions
- Consider it "genre-fluid"

### When to Trust Predictions

**High trust:**
- ✅ Confidence >75%
- ✅ Clear gap to 2nd place (>20%)
- ✅ Audio features match genre
- ✅ You recognize the genre

**Be cautious:**
- ⚠️ Confidence <60%
- ⚠️ Multiple genres close together
- ⚠️ Unusual audio features
- ⚠️ You disagree with prediction

---

## 🎓 Learning More

### Understanding Your Results

**Example Analysis:**

```
Prediction: 🎷 JAZZ (87.3%)
Top 3: Jazz (87.3%), Blues (6.2%), Classical (2.1%)

Audio Features:
🥁 Tempo: 112 BPM     ← Medium tempo, typical for jazz
✨ Brightness: 2847 Hz ← Moderate brightness
📈 Rolloff: 5234 Hz    ← Mid-high frequencies
〰️ ZCR: 0.082         ← Moderate crossing rate
🔊 Energy: 0.124      ← Moderate energy

Interpretation:
- Strong jazz prediction with high confidence
- Blues is distant 2nd (makes sense - similar styles)
- Moderate tempo and energy fit jazz profile
- Brightness suggests brass/wind instruments
- Good prediction! ✅
```

### Genre Characteristics in Features

**Typical patterns:**

**Metal:**
- Fast tempo (140-180 BPM)
- High energy (>0.3)
- High ZCR (>0.15)

**Classical:**
- Variable tempo
- High brightness (>3000 Hz)
- Lower energy

**Hip Hop:**
- Medium tempo (85-115 BPM)
- High ZCR (percussive)
- Moderate energy

**Disco:**
- Fast tempo (115-135 BPM)
- High energy
- Consistent rhythm

---

## 🎉 Have Fun!

Experiment with different songs and discover patterns in:
- Your music library
- Different eras of music
- Various artists and styles
- Genre evolution over time

**Happy classifying! 🎵🤖**

---

*For technical details, see README_APP.md*  
*For model training, see the Jupyter notebook*
