#!flask/bin/python
from flask import Flask,request
import os,random
import json
images=[]
mypath="/home/yusufnuh/ftp/files"
entries = os.listdir(mypath)
                                
app = Flask(__name__)
@app.route('/api/bitirme/images/all',methods=['GET'])

def randomSend():
    
    random.shuffle(entries)
    
    for entry in entries:
        images.append(entry)
        if len(images) == 5:
            break
    jsonobject=json.dumps(images)
    images.clear()
    return jsonobject
@app.route('/api/bitirme/images',methods=['GET'])
def single():
    if 'name' in request.args:
        name =request.args['name']
    else:
        return "Error: No name field provided. Please specify an name."

    results = []

   
    for image in entries:
        if image == name:
            results.append(image)

    jsonobject=json.dumps(results)

    return jsonobject


if __name__ == '__main__':
    app.run(host='46.101.154.46',port='5000', debug=True)
