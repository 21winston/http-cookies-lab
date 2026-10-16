# Experiment 02: HTTP Cookies

## Objective

To demonstrate how an HTTP server sets a cookie, how a client stores it, and how the client returns it in a later request.

## Implementation

A Flask application with two routes:

- `GET /set-cookie` sets `visitor_id=abc123` using the `Set-Cookie` response header.
- `GET /read-cookie` reads `visitor_id` from the incoming request and returns its value, or reports that no visitor cookie was found.

The value `abc123` is hardcoded for this experiment.

## Procedure and Results

The Flask application ran on port 8000 in the Ubuntu Server VM. All requests were sent from Windows using curl.

### 1. Set and store the cookie

```bash
curl -i -c cookies.txt http://192.168.26.129:8000/set-cookie
```

The server returned `HTTP 200 OK` with a `Set-Cookie` header similar to:

```http
Set-Cookie: visitor_id=abc123; Path=/
```

The response body was:

```text
Cookie has been set.
```

The `-c cookies.txt` option told curl to save the received cookie to a cookie-jar file.

### 2. Send the stored cookie

```bash
curl -i -b cookies.txt http://192.168.26.129:8000/read-cookie
```

The application returned:

```text
Your visitor ID is: abc123
```

The `-b cookies.txt` option told curl to send the stored cookie with the request.

## Findings

The test confirmed the full cookie exchange:

1. The server sends the cookie in the `Set-Cookie` response header.
2. The client stores it.
3. The client returns it in a later request using the `Cookie` request header.
4. Flask reads the value through `request.cookies`.

This shows how cookies let an application carry information across separate HTTP requests, since HTTP itself is stateless.

## Limitations

- The cookie value is hardcoded, not generated dynamically.
- The test used plain HTTP, so traffic was unencrypted.
- The `Secure` and `HttpOnly` attributes were not set.
- Verification relied on curl output and Flask logs; no packet capture was done.
- The app ran on Flask's development server, which is not suitable for production.
