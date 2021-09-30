# Variable score contains the user's answers
score = 0

# Function contains the Intro to the program
def intro():
    print("How much money do you owe the IRS? Find out with this short quiz!")
    print("Respond with the number of each answer.")
    print("Entering anything other than a number will break the program!")
    print("-----------------------------------------------------------")
    # Before the quiz starts, the user will be given the option to choose to go right ahead into the questions,
    # OR optionally see "cheat codes" for the answers.
    print("Ready to get started?")
    print("1. Start quiz")
    print("2. Show cheat codes")
    answer = int(input(">"))
    if answer == 1:
        brandsOne() 
    elif answer == 2:
        cheatCodes()
# Function contains "cheat codes" for how to get the various results in this quiz
def cheatCodes():
    print("For result #1 - answer the questions in this order.")
    print("=====================")
    # This is the cheatcode for getting the "you owe $52,189" result
    print("3,5,11,14,20,24,27,32")
    print("")
    print("For result #2 - answer the questions in this order.")
    print("=====================")
    # This is the cheatcode for getting the "you owe $176,092" result 
    print("4,6,9,16,17,22,25,29")
    print("")
    # This is the cheatcode for getting the "you owe nothing" result
    print("For result #3 - find a way to dodge the selected answers OR enter 0 for each question.")
    print("-----------------------------------------------------------")
    # Present the user with the option to begin the quiz after they've been given the chance to review the codes
    print("Ready to get started?")
    print("1. Start quiz")
    answer = int(input(">"))
    if answer == 1:
        brandsOne()
# Function contains question one
# Because I'm using functions, I've set the score variable as global for each of the question's functions.
# This prevents the score variable from being rewritten as an entirely new variable each time
def brandsOne():
    global score
    print("")
    print("Which of the following?") 
    print("")
    print("1. Adidas") 
    print("2. Nike")
    print("3. Skechers")
    print("4. Crocs")
    answer = int(input(">"))
    if answer == 3:
        score = 10 + score
        brandsTwo()
    elif answer == 4:
        score = 15 + score
        brandsTwo()
    else:
        score = 0 + score
        brandsTwo()
# Function contains question two
def brandsTwo():
    global score
    print("")
    print("Which of the following?")
    print("5. American Eagle")
    print("6. Holister Co.")
    print("7. Gap")
    print("8. Hot Topic") 
    answer = int(input(">"))
    if answer == 5:
        score = 100 + score
        brandsThree()
    elif answer == 6:
        score = 150 + score
        brandsThree()
    else: 
        score = 10 + score
        brandsThree()
# Function contains question three
def brandsThree():
    global score
    print("")
    print("Which of the following?")
    print("9. Abercromie and Fitch")
    print("10. Footlocker")
    print("11. Old Navy")
    print("12. Champion") 
    answer = int(input(">"))
    if answer == 11:
        score = 1000 + score
        brandsFour()
    elif answer == 9:
        score = 1500 + score
        brandsFour()
    else: 
        score = 100 + score
        brandsFour()  
# Function contains question four
def brandsFour():
    global score
    print("")
    print("Which of the following?")
    print("13. Hermes")
    print("14. Gucci")
    print("15. Louis Vuitton")
    print("16. Calvin Klein") 
    answer = int(input(">"))
    if answer == 14:
        score = 1 + score
        brandsFive()
    elif answer == 16:
        score = 2 + score
        brandsFive()
    else: 
        score = 0 + score
        brandsFive()
# Function contains question five
def brandsFive():
    global score
    print("")
    print("Which of the following?")
    print("17. Armani Exchange")
    print("18. Tommy Hilfiger")
    print("19. Pacific Sunwear")
    print("20. Under Armour") 
    answer = int(input(">"))
    if answer == 20:
        score = 1 + score
        brandsSix()
    elif answer == 17:
        score = 2 + score
        brandsSix()
    else: 
        score = 0 + score
        brandsSix()
# Function contains question six
def brandsSix():
    global score
    print("")
    print("Which of the following?")
    print("21. Disney")
    print("22. H&M")
    print("23. Jordan")
    print("24. L.L Bean") 
    answer = int(input(">"))
    if answer == 24:
        score = 1 + score
        brandsSeven()
    elif answer == 22:
        score = 2 + score
        brandsSeven()
    else: 
        score = 0 + score
        brandsSeven()
# Function contains question seven
def brandsSeven():
    global score
    print("")
    print("Which of the following?")
    print("25. K-Swiss")
    print("26. Merrell")
    print("27. Clarks")
    print("28. Coach") 
    answer = int(input(">"))
    if answer == 27:
        score = 1 + score
        brandsEight()
    elif answer == 25:
        score = 2 + score
        brandsEight()
    else: 
        score = 0 + score
        brandsEight()
# Function contains question eight
def brandsEight():
    global score
    print("")
    print("Which of the following?")
    print("29. CeCe")
    print("30. Chaser")
    print("31. Eileen West")
    print("32. Fuzzi") 
    answer = int(input(">"))
    if answer == 32:
        score = 1 + score
        scoreCounter()
    elif answer == 29:
        score = 2 + score
        scoreCounter()
    else: 
        score = 0 + score
        scoreCounter()
# Function takes the value of score and prints a result based on the user's answers
def scoreCounter():
    global score 
    if score == 110:
        print("The End! After calculating your results.. you owe the IRS.. nothing!")
    elif score == 1115:
        print("The End! After calculating your results.. you owe the IRS $52,189")
    elif score == 1675:
        print("The End! After calculating your results.. you owe the IRS $176,092")
    # Will print a generic answer for any combination of numbers that were not already calculated above.
    else: 
        print("The End! Afrer calculating your results.. you owe the IRS $1,484,036")
# Starts the program
intro()
