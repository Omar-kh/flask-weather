from flask import Flask, render_template, request, jsonify
import requests as py_request
from form_example import CityForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/')
def index():
    form = CityForm()
    user_ip = request.headers["X-Forwarded-For"]
    r = py_request.get(
        f"http://api.ipstack.com/{user_ip}?access_key=ac818c67553e5e90adad3de5a376ef16")
    user_info = r.json()
    city = user_info.get("city", 'not found')
    lat = user_info.get('latitude', 'Not found')
    lon = user_info.get('longitude', 'Not found')
    r2 = py_request.get(
        f"https://api.darksky.net/forecast/0b1f03d065f776f4082cbaebe7f4b653/{lat},{lon}"
    )
    weather_info = r2.json()["currently"]["summary"]
    return render_template("index.html", user_ip=user_ip, city=city, weather=weather_info, latitude=lat, longitude=lon, form=form)


if __name__ == "__main__":
    app.run(debug=True,  host="0.0.0.0")
