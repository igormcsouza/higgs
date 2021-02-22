from datetime import datetime

from flask import abort
from flask_restful import Resource, reqparse
from bson.objectid import ObjectId

from backend.services.database import DatabaseWrapper


db = DatabaseWrapper('main')

class TransactionOneResouce(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'type', type=str, help='Transaction Type', required=True)

    def get(self, _id):
        try:
            transaction = db.search({'_id': ObjectId(_id)})
        except Exception as e:
            abort(500, f'Internal Error: {e}')

        return { 'msg': 'done', 'transaction': transaction }, 200

    def put(self, _id):
        args = self.parser.parse_args()

        try:
            db.update({ '_id': ObjectId(_id) }, args)
        except Exception as e:
            abort(500, f'Internal Error: {e}')

        return { 'msg': 'done' }, 200

    def delete(self, _id):
        try:
            db.delete({ '_id': ObjectId(_id) })
        except Exception as e:
            abort(500, f'Internal Error: {e}')

        return { 'msg': 'done' }, 200