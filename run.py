from flask import Flask, request,make_response,jsonify
from chatbot import makeRequest
app = Flask(__name__)

@app.route('/api/v1/chatgpt', methods=['POST'])
def create_todo():
   data = request.get_json()
   result = makeRequest(data['message'])
   return make_response(jsonify({"chatgpt": result}), 200)

if __name__ == '__main__':
    app.run()