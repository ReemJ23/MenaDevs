from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

previous_typing_speed = None
previous_paragraph = None

# Define the predict endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    global previous_typing_speed, previous_paragraph

    # Get paragraph from request data
    paragraph = request.json['paragraph']

    # Analyze typing speed
    typing_speed = calculate_typing_speed(paragraph)

    # Analyze paragraph content
    if previous_paragraph is not None and previous_paragraph != paragraph:
        paragraph_analysis = 'Abnormal: Paragraph content has changed.'
    else:
        paragraph_analysis = 'Normal: Paragraph content is unchanged.'

    # Compare typing speed with previous typing speed
    if previous_typing_speed is not None and typing_speed != previous_typing_speed:
        speed_analysis = 'Abnormal: Typing speed has changed.'
    else:
        speed_analysis = 'Normal: Typing speed is unchanged.'

    # Update previous typing speed and paragraph
    previous_typing_speed = typing_speed
    previous_paragraph = paragraph

    return jsonify({
        'speed_analysis': speed_analysis,
        'paragraph_analysis': paragraph_analysis
    })

def calculate_typing_speed(paragraph):
    # Calculate typing speed (for demonstration, using a simple calculation)
    words = paragraph.split()
    typing_time = 10  # Placeholder value (in seconds) for total typing time
    typing_speed = len(words) / typing_time  # Words per second
    return typing_speed

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
