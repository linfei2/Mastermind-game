import random


NUMBER_TO_GUESS = str(random.randrange(1000, 9999))
LOOPS_COUNT = 1

def compare(user_number, computer_number):
    for i in range(0, 4):
        if user_number[i] == computer_number[i]:
            print(user_number[i], ': in place')
        elif user_number[i] in computer_number:
            print(user_number[i], ': somewhere else')
        else:
            print(user_number[i], ': none')
           
        
def main():   
    while True:
        user_input = input('Guess a 4-digit number: ')
        try:
            value = int(user_input)
        except ValueError:
            print('Numbers, please!')
            continue   
        if user_input == number_to_guess:
            print('Right! It is ', number_to_guess, '. You guessed in ', loops_count, ' tries.')
            break
        else:
            compare(user_input, number_to_guess)
            LOOPS_COUNT += 1
  

if __name__ == '__main__':
    main()




