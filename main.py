from test import dec

path_to_logs = 'logs.json'

@dec(path_to_logs)

def test(a, b):
    return(a+b)

test(3, 8)