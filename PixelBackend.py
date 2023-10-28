from flask import Flask, request, send_file, session, jsonify
import json
from datetime import datetime
import io
from PIL import Image
import os
import uuid
from datetime import timedelta

app = Flask(__name__)
app.secret_key = '123'
app.permanent_session_lifetime = timedelta(minutes=10)




def check_linked_purchase():
    events = session.get('events', [])
    event_types = [event['event_type'] for event in events]
    return 'video_played' in event_types and 'product_added_to_cart' in event_types

@app.route('/')
def test():
    session.permanent = True
    img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')

    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
        session['events'] = []

    event_type = request.args.get('event', 'unknown')
    product = request.args.get('product', 'unknown')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    session['events'].append({
        'event_type': event_type,
        'timestamp': timestamp,
        'product': product
    })

    linked_purchase = check_linked_purchase()
    if linked_purchase:
        purchase_info = {
            'user_id': session['user_id'],
            'purchase_made': True,
            'product': product,
            'timestamp': timestamp
        }

        with open('purchase_records.json', 'a') as f:
            json.dump(purchase_info, f)
            f.write('\n')

        return jsonify({"status": "Purchase linked", "details": purchase_info})

    return send_file(io.BytesIO(byte_arr.getvalue()), mimetype='image/png')

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
