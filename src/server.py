from flask import Flask
server = Flask(__name__)

@server.route("/")
def mypythonapp():
  return "This is a sample app to test multi repo with common core code"

if __name__ == "__main__":
  server.run(host='0.0.0.0')
