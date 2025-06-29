
import streamlit as st
import pickle
import numpy as np

with open("personality_model.pkl","rb") as file:
  model=pickle.load(file)

st.title("Personality Predictor(Introvert vs Extrovert)")
st.markdown("### Please enter the following info:")

time_alone = st.slider("Time Spent Alone(0-10)",0.0,10.0,5.0)
stage_fear = st.radio("Do you have stage fear?",["Yes","No"])
social_event = st.slider("Social Event Attendance(0-10)",0.0,10.0,5.0)
going_outside = st.slider("How often do you go outside?(0-10)",0.0,10.0,5.0)
drained_socializing = st.radio("Do you feel drained after socializing?",["Yes","No"])
friend_circle = st.slider("Size of friends circle(0-10)",0.0,10.0,5.0)
post_frequency = st.slider("How often do you post on social media?(0-10)",0.0,10.0,5.0)

stage_fear = 1 if stage_fear == "Yes" else 0
drained_socializing = 1 if drained_socializing == "Yes" else 0

input_data = np.array([[time_alone,stage_fear,social_event,going_outside,drained_socializing,friend_circle,post_frequency]])


if st.button("Predict"):
  result = model.predict(input_data)[0]
  st.success("Prediction:"+ ("You're an Extrovert" if result == 1 else "You're an Introvert"))
