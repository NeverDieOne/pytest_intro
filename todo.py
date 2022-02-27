import argparse
import sqlite3
from dotenv import load_dotenv
import os


def create_db(db_conn):
    cur = db_conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS todo (todo_text TEXT);')
    db_conn.commit()


def get_todos(db_conn):
    cur = db_conn.cursor()
    cur.execute('SELECT * FROM todo;')
    return cur.fetchall()


def add_todo(db_conn, todo_text):
    cur = db_conn.cursor()
    cur.execute('INSERT INTO todo VALUES (?);', (todo_text,))
    db_conn.commit()


def delete_todo(db_conn, todo_text):
    cur = db_conn.cursor()
    cur.execute('DELETE FROM todo WHERE todo_text=?;', (todo_text,))
    db_conn.commit()


def get_args():
    parser = argparse.ArgumentParser(
        description='TODO Application'
    )
    parser.add_argument(
        '--add', '-a',
        help='Добавить todo в общий список'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='Отобразить список всех todo'
    )
    parser.add_argument(
        '--delete', '-d',
        help='Удалить todo из общего списка'
    )
    return parser.parse_args()


def main():
    load_dotenv()
    db_name = os.getenv('DB_NAME')
    args = get_args()
    db_conn = sqlite3.connect(db_name)

    try:
        create_db(db_conn)

        if args.add:
            add_todo(db_conn, args.add)
        if args.delete:
            delete_todo(db_conn, args.delete)
        if args.list:
            todos = get_todos(db_conn)
            print(todos)
    finally:
        db_conn.close()


if __name__ == '__main__':
    main()
