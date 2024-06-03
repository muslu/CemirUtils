# from cemirutils.utils import Dict2Dot
#
# data = {"name": "muslu", "age": 30, "cities": {"name": "sivas", "age": 10}, "listem": [1, 2, 3, 4, 5]}
# dic = Dict2Dot(data)
# print(dic.name)  # muslu
# print(type(dic.cities), dic.cities)  # 10
# print(dic.cities.age)  # 10
# print(type(dic.listem), dic.listem)  # [1, 2, 3, 4, 5]
#

from cemirutils.utils import CemirUtils
utils = CemirUtils()
for k in utils.getmethods():
    print(k)

# utils =CemirUtils()
print(utils.time_add_days_to_date("2024-05-10", 100))
print(utils.time_todatetime("2024-05-10"))