# Webhooks

An example of how webhooks might be implemented as an integration point for a web application.


## Tech stack

* Python, Django
* PostgreSQL
* ElasticMQ (In-memory message queue with an Amazon SQS-compatible interface. Runs stand-alone or embedded.)


## Architecture

A main web app exists and new webhooks functionality is added by creating a microservice.

![Webhooks](images/webhooks.png)
