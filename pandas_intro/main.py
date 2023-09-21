# #1. with open('./pandas_intro/226 weather-data.csv') as file:
# #     weather_list = file.readlines()
# #     print(weather_list)

# #2. import csv

# # with open('./pandas_intro/226 weather-data.csv') as file:
# #     data_file = csv.reader(file)
# #     counter = 0
# #     temperatures = []
    
# #     for row in data_file:
# #         if counter > 0:
# #             temp_row = row[1]
# #             temperatures.append(int(temp_row))
# #         counter += 1
        
            
# #     print(temperatures)
    
# ##3. Using pandas
# import pandas
    
# data_frame = pandas.read_csv('pandas_intro/226 weather-data.csv')
# print(data_frame['temp'])

# # Finding Average.
# # average = sum(data_frame['temp'])/len(data_frame['temp'])
# # print(average)
# print(data_frame['temp'].mean())
# print(data_frame['temp'].max())

# #Printing the row of data that had the highest temperature.
# print(data_frame[data_frame['temp'] == data_frame['temp'].max()])

# #Converting Monday's temperature to farenheit
# monday_data = data_frame[data_frame['day'] == 'Monday']
# monday_temp = int(monday_data['temp'])

# farenheit_temp = (monday_temp * (9/5)) + 32
# print(f'The temperature in Farenheit is {farenheit_temp} ℉')

# # Creating a new DataFrame
# main_characters = {
#     "Name": ['Naruto', 'Luffy', 'Ichigo'],
#     "Powers": ['Rasengan', 'Gomu-Gomu', 'Getsugatensho']
# }

# new_dataframe = pandas.DataFrame(main_characters)
# new_dataframe.to_csv('./pandas_intro/main_characters.csv')

import pandas

data = pandas.read_csv('pandas_intro/228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
black = data[data['Primary Fur Color'] == 'Black']
cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
gray = data[data['Primary Fur Color'] == 'Gray']

black_fur = black['Primary Fur Color'].count()
cinnamon_fur = cinnamon['Primary Fur Color'].count()
gray_fur = gray['Primary Fur Color'].count()

data_dict = {
    "Primary Fur Color": ['Black', 'Cinnamon', 'Gray'],
    "Total": [black_fur, cinnamon_fur, gray_fur]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('./pandas_intro/fur.csv')