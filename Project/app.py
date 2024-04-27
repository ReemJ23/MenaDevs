from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

typing_speed_history = []
is_warming_up = True
warm_up_duration = 10  # Warm-up duration in seconds
warm_up_start_time = None

# Define the analyze endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    global is_warming_up, warm_up_start_time

    paragraph = request.json['paragraph']

    # If still warming up, check if warm-up period has ended
    if is_warming_up:
        if time.time() - warm_up_start_time >= warm_up_duration:
            is_warming_up = False
            return jsonify({
                'speed_analysis': 'Warm-up period ended. Starting dynamic analysis...'
            })
        else:
            return jsonify({
                'speed_analysis': 'Warming up...'
            })

    # Analyze typing speed
    typing_speed = calculate_typing_speed(paragraph)

    # Add typing speed to history
    typing_speed_history.append(typing_speed)

    # Check if there is enough typing speed history to analyze
    if len(typing_speed_history) >= 5:
        # Calculate average typing speed
        avg_typing_speed = sum(typing_speed_history) / len(typing_speed_history)

        # Check if typing speed has changed significantly from average
        # For demonstration, let's consider a threshold of 30% change
        if typing_speed < 0.7 * avg_typing_speed or typing_speed > 1.3 * avg_typing_speed:
            speed_analysis = 'Abnormal: Typing speed has changed significantly.'
        else:
            speed_analysis = 'Normal: Typing speed is unchanged.'
    else:
        speed_analysis = 'Normal: Typing speed is being studied...'

    return jsonify({
        'speed_analysis': speed_analysis
    })

def calculate_typing_speed(paragraph):
    # Calculate typing speed (for demonstration, using a simple calculation)
    words = paragraph.split()
    typing_time = 10  # Placeholder value (in seconds) for total typing time
    typing_speed = len(words) / typing_time  # Words per second
    return typing_speed

# Serve index.html by default for the root route '/'
@app.route('/')
def index():
    global is_warming_up, warm_up_start_time
    is_warming_up = True  # Start in the waiting mode
    warm_up_start_time = time.time()
    return render_template('index.html')

# Serve model.html when navigating to '/model'
@app.route('/model')
def model():
    return render_template('model.html')

if __name__ == '__main__':
    app.run(debug=True)
