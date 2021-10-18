from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Contact': '99876544456',
        'Name': 'Raju',
        'done': False
    },
    {
        'id': 2,
        'Contact': '9876543222',
        'Name': 'Rahul',
        'done': False
    }
]

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "please provide the data"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'Name':request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
    }
    contact.append(contact)
    return jsonify({
        "status": "success",
        "message": "task added succssfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })

if(__name__ == "__main__"):
    app.run(debug = True)