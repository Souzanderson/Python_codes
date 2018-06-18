import sqlite3

def cria_banco(nome):
    conn = sqlite3.connect(nome+'.db')
    cursor = conn.cursor()
    op=0
    
    while(op!=9):
        print("""
        >>> Selecione uma op:
        (1)Criar Tabela
        (2)Criar Campo
        (3)Ver banco
        (4)Ver Esquema de Tabela
        (0)Deletar Tabela
        (9)SAIR
        (7)CRIAR BANCO
        ________________""")
        op=int(input("Escolha: "))

        #cria banco
        if op==7:
            nome=input("\nNome do banco: ")
            conn.close
            conn = sqlite3.connect(nome+'.db')
            cursor = conn.cursor()

        #cria tabela no banco de dados
        if op==1:
            print('digite um nome para a tabela:')
            tbl=input("nome: ")
            cursor.execute("""
            CREATE TABLE """+tbl+""" (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
                            );
            """)

            print('tabela ',tbl, 'criada com sucesso')

        #criar campos em uma tabela
        if op==2:
            tbl=input("Tabela: ")
            cont=int(input("Quantidade de campos: "))
            for i in range(0,cont):
                campo=input("Campo: ")
                cursor.execute("""
                ALTER TABLE """+tbl+"""
                ADD COLUMN """+campo)
                conn.commit()

        #mostra as tabelas no banco de dados    
        if op==3:
            cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
            """)

            print('\n________________\nTabelas:\n----------------')
            for tabela in cursor.fetchall():
                print("%s" % (tabela))
            print('________________\n')

        #ver esquema da tabela
        if op==4:
            tbl=input("Digite o nome da tabela que deseja consultar:\n>>> ")
            cursor.execute("""
            SELECT sql FROM sqlite_master WHERE type='table' AND name=?
            """, (tbl,))

            print('\n________________\nEsquema:\n----------------')
            for schema in cursor.fetchall():
                print("%s" % (schema))
            print('________________\n')

        #deleta uma tabela no banco de dados    
        if op==0:
            tbl=input("Qual tabela deseja deletar?\nnome: ")
            cursor.execute("""
            DROP TABLE IF EXISTS """+tbl)


    conn.close()
