import psycopg2


class Database:
    def __init__(self, hostname, database, username, password, port_id):
        self.connection = psycopg2.connect(
            host=hostname, dbname=database, user=username, password=password, port=port_id
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()

    def init_todos_table(self):
        try:
            # Drop old table if exists
            self.cursor.execute("DROP TABLE IF EXISTS todos")

            sql_create_script = """ CREATE TABLE IF NOT EXISTS todos (
                                id      int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                name    varchar(300) NOT NULL,
                                status  varchar(40) NOT NULL)"""
            self.cursor.execute(sql_create_script)
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()

    def insert_into_todos(self, name, status):
        try:
            sql_insert_cmd = f"INSERT INTO todos (name,status) VALUES ('{name}','{status}')"
            self.cursor.execute(sql_insert_cmd)
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()

    def delete_record_by_id(self, id):
        try:
            sql_delete_cmd = f"DELETE FROM todos WHERE id = {id}"
            self.cursor.execute(sql_delete_cmd)
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()

    def update_record_by_id(self, id, new_name, new_status):
        try:
            sql_update_cmd = f"""UPDATE todos
            SET name = '{new_name}', status = '{new_status}'
            WHERE id = {id}"""
            self.cursor.execute(sql_update_cmd)
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()

    def get_record_by_id(self, id):
        try:
            sql_get_cmd = f"SELECT * FROM todos WHERE id = {id}"
            self.cursor.execute(sql_get_cmd)
            record = self.cursor.fetchone()
            return record
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()

    def get_all_records(self):
        try:
            sql_get_cmd = f"SELECT * FROM todos"
            self.cursor.execute(sql_get_cmd)
            records = self.cursor.fetchall()
            return records
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()

    def get_record_by_todo_name(self, name):
        try:
            sql_get_cmd = f"SELECT * FROM todos WHERE name = {name}"
            self.cursor.execute(sql_get_cmd)
            record = self.cursor.fetchone()
            return record
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()

    def preview_todos_table(self):
        try:
            sql_list_cmd = f"SELECT * FROM todos"
            self.cursor.execute(sql_list_cmd)
            todos_records = self.cursor.fetchall()
            for row in todos_records:
                print("")
                for index, elem in enumerate(row):
                    print(f"{row[index]}", end=" || ")
        except Exception as err:
            print(err)
        finally:
            self.connection.commit()


if __name__ == "__main__":
    pass
