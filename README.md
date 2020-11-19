# To build this app
$ docker build -t mypythonapp . --no-cache

# To run this app
$ docker run -p 5000:5000 mypythonapp

# to check 
$ curl http://localhost:5000 # Contents from the current repo 
$ curl http://localhost:5000/base # Contents of base-core repo


