from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Mail, Message

server = Flask(__name__)
CORS(server)


server.config['MAIL_SERVER']='smtp.gmail.com'
server.config['MAIL_PORT'] = 465
server.config['MAIL_USERNAME'] = 'ronaldtestisson@gmail.com'
server.config['MAIL_PASSWORD'] = 'Futureproof1.'
server.config['MAIL_USE_TLS'] = False
server.config['MAIL_USE_SSL'] = True
mail = Mail(server)




@server.route('/')
def home():
    return jsonify({'message': 'Hello and welcome to <insertName>!'}), 200

@server.route("/contact")
def contact():
   msg = Message('Hello', sender = 'ronaldtestisson@gmail.com', recipients = ['OJemireyigbe@gmail.com', 'derejemireyigbe@gmail.com'])
   msg.body = "Hello, thanks for visiting our contact page, do you have any further equiries?"
   mail.send(msg)
   return "Sent"




if __name__ == "__main__":
    server.run(debug=True)