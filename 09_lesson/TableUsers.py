from sqlalchemy import create_engine, text


class TableUsers:

    __scripts = {
        "create": text("""
                INSERT INTO users(user_id, user_email, subject_id)
                VALUES (:id, :email, :subject)
            """),
        "update": text("""
                UPDATE users
                SET subject_id = :subject
                WHERE user_id = :id
            """),
        "delete": text("DELETE FROM users WHERE user_id = :id"),
        "get_by_id": text("SELECT * FROM users WHERE user_id = :id")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def create_uws(self, user_id, email, subject_id=1):
        conn = self.db.connect()
        sql = conn.execute(self.__scripts["create"], {
            "id": user_id,
            "email": email,
            "subject": subject_id
        })

        conn.commit()

    def update_user_ws(self, user_id, subject_id=15):

        conn = self.db.connect()
        sql = conn.execute(self.__scripts["update"], {
            "id": user_id,
            "subject": subject_id
        })
        conn.commit()

    def delete_user_ws(self, user_id):
        conn = self.db.connect()
        sql = conn.execute(self.__scripts["delete"], {"id": user_id})
        conn.commit()

    def get_user_by_id_ws(self, user_id):
        conn = self.db.connect()
        sql = conn.execute(self.__scripts["get_by_id"], {"id": user_id})
        return sql.fetchone()

    def cleanup_user_ws(self, user_id):
        conn = self.db.connect()
        sql = conn.execute(self.__scripts["delete"], {"id": user_id})
        conn.commit()
        