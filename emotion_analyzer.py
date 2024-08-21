# emotion_analyzer.py

from transformers import pipeline

def analyze_emotion(text):
    emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
    emotions = emotion_classifier(text)
    return emotions[0]['label']
