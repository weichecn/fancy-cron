#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class Cron(BaseModel):
    __tablename__ = 'cron'

    id = Column(Integer(), primary_key=True)
    cmd = Column(String(1024), nullable=False, unique=True)
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
    process_time = Column(DateTime(), nullable=False)
    output = Column(Text())
    create_time = Column(
        DateTime(), nullable=False, default=datetime.datetime.now)
