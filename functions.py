from main import * 


def help_(commands, images, user_input):
    com = False 
    for comm in commands:
        if comm.name == user_input[1]:
            com = True 
            print(f'''\nКоманда {comm.name} {comm.description}, и имеет следующий синтаксис:''')
            print(comm.name, *comm.parameters)
            if len(comm.parameters_descriptions) > 0:
                for i in range(len(comm.parameters)):
                    print(comm.parameters[i], '-', comm.parameters_descriptions[i])
    if not com:
        print('Пожалуйста, введите после help (или h) правильное имя команды')


def load(commands, images, user_input):
    try:
        img = Image(user_input[2], path=join(getcwd(), user_input[1]))
        if len(img.img.shape) == 3:
            images.append(img)
            print('Изображение из файла {} загружено в память программы под именем {}'.format(user_input[1], user_input[2]))
    except:
        print('Не удалось загрузить изображение из файла {}'.format(user_input[1]))



def resize_(commands, images, user_input):
    for image in images: 
        if image.name == user_input[1]: 
            result = resize(image.img, (int(user_input[3]) , int(user_input[4])))
    try:
        img = Image(user_input[2], image=result)
        images.append(img)
        print('Размеры изображения {} изменены, новое изображение называется {}'.format(user_input[1], img.name))
    except:
        print('Не удалось изменить размеры изображения {}'.format(user_input[1]))


def blur_(commands, images, user_input):
    for image in images: 
        if image.name == user_input[1]: 
            result = blur(image.img, (int(user_input[3]) , int(user_input[3])))
    try:
        img = Image(user_input[2], image=result)
        images.append(img)
        print('Изображение {} сглажено, новое изображение называется {}'.format(user_input[1], img.name))
    except:
        print('Не удалось сгладить изображение {}'.format(user_input[1]))


def undo(commands, images, user_input):
    images.pop()
    print('Состояние системы успешно откачено на шаг назад. Изображений в памяти: {}.'.format(len(images)))


def state(commands, images, user_input):
    print('Изображений в памяти: {}'.format(len(images)))
    if len(images) > 0: 
        print('Имена изображений, пути к файлам, и размеры файлов следующие:')
        for image in images:
            print(image.name, image.path, image.img.shape)


def save(commands, images, user_input):
    for image in images: 
        if image.name == user_input[1]: 
            try: 
                imwrite(join(getcwd(), user_input[2]), image.img)
                image.path = join(getcwd(), user_input[2])
                print('Изображение {} сохранено в файл {}'.format(user_input[1], user_input[2]))
            except: 
                print('Не удалось сохранить изображение {} в файл {}'.format(user_input[1], user_input[2]))


def exit_(commands, images, user_input):
    print('Программа завершает свою работу, спасибо за использование.')
    exit()
