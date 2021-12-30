

from flask import Flask, jsonify, request,Response
from werkzeug.exceptions import abort

app = Flask(__name__)

records = [
]

@app.route('/records/<string:description>?')

def get_records(amount=None,description=None):
  return jsonify(records)

@app.route('/records/<int:amount>')
def get_last(amount):
    return jsonify(records)

@app.route('/records/<int:age>')
def age(age):
    return jsonify(records)
    
@app.route('/records')
def get_incoms():    
  return jsonify(records)


@app.route('/records', methods=['POST'])
def add_income():
  data=request.get_json()
  print(data)
  if len(data['lastname'])>100 or data['lastname'].isalpha()==False:
      abort(Response('invalid input'))
  elif len(data['firstname'])>100 or data['firstname'].isalpha()==False:
      abort(Response('invalid input'))
  elif data['age']>999:
      abort(Response('age is not valid'))


  records.append(request.get_json())
  print(records)
  return '', 204

@app.route('/records/size/<int:num>',methods=['GET'])
def get_limit(num):

    
    return jsonify(records[0:num])

if __name__=="__main__":
    app.run()
