import psycopg2


class DBWorker():
    def __init__(self):
        self.connection = psycopg2.connect(user = 'postgres', password="gamepro100", host='localhost', port='5432', database='tg_bot')
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.create_tables()
        print('Connect - succes')
    
    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lc_project (id SERIAL PRIMARY KEY, title VARCHAR(50))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lc_city (id SERIAL PRIMARY KEY, title VARCHAR(100))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lc_vacancy_title (id SERIAL PRIMARY KEY, title VARCHAR(100))")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS lc_city_projects (id SERIAL PRIMARY KEY, city_id INTEGER REFERENCES lc_city (id) ,project_id INTEGER REFERENCES lc_project (id))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS lc_vacancy_title_projects (id SERIAL PRIMARY KEY, vacancy_title_id INTEGER REFERENCES lc_vacancy_title (id) ,project_id INTEGER REFERENCES lc_project (id))")
        
db = DBWorker()