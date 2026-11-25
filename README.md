# ocapp

Веб-приложение, сделанное с помощью Flask. Подбирает вакансии к резюме.

## Функционал на данный момент 
- Создание резюме и вакансий
- Подбор к резюме соответствущих по навыкам и образованию и зарплате вакансий
- База данных Sqlite хранит информацию во время работы сервера и после остановки сервера

## Инструкция по установке

Клонируйте репозиторий:
```
git clone https://github.com/oddromancc/ocapp.git
```
Перейдите в папку ocapp:
```
cd ocapp
```
Создайте виртуальное пространство:
```
python -m venv .venv
```
Активируйте его:
```
.\.venv\Scripts\activate
```
Установка нужные модулей:
```
pip install -r requirements.txt
```
Создайте проект npm:
```
npm init -y
```
Установите tailwind и daisyui:
```
npm install tailwindcss@latest @tailwindcss/cli@latest daisyui@latest
```
Создайте .css:
```
npm run build:css
```
Запустите:
```
flask --app .\ocapp.py run
```
