import services.database as db
import models.Cliente as cliente

def Incluir(cliente):
    add_person = ("INSERT INTO pessoa "
               "(id, nome, idade, profissao) "
               "VALUES (%s, %s, %s, %s)")
    data_person = (cliente.id, cliente.nome, cliente.idade, cliente.profissao)

    db.cursor.execute(add_person, data_person)
    emp_no = db.cursor.lastrowid

    db.cnx.commit()
    # db.cnx.close()
    # db.cursor.close()

def selecionarById(id):
    costumerList = []
    id_cliente = [(id)]
    query = ("SELECT * FROM pessoa WHERE id = (%s) ")
    db.cursor.execute(query, id_cliente)

    for row in db.cursor.fetchall():
        print (row)
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))
    return costumerList[0]

def Alterar(cliente):
    add_person = ("UPDATE pessoa "
                  " SET nome = (%s), idade = (%s), profissao = (%s) "
                  "WHERE ID = (%s)")
    data_person = (cliente.nome, cliente.idade, cliente.profissao, cliente.id,)

    db.cursor.execute(add_person, data_person)
    #emp_no = db.cursor.lastrowid

    db.cnx.commit()

def Excluir( id):
    id_delete = [(id)]
    delete_person = ("DELETE FROM pessoa WHERE id = (%s) ")
    db.cursor.execute(delete_person, id_delete)
    #emp_no = db.cursor.lastrowid
    db.cnx.commit()

def selecionarTodos():
    costumerList = []
    query = ("SELECT * FROM pessoa")
    db.cursor.execute(query)
    #print(cursor.fetchall())
    for row in db.cursor.fetchall():
        print (row)
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))
    return costumerList
    
    
