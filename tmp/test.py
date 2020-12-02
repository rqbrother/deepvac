

def attr():
    class test(object):
        def __init__(self, age, grade):
            self.age = age
            self.grade = grade
            self.init(120)

        def init(self, num):
            self.num = num

    student = test(10, 90)
    # student.init(120)
    print(student.__dict__)

def xiushi():
    def log(func):
        def wrapper():
            print('log开始 ...')
            func()
            print('log结束 ...')

        return wrapper

    @log
    def test():
        print('test ..')

    test()

def xiushi2():
    from functools import wraps

    def log(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            print('log开始 ...', func.__name__)
            print(args)
            ret = func(*args, **kwargs)
            print('log结束 ...')
            return ret

        return wrapper

    @log
    def test1(s):
        print('test1 ..', s)
        return s

    @log
    def test2(s1, s2):
        print('test2 ..', s1, s2)
        return s1 + s2

    test1('a')
    test2('a', 'bc')

def test1():
    def function(arg, *args, **kwargs):
        print(arg, args, kwargs)

    function(6, 7, 8, 9, a=1, b=2, c=3)

def test2():
    class A(dict):
        def __init__(self):
            self.name = "bob"
            self.age = 100

    a = A()
    a.grade = 123
    print(a.__dict__)

def log():
    import logging, os
    if not os.path.exists('log'):
        os.makedirs('log')


    logging.debug("this is debug ...")
    logging.info('this is info ...')
    logging.error('this is error ...')
    logging.warning('this is warning ...')
    logging.critical("this is critical ...")

if __name__ == "__main__":
    # xiushi()
    # test1()
    # xiushi2()
    # test2()
    log()