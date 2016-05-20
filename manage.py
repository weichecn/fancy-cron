#!/usr/bin/python
# -*- coding: utf-8 -*-

import contextlib

import click

from fancy_cron.app import app
from fancy_cron.model import create_tables, drop_tables


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    create_tables()


@cli.command()
def destroy():
    drop_tables()


@cli.command()
def migrate():
    pass


@cli.command()
def dump():
    pass


@cli.command()
def run():
    app.run(host='0.0.0.0', debug=True, port=5000)


if __name__ == '__main__':
    cli()
