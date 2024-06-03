from datetime import datetime

from cemirutils import CemirUtils

# Örnek kullanım
utils = CemirUtils(data=False, dbname='test_db3', dbuser='postgres', dbpassword='dD5Yz6xE5m', dbport=5435, dbcreate_db_if_not_exists=True)

# print(utils.psql_create_table('test_table_flat', 'id SERIAL PRIMARY KEY, name VARCHAR(100), surname VARCHAR(100)'))
# print(utils.psql_create_table('test_table_json', 'id SERIAL PRIMARY KEY, dates DATE, content JSONB'))

# print(utils.psql_insert('test_table_flat', ('id', 'name', 'surname'), (3, 'Muslu', 'Yüksektepe'), get_id=True))
print(utils.psql_insert('test_table_json', ('id', 'dates', 'content'), (2, datetime.now(), {"age": 40, "city": "İzmir"}), get_id=True))
print(utils.psql_read('test_table_json'))

print(utils.psql_update('test_table_json', {'dates': datetime.now(), 'content': '{"age": 40, "city": "Sivas"}'}, 'id = 1', get_id=True))
print(utils.psql_read('test_table_json'))

print(utils.psql_delete('test_table_json', 'id = 1'))
print(utils.psql_read('test_table_json'))