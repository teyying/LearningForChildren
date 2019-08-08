class ErrorInfo(object):
    def __init__(self):
        self.aErrorInfo()
    def aErrorInfo(func):
        def debug(*args, **kwargs):
            print(2)
            try:
                func(*args, **kwargs)
            except Exception as e:
                print("错误：", e)
        return debug

@ErrorInfo
def fn(a):
    print(a)
    k()

fn(3)