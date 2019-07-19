from flask import Flask, render_template, request, jsonify
import requests as py_request
app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.headers["X-Forwarded-For"]
    r = py_request.get(
        f"http://api.ipstack.com/{user_ip}?access_key=ac818c67553e5e90adad3de5a376ef16")
    user_info = r.json()
    lat = r.json().get('latitude', 'Not found')
    lon = r.json().get('longitude', 'Not found')
    print(lat, lon)
    return user_info


if __name__ == "__main__":
    app.run(debug=True,  host="0.0.0.0")
