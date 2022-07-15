from datetime import datetime
import json

def decorator(path_to_logs):
    def _decorator(old_function):

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            args_list = []
            for i in args:
                args_list.append(i)
            for i in kwargs:
                args_list.append(i)

            to_json = {
                'name': old_function.__name__,
                'date and time': str(datetime.now()),
                'args': args_list,
                'result': result
            }

            with open(path_to_logs, 'w') as file_json:
                json.dump(to_json, file_json)

            return result

        return new_function

    return _decorator