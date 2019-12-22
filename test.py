from datetime import datetime
#
#
import sys

def process(a, cls):
    print(a, cls)
    return cls.clean(a)

class XLType():
    def __init__(self, cls):
        self.cls = cls

    def clean(self, v):
        return getattr(sys.modules[__name__], self.cls)().clean(v)
#
class XLString():
    @staticmethod
    def clean(v):
        return v.strip()
#
class XLDate():
    @staticmethod
    def clean(v):
        return v.date().isoformat()

l = [{'value': 'a  ','cls': 'XLString'}, {'value':' b','cls': 'XLString'}, {'value': datetime.today(),'cls': 'XLDate'}]

for i in l:
    print(XLType(i.get('cls')).clean(i.get('value')))


# import traceback
#
#
# class CarTypes:
#     class Toyota:
#         def __repr__(self):
#             return "Toyota()"
#         def __str__(self):
#             return "Instance of Toyota() class"
#     class Nissan:
#         def __repr__(self):
#             return "Nissan()"
#         def __str__(self):
#             return "Instance of Nissan() class"
#
#
# class Car:
#     def __init__(self):
#         self._all_classes = {}
#
#     def construct(self, builder_name):
#         setattr(self, builder_name, CarTypes())
#         try:
#             target_class = getattr(CarTypes, builder_name)
#             instance = target_class()
#             self._all_classes[builder_name] = instance
#         except AttributeError:
#             print("Builder {} not defined.".format(builder_name))
#             traceback.print_stack()
#
#     def __getitem__(self, type_name):
#         return self._all_classes[type_name]
#
#     def car_type(self, type_name):
#         return self._all_classes[type_name]
#
#
# IDS = ["Toyota", "Nissan", "Unknown"]
#
# director = Car()
# for id in IDS:
#     director.construct(id)
#
# print(director["Toyota"])
# print(director["Nissan"])
# print(director.car_type("Toyota"))
# print(director.car_type("Nissan"))

