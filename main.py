import requests
from datetime import datetime
import smtplib
import time

MY_LAT =  # Your latitude
MY_LONG = # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

my_email = "example@gmail.com"
password = "example"

while True:
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 or MY_LONG-5 <= iss_latitude <= MY_LONG+5:
        if time_now.hour >= sunset or time_now.hour <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="pycourse@hotmail.com", msg=f"subject:ISS Location\n\nLook Up")
                print(1)
    time.sleep(60)