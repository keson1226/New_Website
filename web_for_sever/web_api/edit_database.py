import sqlite3

con = sqlite3.connect("web_for_sever/web_database/database.db")
cursor = con.cursor()

def use_com(command:str):
    cursor.execute(command)


use_com(
    """

    CREATE TABLE `user_info`(
    `address` VARCHAR (64),  
    `password` VARCHAR (64),  
    `name` VARCHAR (20),  
    `phone_number` VARCHAR (10)
    )
    ;"""
    )


cursor.close()
con.close()
