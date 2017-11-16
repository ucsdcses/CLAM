# CLAM
Computer Lab Activity Monitor for UCSD

## Features and Architecture
- A script in Python which ssh's into each of the lab machines and checks
  whether someone is logged in. Writes this data to the database using PyMongo.
- A database using MongoDB which stores info on who is logged in to which
  computer and lab statistics.
- Web API which handles getting data about who is logged in from the database
- Front-end which renders the map of lab computers and statistics on usage.
