import pymongo
client = pymongo.MongoClient("mongodb+srv://katsumon:115245@cluster0-iygzc.mongodb.net/test?retryWrites=true&w=majority")
db=client['uniqcodes']
nameList=[]

for name in list(range(0,37)):
    tempdict={}
    tempdict['name']=str(name)
    tempdict['vcount']=0
    nameList.append(tempdict)

db.partitest1.insert_many(nameList) #set 1 already inserted use other number!!

#for item in codeList:
#    print (item)




