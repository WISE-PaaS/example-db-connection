# example-db-connection
Examples of short code snippets to connect to various WISE-PaaS DB services.

The main program provides different HTTP request endpoints to test the connections with different WISE-PaaS DB services:

GET /testmongo

Attempts to make a connection to the MongoDB instance with the credentials from the supplied secret in the Kubernetes deployment configuration file. Upon successful connection, the request will return information on the database using the 'dbStats' MongoDB command.

GET /testinflux

Attempts to make a connection to the InfluxDB instance with the credentials from the supplied secret in the Kubernetes deployment configuration file. Upon successful connection, the request will return a list of authorized databases for the given credential.
