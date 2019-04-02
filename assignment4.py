# Full Name: Yauheni Kalionau
# UCID: 30062335


# Function handleInput takes user input as a parameter, and then checks
# if the user's input has "." (dot) at the end.
# Variable "extension" finds "."(dot) in the uuser's input and returns an index:
# if extension is -1, that means that there is no "."(dot) in
# the user input, so that the function adds ".in" extension to the end.
# If extension is not -1(i.e. any other number), that means that there must be "."(dot)
# in the user's input and function has to check whether or not it is ".in"(i.e. not .py,.jpeg,etc)

def handleInput(userInput):
    extension = userInput.find('.')
    if userInput.endswith('.in'):
        choosen_file = userInput
    elif extension == -1:
        choosen_file = str(userInput)+".in"
    return choosen_file

    
            
    
def num_of_paragraphs(userInput):
    inputFile = (open(handleInput(userInput),'r')).read()
    # num_of_words = len(inputFile.split())
    num_of_paragraphs = inputFile.count('\n\n') + 1 
    return num_of_paragraphs
