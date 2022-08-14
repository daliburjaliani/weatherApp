import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def current_weather(city):
    try:
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"q": city}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "12a69e6f6amsha30f238c0359684p17abbbjsn52afd73cfa59"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)

        temp = f"{round(data['main']['temp'] - 273.15)}°C"
        min_temp = f"{round(data['main']['temp_min'] - 273.15)}°C"
        max_temp = f"{round(data['main']['temp_max'] - 273.15)}°C"
        feel_like = f"{round(data['main']['feels_like'] - 273.15)}°"
        humidity = f"{data['main']['humidity']}%"
        visibility = f"{round((data['visibility'] / 1000), 1)}km/h"
        wind_speed = f"{round(data['wind']['speed'], 1)}m/s"
        cloud = f"{data['clouds']['all']}%"
        description = f"{data['weather'][0]['description']}"

        return temp, min_temp, max_temp, feel_like, humidity, visibility, wind_speed, cloud, description

    except Exception:
        return render_template("main.html",
                               city="Not Found")


def hourly_weather(city):
    try:
        url = "https://community-open-weather-map.p.rapidapi.com/forecast"

        querystring = {"q": city}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "12a69e6f6amsha30f238c0359684p17abbbjsn52afd73cfa59"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)

        description0 = data['list'][0]['weather'][0]['main']
        temp0 = f"{round(data['list'][0]['main']['temp'] - 273.15)}°"
        wind0 = f"{round(data['list'][0]['wind']['speed'], 1)}m/s"
        time0 = int(data['list'][0]['dt_txt'][11] + data['list'][0]['dt_txt'][12]) + 3

        description1 = data['list'][1]['weather'][0]['main']
        temp1 = f"{round(data['list'][1]['main']['temp'] - 273.15)}°"
        wind1 = f"{round(data['list'][1]['wind']['speed'], 1)}m/s"
        time1 = time0 + 3

        description2 = data['list'][2]['weather'][0]['main']
        temp2 = f"{round(data['list'][2]['main']['temp'] - 273.15)}°"
        wind2 = f"{round(data['list'][2]['wind']['speed'], 1)}m/s"
        time2 = time1 + 3

        description3 = data['list'][3]['weather'][0]['main']
        temp3 = f"{round(data['list'][3]['main']['temp'] - 273.15)}°"
        wind3 = f"{round(data['list'][3]['wind']['speed'], 1)}m/s"
        time3 = time2 + 3

        description4 = data['list'][4]['weather'][0]['main']
        temp4 = f"{round(data['list'][4]['main']['temp'] - 273.15)}°"
        wind4 = f"{round(data['list'][4]['wind']['speed'], 1)}m/s"
        time4 = time3 + 3

        description5 = data['list'][5]['weather'][0]['main']
        temp5 = f"{round(data['list'][5]['main']['temp'] - 273.15)}°"
        wind5 = f"{round(data['list'][5]['wind']['speed'], 1)}m/s"
        time5 = time4 + 3

        description6 = data['list'][6]['weather'][0]['main']
        temp6 = f"{round(data['list'][6]['main']['temp'] - 273.15)}°"
        wind6 = f"{round(data['list'][6]['wind']['speed'], 1)}m/s"
        time6 = time5 + 3

        description7 = data['list'][7]['weather'][0]['main']
        temp7 = f"{round(data['list'][7]['main']['temp'] - 273.15)}°"
        wind7 = f"{round(data['list'][7]['wind']['speed'], 1)}m/s"
        time7 = time6 + 3

        return description1, wind1, temp1, description0, wind0, temp0, description2, wind2, temp2, \
               description3, wind3, temp3, description4, wind4, temp4, description5, wind5, temp5, \
               description6, wind6, temp6, description7, wind7, temp7, time0, time1, time2, time3, \
               time4, time5, time6, time7

    except Exception:
        return render_template("hour.html",
                               city="Not Found")


