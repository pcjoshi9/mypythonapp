from flask import Flask, render_template 
server = Flask(__name__,template_folder='template')

@server.route("/")
def mypythonapp():
  return "This is a sample app to test multi repo with common core code... Check out http://localhost:5000/base " 

f = open("/base-core/folder2/file2.txt", "r")
print(f.read())

with open('/base-core/folder2/file2.txt', 'r') as file:
  data = file.read().replace('\n', '')

@server.route("/base")
def base():
  return "Output from core files --- " + data

if __name__ == "__main__":
  server.run(host='0.0.0.0')
