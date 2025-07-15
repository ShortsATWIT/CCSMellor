Welcome to my Guitar Shop API!

I created a FastAPI-based web service that replicates SQL queries 
from Lab 4 using Python. It shows both GET and PUT routes can be used to 
interact with a MySQL database and return data in a clean JSON format via 
an API.

The main FastAPI app is built on top of the Lab5.py logic, which includes 
several Python functions that query the Guitar Shop database. The FastAPI 
routes map directly to those functions and allow external users or programs
to request data or send inputs via query strings or request bodies.

My favorite part of the project was seeing the API display live data directly 
from my local MySQL database. Combining FastAPI with MySQL and seeing it all 
work through Swagger UI was really satisfying.
