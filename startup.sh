#!/bin/bash

DBFILE=./app.sqlite

if test -f "$DBFILE"; then
    echo "Database file exists. Starting API"
    python3 webapp.py
else
    echo "Database file does not exist.  Creating and starting API"
    python3 create_db.py
    python3 webapp.py
fi