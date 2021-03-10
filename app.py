import re
import sys
import os
from pathlib import Path
import time
import shutil
from pywinauto.keyboard import send_keys
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError, ElementAmbiguousError, ElementNotFoundError
import clipboard
import warnings
import ftplib

# import settings

# Дериктория программы
BASE_DIR = Path(__file__).parent
# Дериктория папок с изображениями
PHOTO_DIR = BASE_DIR.parent / 'photo-animation' / 'main-dir'

warnings.simplefilter('ignore', category=UserWarning)
windows = Desktop(backend="uia").windows()

app = Application()
try:
    app.connect(title_re=".*(?i)(chrome).*")
except ElementAmbiguousError as e:
    print('Ошибка: запущено более одного браузера Chrome: ', e)
    sys.exit("Программа завершена с ошибками")
except ElementNotFoundError as e:
    print('Ошибка: окно браузера Chrome не найдено: ', e)
    sys.exit("Программа завершена с ошибками")

count = 0
# список названий папок для архивации
dir_name_list = []

for x in os.listdir(PHOTO_DIR):
    if os.path.isdir(PHOTO_DIR / x):
        dir_name_list.append(x)

if len(dir_name_list) == 0:
    sys.exit("Ошибка: в папке main-dir отсутствуют папки с изображениями")

# Access app window object
app_dialog = app.window()
# list of tuples: (directory name, product id)
dir_ids = []

for x in dir_name_list:
    app_dialog.set_focus()
    time.sleep(0.5)
    send_keys('^{TAB}')
    send_keys('^l^c')
    # Get product url
    url = clipboard.paste()
    # Get product id
    try:
        id_product = re.search(r"/(\d+)/?$", url).group(1)
    except AttributeError as e:
        print(url)
        print("не удалось получить id товара: ", e)
        sys.exit("Программа завершена с ошибками")
    dir_ids.append((x, id_product))

for dir_name, id_product in dir_ids:
    print(PHOTO_DIR / id_product, PHOTO_DIR / dir_name)
    shutil.make_archive(PHOTO_DIR / id_product, 'zip', PHOTO_DIR / dir_name)

sys.exit(0)

session = ftplib.FTP(settings.HOST, settings.USER, settings.PASSWORD)
file = open('img3d_002179.rar', 'rb')  # file to send
session.storbinary('STOR img3d_002179.rar', file)  # send the file
file.close()  # close file and FTP
session.quit()
