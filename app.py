
from flask import Flask, request, render_template
from description_generator import generate_image_description
from emotion_analyzer import analyze_emotion
import streamlit as st

st.title("Emotion Tone App")
st.write("This is a sample Streamlit app.")


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    description = None
    emotion = None

    if request.method == "POST":
        image_url = request.form["image_url"]
        description = generate_image_description(image_url)
        emotion = analyze_emotion(description)

    return render_template("index.html", description=description, emotion=emotion)

if __name__ == "__main__":
    app.run(debug=True)
