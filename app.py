from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Cloud Computing Lab Project - Deployed on PaaS!"

if __name__ == '__main__':
    app.run()