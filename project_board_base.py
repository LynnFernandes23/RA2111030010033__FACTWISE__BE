import os
import json
import psycopg2

class ProjectBoardBase:
    

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
                            CREATE TABLE IF NOT EXISTS project_boards (
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(64) NOT NULL,
                                description VARCHAR(128) NOT NULL,
                                team_id INTEGER NOT NULL,
                                creation_time TIMESTAMP NOT NULL
                                )
                                ''')

    # create a board

    def create_board(self, request: str):
        
        try:
            result = ""
            json_request = json.loads(request)

            assert len(json_request['name']) <= 64
            assert len(json_request['description']) <= 128

            self.cursor.execute('''
                            INSERT INTO project_boards (name, description, team_id, creation_time) VALUES (%s, %s, %s, %s) RETURNING id
                            ''',
                                (json_request['name'], json_request['description'], json_request['team_id'],
                                 json_request['creation_time']))

            result = json.dumps({"id": self.cursor.fetchone()[0]})

            return result

        except Exception as e:
            print(e)

    # close a board
    def close_board(self, request: str) -> str:
     
        try:
            result = ""
            json_request = json.loads(request)

            self.cursor.execute('''
                           UPDATE project_boards SET status = %s WHERE id = %s
                           ''',
                                (json_request['status'], json_request['id']))

            result = json.dumps({"id": self.cursor.fetchone()[0]})

            return result
        except Exception as e:
            print(e)

    # add task to board

    def add_task(self, request: str) -> str:
        
        try:
            result = ""
            json_request = json.loads(request)

            assert len(json_request['title']) <= 64
            assert len(json_request['description']) <= 128

            self.cursor.execute('''
                            INSERT INTO tasks (title, description, user_id, creation_time) VALUES (%s, %s, %s, %s) RETURNING id
                            ''',
                                (json_request['title'], json_request['description'], json_request['user_id'],
                                 json_request['creation_time']))

            result = json.dumps({"id": self.cursor.fetchone()[0]})

            return result
        except Exception as e:
            print(e)

    # update the status of a task
    def update_task_status(self, request: str):
        """
        :param request: A json string with the user details
        {
            "id" : "<task_id>",
            "status" : "OPEN | IN_PROGRESS | COMPLETE"
        }
        """
        pass

    # list all open boards for a team
    def list_boards(self, request: str) -> str:
        """
        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<board_id>",
            "name" : "<board_name>"
          }
        ]
        """
        try:
            result = ""
            json_request = json.loads(request)

            self.cursor.execute('''
                           SELECT * FROM project_boards WHERE id = %s
                           ''',
                                (json_request['id'],))

            result = json.dumps(self.cursor.fetchone())

            return result
        except Exception as e:
            print(e)

    def export_board(self, request: str) -> str:
       
        try:
            result = ""
            json_request = json.loads(request)

            self.cursor.execute('''
                           SELECT * FROM project_boards WHERE id = %s
                           ''',
                                (json_request['id'],))

            result = json.dumps(self.cursor.fetchone())

            out_file = open("out.txt", "w")
            out_file.write(result)

        except Exception as e:
            print(e)
