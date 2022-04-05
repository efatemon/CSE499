cluster  = MongoClient("mongodb+srv://istiak:12345@cluster0.lqy6z.mongodb.net/test?retryWrites=true&w=majority ") 
db = cluster["test"] 
collection = db["test"] 
post = {"_id": 14, "content": main_text} try: 
    collection.insert_one(post) 
    print('Stored successfully') 
except: 
   print('an error occurred quotes were not stored to db. Try changing the ID number in post') 