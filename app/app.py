from flask import Flask
import redis
import os

app = Flask(__name__)

# Initialize Redis connection
cache = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'),port=6379)

@app.route('/')
def index():
    count = cache.incr('visits')
    return f'Welcome to our world, You are visitor number {count}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

