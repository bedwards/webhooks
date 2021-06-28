# Webhooks

An example of how webhooks might be implemented as an integration point for a web application.

When I worked at Atlassian I headed up the effort to [revamp the webhooks offering](https://bitbucket.org/blog/the-new-bitbucket-webhooks). This is a very simple example of a webhooks subsystem based on that experience. This is not a full-feature webhooks implementation. This is a quick-and-dirty spin-up to include in my portfolio of example creations when I apply for jobs.


## Tech stack

* Python, Django, requests, boto3
* PostgreSQL
* ElasticMQ (In-memory message queue with an Amazon SQS-compatible interface. Runs stand-alone or embedded.)
* Docker, docker-compose


## Architecture

A main web app exists and new webhooks functionality is added by creating a microservice.

![Webhooks](images/webhooks.png)


## Example usage

Install AWS boto3 dependency for producer script which simulates an event occuring in the main web app.

    % pip3 install boto3

Start up the services.

    % docker-compose up -d db mq
    % docker-compose up web worker

Create a webhook definition using the API.

    % http POST localhost:8000/webhooks/ url=http://10.0.2.2:7777
    HTTP/1.1 200 OK
    Content-Length: 78
    Content-Type: application/json
    Date: Mon, 28 Jun 2021 17:49:47 GMT
    Referrer-Policy: same-origin
    Server: WSGIServer/0.2 CPython/3.9.5
    X-Content-Type-Options: nosniff
    X-Frame-Options: DENY

    [
        {
            "fields": {
                "url": "http://10.0.2.2:7777"
            },
            "model": "app.webhook",
            "pk": 7
        }
    ]

Add 10.0.2.2 as a loopback address on your Mac.

    % sudo ifconfig lo0 alias 10.0.2.2

Start the simple "third-pary" webhook consumer at the same URL used when defining the webhook configuration in the microservice. This consumer will just print out the payload of any webhooks it receives.

    % python3 consumer.py

Simulate an event occuring in the main web app by running the producer script.

    % python3 producer.py

Note the printed messages in the consumer terminal.

    {"event": "Hello webhooks world"}
