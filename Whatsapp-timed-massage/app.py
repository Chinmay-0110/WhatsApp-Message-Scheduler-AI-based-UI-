from flask import Flask, request, render_template, jsonify
import pywhatkit
import threading
from datetime import datetime

app = Flask(__name__)

def send_message(phone, message, hour, minute):
    pywhatkit.sendwhatmsg(phone, message, hour, minute)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule_message():
    data = request.json
    number = data['number']
    message = data['message']
    time_str = data['time']  # format: "HH:MM"

    try:
        hour, minute = map(int, time_str.split(':'))

        # Run sending in a separate thread
        threading.Thread(target=send_message, args=(number, message, hour, minute)).start()
        return jsonify({'status': 'success', 'msg': 'Message scheduled'})
    except Exception as e:
        return jsonify({'status': 'error', 'msg': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
