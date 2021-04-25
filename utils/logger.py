from datetime import datetime

def getNow():
    return str(datetime.now())[0:19]

class Logger:
    def debug(str):
        print("[{}] {}".format(getNow(), str))