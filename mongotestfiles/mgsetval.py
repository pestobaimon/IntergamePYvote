import pymongo

client = pymongo.MongoClient("")
db=client['uniqcodes']
getid = 'SZHRDMT5' #set id to change value here
fcode= db.set1.find_one({'id':getid})
reformdict=dict()
reformdict['id'] = fcode['id']
reformdict['status'] = fcode['status']
myquery = {'id':reformdict['id']}
newval = {'$set' :{'status':1}} #set value here
db.set1.update_one(myquery,newval)
print(db.set1.find_one({'id':getid}))
