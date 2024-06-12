from cemirutils.utils import CemirUtils

cemir_utils = CemirUtils()

utils = CemirUtils(data=False, dbname='test_db3', dbuser='postgres', dbpassword='', dbport=5437, dbcreate_db_if_not_exists=False)

# print(utils.psql_insert('test_table_json', ('id', 'dates', 'content'), (2, datetime.now(), {"age": 41, "city": "İzmir"}), get_id=True))

# print(utils.psql_read('test_table_json'))

asd = utils.psql_read(table_name='test_table_json', columns="content", condition="content ->> 'age' = '40'")
# asd = utils.psql_read(table_name='test_table_json', columns="content", condition="content ->> 'age' like '%4%'")
print(type(asd), asd)

# asdd = Dict2Dot(asd[0])
# print(type(asd), asdd.id)
