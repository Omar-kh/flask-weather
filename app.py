from flask import Flask, render_template, request, jsonify
import requests as py_request
app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.headers["X-Forwarded-For"]
    r = py_request.get(
        f"http://api.ipstack.com/{user_ip}?access_key=ac818c67553e5e90adad3de5a376ef16")
    user_info = r.json()
    city = user_info.get("city", 'not found')
    lat = user_info.get('latitude', 'Not found')
    lon = user_info.get('longitude', 'Not found')
    print(lat, lon)
    return render_template("index.html", user_ip=user_ip, city=city)


if __name__ == "__main__":
    app.run(debug=True,  host="0.0.0.0")
