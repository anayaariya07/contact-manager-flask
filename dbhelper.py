import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(  # keep your credentials here
            host='localhost',
            port='3306',
            user='root',
            password='Vitrizard90@',
            database='pythontest'
        )

        query = '''
        CREATE TABLE IF NOT EXISTS user(
            userId INT PRIMARY KEY,
            userName VARCHAR(200),
            phone VARCHAR(12)
        )
        '''
        cur = self.con.cursor()
        cur.execute(query)

    # INSERT
    def insert_user(self, userid, username, phone):
        query = "INSERT INTO user (userId, userName, phone) VALUES (%s, %s, %s)"
        cur = self.con.cursor()
        cur.execute(query, (userid, username, phone))
        self.con.commit()

    # FETCH ALL (IMPORTANT CHANGE)
    def fetch_all(self):
        query = "SELECT * FROM user"
        cur = self.con.cursor()
        cur.execute(query)

        data = []
        for row in cur:
            data.append({
                "id": row[0],
                "name": row[1],
                "phone": row[2]
            })
        return data

    # DELETE
    def delete_user(self, userId):
        query = "DELETE FROM user WHERE userId = %s"
        cur = self.con.cursor()
        cur.execute(query, (userId,))
        self.con.commit()

    # UPDATE
    def update_user(self, userId, newName, newPhone):
        query = "UPDATE user SET userName = %s, phone = %s WHERE userId = %s"
        cur = self.con.cursor()
        cur.execute(query, (newName, newPhone, userId))
        self.con.commit()