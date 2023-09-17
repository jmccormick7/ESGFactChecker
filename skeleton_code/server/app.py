import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from db import PostgreSQLDatabase

app = Flask(__name__)
load_dotenv() 

# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
# db = SQLAlchemy(app)

# class Tweet(db.Model):
#     __tablename__ = "Tweets"

#     id = db.Column(db.Integer, primary_key = True)
#     author = db.Column(db.Text(), nullable = False)
#     tweet = db.Column(db.String(150), nullable = False)


#     def __init__(self, author, tweet):
#         self.author = author
#         self.tweet = tweet
    
#     def map(self):
#         return {'id': self.id, 'author': self.author, 'tweet': self.tweet}


db = PostgreSQLDatabase('Foret','user', 'pass' , 'localhost', '5432')
connection = db.connect()

@app.route('/')
def hello():
    return 'hello world'

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    query_string = request.args.get('q', default="", type=str)
    
    # Use the query_string to fetch data from the PostgreSQL database
    # For now, let's just return the query string as a placeholder
    return jsonify({"query": query_string})

@app.route('/add', methods = ['POST'])
def addMessage():
    data = request.get_json()
    tweet = Tweet(data['author'], data['tweet'])
    db.session.add(tweet)
    db.session.commit()
    return jsonify(tweet.map())

# @app.route('/delete/<id>', methods = ['DELETE'])
# def deleteMessage(id):
#     tweet = Tweet.query.get(int(id))
#     db.session.delete(tweet)
#     db.session.commit()
#     return jsonify(tweet.map())

# with app.app_context():
#     db.create_all()
#     db.session.commit()
 
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)
