# Tree_Menu - тестовое для UpTrader

## Запуск локально

1. Клонируйте репозиторий и перейдите в него в командной строке:
        ```
	git clone https://github.com/glebn5/test_Up_Trader.git
	```
2. Установите и активируйте виртуальное окружение:
	```
	python -m venv venv
	```
	Для Windows
	```
	source venv/Scripts/activate
	```
	Для linux/MacOs
	```
	source venv/Scripts/activate
	```
3. Установите зависимости из файла requirements.txt:
	```
	pip install -r requirements.txt
	```
4. Перейдите в `test_UpTrader` с файлом manage.py выполните миграции:
	```
	python manage.py migrate
	```
5. Создайте администратора
	```
	python manage.py createsuperuser
	```
6. Запустите сервер:
	```
	python manage.py runserver
	```
7. Зайдите в админку и создайте запись   
   ![](https://github.com/glebn5/test_Up_Trader/blob/main/Pasted%20image%2020250501111536.png?raw=true)   
   Где main_menu - одинаковое название как в {% draw_menu 'main_menu' %}
9. Далее создайте вторую запись, например О нас   
   ![](https://github.com/glebn5/test_Up_Trader/blob/main/Pasted%20image%2020250501111536.png?raw=true)   
10. Перейдите на http://127.0.0.1:8000/main_menu/. При наведении на main_menu должно отобразиться так:   
   ![](https://github.com/glebn5/test_Up_Trader/blob/main/Pasted%20image%2020250501112023.png?raw=true)
   
