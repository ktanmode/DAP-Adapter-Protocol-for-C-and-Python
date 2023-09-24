
import random
import string
import debugpy


def helloWorld(input):
    if(isinstance(input, str)):

        word = input.upper()
        try:

            if word[0] == "H":
                if word[1] == "E":
                    if word[2] == "L":
                        if word[3] == "L":
                            if word[4] == "O":
                                if word[5] == "W":
                                    if word[6] == "O":
                                        if word[7] == "R":
                                            if word[8] == "L":
                                                if word[9] == "D":
                                                    return ("Valid Input")
                                                return ("Invalid Input at 10")
                                            return ("Invalid Input at 9")
                                        return ("Invalid Input at 8")
                                    return ("Invalid Input at 7")
                                return ("Invalid Input at 6")
                            return ("Invalid Input at 5")
                        return ("Invalid Input at 4")
                    return ("Invalid Input at 3")
                return ("Invalid Input at 2")
            return ("Invalid Input at 1")

        
        except IndexError:
            raise ValueError("Incomplete Input")
            #return "Incomplete Input"
        
    else:
        return ValueError("Not a string")


def get_random_char():
    # choose from all lowercase letter
    letter = random.choice(string.ascii_lowercase)
    return letter

randominput = ''

helloWorld("helloworld")

#while (helloWorld(randominput) != "Valid Input"):

#    randominput = randominput + get_random_char()
#    print(randominput+"\n")
    

#print("Input String:")