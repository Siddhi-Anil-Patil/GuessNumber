import random

the_num = random.randint(1, 100)
print('The number to guess is',the_num)
comp_guess = random.randint(1, 100)
print('The computer guesses ', comp_guess)
t = 1

while comp_guess != the_num:
    print('The computer guesses ', comp_guess)
    t = t+1
    if comp_guess > the_num:
        comp_guess = comp_guess-1
    elif comp_guess < the_num:
        comp_guess = comp_guess+1
    elif comp_guess == the_num:
        break

print(t)
print('The computer guessed it right!')
