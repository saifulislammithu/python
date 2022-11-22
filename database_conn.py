import sqlite3

stocks=[('GOOG',100,490.1),
        ('AAPL',50,545.75),
        ('FB',150,7.45),
        ('HPQ',75,33.2),]
def db_connect():
    db = sqlite3.connect('database.db')
    print('Database Connected........')
    c = db.cursor()
    return c




# for row in db.execute('select * from portfolio'):
#     print(row)