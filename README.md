# ocapp

Веб-приложение, сделанное с помощью Flask. Подбирает вакансии к резюме.

## Функционал на данный момент 
- Создание резюме и вакансий
- Подбор к резюме соответствущих по навыкам и образованию и зарплате вакансий
- База данных Sqlite хранит информацию во время работы сервера и после остановки сервера

## Инструкция по установке

0. Клонируйте репозиторий:
`git clone https://github.com/oddromancc/ocapp.git`
`cd ocapp`
2. Создайте и активируйте виртуальное пространство:`python -m venv .venv` `.\.venv\Scripts\activate`
3. Установка модулей `pip install -r requirements.txt`
4. Создайте проект: `npm init -y`
5. Установите tailwind и daisyui: `npm install tailwindcss@latest @tailwindcss/cli@latest daisyui@latest`
6. Создайте .css: `npm run build:css`
7. Запустите: `flask --app .\ocapp.py run`
