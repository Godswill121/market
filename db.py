import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'emarket',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS items(
        ID INT NOT NULL AUTO_INCREMENT,
        itmename VARCHAR(255),
        price VARCHAR(255),
        seller INT,
        PRIMARY KEY(ID)
    )
    """
)




mycursor.execute(
    """CREATE TABLE IF NOT EXISTS itemtable(
        ID INT NOT NULL AUTO_INCREMENT,
        itmename VARCHAR(255),
        price INT,
        seller VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)



mycursor.execute(
    """CREATE TABLE IF NOT EXISTS itemstable(
        ID INT NOT NULL AUTO_INCREMENT,
        itmename VARCHAR(255),
        price INT,
        seller VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)
