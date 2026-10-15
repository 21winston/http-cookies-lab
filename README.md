# HTTP and Cookies Lab

A practical networking lab exploring HTTP communication, browser
behaviour, and cookie-based state management using Ubuntu Server,
Python, Flask, and a Windows client.

The goal of this project is to connect application-layer networking
concepts with observable behaviour in a working environment.

Rather than relying entirely on theory, each experiment investigates
a specific concept, records the results, and explains the underlying
behaviour.

## Objectives

- Understand the structure of HTTP requests and responses.
- Inspect HTTP status codes and response headers.
- Observe how browsers generate additional HTTP requests.
- Investigate how HTTP cookies are created, stored, and transmitted.
- Explore how web applications maintain state across requests.
- Examine cookie attributes and their effects on browser behaviour.
- Develop practical troubleshooting and documentation skills.

## Lab Environment

| Component | Details |
|---|---|
| Server OS | Ubuntu Server |
| Client OS | Windows 11 |
| Programming language | Python 3 |
| Web framework | Flask |
| Command-line HTTP client | curl |
| Web browser | Brave |
| Virtualisation | VMware Workstation |

The Flask application runs on the Ubuntu Server VM and is accessed
from the Windows client over the local virtual network.

## Experiments

### Experiment 1: HTTP Requests and Responses

**Status: Completed**

Investigated HTTP communication between a Windows client and an
Ubuntu Server running a small Flask application.

Topics covered:

- HTTP response status lines.
- Response headers and message bodies.
- The `200 OK` and `404 Not Found` status codes.
- Differences between requests made by `curl` and a web browser.
- Browser-generated requests for a favicon.
- Basic Flask access logs.

Documentation: [Experiment 1 - HTTP Basics](docs/experiment-01-http-basics.md)

### Experiment 2: HTTP Cookies

**Status: Planned**

Investigate how a server instructs a browser to store cookies and
how the browser returns them in subsequent requests.

Planned topics:

- The `Set-Cookie` and `Cookie` headers.
- Cookie creation and transmission.
- Browser cookie storage.
- Cookie attributes and their effects.
- Client-side values versus server-side application state.

Further experiments will be documented as they are completed.

## Repository Structure

    http-cookies-lab/
    ├── README.md
    ├── app.py
    └── docs/
        └── experiment-01-http-basics.md

Additional application code and experiment documentation will be
added as the project develops.

## Running the Lab

The application requires Python 3 and Flask.

### 1. Clone the repository

    git clone https://github.com/21winston/http-cookies-lab
    cd http-cookies-lab

### 2. Create a virtual environment

    python3 -m venv .venv
    source .venv/bin/activate

### 3. Install Flask

    python -m pip install Flask

### 4. Start the application

    python app.py

The application listens on port `8000`.

Open the following address on the server:

    http://127.0.0.1:8000/

To access it from another machine on the same reachable network,
use the server's IP address:

    http://<server-ip>:8000/

Replace `<server-ip>` with the appropriate address for your
environment.

**Note:** The application uses Flask's development server for
learning purposes. It is not intended for production deployment.

## Learning Approach

Each experiment follows a practical workflow:

1. Define the concept being investigated.
2. Perform a controlled test.
3. Observe the application's behaviour.
4. Interpret the results using networking concepts.
5. Document the procedure, evidence, and conclusions.

## Scope

This is a learning lab focused on HTTP, application behaviour,
networking fundamentals, and basic systems administration.

It is not a production web application or a comprehensive
implementation of authentication or session management.

## Progress

- [x] Create the Flask application.
- [x] Access the application from a Windows client.
- [x] Inspect HTTP response headers and status codes.
- [x] Observe a browser-generated favicon request.
- [ ] Investigate HTTP cookie creation and transmission.
- [ ] Explore cookie attributes.
- [ ] Document the completed experiments.

## Disclaimer

This project is intended for educational purposes and local
experimentation.
