from flask import Flask, render_template, request
import requests as py_request
app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    r = py_request.get(
        f"http://api.ipstack.com/{user_ip}?access_key=ac818c67553e5e90adad3de5a376ef16")
    print(r.json())
    lat = r.json().get('latitude', 'Not found')
    lon = r.json().get('longitude', 'Not found')
    print(lat, lon)
    return render_template('index.html', user_ip=user_ip)


if __name__ == "__main__":
    app.run(debug=True,  host="0.0.0.0")
