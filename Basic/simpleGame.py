import random
# GET GUESS

def get_guess():
    return list(input("What is your guess: "))

# GENERATE Computer code 

def generate_code():
    digit=[str(num) for num in range(10)]

    #shuffle the digits
    random.shuffle(digit)
    # Then grab first 3 difgit
    a=digit[:3]
    print("This is the code {0}".format(a))
    return a

# Generate the clues

def generate_clues(code,user_guess):

    if user_guess==code:
        return "CODE CRACKED"

    clues=[]

    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("closed")
    if clues==[]:
        return ["Nope"]
    else:
        return clues

# Run game logic
print("Welcome Code Breaker !")

secret_code=generate_code()

clue_report=[]

while clue_report!="CODE CRACKED":
    gess=get_guess()
    clue_report=generate_clues(gess,secret_code)
    print("here is the result of your guess :")
    for clue in clue_report:
        print(clue)



# x=get_guess()
# print(x)
# print(type(x))