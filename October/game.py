from random import randint
rand = randint(1,100)
while True:
    a = int(input('Угадай число '))
    if a>rand:
        print('Попробуйте меньше \n')
    elif rand>a:
        print('Попробуйте больше \n')
    else:
        print('Вы победили!!!')
        break