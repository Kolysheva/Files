import os
import pathlib
from glob import glob
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-name', nargs='?', default='Аноним')
parser.add_argument('-sogl', help="Продолжить или нет")
args = parser.parse_args()

pathlib.Path('test').expanduser().mkdir(parents=True, exist_ok=True)
with open('text.txt', 'w', encoding='utf8') as zad6:
    otvet = input('Здравствуйте! Рады видеть вас здесь. Вы согласны провести работу? \n '
                  'yes - для продолжения, no - для удаления файла \n')

    if otvet == 'Ок' or 'Ok':
        print(f'Имя: {args.name}', file=zad6)
    else:
        zad6.close()
        os.remove('text.txt')

    print(f'Отлично {args.name}! Дальше нам надо найти какое-нибудь изображение', file=zad6)
    print(f'Отлично {args.name}! Дальше нам надо найти какое-нибудь изображение')
    ListImage = glob("Pictures\Аватарки\*.jpg", recursive=True)
    print(ListImage)
