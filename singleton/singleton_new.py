class Signleton(object):
	"""
	单例模式类
	"""
    _instance = None
	
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            _instance = super(Signleton, cls).__new__(cls, *args, **kwargs)
        else:
            return cls._instance

			
class MyClass(Signleton):
	"""
	该类继承单例模式类
	"""
    pass

	
# class_a与class_b为同一对象
class_a = MyClass()
class_b = MyClass()
print("class_a,id:",id(class_a),"class_b,id:",id(class_b))
print(class_a is class_b)