import pymongo

client = pymongo.MongoClient("")
db=client['uniqcodes']
getid = '123'
fcode= db.set1.find_one({'id':getid})
print(fcode)
reformdict=dict()
reformdict['id'] = fcode['id']
reformdict['status'] = fcode['status']
print (reformdict)

if reformdict['status'] == 1:
    myquery = {'id':reformdict['id']}
    newval = {'$set' :{'status':0}}
    db.set1.update_one(myquery,newval)
else:
    print('failed to vote')

print(db.set1.find_one({'id':getid}))

