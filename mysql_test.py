import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "RangerUp1515!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)
finally:
    db.close()