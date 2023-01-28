from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    print(f"data {request.args}")
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        data['success'] = 'true'
        print(json.dumps(data))
        return json.dumps(data)
    else:
        id = request.args.get('id')
        value = request.args.get('value')
        data = {'id': id, 'value': value, 'success': 'true'}
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
