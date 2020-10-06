import mysql.connector

config = {
  'host' : "localhost",
  'user' : "root",
  'password' : "root",
  'database' : "testdb"
}

mydb = mysql.connector.connect(**config)

mycursor = mydb.cursor()

DB_NAME = 'testdb'

TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    " `text` varchar(250) NOT NULL,"
    " `user` varchar(250) NOT NULL,"
    " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

def create_database():
    mycursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

def create_tables():
    mycursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            mycursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)

create_database()
create_tables()

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    mycursor.execute(sql, (text, user,))
    db.commit()
    log_id = mycursor.lastrowid
    print("Added log {}".format(log_id))


def get_logs():
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    mycursor.execute(sql)
    result = mycursor.fetchall()

    for row in result:
        print(row[1])


def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s")
    mycursor.execute(sql, (id,))
    result = mycursor.fetchone()

    for row in result:
        print(row)


def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    mycursor.execute(sql, (text, id))
    db.commit()
    print("Log updated")


def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    mycursor.execute(sql, (id,))
    db.commit()
    print("Log removed")