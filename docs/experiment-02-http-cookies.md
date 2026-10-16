Experiment 02: HTTP Cookies

Objective

Demonstrate how an HTTP server sets a cookie, how a client stores it, and how the client sends it in a subsequent request.

Implementation

The Flask application provides two routes:

GET /set-cookie sets visitor_id=abc123 using the Set-Cookie response header.

GET /read-cookie reads visitor_id from the incoming request and returns its value, or reports that no visitor cookie was found.

The value abc123 is hardcoded for this experiment.

Procedure and Results

The Flask application ran on port 8000 inside the Ubuntu Server VM. The following requests were issued from Windows using curl.

1. Set and store the cookie

curl -i -c cookies.txt http://192.168.26.129:8000/set-cookie

The server returned HTTP 200 OK, a Set-Cookie response header similar to:

Set-Cookie: visitor_id=abc123; Path=/

The response body was:

Cookie has been set.

The -c cookies.txt option instructed curl to save the received cookie in a cookie-jar file.

2. Send the stored cookie

curl -i -b cookies.txt http://192.168.26.129:8000/read-cookie

The application returned:

Your visitor ID is: abc123

The -b cookies.txt option instructed curl to send the stored cookie with the request.

Findings

The test demonstrated the cookie exchange:

The server sends a cookie in the Set-Cookie response header.

The client stores the cookie.

The client sends it in a later request using the Cookie request header.

Flask retrieves the value through request.cookies.

This shows how cookies can help an application recognise information across separate HTTP requests.

Limitations

The cookie value is hardcoded rather than generated dynamically.

The test used HTTP, so traffic was not encrypted.

Attributes such as Secure and HttpOnly were not configured.

Verification used curl responses and Flask logs; no packet capture was performed.

The application ran using Flask's development server.
