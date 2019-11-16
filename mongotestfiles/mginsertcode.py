import pymongo
client = pymongo.MongoClient("")
db=client['uniqcodes']

file = open("1000_unique_codes.csv",'r')
codeList=[]

for line in file.readlines():
    tempdict={}
    token = line.strip().split(',')
    tempdict['id']=token[0]
    tempdict['status']=int(token[1])
    codeList.append(tempdict)
db.set1.insert_many(codeList) #set 1 already inserted use other number!!

#for item in codeList:
#    print (item)




