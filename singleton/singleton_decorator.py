from functools import wraps


def singleton(cls):
    """"
    单例模式装饰器
    """
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass(object):
    pass


class_a = MyClass()
class_b = MyClass()
print("class_a,id:", id(class_a), "class_b,id:", id(class_b))
print(class_a is class_b)
