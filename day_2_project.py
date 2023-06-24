print("Welcome to this soulless calculator")
total_bill = input("What's the total amount you losers spent? $")
percentage = input("What percentage can you broke fellas afford to give? 10, 12, or 15? ")
no_people = input("How many losers are you lot? ")

tip_percentage = float(total_bill) * (int(percentage)/100)
tip_per_person = tip_percentage / int(no_people)
split_bill = float(total_bill)/int(no_people)
result = round(tip_per_person + split_bill, 2)

if(int(percentage) <= 0):
    print("I'm too poor to afford to tip you lol!")
else:
    print(f"Each person should pay: ${result}")