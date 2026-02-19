import sqlite3 as conector

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

comando = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
cursor.execute(comando, {"usa_oculos": True, "cpf": 20000000099})

conexao.commit()
cursor.close()
conexao.close()

