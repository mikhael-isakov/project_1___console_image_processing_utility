from os import getcwd 
from os.path import join 
from sys import exit 
from json import loads 
from cv2 import imread, imwrite, resize, blur  
from functions import * 
from classes import * 


commands = []
images = []


with open(join(getcwd(), 'commands.json'), encoding='utf-8') as f: 
    commands_dict = loads(f.read())


for command in commands_dict: 
    cmd = commands_dict[command]
    for name in cmd["command_names"]: 
        commands.append(Command(name, cmd["function_name"], 
                                cmd["command_parameters"], 
                                cmd["command_description"], 
                                cmd["command_parameters_descriptions"]))


def main(): 
    
    while True: 

        print('\n==================================================')
        print('Программа обработки изображений, версия 2021.05.29')
        print('Изображений в памяти программы: {}'.format(len(images)))
        print('Доступны следующие команды: ', *commands) 
        print('Для справки по команде введите help (или h) и через пробел имя команды.')

        user_input = input('Ожидается ввод: ').split()
        
        com = False
        for command in commands: 
            if user_input[0] == command.name: 
                com = True 
                if len(user_input) - 1 == len(command.parameters): 
                    # получение объекта функции по её имени
                    f = globals()[command.function] 
                    f(commands, images, user_input)
                else: 
                    print('Количество параметров не соответствует синтаксису команды.')
        if not com: 
            print('Такая команда не поддерживается. Попробуйте снова.')


if __name__ == "__main__": 
    main()
