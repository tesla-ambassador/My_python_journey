# I'm supposed to return a list that contains numbers that are common in both files.

with open('day_26/file_1.txt') as file_1:
    file_1_list = file_1.readlines()

with open('day_26/file_2.txt') as file_2:
    file_2_list = file_2.readlines()
        
result = [int(num.strip()) for num in file_2_list if num in file_1_list]
print(result)