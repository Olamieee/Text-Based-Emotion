import streamlit as st
import joblib

# Page configuration with emoji icon
st.set_page_config(page_title="Emotion Detector", page_icon="😊")

# Simple custom CSS
st.markdown("""
<style>
    .emotion-result {
        font-size: 1.8rem;
        padding: 0.7rem;
        border-radius: 8px;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("TBED model.joblib")

# App header with color
st.title("Text-Based Emotion Detection 🔍")
st.markdown("Enter text describing how you feel and we will detect your emotion")

# User input
user_input = st.text_area("Describe how you feel:", placeholder="Example: I'm so excited about the weekend...")

# Emotion emojis mapping
emotion_emojis = {
    0: ("Anger", "😠", "#FF5252"),
    1: ("Boredom", "😒", "#9E9E9E"),
    2: ("Empty", "😶", "#78909C"),
    3: ("Enthusiasm", "🤩", "#FF9800"),
    4: ("Fun", "😄", "#FFC107"),
    5: ("Happiness", "😊", "#4CAF50"),
    6: ("Hate", "😡", "#D32F2F"),
    7: ("Love", "❤️", "#E91E63"),
    8: ("Neutral", "😐", "#607D8B"),
    9: ("Relief", "😌", "#8BC34A"),
    10: ("Sadness", "😢", "#2196F3"),
    11: ("Surprise", "😲", "#673AB7"),
    12: ("Worry", "😟", "#795548")
}

# Detection button
col1, col2 = st.columns([3, 1])
with col1:
    detect_button = st.button("Detect Emotion", type="primary", use_container_width=True)
with col2:
    clear_button = st.button("Clear", use_container_width=True)

if clear_button:
    st.experimental_rerun()

# Process and display result
if detect_button:
    if user_input:
        with st.spinner('Analyzing...'):
            emotion = model.predict([user_input])[0]
            
            # Get emotion details from mapping
            emotion_name, emoji, color = emotion_emojis[emotion]
            
            # Display styled result
            st.markdown(f"""
            <div class='emotion-result' style='background-color: {color}25; color: {color}; border: 2px solid {color};'>
                {emoji} Detected Emotion: <strong>{emotion_name}</strong> {emoji}
            </div>
            """, unsafe_allow_html=True)
            
            # Quick suggestion based on emotion
            if emotion in [0, 6, 10, 12]:  # Negative emotions
                st.info("💡 Tip: Take a deep breath and try to relax. Consider talking to someone you trust.")
            elif emotion in [3, 4, 5, 7, 9]:  # Positive emotions
                st.success("💡 Tip: Wonderful! Share your positive energy with others around you.")
            else:  # Neutral emotions
                st.info("💡 Tip: This might be a good time for reflection or trying something new.")
                
    else:
        st.warning("Please enter some text to detect your emotion")

# About section at the bottom
if st.button('About this Project'):
    st.markdown("""
    ## About Text-Based Emotion Detection
    
    This application uses machine learning to analyze text and identify the emotion behind it. 
    The model can detect 13 different emotions from written text.
    
    ### How it works:
    1. Enter text describing your feelings
    2. Our AI model analyzes your text
    3. The system identifies the emotion expressed
    
    **Technical details:** Built using Streamlit and scikit-learn.
    """)
    st.balloons()