from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to DevOps Application"

@app.route('/health')
def health():
    return "Application is Healthy"

@app.route('/orders')
def orders():
    return "Orders Service Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
