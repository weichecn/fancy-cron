#!/usr/bin/python
# -*- coding: utf-8 -*-

from faker import Factory

from fancy_cron.app import app
from fancy_cron.model import create_tables


client = app.test_client()
fake = Factory.create('zh_CN')


def setup():
    create_tables()


def test_upload_log():
    data = dict(
        cmd=fake.sentence(),
        exit_status=fake.pyint(),
        start_time=fake.date_time().isoformat(),
        end_time=fake.date_time().isoformat(),
        process_time=fake.pyint(),
        output=fake.text()
    )
    assert client.post('/api/logs', data=data).status_code == 200
