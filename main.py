from random import choice

passwords = open('passwords').read().split('\n')
lose = False
score = 0
while not lose:
    pass1, pass2 = choice(passwords), choice(passwords)
    user_choice = input(f'What password more popular {pass1}, {pass2}(input 1 or 2)?: ')
    while user_choice not in ('1', '2'):
        user_choice = input('Please, input 1 or 2: ')
    if (user_choice == '1' and passwords.index(pass1) < passwords.index(pass2)) or (user_choice == '2' and  passwords.index(pass1) > passwords.index(pass2)):
        print('Congrats, you guessed correctly')
        score += 1
    else:
        lose = True

print(f'You lost!!! Your score is {score}')
