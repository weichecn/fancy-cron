#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import create_engine, Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config


mysql_url = \
    '%(scheme)s://%(user)s:%(passwd)s@%(host)s:%(port)d/%(db)s?charset=utf8'
engine = create_engine(mysql_url % config['db'],
                       echo_pool=True,
                       echo=config['debug'],
                       pool_size=config['db']['pool_size'],
                       pool_recycle=600)
Session = sessionmaker(bind=engine)


BaseModel = declarative_base()


class Cron(BaseModel):
    __tablename__ = 'cron'

    id = Column(Integer(), primary_key=True)
    cmd = Column(String(255), nullable=False, unique=True)
    total_count = Column(Integer(), nullable=False, default=0)
    success_count = Column(Integer(), nullable=False, default=0)
    fail_count = Column(Integer(), nullable=False, default=0)
    create_time = Column(
        DateTime(), nullable=False, default=datetime.datetime.now)
    update_time = Column(
        DateTime(), nullable=False, default=datetime.datetime.now, index=True)


class CronLog(BaseModel):
    __tablename__ = 'cron_log'

    id = Column(Integer(), primary_key=True)
    cron_id = Column(Integer(), nullable=False, index=True)
    exit_status = Column(Integer(), nullable=False)
    start_time = Column(DateTime(), nullable=False)
    end_time = Column(DateTime(), nullable=False)
    process_time = Column(Integer(), nullable=False)
    output = Column(Text(), nullable=False)
    create_time = Column(
        DateTime(), nullable=False, default=datetime.datetime.now)


def create_tables():
    BaseModel.metadata.create_all(engine)


def drop_tables():
    BaseModel.metadata.drop_all(engine)
