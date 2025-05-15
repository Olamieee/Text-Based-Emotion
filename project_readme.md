# Text-Based Emotion Detection

A machine learning web application that analyzes text input to detect emotions.

## Features

- Detects 13 different emotions from text input
- Provides visual feedback with emojis and color-coding
- Offers simple tips based on detected emotions
- Simple, user-friendly interface

## How to Use

1. Enter text describing your feelings in the text area
2. Click "Detect Emotion" to analyze
3. View your detected emotion with visual indicators
4. Get a helpful tip based on your emotional state

## Technical Details

- Built with Python and Streamlit
- Uses a machine learning model trained on emotion-labeled text data
- Classifies text into 13 emotion categories:
  - Anger, Boredom, Empty, Enthusiasm, Fun, Happiness, Hate, 
    Love, Neutral, Relief, Sadness, Surprise, and Worry

## Installation

```
pip install streamlit joblib scikit-learn
```

## Running the App

```
streamlit run Tbed_web.py
```

## Requirements

- Python 3.7+
- Streamlit
- Joblib
- Scikit-learn (for the model)