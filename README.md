Микро приложение для работы с TODO-листом.

## Настройка

Переменные окружения:

```
DB_NAME: имя базы данных, в которой будет хранится TODO list.
```

## Установка

1. Создать виртуальное окружение

```shell
> python -m venv venv
```

2. Активировать виртуальное окружение

```shell
> . venv/bin/activate
```

```shell
> /venv/Scripts/Activate
```

3. Установить зависимости

```shell
> pip install -r requirements.txt
```

## Примеры использования

Получение справки:

```shell
> python todo.py -h
```

1. Добавление записи

```shell
> python todo.py -a "Some todo"
```

2. Удаление записи

```shell
> python todo.py -d "Some todo"
```

3. Посмотреть список записей

```shell
> python todo.py -l
```

## Тестирование

TODO: написать тесты и описать как их запускать
