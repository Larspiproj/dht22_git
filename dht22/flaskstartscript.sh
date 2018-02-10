#!/bin/bash

export FLASK_APP=dht22_routes.py
export FLASK_DEBUG=True

flask run --host=0.0.0.0
