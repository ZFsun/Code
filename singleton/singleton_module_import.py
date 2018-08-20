from singleton_module import MySingleton

a = MySingleton
b = MySingleton
print(id(a))
print(id(b))
