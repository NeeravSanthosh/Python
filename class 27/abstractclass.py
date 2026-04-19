from abc import ABC, abstractmethod
class absclass(ABC):
    def print(sekf,x):
        print("passed value: ", x)
    @abstractmethod
    def task(self):
        pass
class test_class(absclass):
    def task(self):
        print("we re inside test_class task")
test_obj = test_class()
test_obj.task()
test_obj.print(100)