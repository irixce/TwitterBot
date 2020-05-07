from flask import Flask, jsonify, request
from flask_cors import CORS
from subprocess import call

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

screen_names = []
db_list = []
db_dict = {}
common_followers_list = []
followers_dict = {}

@app.route('/usernamesLink', methods=['GET', 'POST'])
def usernames():
    if request.method == 'POST':
        if (request.get_json()["exitCue"] == True):
            screen_names.clear()
        elif (request.get_json()["exitCue"] == "snDel"):
            sn_to_delete = request.get_json()["deleteSn"]
            screen_names.remove(sn_to_delete)
        else:
            screen_name = request.get_json()["sn"]
            screen_names.append(screen_name)
    else:
        return jsonify({
        'status': 'success',
        'screenNames': screen_names
    })

@app.route('/database', methods=['GET', 'POST'])
def db():
    if request.method == 'POST':
        res = list(request.get_json())
        db_list.append(list(request.get_json()))
        #creating custom dict
        db_dict[res[0]['screen_name'].lower()] = {'protected': res[0]['protected'], 'description': res[0]['description']}
        print(db_dict)
        #print(list(request.get_json()))
    else:
        call(["node", "bot.js"])
        #print(db_list[0][0]["protected"])
        return jsonify({
        'status': 'success',
        'db': db_dict

    })

@app.route('/followers', methods=['GET', 'POST'])
def followersFunc():
    if request.method == 'POST':
        print([request.get_json()["follower_screen_name"]])
        if screen_names[-1] in followers_dict.keys():
            followers_dict[screen_names[-1]].extend([request.get_json()["follower_screen_name"]])
            print(followers_dict)
        else:
            followers_dict[screen_names[-1]] = []
    else:
        common_followers_list = calculate_common_followers()
        return jsonify({
        'status': 'success',
        'common_followers_list': common_followers_list,
        'followers': followers_dict

    })

def calculate_common_followers():
    set_list = []
    for k in followers_dict.keys():
        print(followers_dict[k])
        set_list.append(set(followers_dict[k]))
    print(set_list)
    return list(set.intersection(*set_list))

if __name__ == '__main__':
    app.run()