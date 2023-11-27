# PixelTracking

This is a simple implementation of pixel tracking for user purchase after viewing product video.
# PixelBackend.py: 
  This Flask application serves as a basic web analytics tracker that listens on the /track endpoint for user events. It captures parameters like user_id, event, time, and optionally video_time from GET requests. The captured events, except those marked as video_play, are then stored in a JSON file named webpage_tracking.json. Additionally, the application returns a 1x1 transparent PNG pixel image as a response, commonly used as a tracking pixel on web pages. The entire app is intended to run in debug mode when executed directly.

  # Page1.html
  The HTML file includes JavaScript to track user interactions with a video and a "Purchase" button. When the video is played, a 'play' event is captured, and a GET request is made to a Flask server via an invisible tracking pixel. Similarly, clicking the "Purchase" button triggers another GET request if the video was played within the last 10 seconds. These GET requests contain query parameters like user_id, event, and time to log the user's actions on the server.

# Product.html
This is a simple HTML-based product page example with a JavaScript function that adds a product to a shopping cart. The code also implements a tracking pixel to record the "Add to Cart" events.

# Cart.html 
This is an HTML-based cart page example that uses JavaScript to dynamically display items in the shopping cart. It retrieves products from the browser's local storage, allowing the user to view their selected items and remove them if desired.
