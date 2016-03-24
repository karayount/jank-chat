from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def show_chat():

    return render_template("chat-client.html")


@app.route('/create_message', methods=['POST'])
def create_message():

    new_message = request.form.get("message-field")
    global messages
    messages.append(new_message)

    return jsonify({})


@app.route('/deliver_new_messages.json')
def deliver_messages():

    global messages
    return jsonify(messages=messages)

if __name__ == '__main__':
    app.run()


# curl 127.0.0.1:5000/deliver_new_messages.json
# {
#   "messages": [
#     "I am a string",
#     "'string'",
#     "string"
#   ]
# }
# curl --data "message-field=string" 127.0.0.1:5000/create_message
# {}
