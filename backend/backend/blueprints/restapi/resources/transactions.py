from datetime import datetime

from flask import abort
from flask_restful import Resource, reqparse
from bson.objectid import ObjectId

from backend.services.database import DatabaseWrapper


db = DatabaseWrapper('igorm')

class TransactionsResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'type', type=str, help='Transaction Type', required=True)

    def get(self):
        try:
            transaction = db.search({})
        except Exception as e:
            abort(500, f'Internal Error: {e}')

        return { 'msg': 'done', 'transaction': transaction }, 200

    def post(self):
        args = self.parser.parse_args()

        try:
            _id = db.insert(args)
        except Exception as e:
            abort(500, f'Internal Error: {e}')

        return { 'msg': 'done', '_id': _id }, 200
