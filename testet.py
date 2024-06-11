from cemirutils.utils import CemirUtils

utils = CemirUtils(data=False, dbname='test_db3', dbuser='postgres', dbpassword='asd', dbport=5435, dbcreate_db_if_not_exists=False)

asd = utils.listen_for_icmp(print_query=True, insert_db=True)
print(asd)


