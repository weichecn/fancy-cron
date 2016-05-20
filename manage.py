#!/usr/bin/python
# -*- coding: utf-8 -*-

import click


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    database.create_tables(tables, safe=True)


@cli.command()
def destroy():
    database.drop_tables(tables, safe=True)


@cli.command()
def migrate():
    database.drop_tables([Xiehouyu], safe=True)
    database.create_tables([Xiehouyu], safe=True)


@cli.command()
def dump():
    pass


if __name__ == '__main__':
    cli()
