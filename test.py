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


# class DBManager:

#     def __init__(self) -> None:
#         self.connection = DBConnection()
#         self.prefix = "1mxs"
    
#     def get_parser_pairs(self):
#         """Получение доступных обменов"""
#         self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_parser_pairs""")
#         return [el for el in self.connection.cur]

#     def get_valuts(self, id):
#             """Получение доступных валют"""
#             self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_valuts WHERE id = {id} """)
#             return [el for el in self.connection.cur]
            
#     def get_all_napobmens(self):
#             """Получение доступных обменов"""
#             self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_napobmens WHERE status = 1""")
#             napobmens = [el for el in self.connection.cur]
#             text = "\n".join([f"{self.get_valuts(napobmen[1])[0][4]} -> {self.get_valuts(napobmen[2])[0][4]} {napobmen[3] if napobmen[3] != '1' else napobmen[4]}" for napobmen in napobmens])
#             return text

import datetime
class DBManager:
    def __init__(self) -> None:
            self.connection = DBConnection()
            self.prefix = "1mxs"

    def get_valuts(self):
            """Получение доступных валют"""
            self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_valuts""")
            return [el for el in self.connection.cur]

    def get_napobmens_2(self, id: str):
            """Получение доступных обменов"""
            self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_napobmens WHERE valsid1 = {id} AND status = 1""")
            return [el for el in self.connection.cur]

    def get_napobmens(self):
            """Получение доступных обменов"""
            self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_napobmens WHERE status = 1""")
            return [el for el in self.connection.cur]

    def get_course(self, first_id: str, second_id: str) -> str:
        self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_napobmens WHERE valsid1 = {first_id} AND valsid2 = {second_id}""")
        return [el for el in self.connection.cur]

    def get_pay_method(self, id: str):
        """Получаем информацию о платежном методе по ID"""
        self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_valuts WHERE id = {id}""")
        return [el for el in self.connection.cur]

    def get_xml(self, xml_cod: str):
        """Получаем инфу по xml_id"""
        self.connection.cur.execute(f"""SELECT * FROM {self.prefix}_valuts WHERE xml_value = '{xml_cod}'""")
        return [el for el in self.connection.cur]

    def add_order(
      self, 
      telegram_id: int, 
      fname: str, 
      login_tg: str, 
      summ1: str, 
      summ2: str, tdate, first_valute: str, second_valute: str):
        """Добавляем заявку"""
        self.connection.cur.execute(f"""
        INSERT INTO {self.prefix}_bids (
          email, 
          fio, 
          fname,
          tel, 
          summ1, 
          summ2, 
          status, 
          tdate, 
          schet1, 
          schet2, hashed, valut1, valut2, valut1type, valut2type, naprid, dop1, dop2, userip, skype, dmetas, acomments, editdate, naschet, iname, oname, pnomer, schet1_hash, schet2_hash, ucomments, user_hash, naschet_h, parthide) VALUES 
        ('{telegram_id}', '{fname} · {login_tg}', '{fname}', '{login_tg}', '{summ1}', '{summ2}', 'success', '{tdate}', '1', '2', 'hash', '{first_valute}', '{second_valute}', '0', '0', 0, '0', '0', '0', '0', '0', '0', '{tdate}', '0', '0', '0', '0', '0', '0', '0', '0', '0', 1)""")
        self.connection.mydb.commit()

    def get_last_order_id(self):
        """Получаем ID последней заявки"""
        self.connection.cur.execute(f"""SELECT id FROM {self.prefix}_bids ORDER BY id DESC""")
        return [el for el in self.connection.cur][0][0]


db = DBManager()

a = db.add_order(telegram_id=1, fname='s', login_tg='s', summ1='1', summ2='2', tdate=datetime.datetime.now(), first_valute='1', second_valute='s')
print(a)