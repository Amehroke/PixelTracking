from flask import Flask, request, send_file
import json
from datetime import datetime
import io
from PIL import Image
import os

app = Flask(__name__)

@app.route('/track')
def track():
    user_id = request.args.get('user_id')
    event = request.args.get('event')
    time = request.args.get('time')
    video_time = request.args.get('video_time')  # Time when video was played

    print(f"Tracked event {event} for user {user_id} at {time}")

    # File where events are stored
    filename = "webpage_tracking.json"

    # Only record events that are not 'video_play'
    if event != "video_play":
        new_event = {
            'user_id': user_id,
            'event': event,
            'time': time
        }

        if video_time:
            new_event['video_time'] = video_time

        # Check if the file exists
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing_data = json.load(f)
            existing_data.append(new_event)
        else:
            existing_data = [new_event]

        # Write updated data back to file
        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)

    # Create a 1x1 transparent pixel
    img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')

    return send_file(io.BytesIO(byte_arr.getvalue()), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
