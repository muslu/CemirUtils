from cemirutils import CemirUtils

# Örnek kullanım
utils = CemirUtils(data=False, dbname='test_db3', dbuser='postgres', dbpassword='', dbport=5435, dbcreate_db_if_not_exists=True)
print(utils.psql_create_table('test_table_flat', 'id SERIAL PRIMARY KEY, name VARCHAR(100), surname VARCHAR(100)'))
print(utils.psql_insert('test_table', ('id', 'name', 'data'), (3, "emir", {"age": 40, "city": "İzmir"}), get_id=True))
print(utils.psql_insert('test_table_flat', ('id', 'name', 'surname'), (3, 'Muslu', 'Yüksektepe'), get_id=True))
print(utils.psql_read('test_table'))
print(utils.psql_read('test_table_flat'))
print(utils.psql_update('test_table', {'name': 'MusluY', 'data': '{"age": 40, "city": "Sivas"}'}, 'id = 2', get_id=True))
print(utils.psql_delete('test_table', 'id = 2'))
