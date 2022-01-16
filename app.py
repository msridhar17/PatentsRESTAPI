import glob
import pymongo
import os
import time
from flask import Flask,request
from datapreprocess import download_url,extract_zip,get_predata

'''
  1) Initiate the db
'''
def init_db():
    data = pymongo.MongoClient("mongodb://mongodb:27017")
    data_db = data["test_patent"]
    col = data_db["patents"]
    return col
'''
  Two end points
  1) load the url and insert required data to the db
  input: is the url to download zip file of the patents
  checklist:path exists or not and when api called three modules
  integrates with api, and write the response data from third module to the db
  response:results in length of patents and data
  errors(may rise):results in unpacked zipfile as its try to unzip with out proper content 
     stream i.e include time.sleep
  2) delete the patent info using key as patent_id
  
'''
app = Flask(__name__)

@app.route("/loadarchieves",methods=["GET"])
def fun_data():
    url = request.args.get("url")
    if not os.path.exists("test_patent.zip"):
           download_url(url,"test_patent.zip")
    time.sleep(3)
    if not os.path.isdir("test_patents"):
      extract_zip("test_patent.zip","test_patents")
    total_file_lists = []
    total_data = []
    for name in glob.glob('{}/*.xml'.format("test_patents")):
        total_file_lists.append(name)
        data = get_predata(name)
        total_data.append(data)
        data.pop('text-content')
        init_db().insert_one(data)
        data.pop('_id')
    return ({'status_code':200,'len':len(total_file_lists),"total_data":total_data})

@app.route("/deletepatent",methods=["DELETE"])
def fun_data_del():
    id_del = request.args.get("patentid")
    find_one = init_db().find_one({'patent_id':id_del})
    if find_one:
        del_id = init_db().delete_one({'patent_id':id_del})
        return ({'status_code':200,'response':'deleted successfully'})
    else:
        return ({'status_code': 404, 'response': 'requested id not found'})



