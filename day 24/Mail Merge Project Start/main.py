#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as Letter:
    currentLetter = Letter.read()
    with open("./Input/Names/invited_names.txt") as names:
        ListOfNames = names.readlines()
        for name in ListOfNames:
            temp = currentLetter.replace("[name]", name.strip())
            latterName = f"{name.strip()}_latter.txt"
            with open(f"./Output/ReadyToSend/{latterName}", mode="w") as invites:
                invites.write(temp)
                print(f"Letter created for {name}")