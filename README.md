**Установка**
1. Убедиться, что имеет место такая структура:
    - D
      - photo
        - photo-animation
          - main-dir
          - Новая папка
2. Клонируем проект в D:\photo
3. Создаем файл .env
4. Копируем в .env содержимое .env.example
5. В .env указываем настройки для доступа по ftp
6. Запускаем cmd.
7. Переходим в директорию программы
    ``` 
    d: & cd .\photo\images360upload
    ```
8. Создаем окружение
    ```
    python -m venv env
    ```
9. Активируем виртуальное окружение
    ``` 
    .\env\Scripts\activate.bat
    ```
10. Если видем такую строку
    ``` 
    (env) D:\photo\images360upload>
    ```
11. Устанавливаем зависимости
    ```
    pip install -r requirements.txt
    ```
**Для фотографа**
1. Копируем папки с фотографиями в D:\photo\photo-animation\main-dir
2. Запускаем командную строку cmd.
3. **Раскладка клавиатуры английская**
4. Переходим в папку программы и активируем виртуальное окружение и запускаем программу
    ```
   d: & cd .\photo\images360upload & .\env\Scripts\activate.bat & python app.py
   ```
5. В процессе выполнения, программа запрашивает разрешение на выгрузку архивов на сервер. Ввести y и нажать enter
6. Если 3Д успешно загружены на сервер, папку main-dir очистить