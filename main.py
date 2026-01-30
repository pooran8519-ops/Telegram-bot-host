# At the top add render specific imports
import os
import sys
import signal

# Flask app for uptime (already in your code)
from flask import Flask
from threading import Thread

# At the bottom replace main execution with:
if __name__ == '__main__':
    # Render specific setup
    port = int(os.environ.get("PORT", 10000))
    
    # Start Flask server in background
    keep_alive()
    
    # Start bot polling with error handling
    logger.info("🚀 Bot starting on Render...")
    
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=30)
        except Exception as e:
            logger.error(f"Polling error: {e}")
            import time
            time.sleep(5)
