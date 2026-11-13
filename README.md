# ocapp

Подбор вакансий по резюме

## Функционал на данный момент 
- Создание резюме и вакансий
- Подбор к резюме соответствущих по навыкам и образованию и зарплате вакансий

## Инструкция по установке

0. Клонируйте репозиторий: `git clone https://github.com/oddromancc/ocapp.git && cd ocapp`
1. Создайте виртуальное пространство: `python -m venv .venv`
2. Установка модулей `pip install -r requirements.txt`
3. Создайте проект: `npm init -y`
4. Установите tailwind и daisyui: `npm install tailwindcss@latest @tailwindcss/cli@latest daisyui@latest`
5. Создайте .css: `npm run build:css`
6. Запустите: `flask --app .\ocapp.py run`
