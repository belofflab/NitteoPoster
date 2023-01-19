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
    
    def get_parser_pairs(self):
        """Получение доступных обменов"""
        self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_parser_pairs""")
        return [el for el in self.connection.cur]

    def get_valuts(self, id):
            """Получение доступных валют"""
            self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_valuts WHERE id = {id} """)
            return [el for el in self.connection.cur]
            
    def get_all_napobmens(self):
            """Получение доступных обменов"""
            self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_napobmens WHERE status = 1""")
            napobmens = [el for el in self.connection.cur]
            text ="1"
            # text = "".join([f"{self.get_valuts(napobmen[1])[4]} -> {self.get_valuts(napobmen[2])[4]} {napobmen[3] if napobmen[3] != '1' else napobmen[4]}" for napobmen in napobmens])
            print([self.get_valuts(napobmen[1])[4] for napobmen in napobmens])
            return text
