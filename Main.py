from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
  {
    'id': 1,
    'contact': "9999999999",
    'name': 'Siddharth',
    'saved': False
  },
  {
    'id': 2,
    'contact': '9876543210',
    'name': 'Geetha',
    'saved': False
  }
]

@app.route('/get-data', methods = ['GET'])
def getTask():
  return jsonify({
    'data': contacts
  })

@app.route('/add-data', methods = ['POST'])
def addTask():
  if not request.json():
    return jsonify({
      'status': 'Error',
      'message': 'Please provide the data.'
    }, 400)
  contact = {
    'id': contacts[-1]["id"]+1,
    'name': request.json['name'],
    'contact': request.json.get('contact', ''),
    'saved': False
  }

  contacts.append(contact)
  return jsonify({
    'status': 'Success!',
    'message': 'Data added to the API successfully.'
  })

if __name__=="__main__":
  app.run(debug=True)