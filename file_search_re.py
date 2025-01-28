import re
import os
import time
import datetime
from pathlib import Path
import math

start = time.time()

base_path = Path(Path().home(), "Downloads")
path_folder = Path(base_path,"myzip","Mi_Gran_Directorio")

pattern = r'N\D{3}-\d{5}'

today = datetime.date.today()

numbers_found = []
files_found = []

def search_number(file_path, pattern):
    my_file = open(file_path, 'r')
    content = my_file.read()
    if re.search(pattern, content):
        return re.search(pattern, content)
    else:
        return ''


def create_list():
    for folder, subfolder, file in os.walk(path_folder):
        for f in file:
            result = search_number(Path(folder,f), pattern)
            if result != '':
                numbers_found.append(result.group())
                files_found.append(f.title())


def init():
    print('-' * 50)
    print(f'Searching date: {today.day}/{today.month}/{today.year}')
    print('\n')
    print('FILE\t\t\tNRO. SERIE')
    print('-------------\t----------')

    for k,f in enumerate(files_found):
        print(f'{f}\t{numbers_found[k]}')

    print('\n')
    print(f'Numbers found: {len(numbers_found)}')

    end = time.time()
    duration = end - start
    print(f'Searching duration: {math.ceil(duration)} seg')

    print('-' * 50)


create_list()
init()


