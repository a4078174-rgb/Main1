# Main1# GitHub User Finder

## Автор
Артем Чигарев
## Описание
Приложение для поиска пользователей GitHub с возможностью добавления в избранное.

## Используемые технологии
- Python
- Tkinter (GUI)
- GitHub API

## Как использовать API
Используется endpoint:

https://api.github.com/search/users?q=USERNAME

Пример:
https://api.github.com/search/users?q=octocat

## Как запустить
1. Установить зависимости:
   pip install requests

2. Запустить:
   python main.py

## Функционал
- Поиск пользователей
- Отображение списка
- Добавление в избранное
- Сохранение в JSON

## Примеры использования
Поиск: "john"
Результат: список пользователей GitHub с именем john
