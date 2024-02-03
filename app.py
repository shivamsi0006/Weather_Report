from flask import Flask,render_template,request
import requests

api_key='db079e4025f64cab6510aca527846269'
app=Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
    
    return render_template("home.html")
@app.route('/search', methods=["GET","POST"])
def search():
    if request.method == "POST":
      
       city = request.form.get("val")
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    city=city.upper()
    if weather_data.json()['cod']=='404':
        return "NO CITY FOUND ..."
    else:
       
        # city=city.upper()
        weather=weather_data.json()['weather'][0]['main']
        temp=round(weather_data.json()['main']['temp'])
        temp=round((temp-32)*0.56)
        pressue=weather_data.json()['main']['pressure']
        humidity=weather_data.json()['main']['humidity']
        wind=weather_data.json()['wind']['speed']
        return render_template('home.html',temp=temp,pressure=pressue,humidity=humidity,wind=wind,weather=weather,city=city)

    
if __name__=='__main__':
    app.run(debug=True)