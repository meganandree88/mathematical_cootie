'''
File name: finalProject.py 
Project Owners: Megan Andree and Amelia McDowell
This file includes the necessary function to play a game Mathematical Caterpillar where a user answers mathematical equations and builds a caterpillar.
'''


import random
from cImage import *

def instruction():
    '''
    This function prints out the instructions for the game.
    '''
    
    print('Welcome to Mathematical Caterpillar!')
    print('*******************************')
    print('*******************************')
    print('The rules of the game are:')
    print('\n~The player will be presented with a mathetical question.\n If you answer the question correctly, the player will \n roll a five-sided die. Each number of the die corresponds to a \n part of the ant as follows:')
    print('\t 1 - Body \n\t 2 - Head \n\t 3 -  Antennae, Hat,  or Bow \n\t 4 - Eye \n\t 5  - Tongue, Teeth, or Lips')
    print('\n~The body part corresponding to the \n rolled number will be added if:')
    print('\tThe user already has a body. \n\t The body must be the first part of the caterpillar built. \n\t No body part will be added until the user has a body.')
    print('\tThe player has not already completed \n\t the structure for that specific body part')
    print('\n~The body part corresponding to the \n rolled number will not be added if:')
    print('\tThe body part for that specific number \n\t has been completed')
    print('\n~Then, the player will be  presented a new multiplcation question.')
    print('~If the  question is not answered correctly,\n the player  will get a STRIKE (X), and will be presented \n with a new mathematical problem.')
    print('~To win, the player must obtain one body,\n one head, one antennae, hat, or bow, two  eyes,\n and one tongue, teeth, or lips their caterpillar.')
    print('~The player will lose if they obtain 3 STRIKES (XXX) \n before completing the caterpillar structure.')
    print('\nThe difficulty levels of the mathemetical problems are:')
    print('1 - simple addition and subtraction')
    print('2 - single digit multiplcation')

def constructEquation1(choice):
    '''
    This function creates a list that includes the necessary parts of the equation. This function generates two random numbers and adds the signs of the equation needed to make the mathematical equation. 
    This function has one input: choice
    This function has one output: equation
    '''
    equation = []
    if choice == 1 or choice == 2 :
        numOne = random.randint(1,9)
        numTwo = random.randint(1,9)
        equation.append(numOne)
        equation.append(numTwo)
        equation.append('x')
        sign = random.randint(1,2)
        if choice == 1:
            if sign == 1:
                equation.append('+')
            else:
                equation.append('-')
        if choice == 2:
            equation.append('X')
        return equation
    else:
        print('You did not enter a valid selection from the menu.')

