from flask import Flask, request, render_template
from image_captioning import generate_caption
from emotion_analysis import analyze_emotion

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_url = request.form['image_url']
        caption = generate_caption(image_url)
        emotion = analyze_emotion(caption)
        return render_template('index.html', caption=caption, emotion=emotion)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
