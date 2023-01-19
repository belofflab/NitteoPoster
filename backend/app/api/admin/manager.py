import mysql.connector

class DBConnection:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="185.18.54.104",
            user="sql_gogo_exchang",
            passwd="dnNjfm4j6fArxLGx",
            database="sql_gogo_exchang"
        )
        self.cur = self.mydb.cursor()
   
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mydb.connection.close()


class DBManager:

    def __init__(self) -> None:
        self.connection = DBConnection()
        self.prefix = "1mxs"
    
    def get_parser_pairs(self, title_birg):
        """Получение доступных обменов"""
        self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_parser_pairs WHERE title_birg = {title_birg}""")
        return [el for el in self.connection.cur]