def weekly(city):
    import datetime

    try:
        url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

        querystring = {"q": city, "lat": "35", "lon": "139", "cnt": "10", "units": "metric or imperial"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "12a69e6f6amsha30f238c0359684p17abbbjsn52afd73cfa59"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)

        hum0 = f"{data['list'][0]['humidity']}%"
        wind0 = f"{round(data['list'][0]['speed'], 1)}m/s"
        desc0 = data['list'][0]['weather'][0]['main']
        temp0 = f"{round(data['list'][0]['temp']['day'] - 273.15)}°"

        hum1 = f"{data['list'][1]['humidity']}%"
        wind1 = f"{round(data['list'][1]['speed'], 1)}m/s"
        desc1 = data['list'][1]['weather'][0]['main']
        temp1 = f"{round(data['list'][1]['temp']['day'] - 273.15)}°"

        hum2 = f"{data['list'][2]['humidity']}%"
        wind2 = f"{round(data['list'][2]['speed'])}m/s"
        desc2 = data['list'][2]['weather'][0]['main']
        temp2 = f"{round(data['list'][2]['temp']['day'] - 273.15)}°"

        hum3 = f"{data['list'][3]['humidity']}%"
        wind3 = f"{round(data['list'][3]['speed'], 1)}m/s"
        desc3 = data['list'][3]['weather'][0]['main']
        temp3 = f"{round(data['list'][3]['temp']['day'] - 273.15)}°"

        hum4 = f"{data['list'][4]['humidity']}%"
        wind4 = f"{round(data['list'][4]['speed'], 1)}m/s"
        desc4 = data['list'][4]['weather'][0]['main']
        temp4 = f"{round(data['list'][4]['temp']['day'] - 273.15)}°"

        import datetime

        weekday = ['Mon', 'Sun', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
        day1 = (datetime.datetime.today() + datetime.timedelta(days=1)).weekday()
        day2 = (datetime.datetime.today() + datetime.timedelta(days=2)).weekday()
        day3 = (datetime.datetime.today() + datetime.timedelta(days=3)).weekday()
        day4 = (datetime.datetime.today() + datetime.timedelta(days=4)).weekday()
        day5 = (datetime.datetime.today() + datetime.timedelta(days=5)).weekday()

        return hum0, wind0, desc0, temp0, hum1, wind1, desc1, temp1, hum2, wind2, desc2, temp2, \
               hum3, wind3, desc3, temp3, hum4, wind4, desc4, temp4, weekday[day1], weekday[day2], \
               weekday[day3], weekday[day4], weekday[day5]

    except Exception:
        return render_template("weekly.html",
                               city="Not Found")


@app.route('/', methods=["POST", "GET"])
def main():
    cit1, cit2, cit3, cit4, cit5, = "new york", "london", "tbilisi", "berlin", "paris"

    deg1, w1 = current_weather(cit1)[0], current_weather(cit1)[8]
    deg2, w2 = current_weather(cit2)[0], current_weather(cit2)[8]
    deg3, w3 = current_weather(cit3)[0], current_weather(cit3)[8]
    deg4, w4 = current_weather(cit4)[0], current_weather(cit4)[8]
    deg5, w5 = current_weather(cit5)[0], current_weather(cit5)[8]

    try:

        if request.method == 'POST':
            city = request.form['city']

            if current_weather(city)[8] == "cloudy" :
                url = "../static/cloud.png"
            else:
                url = "../static/sun.png"

            temp, min_temp, max_temp, feel_like, humidity, visibility, wind_speed, cloud, description = current_weather(city)

        else:

            city="london"

            if current_weather(city)[8] == "cloud":
                url = "../static/cloud.png"
            else:
                url = "../static/sun.png"

            temp, min_temp, max_temp, feel_like, humidity, visibility, wind_speed, cloud, description = current_weather(
                city)

        return render_template("main.html",
                               city=city.title(),
                               description=description.title(),
                               wind=wind_speed,
                               humidity=humidity,
                               temp=temp,
                               temp_min=min_temp,
                               temp_max=max_temp,
                               feel_like=feel_like,
                               visibility=visibility,
                               cloud=cloud,
                               deg1=deg1,
                               deg2=deg2,
                               deg3=deg3,
                               deg4=deg4,
                               deg5=deg5,
                               w1=w1,
                               w2=w2,
                               w3=w3,
                               w4=w4,
                               w5=w5,
                               url=url)
    except Exception:
        return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)
