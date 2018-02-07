#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)


import inspect

def debug(func):
    def wrapper(*args,**kwargs):
        print ("类：%s;方法%s()"%(func.__class__,func.__name__))
        return func(*args,**kwargs)
    return wrapper


class aa():
    @debug
    def say_hello(self):
        print ("hello!")

a = aa()
a.say_hello()




import inspect
def get_current_function_name():
    return inspect.stack()[1][3]
class MyClass:
    def function_one(self):
        print ("%s.%s ******"%(self.__class__.__name__, get_current_function_name()))
if __name__ == "__main__":
    myclass = MyClass()
    myclass.function_one()