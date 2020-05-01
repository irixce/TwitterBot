from flask import Flask, jsonify, request
from flask_cors import CORS

print("here")
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

screen_names = ["samp1"]

@app.route('/usernamesLink', methods=['GET', 'POST'])
def usernames():
    if request.method == 'POST':
        if (request.get_json()["exitCue"]):
            screen_names.clear()
        else:
            screen_name = request.get_json()["sn"]
            screen_names.append(screen_name)
    else:
        return jsonify({
        'status': 'success',
        'screenNames': screen_names
    })

if __name__ == '__main__':
    app.run()