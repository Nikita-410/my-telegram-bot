from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mine', methods=['POST'])
def mine():
    data = request.get_json()
    earned = data.get("earned", 0)
    return jsonify({"status": "success", "earned": earned})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