def constructEquation2(equation):
    '''
    This function creates a string of the mathematical equation, depending on the type of mathematical equation needed.
    This function takes one input: equation
    This function takes one output: string
    '''
    
    equation2 = []
    for i in range(len(equation)):
        equation2.append(str(equation[i]))
    string = ''
    if equation2[3] == '-' or equation2[3] == '+':
        firstRandom = random.randint(1,3)
        string = string + str(equation2[firstRandom - 1]) + ' '
        firstRemove = str(equation2[firstRandom -1])
        equation2.remove(firstRemove)
        string = string + str(equation2[2]) + ' '
        equation2.remove(str(equation2[2]))
        secondRandom = random.randint(1,2)
        string = string + str(equation2[secondRandom - 1]) + ' '
        secondRemove = str(equation2[secondRandom - 1])
        equation2.remove(secondRemove)
        string = string + '=  '
        string = string + equation2[0]
        return string
    elif equation2[3] == 'X':
        if equation[0] > equation[1] and (equation[0] / equation[1]) == (equation[0] // equation[1]):
            string = string + str(equation[1])  + ' ' + str(equation[3])
            string = string + ' ' + str(equation[2]) + ' = ' + str(equation[0])
            return string
        
        elif equation[1] > equation[0] and (equation[1] / equation[0]) == (equation[1] // equation[0]):
            string = string + str(equation[0]) + ' ' + str(equation[3])
            string = string + ' ' + str(equation[2]) + ' = ' + str(equation2[1])
            return string
        
        else:
            string = string + str(equation[0]) + ' ' + str(equation[3])
            string = string + ' ' + str(equation[1]) + ' = ' + str(equation[2])
            return string

def sameFormat(equation):
    '''
    This function coverts the equation inputted by the user to one consistent format. This function converts all letters to lowercase and deletes any spaces in the equation.
    This function has one input: equation
    This function has one output: equation
    '''
    equation = equation.lower()
    equation = equation.replace(' ','')
      
    return equation


def solve(equationString):
    '''
    This function solves the mathematical equation based on the type of mathematical equation and the placement of the variable x in the equation.
    This function has one input: equationString
    This function has one output depending on the type of mathematical equation:
    substraction, addition, multiplication
    '''
    splitString = equationString.split()
    if splitString[1] == '-' or splitString[1] == '+':
        newEquation = sameFormat(equationString)
    if splitString[1] == '-':
        for i in range(len(newEquation)): 
            if newEquation.index('x') > newEquation.index('='): #if x comes after the equal sign
                  subSign = newEquation.index('-')
                  equalSign = newEquation.index('=')
                  num1 = newEquation[0:subSign]
                  num2 = newEquation[subSign+1:equalSign]
                  num1 = int(num1)
                  num2 = int(num2)
                  subtraction = num1 - num2
            elif newEquation.index('x') == 0: #if x comes before the - sign
                  subSign = newEquation.index('-')
                  equalSign = newEquation.index('=')
                  num1 = newEquation[subSign + 1: equalSign]
                  num2 = newEquation[equalSign + 1: len(newEquation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  subtraction = num2 + num1
            else: #if x comes after the - sign but before the = sign
                  subSign = newEquation.index('-')
                  equalSign = newEquation.index('=')
                  num1 = newEquation[0:subSign]
                  num2 = newEquation[equalSign+1: len(newEquation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  subtraction = num1 - num2
                  
        return subtraction
    elif splitString[1] == '+':
        for i in range(len(newEquation)):
            if newEquation.index('x') > newEquation.index('='): #if x comes after the = sign
                  addSign = newEquation.index('+')
                  equalSign = newEquation.index('=')
                  num1 = newEquation[0:addSign]
                  num2 = newEquation[addSign+1:equalSign]
                  num1 = int(num1)
                  num2 = int(num2)
                  addition = num1 + num2
            elif newEquation.index('x') == 0: #if x comes before the + sign
                  addSign = newEquation.index('+')
                  equalSign = newEquation.index('=')
                  num1 = newEquation[addSign + 1: equalSign]
                  num2 = newEquation[equalSign + 1: len(newEquation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  addition = num2 - num1
            else: #if x comes after the + sign but before the = sign
                  addSign = newEquation.index('+')
                  equalSign = newEquation.index('=')
                  num1 = newEquation[0: addSign]
                  num2 = newEquation[equalSign + 1: len(newEquation) + 1]
                  num1 = int(num1)
                  num2 = int(num2)
                  addition = num2 - num1
        return addition
    elif splitString[1] == 'X':
        if splitString[4] == 'x':
            multiplication = int(splitString[0]) * int(splitString[2])
        else:
            multiplication = int(splitString[4]) // int(splitString[0])
        return multiplication
                
def buildBody(roll, bodyCount, myWin):
    '''
    this function shows the body of the caterpillar and accumulates the variable bodyCount
    This function takes three inputs: roll, bodyCount, myWin
    this function has one output: bodyCount
    '''
    body = FileImage('body.png')
    body.setPosition(body.getWidth()/2, body.getHeight()/4)
    body.draw(myWin)
    bodyCount = bodyCount + 1
    return bodyCount

def buildHead(roll, bodyCount, headCount, myWin):
    '''
    This function displays the head of the caterpillar and accumulates the variable headCount
    This function has four inputs: roll, bodyCount, headCount, myWin
    This function has one output: headCount
    '''
    body = FileImage('body.png')
    head = FileImage('head.png')
    head.setPosition((body.getWidth()/2)+ 40, body.getHeight()/1.1)
    head.draw(myWin)
    headCount = headCount +  1
    return headCount

def buildHat(roll, headCount, hatCount, myWin):
    '''
    This function displays the top accessory of the caterpillar and accumulates the variable hatCount
    This function has four inputs: roll,headCount, hatCount, myWin
    This function has one output: hatCount
    '''
    head = FileImage('head.png')
    body = FileImage('body.png')
    hat = FileImage('hat.png')
    bow = FileImage('bow.PNG')
    antennae = FileImage('antennae.png')
    headChoice = input('Do you want a hat(1), bow(2), or antennae(3) Enter a number value? ')
    if headChoice == '1':
        hat.setPosition((body.getWidth()/2)+92, body.getHeight()/2 + head.getHeight()/1.75)
        hat.draw(myWin)
    elif headChoice == '2':
        bow.setPosition((body.getWidth()/2)+155, body.getHeight()/2 + head.getHeight()/1.75)
        bow.draw(myWin)
    elif headChoice == '3':
        antennae.setPosition((body.getWidth()/2)+120, body.getHeight()/2 + (head.getHeight()/1.75)-35)
        antennae.draw(myWin)
    else:
        print('You did not enter a valid choice. A hat was added automatically.')
        hat.setPosition((body.getWidth()/2)+92, body.getHeight()/2 + head.getHeight()/1.75)
        hat.draw(myWin)
    hatCount = hatCount + 1
    return hatCount
def buildEye(roll, headCount, eyeCount, myWin):
    '''
    This function displays the eyes of the caterpillar and accumulates the variable eyeCount
    This function has four inputs: roll,headCount, eyeCount, myWin
    This function has one output: eyeCount
    '''
    head = FileImage('head.png')
    body = FileImage('body.png')
    eyes = FileImage('eyes.png')
    eyes.setPosition((body.getWidth()/2)+150, body.getHeight()/2 + head.getHeight())
    eyes.draw(myWin)
    eyeCount  = eyeCount + 1
    return eyeCount
def buildTeeth(roll, headCount, teethCount, myWin):
    '''
    This function displays the mouth accessory of the caterpillar and accumulates the variable teethCount
    This function has four inputs: roll,headCount, teethCount, myWin
    This function has one output: teethCount
    '''
    head = FileImage('head.png')
    body = FileImage('body.png')
    tongue =FileImage('tongue.png')
    lips = FileImage('lips.png')
    teeth = FileImage('teeth.png')
    mouthChoice = input('Do you want tongue(1), lips(2), or teeth(3)? ')
    if mouthChoice == '1':
        tongue.setPosition((body.getWidth()/2)+200, body.getHeight()/2 + head.getHeight()/(3/4)+38)
        tongue.draw(myWin)
    elif mouthChoice == '2':
        lips.setPosition((body.getWidth()/2)+175, body.getHeight()/2 + head.getHeight()/(3/4)-12)
        lips.draw(myWin)
    elif mouthChoice == '3':
        teeth.setPosition((body.getWidth()/2)+175, body.getHeight()/2 + head.getHeight()/(3/4)-12)
        teeth.draw(myWin)
    else:
        print('You did not enter a valid number. Teeth were added automatically.')
        teeth.setPosition((body.getWidth()/2)+175, body.getHeight()/2 + head.getHeight()/(3/4)-12)
        teeth.draw(myWin)
    teethCount = teethCount + 1
    return teethCount

def checkIfWin(bodyCount, headCount, hatCount, eyeCount, teethCount):
    if bodyCount == 1 and headCount == 1 and hatCount == 1 and eyeCount == 1 and teethCount == 1:
        return True
    else:
        return False

def main():
    #calls instruction function
    instruction()

    #prompts the user to input a difficulty level 
    choice = int(input('\nPlease select a level of difficulty for your mathematical practice.'))
    
    playAgain = 'y' #initializes variable playAgain
    
    while playAgain == 'y':

        #initializes variables to certain values
        builtCaterpillar = False
        myWinOpen = False
        correct = 0
        incorrect = 0
        buildCount = 0
        bodyCount = 0
        headCount = 0
        teethCount = 0
        hatCount = 0
        eyeCount = 0

        #while loop to generate new equations until game is won or lost
        while incorrect < 3 and builtCaterpillar == False:

            #calls constructEquation1 and constructEquation2 to generate mathematical equations and prints out the equation
            equation = constructEquation1(choice)
            equationString = constructEquation2(equation)
            print('Solve the following mathematical equation for x: ')
            print(equationString)

            #prompts the user to enter their answer
            answer = input('Enter your answer here: ')
            actualAnswer = solve(equationString) #calls the solve function to get the correct answer

            #checks to see if the answer is correct
            if answer == str(actualAnswer):
                print('You are correct!')
                correct = correct + 1

                #rolls a dice and generates a random number 1-5
                roll = random.randint(1,5)
                print('You rolled a ' + str(roll) + '!')

                #if the roll is one or the user has a body:
                if roll == 1 or bodyCount == 1:

                    #if roll is one, but there is no body:
                    if roll == 1 and bodyCount == 0:

                        #assigns body image to variable and opens image window
                        body = FileImage('body.png')
                        myWin = ImageWin('Cootie Building' , body.getWidth()*2, body.getHeight()*2)
                        myWinOpen = True #sets image window variable to True
                        bodyCount = buildBody(roll, bodyCount, myWin) #calls buildBody function
                    else:

                        #if roll is 2, there is a body, and there is no head, calls buildHead function
                        if roll == 2 and bodyCount == 1 and headCount == 0:
                            headCount = buildHead(roll, bodyCount, headCount, myWin)
                            
                        #if roll is 3, there is a body, a head and no hat, calls buildHat function
                        if roll == 3 and bodyCount == 1 and headCount == 1 and hatCount == 0:
                            hatCount = buildHat(roll, headCount, hatCount, myWin)

                        #if roll is 4, there is a body, a head, and no eyes, calls the buildEye function
                        if roll == 4 and bodyCount == 1 and headCount == 1 and eyeCount == 0:
                            eyeCount = buildEye(roll, headCount, eyeCount, myWin)

                        #if roll is 5, there is a body, head, and no teeth, calls buildTeeth function
                        if roll == 5 and bodyCount == 1 and headCount == 1 and teethCount == 0:
                            teethCount = buildTeeth(roll, headCount, teethCount, myWin)

                #calls the checkIfWin function to see if the user has won and assigns it to a variable
                builtCaterpillar = checkIfWin(bodyCount, headCount, hatCount, eyeCount, teethCount)
                
            else:
                '''
                if the answer from the user for the mathematical equation is not correct, 
                adds one to the accumulating variable incorrect and prints out the number of strikes,
                and exits the while loop if the number of incorrect answers is equal to 3.
                '''
                incorrect = incorrect + 1
                print('You are incorrect. You now have ' + str(incorrect) + ' strike(s).')
                if incorrect == 3:
                    break

        '''
        if the caterpillar is complete, prints out that the user has build the caterpillar,
        tells the user to click on the image to exit the image, and prints the final score.
        '''
        if builtCaterpillar == True:
            print('You have built the Caterpillar! Congratulations!')
            if myWinOpen == True:
                print('Please click on the image to close the game.')
                myWin.exitOnClick()
            print('Final Score')
            print('***********')
            print('Correct: ' + str(correct))
            print('Incorrect: ' + str(incorrect))

      
        elif incorrect >= 3 :
            '''
            if the number of incorrect answers is equal to or greater than 3, 
            prints out that the user has lost and prints the final score
            '''
            print('Oh no! you answered too many questions incorrectly. You lost!')

            #if the window for the caterpillar is open, prompts the user to click on the window to close the window
            if myWinOpen == True: 
                print('Please click on the image to close the game.')
                myWin.exitOnClick()
            print('Final Score')
            print('***********')
            print('Correct: ' + str(correct))
            print('Incorrect: ' + str(incorrect))

        #prompts the user to play again
        playAgain = input('Would you like to play again? Enter y for yes and n for no.')
            
        
    
main()
