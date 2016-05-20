#!/usr/bin/python
# -*- coding: utf-8 -*-

from click.testing import CliRunner

import manage

runner = CliRunner()


def test_initdb():
    runner.invoke(manage.initdb)


def test_destroy():
    runner.invoke(manage.destroy)
