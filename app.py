from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>RHEL 9.6 CI/CD Pipeline is Live!</h1><p>Status: Successfully Deployed via Jenkins & Podman</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
