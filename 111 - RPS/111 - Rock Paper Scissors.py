import random


values = ["rock","paper","scissors"]




def game_logic(user_val):
    computer_val = random.choice(values)
    print "Computer Chose: %s" % computer_val
    if computer_val =="rock" and user_val == "scissors":
        



def get_input():
    user_val = raw_input("Throw: ")
    if user_val not in values:
        print "Not a valid value"
        # yeet in exception here
    else:
        return user_val

def main():

    game_logic(get_input())

if __name__ == '__main__':
    main()