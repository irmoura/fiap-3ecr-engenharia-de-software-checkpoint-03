import sqlite3
class Cliente_model():
    def __init__(self):
        #self.connection = sqlite3.connect(r'/C:/Users/logonpflocal/PycharmProjects/mvc/projetinho.db')
        self.connection = sqlite3.connect(r'/C:/Users/corag/OneDrive/FIAP/3ECR/Engenharia de Software/Checkpoints/03/mvc/mvc/projetinho.db')
        self.cursor = self.connection.cursor()

    def salvar(self, nome, email, telefone):
        try:
            print("[model] salvando...")
            query = "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT)"
            self.cursor.execute(query)
            query = "INSERT INTO clientes (nome, email, telefone) VALUES ('"+str(nome)+"', '"+str(email)+"', '"+str(telefone)+"')"
            self.cursor.execute(query)
            self.connection.commit()
            #self.connection.close()
            print("[model] salvou no model!")
        except sqlite3.Error as erro:
            print("[model] Algo deu errado: ", erro)

    def listar(self):
        try:
            print("[model] listando...")
            query = "SELECT * FROM clientes"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as erro:
            print("[model] Algo deu errado ao listar: ", erro)

