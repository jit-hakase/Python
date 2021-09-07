import json
from datetime import date, datetime

class JsonDumper(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H-%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, bytes):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class JS:
    @staticmethod
    def load(arr):
        return json.loads(arr)

    @staticmethod
    def dump(arr):
        return json.dumps(arr, cls=JsonDumper)
