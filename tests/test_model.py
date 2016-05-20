#!/usr/bin/python
# -*- coding: utf-8 -*-

from fancy_cron.model import create_tables, drop_tables


def test_create_tables():
    create_tables()


def test_drop_tables():
    drop_tables()
