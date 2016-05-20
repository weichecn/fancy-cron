#!/usr/bin/python
# -*- coding: utf-8 -*-

import contextlib

import click

from fancy_cron.app import app
from fancy_cron.model import BaseModel, engine


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    BaseModel.metadata.create_all(engine)


@cli.command()
def destroy():
    BaseModel.metadata.drop_all(engine)


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
