from flask import Flask 

app = Flask(__name__)


@app.route("/")
def home():
    return  """
    <!DOCTYPE html>
    <html>
       <head>
           <title>HTTP Cookies  Lab</title>
       </head>
       <body>
           <h1>Hello from Ubuntu Server!</h1>
           <p>This is our HTTP and Cookies laboratory.<p/>
       </body>
   </html>
   """



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8000, debug=False)
