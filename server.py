from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Mail, Message
from werkzeug import exceptions
from controllers import dogs
from controllers import owners

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
    return jsonify({'message': 'Hello and welcome to our site!'}), 200

#we would use user input i.e. from a form for the recipients attribute - have just hard coded it for now
#to show a proof of concept
#Also we would probably use a dedicated email service but this is a naive solution
@server.route("/contact")
def contact():
   msg = Message('Hello', sender = 'ronaldtestisson@gmail.com', recipients = ['OJemireyigbe@gmail.com'])
   msg.body = "Hello, thanks for visiting our contact page, do you have any further inquiries regarding dogs or their owners?"
   mail.send(msg)
   return "Sent"

@server.route('/api/dogs', methods=['GET', 'POST'])
def dogs_handler():
    fns = {
        'GET': dogs.index,
        'POST': dogs.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


@server.route('/api/owners', methods=['GET', 'POST'])
def owners_handler():
    fns = {
        'GET': owners.index,
        'POST': owners.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


@server.route('/api/dogs/<int:dog_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def dog_handler(dog_id):
    fns = {
        'GET': dogs.show,
        'PATCH': dogs.update,
        'PUT': dogs.update,
        'DELETE': dogs.destroy
    }
    resp, code = fns[request.method](request, dog_id)
    return jsonify(resp), code

@server.route('/api/owners/<int:owner_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def owner_handler(owner_id):
    fns = {
        'GET': owners.show,
        'PATCH': owners.update,
        'PUT': owners.update,
        'DELETE': owners.destroy
    }
    resp, code = fns[request.method](request, owner_id)
    return jsonify(resp), code


@server.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@server.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

if __name__ == "__main__":
    server.run(debug=True)