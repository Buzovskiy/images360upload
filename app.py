import sys
import time
from pywinauto.keyboard import send_keys
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError, ElementAmbiguousError, ElementNotFoundError
import clipboard
import warnings
import settings
import ftplib


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

# Access app window object
app_dialog = app.window()
app_dialog.set_focus()
time.sleep(2)
send_keys('^{TAB}')
send_keys('^l^c')
text = clipboard.paste()
print(text)
time.sleep(2)
send_keys('^{TAB}')
send_keys('^l^c')
text = clipboard.paste()
print(text)
time.sleep(2)
send_keys('^{TAB}')
send_keys('^l^c')
text = clipboard.paste()
print(text)
session = ftplib.FTP(settings.HOST,settings.USER,settings.PASSWORD)
file = open('img3d_002179.rar','rb')                  # file to send
session.storbinary('STOR img3d_002179.rar', file)     # send the file
file.close()                                    # close file and FTP
session.quit()
