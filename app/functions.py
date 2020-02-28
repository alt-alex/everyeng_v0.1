def input_in_db():
    import  sqlite3
    from flask import Flask, request
    if request.method == 'POST':
        try:
            date = request.form['date']
            time = request.form['time']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO date (date,time) VALUES (?,?)",(date,time))
                con.commit()
                msg = "Record successfully added"
        except:
#                con.rollback()
                msg = "error in insert operation"

#        finally:
#                con.close()
    return msg


def get_from_db():
    import sqlite3
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from date")

    rows = cur.fetchall();
    return rows

