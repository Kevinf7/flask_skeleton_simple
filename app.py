import time
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
