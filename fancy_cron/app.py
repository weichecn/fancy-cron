#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

from fancy_cron import api

app = Flask(__name__)

app.register_blueprint(api.api_bp, url_prefix='/api')
