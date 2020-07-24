import random

#Generating random 4-digit number
number_to_guess = str(random.randrange(1000, 9999))
#Initializing tries counter
loops_count = 1

#Function that compares user input to computer generated number 
def compare(user_number, computer_number):
    for i in range(0, 4):
        if user_number[i] == computer_number[i]: #Checking for numbers located correctly
            print(user_number[i], ': in place')
        elif user_number[i] in computer_number: #Checking for numbers that should be moved to another place
            print(user_number[i], ': somewhere else')
        else:
            print(user_number[i], ': none') #Numbers not in final answer

#Game loop
while True:
    user_input = input('Guess a 4-digit number: ')
#Checking if user input can be changed into integer - if not, printing message asking for numbers  
    try:
        value = int(user_input)
    except ValueError:
        print('Numbers, please!')
        continue   
    if user_input == number_to_guess:
        print('Right! It is ', number_to_guess, '. You guessed in ', loops_count, ' tries.')
        break
    else:
        compare(user_input, number_to_guess) #Calling compare function
        loops_count += 1 #Adding 1 to tries counter after every finished loop
  






