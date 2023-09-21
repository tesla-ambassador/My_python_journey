#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Mail Merge Project Start/Input/Letters/starting_letter.txt') as file:
    letter = file.read()
    with open('Mail Merge Project Start/Input/Names/invited_names.txt') as guests:
        
        names = guests.readlines()
        
        for name in names:
            invite = letter.replace('[name]', name.strip())
            with open(f'Mail Merge Project Start/Output/ReadyToSend/{name}.txt', 'w') as output_file:
                output_file.write(invite)