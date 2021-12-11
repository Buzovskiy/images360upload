import sys
import os
from pathlib import Path
import shutil
import ftplib

import settings

# Дериктория программы
BASE_DIR = Path(__file__).resolve().parent
# Дериктория папок с изображениями
PHOTO_DIR = BASE_DIR.parent / 'photo-animation' / 'main-dir'

# список названий папок для архивации
dir_name_list = []

for x in os.listdir(PHOTO_DIR):
    if os.path.isdir(PHOTO_DIR / x):
        dir_name_list.append(x)

if len(dir_name_list) == 0:
    sys.exit("Ошибка: в папке main-dir отсутствуют папки с изображениями")

archive_paths = []
for dir_name in dir_name_list:
    archive_name = str(shutil.make_archive(PHOTO_DIR / dir_name, 'zip', PHOTO_DIR / dir_name))
    archive_paths.append((dir_name+'.zip', archive_name))

ans = input("Проверьте, сформированы ли архивы. \nЗагрузить архивы на сервер? (y/n): ")
if ans != 'y':
    sys.exit("Архивы на сервер не загружены. Программа остановлена")

session = ftplib.FTP(settings.HOST, settings.USER, settings.PASSWORD)
count = 0

for archive, path_to_archive in archive_paths:
    if os.path.exists(path_to_archive):
        file = open(path_to_archive, 'rb')  # file to send
        session.storbinary('STOR ' + archive, file)  # send the file
        count += 1
        print(f"------ {archive} загружен -------")
        file.close()  # close file and FTP
session.quit()
sys.exit(f"На сервер загружено {count} файлов \nВыполнение программы окончено")
