import streamlit as st
import joblib


model = joblib.load("TBED model.joblib")
st.title("Text-Based Emotion Detection")
st.markdown("Enter text describing the way how you feel and we will detect your emotion")

user_input = st.text_area("Describe how you feel.")

if st.button("Detect Emotion"):
    if user_input:
        emotion = model.predict([user_input])

        if emotion == 0:
            st.write("Detected Emotion: Anger")
        elif emotion == 1:
            st.write("Detected Emotion: Boredom")
        if emotion == 2:
            st.write("Detected Emotion: Empty")
        elif emotion == 3:
            st.write("Detected Emotion: Enthusiasm")
        if emotion == 4:
            st.write("Detected Emotion: Fun")
        elif emotion == 5:
            st.write("Detected Emotion: Happiness")
        if emotion == 6:
            st.write("Detected Emotion: Hate")
        elif emotion == 7:
            st.write("Detected Emotion: Love")
        if emotion == 8:
            st.write("Detected Emotion: Neutral")
        elif emotion == 9:
            st.write("Detected Emotion: Relief")
        if emotion == 10:
            st.write("Detected Emotion: Sadness")
        elif emotion == 11:
            st.write("Detected Emotion: Surprise")
        elif emotion==12:
            st.write("Detected Emotion: Worry")
    else:
        st.warning("Please enter some texts to dectect your emotion")

if st.button('About'):
    st.write("Made with love by ALONGE OLAMIDE SAMSON with matric number CSC/2019/1093 Under the supervision of Dr. Akingbesote A.")
    st.balloons()