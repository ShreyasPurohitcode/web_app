from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Shreyas' DevOps Journey!</h1><p>This simple web app is Dockerized and CI/CD automated. Let's keep the cool stuff rolling, one commit at a time!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)