from . import api
from flask import request, jsonify
from app.models import AccessLog, Channel
import re
from datetime import datetime


@api.route('/accesslog', methods=['GET'])
def get_access_log():
    start_date = request.args.get('start')
    end_date = request.args.get('end')

    token = request.args.get('token')

    channel = Channel.query.filter_by(token=token).first()

    if channel == None:
        return jsonify({
            'code': '101',
            'message': 'invalid token'
        })
    else:
        if start_date == None:
            return jsonify({
                'code': '102',
                'message': 'params error'
            })
        if start_date < '20171213':
            start_date = '20171213'
        if end_date == None or end_date == '':
            end_date = datetime.now().strftime('%Y%m%d')
        if r start_date) and re.match('\d{8}', end_date):
            print 'hello'e.match('\d{8}',
            accesslogs = AccessLog.query.filter(
                AccessLog.timestamp > start_date + '000000').filter(AccessLog.timestamp < end_date + '235959').all()
            return jsonify({
                'code': '0',
                'message': 'sucess',
                'data': [al.to_json() for al in accesslogs]
            })
