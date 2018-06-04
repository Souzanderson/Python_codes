import sqlite3

def Cad_pessoaf():
    conn = sqlite3.connect('clientes.db')
    cursor=conn.cursor()

    nome=input("nome: ")
    telef=input("telefone: ")
    cpf=input("CPF: ")
    
    cursor.execute("""
    INSERT INTO pessoa (nome,fone,CPF)
    VALUES (?,?,?)
    """,(nome,telef,cpf))
    conn.commit()
    print('Dados inseridos com sucesso!')
    conn.close

def Lista_pessoaf():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
    SELECT * FROM pessoa;
    """)

    for linha in cursor.fetchall():
        print(linha)
    print("\n\n")
    conn.close()
