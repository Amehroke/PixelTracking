# PixelTracking

This is a simple implementation of pixel tracking for user purchase after viewing product video.
# PixelBackend.py: 
  This Flask application serves as a basic web analytics tracker that listens on the /track endpoint for user events. It captures parameters like user_id, event, time, and optionally video_time from GET requests. The captured events, except those marked as video_play, are then stored in a JSON file named webpage_tracking.json. Additionally, the application returns a 1x1 transparent PNG pixel image as a response, commonly used as a tracking pixel on web pages. The entire app is intended to run in debug mode when executed directly.

  # Page1.html
  Basic mock
  
