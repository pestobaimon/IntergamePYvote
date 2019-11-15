from flask import request
from flask import jsonify
import pymongo
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route('/vote')
def vote():
    client = pymongo.MongoClient("mongodb+srv://katsumon:115245@cluster0-iygzc.mongodb.net/test?retryWrites=true&w=majority")
    db=client['uniqcodes']
    name_code = request.args.get('id').split(',')
    getname = name_code[0]
    getcode= name_code[1]
    fcode = db.set1.find_one({'id':getcode}) #find corresponding code
    if fcode is None:
        return ({'status':2})
    fname = db.partitest1.find_one({'name':getname}) #find corresponding participant name

    reformDictCode = dict()
    reformDictCode['id'] = fcode['id']
    reformDictCode['status'] = fcode['status']

    reformDictName = dict()
    reformDictName['name'] = fname['name']
    reformDictName['vcount'] = fname['vcount']
    if reformDictCode['status'] == 1: #check for valid code
        querycode = {'id':reformDictCode['id']} #update code to used state
        newvalcode = {'$set' : {'status':0}}
        db.set1.update_one(querycode,newvalcode)

        queryname = {'name':getname}
        updatevote = {'$set' : {'vcount':reformDictName['vcount']+1}}
        db.partitest1.update_one(queryname,updatevote)

        return ({"status":1})
    else:
        return ({"status":0})

