import json
import subprocess


class CemirUtils:
    def __init__(self, dbname, user, password, host='localhost', port=5432, create_db_if_not_exists=False):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        if create_db_if_not_exists:
            self.create_database(dbname)

    def parse_psql_output(self, output):
        """
        psql komutunun çıktısını parse ederek dict yapısına çevirir.

        Args:
            output (str): psql komutunun çıktısı.

        Returns:
            dict: Dict formatında çıktı.
        """
        lines = output.strip().split('\n')
        headers = lines[0].split('|')
        data = []

        for line in lines[2:-1]:  # İlk iki satır ve son satır başlık ve ayırıcılar olduğu için atlanır
            values = line.split('|')
            data.append({header.strip(): value.strip() for header, value in zip(headers, values)})

        return data

    def execute_query(self, query, dbname=None):
        """
        Veritabanına SQL sorgusu gönderir ve sonucu döndürür.

        Args:
            query (str): SQL sorgusu.
            dbname (str, optional): Veritabanı adı. Eğer verilmezse, self.dbname kullanılır.

        Returns:
            str: Sorgu sonucu veya JSON formatında hata bilgisi.
        """
        if dbname is None:
            dbname = self.dbname

        command = f'PGPASSWORD={self.password} psql -h {self.host} -p {self.port} -U {self.user} -d {dbname} -c {json.dumps(query, ensure_ascii=False)}'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            error_info = {
                "error": "Query failed",
                "message": result.stderr.strip()
            }
            return json.dumps(error_info, ensure_ascii=False)
        return result.stdout.strip()

    def insert(self, table_name, columns, values, get_id=False):
        """
        Veritabanına yeni kayıt ekler.

        Args:
            table_name (str): Tablo adı.
            columns (tuple): Kolon adları (örnek: ("id", "name", "data")).
            values (tuple): Kolon değerleri (örnek: (1, "John Doe", {"age": 30, "city": "Istanbul"})).

        Returns:
            str: Sorgu sonucu veya JSON formatında hata bilgisi.
        """
        columns_str = ', '.join(columns)

        formatted_values = []
        for value in values:
            if isinstance(value, dict):
                formatted_values.append(f"'{json.dumps(value)}'::jsonb")
            else:
                formatted_values.append(f"'{value}'")

        values_str = ', '.join(formatted_values)
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
        if get_id:
            query += f" RETURNING id;"
            try:
                result = self.execute_query(query).split()[2]
                return {"error": False, "id": int(result)}
            except ValueError:
                return self.execute_query(query)

        return self.execute_query(query)

    def create_database(self, dbname):
        """
        Belirtilen ad ile yeni bir veritabanı oluşturur.

        Args:
            dbname (str): Oluşturulacak veritabanının adı.

        Returns:
            str: Sorgu sonucu veya JSON formatında hata bilgisi.
        """
        query = f"CREATE DATABASE {dbname};"
        return self.execute_query(query, dbname='postgres')

    def create_table(self, table_name, schema):
        """
        Veritabanında tablo oluşturur.

        Args:
            table_name (str): Tablo adı.
            schema (str): Tablo şeması (örnek: "id SERIAL PRIMARY KEY, name VARCHAR(100), data JSONB").

        Returns:
            str: Sorgu sonucu veya JSON formatında hata bilgisi.
        """
        query = f"CREATE TABLE {table_name} ({schema});"
        return self.execute_query(query)

    def read(self, table_name, columns='*', condition=None, jsonb_field=None, jsonb_key=None):
        """
        Veritabanından kayıt okur.

        Args:
            table_name (str): Tablo adı.
            columns (str or tuple): Kolon adları veya * (örnek: "*" veya ("id", "name")).
            condition (str): Koşul (örnek: "id = 1").
            jsonb_field (str, optional): JSONB alan adı.
            jsonb_key (str, optional): JSONB alanındaki anahtar adı.

        Returns:
            str: Sorgu sonucu veya JSON formatında hata bilgisi.
        """
        if isinstance(columns, tuple):
            columns = ', '.join(columns)

        query = f"SELECT {columns} FROM {table_name}"
        if jsonb_field and jsonb_key:
            query = f"SELECT {columns}, {jsonb_field} ->> '{jsonb_key}' AS {jsonb_key} FROM {table_name}"

        if condition:
            query += f" WHERE {condition}"
        query += ";"

        return self.parse_psql_output(self.execute_query(query))

    def update(self, table_name, updates, condition, get_id=False):
        """
        Veritabanındaki kaydı günceller.

        Args:
            table_name (str): Tablo adı.
            updates (dict): Güncellemeler (örnek: {"name": "Jane Doe"}).
            condition (str): Koşul (örnek: "id = 1").

        Returns:
            str: Sorgu sonucu veya JSON formatında hata bilgisi.
        """
        update_str = ', '.join(f"{k} = '{json.dumps(v)}'" if isinstance(v, dict) else f"{k} = '{v}'" for k, v in updates.items())
        query = f"UPDATE {table_name} SET {update_str} WHERE {condition}"
        if get_id:
            query += f" RETURNING id;"
            try:
                result = self.execute_query(query).split()[2]
                return {"error": False, "id": int(result)}
            except ValueError:
                return self.execute_query(query)

        return self.execute_query(query)

    def delete(self, table_name, condition):
        """
        Veritabanındaki kaydı siler.

        Args:
            table_name (str): Tablo adı.
            condition (str): Koşul (örnek: "id = 1").

        Returns:
            str: Sorgu sonucu veya JSON formatında hata bilgisi.
        """
        query = f"DELETE FROM {table_name} WHERE {condition};"
        try:
            result = int(self.execute_query(query).split()[1])
            if result >= 0:
                return {"error": False}
        except:
            return self.execute_query(query)


# Örnek kullanım
utils = CemirUtils(dbname='test_db3', user='postgres', password='', port=5435, create_db_if_not_exists=True)
# print(utils.create_table('test_table_flat', 'id SERIAL PRIMARY KEY, name VARCHAR(100), surname VARCHAR(100)'))
# print(utils.insert('test_table', ('id', 'name', 'data'), (3, "emir", {"age": 40, "city": "İzmir"}), get_id=True))
# print(utils.insert('test_table_flat', ('id', 'name', 'surname'), (3, 'Muslu', 'Yüksektepe'), get_id=True))
# print(utils.read('test_table'))
# print(utils.read('test_table_flat'))
# print(utils.update('test_table', {'name': 'MusluY', 'data': '{"age": 40, "city": "Sivas"}'}, 'id = 2', get_id=True))
# print(utils.delete('test_table', 'id = 2'))
