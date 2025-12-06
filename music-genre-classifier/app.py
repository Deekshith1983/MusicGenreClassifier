"""
🎵 Music Genre Classifier Web App
A beautiful Streamlit interface for classifying music genres using deep learning
"""

import streamlit as st
import tensorflow as tf
import librosa
import numpy as np
import pickle
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
import tempfile
import os

# Page configuration
st.set_page_config(
    page_title="🎵 Music Genre Classifier",
    page_icon="🎸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .upload-text {
        font-size: 1.2rem;
        color: #ffffff;
        text-align: center;
        padding: 20px;
    }
    .prediction-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 2rem;
        font-weight: bold;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        margin: 20px 0;
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 1.1rem;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    h1, h2, h3 {
        color: #ffffff !important;
    }
    .genre-badge {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.2);
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Genre emoji mapping
GENRE_EMOJIS = {
    'blues': '🎸',
    'classical': '🎻',
    'country': '🤠',
    'disco': '🕺',
    'hiphop': '🎤',
    'jazz': '🎷',
    'metal': '🤘',
    'pop': '🎵',
    'reggae': '🏝️',
    'rock': '🎸'
}

# Genre color mapping for visualization
GENRE_COLORS = {
    'blues': '#4169E1',
    'classical': '#8B4513',
    'country': '#DEB887',
    'disco': '#FF1493',
    'hiphop': '#FFD700',
    'jazz': '#9370DB',
    'metal': '#2F4F4F',
    'pop': '#FF69B4',
    'reggae': '#32CD32',
    'rock': '#DC143C'
}

# Genre name mapping (index to genre name)
GENRE_MAPPING = {
    0: 'blues',
    1: 'classical',
    2: 'country',
    3: 'disco',
    4: 'hiphop',
    5: 'jazz',
    6: 'metal',
    7: 'pop',
    8: 'reggae',
    9: 'rock'
}

@st.cache_resource
def load_model_and_encoder():
    """Load the trained model and label encoder"""
    try:
        model = tf.keras.models.load_model('music_genre_classifier_model.h5')
        with open('label_encoder.pkl', 'rb') as f:
            label_encoder = pickle.load(f)
        return model, label_encoder
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.info("Please ensure 'music_genre_classifier_model.h5' and 'label_encoder.pkl' are in the same directory as app.py")
        return None, None

def extract_features(audio_path):
    """Extract features from audio file matching the training dataset format"""
    try:
        # Load audio file
        audio, sample_rate = librosa.load(audio_path, res_type='kaiser_fast', duration=30)
        
        # Extract all features (same as training)
        chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sample_rate)
        rms = librosa.feature.rms(y=audio)
        spec_cent = librosa.feature.spectral_centroid(y=audio, sr=sample_rate)
        spec_bw = librosa.feature.spectral_bandwidth(y=audio, sr=sample_rate)
        rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sample_rate)
        zcr = librosa.feature.zero_crossing_rate(audio)
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
        
        # Calculate mean and variance for each feature
        features = []
        
        # Chroma STFT
        features.append(np.mean(chroma_stft))
        features.append(np.var(chroma_stft))
        
        # RMS
        features.append(np.mean(rms))
        features.append(np.var(rms))
        
        # Spectral Centroid
        features.append(np.mean(spec_cent))
        features.append(np.var(spec_cent))
        
        # Spectral Bandwidth
        features.append(np.mean(spec_bw))
        features.append(np.var(spec_bw))
        
        # Rolloff
        features.append(np.mean(rolloff))
        features.append(np.var(rolloff))
        
        # Zero Crossing Rate
        features.append(np.mean(zcr))
        features.append(np.var(zcr))
        
        # MFCCs (20 coefficients, mean and variance for each)
        for coeff in mfcc:
            features.append(np.mean(coeff))
            features.append(np.var(coeff))
        
        # Harmony and Perceptr features to match training data (58 features total)
        # Extract harmonic and percussive components
        harmony = librosa.effects.harmonic(y=audio)
        perceptr = librosa.effects.percussive(y=audio)
        
        # Calculate mean and variance of the harmonic component
        features.append(float(np.mean(harmony)))
        features.append(float(np.var(harmony)))
        
        # Calculate mean and variance of the percussive component
        features.append(float(np.mean(perceptr)))
        features.append(float(np.var(perceptr)))
        
        # Tempo (mean and var = 2 features)
        tempo, _ = librosa.beat.beat_track(y=audio, sr=sample_rate)
        features.append(float(tempo))
        features.append(0.0)  # variance of tempo (single value, so 0)
        
        # Total: 2+2+2+2+2+2+40+4+2 = 58 features
        
        return np.array(features, dtype=np.float32)
    except Exception as e:
        st.error(f"Error extracting features: {str(e)}")
        return None

