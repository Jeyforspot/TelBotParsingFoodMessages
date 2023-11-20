import sqlite3 as sq
import logging


def sql_start():
    global base, cur
    base = sq.connect(r"tgbot\infrastructure\sqlite_food_bot.db")
    cur = base.cursor()

    if base:
        logging.info(f"DB started successfully")
    sql_get_words()


def sql_add_user(user_id):
    cur.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
    base.commit()


def sql_delete_user(user_id):
    cur.execute("DELETE FROM users WHERE user_id = (?)", (user_id, ))
    num_rows_affected = cur.rowcount
    base.commit()
    return num_rows_affected


def sql_get_users():
    cur.execute("SELECT user_id FROM users")
    return cur.fetchall()


def sql_get_words():
    cur.execute("SELECT special_words FROM words")
    # dd = cur.fetchall()
    # for i in set(dd):
    #     print(i)
    return cur.fetchall()
