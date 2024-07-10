import json
import os

import psycopg2


class TeamBase:
 
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv('POSTGRES_HOSTNAME'),
            port=os.getenv('POSTGRES_PORT'),
            user=os.getenv('POSTGRES_USERNAME'),
            password=os.getenv('POSTGRES_PASSWORD'),
            database=os.getenv('POSTGRES_DBNAME')
        )
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS teams (
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(64) NOT NULL UNIQUE,
                                description VARCHAR(256) NOT NULL,
                                creation_time TIMESTAMP NOT NULL DEFAULT NOW(),
                                admin VARCHAR(64) NOT NULL
                                )
                            ''')

    # create a team

    def create_team(self, request: str) -> str:
     
        try:
            result = ""
            json_request = json.loads(request)

            assert len(json_request['name']) <= 64
            assert len(json_request['description']) <= 128

            self.cursor.execute('''
                          INSERT INTO teams (name, description, admin) VALUES (%s, %s, %s) RETURNING id
                          ''',
                                (json_request['name'], json_request['description'], json_request['admin']))

            result = json.dumps({"id": self.cursor.fetchone()[0]})

            return result
        except Exception as e:
            print(e)

    # list all teams
    def list_teams(self) -> str:
      
        try:
            result = ""
            self.cursor.execute('''
                          SELECT * FROM teams
                          ''')

            result = json.dumps(self.cursor.fetchall())

            return result
        except Exception as e:
            print(e)

    # describe team
    def describe_team(self, request: str) -> str:
        
        try:
            result = ""
            json_request = json.loads(request)
            self.cursor.execute('''
                          SELECT * FROM teams WHERE id = %s
                          ''',
                                (json_request['id'],))

            result = json.dumps(self.cursor.fetchone())

            return result
        except Exception as e:
            print(e)

    # update team
    def update_team(self, request: str) -> str:
    
        try:
            result = ""
            json_request = json.loads(request)

            assert len(json_request['team']['name']) <= 64
            assert len(json_request['team']['description']) <= 128

            self.cursor.execute('''
                           UPDATE teams SET description = %s WHERE id = %s
                           ''',
                                (json_request['description'], json_request['id']))

            result = json.dumps({"id": self.cursor.fetchone()[0]})

            return result
        except Exception as e:
            print(e)

    # add users to team
    def add_users_to_team(self, request: str):
        
        try:
            result = ""
            json_request = json.loads(request)

            assert len(json_request['users']) <= 50

            self.cursor.execute('''
                           UPDATE teams SET users = %s WHERE id = %s
                           ''',
                                (json_request['users'], json_request['id']))

            result = json.dumps({"id": self.cursor.fetchone()[0]})

            return result
        except Exception as e:
            print(e)

    # add users to team
    def remove_users_from_team(self, request: str):
    
        try:
            result = ""
            json_request = json.loads(request)

            assert len(json_request['users']) <= 50

            self.cursor.execute('''
                           UPDATE teams SET users = %s WHERE id = %s
                           ''',
                                (json_request['users'], json_request['id']))

            result = json.dumps({"id": self.cursor.fetchone()[0]})

            return result
        except Exception as e:
            print(e)

    # list users of a team
    def list_team_users(self, request: str):
        
        try:
            result = ""
            json_request = json.loads(request)

            self.cursor.execute('''
                           SELECT * FROM users WHERE id = %s
                           ''',
                                (json_request['id'],))

            result = json.dumps(self.cursor.fetchone())

            return result
        except Exception as e:
            print(e)
