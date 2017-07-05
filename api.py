from flask import Flask, request, jsonify
#sudo pip install flask-cors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])

def home_page():
    return "Hello, World!"


@app.route('/hand_checker', methods=['POST'])
def hand_checker():

    # print request.form
    hand = request.form.getlist('hand[]')
    print hand
    #hand = ['1h 2h 1s 9d 13d']
    
    return jsonify({'message': 'You have %s and %s!' % (hand[0], hand[1])})

if __name__ == '__main__':
    app.run(debug=True)

