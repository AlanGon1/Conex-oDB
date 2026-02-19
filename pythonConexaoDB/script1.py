import sqlite3 as conecector

try:
    # abertura da conexão e aquisição de cursor
    conexao = conecector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = '''CREATE TABLE Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (CPF)
                    );'''
    cursor.execute(comando)
    conexao.commit()

except conecector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    #Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()