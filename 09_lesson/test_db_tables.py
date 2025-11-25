from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:0208@localhost:5432/QA"
db = create_engine(db_connection_string)



def test_insert_user():

    with db.connect() as cleanup_conn:
        cleanup_conn.execute(text('DELETE FROM users WHERE "user_id" = 2411'))
        cleanup_conn.commit()

    try:
        connection = db.connect()
        transaction = connection.begin()

        sql = text("insert into users(\"user_id\", \"user_email\", \"subject_id\" ) values (2411, 'new_user_email', 1)")
        connection.execute(sql, {"new_user_name":"test2411@mail.ru"})

        transaction.commit()
        connection.close()

    finally:
        with db.connect() as cleanup_conn:
            cleanup_conn.execute(text('DELETE FROM users WHERE "user_id" = 2411'))
            cleanup_conn.commit()


    

def test_update_user():

    with db.connect() as cleanup_conn:
        cleanup_conn.execute(text('DELETE FROM users WHERE "user_id" = 2411'))
        cleanup_conn.commit()

    try:
        connection = db.connect()
        transaction = connection.begin()

        sql = text("update users set subject_id = :sb_id where \"user_email\" = 'test2411@mail.ru'")
        connection.execute(sql, {"sb_id": 15})

        transaction.commit()
        connection.close()

    finally:
        with db.connect() as cleanup_conn:
            cleanup_conn.execute(text('DELETE FROM users WHERE "user_id" = 2411'))
            cleanup_conn.commit()




def test_delete_user():

    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM company WHERE user_id = :us_id")
    connection.execute(sql, {"us_id": 2411})

    transaction.commit()
    connection.close()






    



