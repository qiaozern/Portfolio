#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    text = starting_letter.readlines()

with open("./Input/Names/invited_names.txt") as invited_names:
    names = (invited_names.readlines())
    name_list = []
    for i in names:
        name_list.append(i.strip())


for name in name_list:
    with open(f"./Output/ReadyToSend/output_{name}.txt", "w") as output:
        for txt in text:
            output.write(txt.replace(PLACEHOLDER, name))
