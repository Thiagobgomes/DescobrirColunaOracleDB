import cx_Oracle, os, time



os.system('cls') # pdbmail.publica.lan.oraclevcn.com
dsn_tns = cx_Oracle.makedsn('10.0.2.7', '1521', service_name='pdbgera.publica.lan.oraclevcn.com') 
conn = cx_Oracle.connect(user=f'thiago', password=f'thiago', dsn=dsn_tns)




def Validar():
    if conn:
        return True

    return False



def Descobrir(Nome_Coluna):
    cur = conn.cursor() # INFO
    cur_Colunas = conn.cursor() 
    if Validar:

        tables = cur.execute(
            """
            SELECT TABLE_NAME FROM ALL_ALL_TABLES WHERE OWNER='DBCRED'
            """
        ).fetchall()

        for table in tables:
            colunas = cur_Colunas.execute(f"""
            SELECT COUNT(*) 
            FROM ALL_COL_COMMENTS 
            WHERE TABLE_NAME = '{table[0]}' AND COLUMN_NAME LIKE '%{Nome_Coluna.upper()}%'""").fetchall()

            for coluna in colunas:
                if coluna[0] >= 1 and '_NEW' in str(table[0]):
                    with open(f'Tables/tabelas_encontradas_{Nome_Coluna}.txt', 'a') as file:
                        file.write(f'{table[0]}\n')


                    
        cur.close()
        cur_Colunas.close()
        conn.close()
    else:
        print('Errro ao conectar ao programa')


TableName = input('Digite o nome da tabela que procura: ')

Descobrir(TableName)

