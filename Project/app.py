from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

typing_speed_history = []
change_percentage_threshold = 0.5  # Threshold for detecting significant change in typing speed
last_typing_time = None

# Define the analyze endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    global last_typing_time

    paragraph = request.json['paragraph']
    current_time = time.time()

    # Calculate typing speed
    typing_speed = calculate_typing_speed(paragraph)

    # Add typing speed to history
    typing_speed_history.append(typing_speed)

    # Keep only the most recent typing speeds based on the window size
    if len(typing_speed_history) > 10:
        typing_speed_history.pop(0)

    # Check if there is enough typing speed history to analyze
    if len(typing_speed_history) >= 10:
        # Calculate average typing speed
        avg_typing_speed = sum(typing_speed_history) / len(typing_speed_history)

        # Calculate the change percentage of the current typing speed
        change_percentage = abs(typing_speed - avg_typing_speed) / avg_typing_speed

        # Check if typing speed has changed significantly from average
        if change_percentage > change_percentage_threshold:
            speed_analysis = 'Abnormal: Typing speed has changed significantly.'
        else:
            speed_analysis = 'Normal: Typing speed is unchanged.'
    else:
        speed_analysis = 'Normal: Typing speed is being studied...'

    last_typing_time = current_time

    return jsonify({
        'speed_analysis': speed_analysis
    })

def calculate_typing_speed(paragraph):
    # Calculate typing speed (for demonstration, using a simple calculation)
    words = paragraph.split()
    typing_time = 10  # Placeholder value (in seconds) for total typing time
    typing_speed = len(words) / typing_time  # Words per second
    return typing_speed

@app.route('/')
def index():
    global last_typing_time
    typing_speed_history.clear()  # Reset typing speed history
    last_typing_time = time.time()  # Update last typing time
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
