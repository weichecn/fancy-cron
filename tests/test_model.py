#!/usr/bin/python
# -*- coding: utf-8 -*-

from fancy_cron.model import BaseModel, engine


def setup():
    BaseModel.metadata.create_all(engine)