def extract_additional_features(audio_path):
    """Extract additional features for visualization"""
    try:
        audio, sr = librosa.load(audio_path, duration=30)
        
        # Extract features
        tempo, _ = librosa.beat.beat_track(y=audio, sr=sr)
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr))
        spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=audio, sr=sr))
        zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(audio))
        rms = np.mean(librosa.feature.rms(y=audio))
        
        return {
            'tempo': float(tempo),
            'spectral_centroid': float(spectral_centroid),
            'spectral_rolloff': float(spectral_rolloff),
            'zero_crossing_rate': float(zero_crossing_rate),
            'rms_energy': float(rms)
        }
    except:
        return None

def plot_waveform(audio_path):
    """Plot audio waveform"""
    audio, sr = librosa.load(audio_path, duration=30)
    time = np.linspace(0, len(audio) / sr, num=len(audio))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=time,
        y=audio,
        mode='lines',
        line=dict(color='#667eea', width=1),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    fig.update_layout(
        title="🎵 Audio Waveform",
        xaxis_title="Time (seconds)",
        yaxis_title="Amplitude",
        template="plotly_dark",
        height=300,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    return fig

def plot_spectrogram(audio_path):
    """Plot mel spectrogram"""
    audio, sr = librosa.load(audio_path, duration=30)
    mels = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128)
    mels_db = librosa.power_to_db(mels, ref=np.max)
    
    fig = go.Figure(data=go.Heatmap(
        z=mels_db,
        colorscale='Viridis',
        colorbar=dict(title='dB')
    ))
    
    fig.update_layout(
        title="🎨 Mel Spectrogram",
        xaxis_title="Time",
        yaxis_title="Mel Frequency",
        template="plotly_dark",
        height=300,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    return fig

def plot_prediction_confidence(predictions, genres):
    """Plot prediction confidence as a bar chart"""
    # Sort by confidence
    sorted_indices = np.argsort(predictions)[::-1]
    sorted_genres = [str(genres[i]) for i in sorted_indices]
    sorted_predictions = [predictions[i] * 100 for i in sorted_indices]
    
    # Color bars
    colors = [GENRE_COLORS.get(genre.lower(), '#667eea') for genre in sorted_genres]
    
    fig = go.Figure(data=[
        go.Bar(
            x=sorted_predictions,
            y=sorted_genres,
            orientation='h',
            marker=dict(
                color=colors,
                line=dict(color='white', width=2)
            ),
            text=[f'{p:.1f}%' for p in sorted_predictions],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="🎯 Genre Prediction Confidence",
        xaxis_title="Confidence (%)",
        yaxis_title="Genre",
        template="plotly_dark",
        height=400,
        margin=dict(l=0, r=0, t=40, b=0),
        showlegend=False
    )
    
    return fig

def main():
    # Header
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>🎵 Music Genre Classifier</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-size: 1.3rem;'>Powered by Deep Learning • LSTM with Attention Mechanism</p>", unsafe_allow_html=True)
    
    # Load model
    with st.spinner('🔄 Loading AI model...'):
        model, label_encoder = load_model_and_encoder()
    
    if model is None or label_encoder is None:
        st.stop()
    
    st.success('✅ Model loaded successfully!')
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 📊 About")
        st.info("""
        This app uses a **Bidirectional LSTM** with **Attention Mechanism** to classify music into 10 genres.
        
        **Accuracy:** ~75-85%
        
        **Supported Genres:**
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
        """)
        
        st.markdown("---")
        st.markdown("## ⚙️ Settings")
        show_visualizations = st.checkbox("Show Visualizations", value=True)
        show_features = st.checkbox("Show Audio Features", value=True)
        
        st.markdown("---")
        st.markdown("### 📝 Instructions")
        st.markdown("""
        1. Upload an audio file (.wav, .mp3)
        2. Wait for processing
        3. View predictions & insights
        4. Explore visualizations
        """)
    
    # Main content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div class='upload-text'>📤 Upload your music file below</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Choose an audio file",
            type=['wav', 'mp3', 'ogg', 'flac'],
            label_visibility="collapsed"
        )
    
    if uploaded_file is not None:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name
        
        try:
            # Display file info
            st.markdown("---")
            file_col1, file_col2, file_col3 = st.columns(3)
            with file_col1:
                st.metric("📁 File Name", uploaded_file.name)
            with file_col2:
                st.metric("📦 File Size", f"{uploaded_file.size / 1024:.2f} KB")
            with file_col3:
                st.metric("🎼 Format", Path(uploaded_file.name).suffix.upper())
            
            # Audio player
            st.markdown("### 🎧 Preview Your Music")
            st.audio(uploaded_file, format=f'audio/{Path(uploaded_file.name).suffix[1:]}')
            
            # Predict button
            st.markdown("---")
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                predict_button = st.button("🎯 Classify Genre", use_container_width=True)
            
            if predict_button:
                with st.spinner('🔮 Analyzing your music...'):
                    # Extract features
                    features = extract_features(tmp_path)
                    
                    if features is not None:
                        # Reshape for model (batch_size, timesteps, features)
                        # Model expects shape: (1, 1, 58)
                        features_reshaped = features.reshape(1, 1, -1)
                        
                        # Predict
                        predictions = model.predict(features_reshaped, verbose=0)[0]
                        predicted_class = np.argmax(predictions)
                        
                        # Map the predicted class to genre name
                        predicted_genre = GENRE_MAPPING.get(predicted_class, f'genre_{predicted_class}')
                        confidence = predictions[predicted_class] * 100
                        
                        # Display prediction
                        st.markdown("---")
                        st.markdown("## 🎊 Prediction Results")
                        
                        emoji = GENRE_EMOJIS.get(predicted_genre.lower(), '🎵')
                        st.markdown(
                            f"<div class='prediction-box'>{emoji} {predicted_genre.upper()} {emoji}<br>"
                            f"<span style='font-size: 1.2rem;'>Confidence: {confidence:.1f}%</span></div>",
                            unsafe_allow_html=True
                        )
                        
                        # Confidence chart
                        genre_names = [GENRE_MAPPING.get(i, f'genre_{i}') for i in range(10)]
                        st.plotly_chart(
                            plot_prediction_confidence(predictions, genre_names),
                            use_container_width=True
                        )
                        
                        # Top 3 predictions
                        st.markdown("### 🏆 Top 3 Predictions")
                        top3_indices = np.argsort(predictions)[::-1][:3]
                        
                        cols = st.columns(3)
                        for idx, col in enumerate(cols):
                            genre_idx = top3_indices[idx]
                            genre = GENRE_MAPPING.get(genre_idx, f'genre_{genre_idx}')
                            prob = predictions[genre_idx] * 100
                            emoji = GENRE_EMOJIS.get(genre.lower(), '🎵')
                            
                            with col:
                                st.markdown(f"""
                                <div class='metric-card'>
                                    <h3 style='text-align: center; margin: 0;'>{emoji}</h3>
                                    <h4 style='text-align: center; margin: 10px 0;'>{genre.title()}</h4>
                                    <p style='text-align: center; font-size: 1.5rem; margin: 0;'>{prob:.1f}%</p>
                                </div>
                                """, unsafe_allow_html=True)
                        
                        # Visualizations
                        if show_visualizations:
                            st.markdown("---")
                            st.markdown("## 📊 Audio Analysis")
                            
                            viz_col1, viz_col2 = st.columns(2)
                            
                            with viz_col1:
                                st.plotly_chart(plot_waveform(tmp_path), use_container_width=True)
                            
                            with viz_col2:
                                st.plotly_chart(plot_spectrogram(tmp_path), use_container_width=True)
                        
                        # Audio features
                        if show_features:
                            st.markdown("---")
                            st.markdown("## 🎼 Audio Features")
                            
                            features_data = extract_additional_features(tmp_path)
                            
                            if features_data:
                                feat_col1, feat_col2, feat_col3, feat_col4, feat_col5 = st.columns(5)
                                
                                with feat_col1:
                                    st.metric("🥁 Tempo", f"{features_data['tempo']:.1f} BPM")
                                with feat_col2:
                                    st.metric("✨ Brightness", f"{features_data['spectral_centroid']:.0f} Hz")
                                with feat_col3:
                                    st.metric("📈 Rolloff", f"{features_data['spectral_rolloff']:.0f} Hz")
                                with feat_col4:
                                    st.metric("〰️ ZCR", f"{features_data['zero_crossing_rate']:.4f}")
                                with feat_col5:
                                    st.metric("🔊 Energy", f"{features_data['rms_energy']:.4f}")
            
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
    
    else:
        # Show example genres when no file uploaded
        st.markdown("---")
        st.markdown("## 🎭 Supported Genres")
        
        genre_cols = st.columns(5)
        genres_list = list(GENRE_EMOJIS.keys())
        
        for idx, (genre, emoji) in enumerate(GENRE_EMOJIS.items()):
            with genre_cols[idx % 5]:
                st.markdown(f"""
                <div class='metric-card' style='text-align: center; padding: 30px 10px;'>
                    <h2 style='margin: 0; font-size: 3rem;'>{emoji}</h2>
                    <p style='margin: 10px 0 0 0; font-size: 1.1rem;'>{genre.title()}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: white; padding: 20px;'>
        <p style='font-size: 0.9rem;'>Built with ❤️ using Streamlit & TensorFlow</p>
        <p style='font-size: 0.8rem;'>LSTM with Attention Mechanism • Trained on GTZAN Dataset</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
