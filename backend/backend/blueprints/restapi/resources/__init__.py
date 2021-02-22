from .transactions import TransactionsResource
from .transaction_one import TransactionOneResouce

def init_api(api):
    api.add_resource(TransactionsResource, "/transaction")
    api.add_resource(TransactionOneResouce, "/transaction/<string:_id>")