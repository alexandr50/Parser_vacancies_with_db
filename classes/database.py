import psycopg2

from utils.config import config


class DBManager:

    def __init__(self, name_bd: str, params: dict):
        self.name_db = name_bd
        self.params = params


    def create_database(self):
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(f"""DROP DATABASE IF EXISTS {self.name_db}""")
            cur.execute(f"""CREATE DATABASE {self.name_db}""")

        with psycopg2.connect(dbname=self.name_db, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""CREATE TABLE IF NOT EXISTS employers (
                    employer_id INT PRIMARY KEY,
                    company_name VARCHAR(50) UNIQUE NOT NULL);
                """)

                cur.execute(f"""CREATE TABLE IF NOT EXISTS vacancies (
                    vacancy_id INT PRIMARY KEY,
                    title VARCHAR(255),
                    expierence VARCHAR(255),
                    employment VARCHAR(255),
                    requirements VARCHAR(255),
                    salary VARCHAR(30),
                    url VARCHAR(30),
                    emploier_id INT REFERENCES employers(employer_id) NOT NULL);
                """)


    def insert(self, table: str, data: list):
        with psycopg2.connect(dbname=self.name_db, **self.params) as conn:
            with conn.cursor() as cur:
                if table == 'employers':
                    cur.execute(f"""INSERT INTO employers (employer_id, company_name)
                                VALUES (%s, %s)""", data)
                elif table == 'vacancies':
                    cur.execute(f"""INSERT INTO vacancies (vacancy_id, title, expierence, employment, requirements, salary, url)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)""", data)


# params = config()
# db = DBManager('vacancies_db', params)
# db.create_database()