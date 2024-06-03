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
# utils = CemirUtils()
# for k in utils.getmethods():
#     print(k)

data = [{'a': 1}, {'b': 2}, {'a': 3}, {"name": "sivas", "age": 10}]
cemd = CemirUtils(data)

print(cemd.dict_get_keys())
print(cemd.dict_filter_by_key('name'))
print(cemd.dict_merge({'a': 1}, {'b': 2}))