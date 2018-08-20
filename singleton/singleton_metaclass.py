class Singleton(type):
    """
    单例模式元类
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# python2
# class MyClass(object):
#     __metaclass__ = Singleton
#     pass


# python3
class MyClass(metaclass=Singleton):
    pass


class_a = MyClass()
class_b = MyClass()
print("class_a,id:", id(class_a), "class_b,id:", id(class_b))
print(class_a is class_b)
