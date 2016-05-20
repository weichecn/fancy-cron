#!/usr/bin/python
# -*- coding: utf-8 -*-

import contextlib
import datetime

from flask import Blueprint, jsonify, request

from fancy_cron.model import Cron, CronLog, Session


api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/')
def index():
    return jsonify(dict())


@api_bp.route('/crons')
def crons():
    return jsonify(dict())


@api_bp.route('/crons/<int:cron_id>')
def cron(cron_id):
    return jsonify(dict())


@api_bp.route('/crons/<int:cron_id>/logs')
def cron_logs(cron_id):
    return jsonify(dict())


@api_bp.route('/logs')
def logs():
    return jsonify(dict())


@api_bp.route('/logs', methods=['POST'])
def upload_log():
    cmd = request.form['cmd']
    exit_status = int(request.form['exit_status'])
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    process_time = int(request.form['process_time'])
    output = request.form['output']

    with contextlib.closing(Session()) as s:
        cron = s.query(Cron).filter(Cron.cmd == cmd).first()
        if not cron:
            cron = Cron()
            cron.cmd = cmd
            cron.total_count = 0
            cron.success_count = 0
            cron.fail_count = 0
            cron.create_time = datetime.datetime.now()
            cron.update_time = datetime.datetime.now()
            s.add(cron)
            s.commit()
        cron_log = CronLog()
        cron_log.cron_id = cron.id
        cron_log.exit_status = exit_status
        cron_log.start_time = start_time
        cron_log.end_time = end_time
        cron_log.process_time = process_time
        cron_log.output = output
        cron_log.create_time = datetime.datetime.now()
        s.add(cron_log)
        s.commit()
        cron.total_count = Cron.total_count + 1
        if exit_status == 0:
            cron.success_count = Cron.total_count + 1
        else:
            cron.fail_count = Cron.fail_count + 1
        s.commit()

    return jsonify(dict())
