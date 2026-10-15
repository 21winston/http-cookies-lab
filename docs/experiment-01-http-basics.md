# Experiment 1: Inspecting HTTP Requests and Responses

## 1. Objective

The objective of this experiment was to observe HTTP communication
between a Windows client and an Ubuntu Server running a small
Flask web application.

The experiment focused on HTTP response structure, status codes,
browser-generated requests, and basic server access logs.

## 2. Environment

| Component | Details |
|---|---|
| Server OS | Ubuntu Server |
| Client OS | Windows 11 |
| Programming language | Python 3.12.3 |
| Web framework | Flask |
| HTTP client | curl |
| Browser | Brave |
| Server address | `192.168.26.129` |
| Application port | `8000` |

The server and client communicated over the local virtual network.

## 3. Application Setup

A small Flask application was created to return an HTML page
when the root path (`/`) was requested.

The application was configured to listen on all IPv4 interfaces
on port `8000`.

The development server was started with:

    python app.py

The application was accessible at:

    http://192.168.26.129:8000/

## 4. Test 1: Requesting the Homepage with curl

### Procedure

The following command was executed from Windows Command Prompt:

    curl -i http://192.168.26.129:8000/

The `-i` option instructs curl to include the HTTP response
headers in its output.

### Observed Result

The server returned:

    HTTP/1.1 200 OK

The response included the following headers:

    Server: Werkzeug/3.1.9 Python/3.12.3
    Date: Wed, 14 Oct 2026 12:48:27 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 253
    Connection: close

The response body contained the HTML for the homepage.

### Analysis

The `200 OK` status indicated that the server successfully
handled the request.

The response headers provided metadata about the response:

- `Server` identified the server software reported by the
  application.
- `Date` indicated when the response was generated.
- `Content-Type` identified the body as HTML encoded using UTF-8.
- `Content-Length` specified the response body's length in bytes.
- `Connection: close` indicated that the connection would be
  closed after the response.

The response consisted of a status line, headers, a blank line,
and the HTML body.

## 5. Test 2: Accessing the Homepage with Brave

### Procedure

The homepage was opened in Brave using:

    http://192.168.26.129:8000/

The page displayed the HTML content returned by the application.

The Flask server logs showed a request for `/` with status `200`.

The logs also showed a request for `/favicon.ico` that returned
status `404`.

### Analysis

Browsers commonly request a favicon, a small icon associated
with a website, using the conventional path `/favicon.ico`.

The Flask application did not provide a favicon at that path.
Consequently, the request returned `404 Not Found`.

This did not indicate that the homepage or the Flask application
had failed.

The observation demonstrated that a browser can make additional
HTTP requests for resources associated with a webpage.

## 6. Test 3: Requesting a Missing Resource with curl

### Procedure

The following command was executed:

    curl -i http://192.168.26.129:8000/favicon.ico

### Observed Result

The server returned:

    HTTP/1.1 404 NOT FOUND

The requested favicon was not available at that path.

### Analysis

The `404 Not Found` status indicated that the requested resource
could not be found.

The result was consistent with the browser's favicon request.

The application remained operational despite the missing resource.

## 7. Key Findings

The experiment demonstrated the following:

1. HTTP responses contain a status line, headers, and a body,
   separated by a blank line.
2. The `200 OK` status indicates a successful request.
3. The `404 Not Found` status indicates that the requested
   resource could not be found.
4. Browsers can generate additional requests beyond the initial
   request for a webpage.
5. `curl` can be used to inspect HTTP response headers and bodies.
6. Flask access logs provide useful information about requested
   paths and response status codes.

## 8. Limitations

The `curl -i` command displayed response headers alongside
the response body, but did not provide a complete raw capture
of the network exchange.

The Flask access logs showed request information and status
codes, but did not display every HTTP header.

The experiment did not include packet capture or detailed
analysis of TCP traffic.

## 9. Conclusion

The experiment successfully demonstrated basic HTTP
communication between a Windows client and an Ubuntu Server.

It connected application-layer networking concepts with
observable behaviour, including response headers, status codes,
browser-generated requests, and server logs.

The next experiment will investigate HTTP cookies and how
browsers and servers exchange cookie information across requests.

## 10. References

- Kurose, J. F., and Ross, K. W.,
  *Computer Networking: A Top-Down Approach*.
- Flask documentation: https://flask.palletsprojects.com/
- curl documentation: https://curl.se/docs/
