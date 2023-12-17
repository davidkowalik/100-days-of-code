#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_path = 'Input\\Names\\invited_names.txt'
letter_path = "Input\\Letters\\starting_letter.txt"
output_path = "Output\\ReadyToSend\\"

PLACEHOLDER = "[name]"

# create a list of names extracted form invited_names.txt
with open (names_path) as names_file:
        names = names_file.read()
        names_list = (names.split("\n"))

with open (letter_path) as letter_file:
      letter = letter_file.read()

for name in names_list:
    new_letter = letter.replace(PLACEHOLDER, name)
    with open((f"{output_path}{name}.txt"), "x") as new_file:
          new_file.write(new_letter)
