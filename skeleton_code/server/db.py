import psycopg2

class PostgreSQLDatabase:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        sslmode = "disable"
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=None):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()

    def fetch_query(self, query, params=None):
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def __del__(self):
        self.close()

# Example usage:

# db = PostgreSQLDatabase(
#     dbname="your_database_name",
#     user="your_username",
#     password="your_password",
#     host="your_host",
#     port="your_port"
# )

# # Insert data
# db.execute_query("INSERT INTO sample (name) VALUES (%s)", ("John Doe",))

# # Fetch data
# rows = db.fetch_query("SELECT * FROM sample")
# print(rows)
