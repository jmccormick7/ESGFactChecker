from db import PostgreSQLDatabase

db = PostgreSQLDatabase('Foret','user', 'pass' , 'localhost', '5173')
connection = db.connect()

db.execute_query("CREATE TABLE IF NOT EXISTS ESGDATA (id SERIAL PRIMARY KEY, company TEXT, gpt TEXT, news JSON;")

with pen("esgfactchecker/src/gpt_outputs/tesla.txt", "r") as f1, open("esgfactchecker/src/news_outputs/tesla.txt", "r") as f2:
    file1_content = f1.read()
    file2_content = f2.read()
db.execute_query("INSERT INTO ESGDATA (company, gpt, news) VALUES (%s, %s, %s)", ("Tesla", file1_content, file2_content))