# This program converts temperatures in degrees Celcius to Farenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
def convert_F(temp_c):
    temp_f = (temp_c * (9/5)) + 32
    return temp_f

weather_f = {day:convert_F(val) for (day, val) in weather_c.items()}

print(weather_f)