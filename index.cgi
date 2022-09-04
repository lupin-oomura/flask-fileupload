#!/usr/local/bin/python3
from wsgiref.handlers import CGIHandler
from application import app
CGIHandler().run(app)
