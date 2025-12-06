"""
🎵 Music Genre Classifier - Streamlit App
Upload an audio file and get genre predictions using CNN
"""

import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import os

# Page configuration
st.set_page_config(
    page_title="Music Genre Classifier",
    page_icon="🎵",
    layout="wide"
)

# Constants
MODEL_PATH = "models/music_genre_cnn.h5"
LABEL_ENCODER_PATH = "models/label_encoder.npy"
SAMPLE_RATE = 22050
DURATION = 30
N_MELS = 128
HOP_LENGTH = 512
N_FFT = 2048

@st.cache_resource
def load_model():
    """Load trained model and label encoder"""
    if not os.path.exists(MODEL_PATH):
        st.error("Model file not found! Please train the model first.")
        return None, None
    
    model = keras.models.load_model(MODEL_PATH)
    label_classes = np.load(LABEL_ENCODER_PATH, allow_pickle=True)
    return model, label_classes

def extract_mel_spectrogram(audio_data, sr, n_mels=128, max_pad_len=1293):
    """Extract mel-spectrogram from audio data"""
    # Extract mel-spectrogram
    mel_spec = librosa.feature.melspectrogram(
        y=audio_data, 
        sr=sr, 
        n_mels=n_mels,
        n_fft=N_FFT,
        hop_length=HOP_LENGTH
    )
    
    # Convert to dB scale
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    
    # Pad or truncate to fixed length
    if mel_spec_db.shape[1] < max_pad_len:
        pad_width = max_pad_len - mel_spec_db.shape[1]
        mel_spec_db = np.pad(mel_spec_db, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mel_spec_db = mel_spec_db[:, :max_pad_len]
    
    return mel_spec_db

def predict_genre(audio_data, sr, model, label_classes):
    """Predict genre from audio data"""
    # Extract features
    mel_spec = extract_mel_spectrogram(audio_data, sr)
    
    # Reshape and normalize
    mel_spec = mel_spec.reshape(1, mel_spec.shape[0], mel_spec.shape[1], 1)
    mel_spec = (mel_spec - mel_spec.min()) / (mel_spec.max() - mel_spec.min())
    
    # Predict
    prediction = model.predict(mel_spec, verbose=0)
    predicted_class = np.argmax(prediction)
    confidence = prediction[0][predicted_class]
    predicted_genre = label_classes[predicted_class]
    
    return predicted_genre, confidence, prediction[0]

def plot_mel_spectrogram(audio_data, sr):
    """Plot mel-spectrogram"""
    mel_spec = librosa.feature.melspectrogram(y=audio_data, sr=sr, n_mels=N_MELS)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    img = librosa.display.specshow(mel_spec_db, sr=sr, hop_length=HOP_LENGTH,
                                    x_axis='time', y_axis='mel', ax=ax)
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    ax.set_title('Mel-Spectrogram')
    return fig

# Main App
st.title("🎵 Music Genre Classifier")
st.markdown("Upload an audio file to classify its genre using a Convolutional Neural Network")

# Load model
model, label_classes = load_model()

if model is not None and label_classes is not None:
    st.success(f"✓ Model loaded successfully! Supports {len(label_classes)} genres")
    
    # Display supported genres
    with st.expander("📋 Supported Genres"):
        cols = st.columns(5)
        for i, genre in enumerate(label_classes):
            cols[i % 5].write(f"• {genre}")
    
    # File upload
    st.markdown("---")
    uploaded_file = st.file_uploader(
        "Choose an audio file (WAV, MP3, OGG)",
        type=['wav', 'mp3', 'ogg', 'flac']
    )
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            # Load audio
            with st.spinner("Loading audio..."):
                audio_data, sr = librosa.load(temp_path, sr=SAMPLE_RATE, duration=DURATION)
                duration = librosa.get_duration(y=audio_data, sr=sr)
            
            # Display audio player
            st.audio(uploaded_file, format=f'audio/{uploaded_file.name.split(".")[-1]}')
            
            # Audio info
            col1, col2, col3 = st.columns(3)
            col1.metric("Sample Rate", f"{sr} Hz")
            col2.metric("Duration", f"{duration:.2f} sec")
            col3.metric("Samples", len(audio_data))
            
            # Predict
            with st.spinner("Analyzing audio and predicting genre..."):
                predicted_genre, confidence, all_probs = predict_genre(
                    audio_data, sr, model, label_classes
                )
            
            st.markdown("---")
            
            # Results
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.subheader("🎯 Prediction Results")
                st.markdown(f"### **{predicted_genre.upper()}**")
                st.markdown(f"**Confidence:** {confidence:.2%}")
                
                # Progress bar
                st.progress(float(confidence))
                
                st.markdown("#### All Genre Probabilities:")
                # Sort by probability
                sorted_indices = np.argsort(all_probs)[::-1]
                
                for idx in sorted_indices:
                    genre_name = label_classes[idx]
                    prob = all_probs[idx]
                    st.write(f"**{genre_name}:** {prob:.2%}")
                    st.progress(float(prob))
            
            with col2:
                st.subheader("📊 Mel-Spectrogram Visualization")
                fig = plot_mel_spectrogram(audio_data, sr)
                st.pyplot(fig)
            
            # Clean up temp file
            os.remove(temp_path)
            
        except Exception as e:
            st.error(f"Error processing audio: {e}")
            if os.path.exists(temp_path):
                os.remove(temp_path)

else:
    st.warning("⚠️ Please train the model first by running the ModelTraining.ipynb notebook")

# Footer
st.markdown("---")
st.markdown("**Built with:** TensorFlow, Librosa, Streamlit | **Model:** CNN | **Dataset:** GTZAN")
