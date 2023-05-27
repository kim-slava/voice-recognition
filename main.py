import speech_recognition
import os


def printInFile(task):
    folder = os.getcwd()
    files = os.listdir(folder)
    try:
        with open(files[-1], 'a+', encoding='utf-8') as f:
            f.write(task)
            f.write('\n')
            print('\nИнформация дозаписана')
    except:
        print('\nВы не создали ни одного файла. Скажите "создай файл"')


def MakeTxtFile():
    folder = os.getcwd()
    files = os.listdir(folder)
    name = files[-1]
    name = int(name.replace('.txt', '')) + 1
    fp = open(f'{name}.txt', 'w', encoding='utf-8')
    fp.close()
    print('\nФайл создан')

def listen():
    print('Говорите')
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        sr.pause_threshold = .5
        sr.adjust_for_ambient_noise(source=mic) #, duration=1
        audio = sr.listen(source=mic)

    try:
        task = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        print(task)

    except speech_recognition.UnknownValueError:
        print('\nкоманда не распознана')
        task = 'команда не распознана'
    return task


if __name__ == '__main__':
    directory = os.path.join(os.getcwd(), 'FilesTxt')
    # print(directory)
    os.chdir(directory)
    while True:
        task = listen()

        if task == 'создать файл':
            MakeTxtFile()
        elif task == 'завершить работу':
            print('\nДо свидания')
            exit()
        elif task == 'команда не распознана':
            pass
        else:
            printInFile(task)