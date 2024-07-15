from random import * 
import time 
def start(): 
    print('Введи первое число') 
    num_1 = int(input()) 
    print('Введи второе число') 
    num_2 = int(input()) 
    if num_1 > num_2: 
        num_1, num_2 = num_2, num_1 
    rnd = randrange(num_1, num_2) 
    print(f'Я загадал число от {num_1} до {num_2}, теперь попробуй его отгадать!') 
    otvet = int(input()) 
    flag = False 
    count = 1 
   
print('Привет! Давай сыграем в игру? Готов начать? Введи "да" или "нет" и нажми Enter') 
sogl = input() 
if sogl.lower() == 'нет': 
        print('Очень жаль! Возвращайся, как захочешь поиграть') 
while sogl != 'нет': 
    if sogl.lower() == 'да': 
        print('Отлично! Начинаем!') 
        time.sleep(3) 
        print('Тебе нужно ввести два числа, я выберу случайное число в этом диапазоне') 
        time.sleep(3) 
        print('Твоя задача будет угадать число которое я загадал') 
        time.sleep(3) 
        print('Не переживай, я буду тебе подсказывать') 
        time.sleep(3) 
        start() 
        print('Сыграем еще раз?') 
        sogl = input() 
        if sogl.lower() == 'нет': 
            print('Правильно, на сегодня достаточно') 
            break