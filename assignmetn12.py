#Diego Espinola
#04.20.20
#this program will work with what we learned from the ReEX tutorials.


import re
# Lets use a regular expression to match a date string. Ignore
# the output since we are just testing if the regex matches.
word = input("Welcome,please type a word")


option = 0

while option != 11:
    print("Now, tell me what do you want to check?")
    print("1)See if your word contains a q")
    print("2)See if your word contains 'the'")
    print("3)See if your word contains a '*'")
    print("4)See if your word contains a digit")
    print("5)See if your word contains a '.'")
    print("6)See if your word contains at least 2 consecutive vowels")
    print("7)See if your word contains a 'white space'")
    print("8)See if your word has any letters that repeat three times in a single word")
    print("9)See if your word contains the word 'Hello'")
    print("10)See if your word contains an email address")
    option = int(input("\n > "))
    if option == 1:
        # Lets use a regular expression to match a date string. Ignore
        # the output since we are just testing if the regex matches.
        regex = "([q])"
        if re.search(regex, word):
            match = re.search(regex,word)
            print("True")
                

        else:
                # If re.search() does not match, then False is returned
            print("False")

    elif option == 2:
        regex = "[The]"
        if re.search(regex, word):
            print("True")
        else:
            print("False")

    elif option == 3:
        regex = "[*]"
        if re.search(regex, word):
            print("True")
        else:
            print("False")
    elif option == 4:
        regex = "[\d]"
        if re.search(regex, word):
            print("True")
        else:
            print("False")

    elif option == 5:
        regex = "[\.]"
        if re.search(regex, word):
            print("True")
        else:
            print("False")

    elif option == 6:
        #here i will the {2} to tell the program that the vowels need to be together.
        regex = "[aeiou]{2}"
        if re.search(regex, word):
            print("True")
        else:
            print("False")

    elif option == 7:
        regex = "\s"
        if re.search(regex, word):
            print("True")
        else:
            print("False")

    elif option == 8:
        regex = "([\D*]{0,3})"
        if re.match(regex, word):
            print("True")
        else:
            print("False")

    elif option == 9:
        regex = "^Hello"
        if re.search(regex, word):
            print("True")
        else:
            print("False")

    # THIS CODE IS A LONGER BUT IT WORKS, FOUND IT ON GOOGLE AND UNDERSTAND HOW IT WORKS.
    elif option == 10:
        regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.search(regex, word):
            print("True")
        else:
            print("False")







