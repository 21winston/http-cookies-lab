from flask import Flask, make_response, request

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
           <p>This is our HTTP and Cookies laboratory.</p>
       </body>
   </html>
   """

@app.route("/set-cookie")
def set_cookie():
    response = make_response("Cookie has been set.")
    response.set_cookie("visitor_id", "abc123")
    return response


@app.route("/read-cookie")
def read_cookie():
    visitor_id = request.cookies.get("visitor_id")

    if visitor_id:
       return f"Your visitor ID is: {visitor_id}"

    return "No visitor cookie found."


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8000, debug=False)
