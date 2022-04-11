from requests import post

print(post('http://localhost:5000/api/jobs',
           json={"id": 2, 'team_leader': 2, 'job': "map floors",
    'work_size': 2, 'collaborators': "2", 'is_finished': False}).json()) #корректное добавление

print(post('http://localhost:5000/api/jobs').json()) #пустой запрос

print(post('http://localhost:5000/api/jobs',
           json={"id": 3, 'job': "map floors",
    'work_size': 2, 'collaborators': "2", 'is_finished': False}).json())  #нет team_leader

print(post('http://localhost:5000/api/jobs',
           json={"id": 2, 'team_leader': 2, 'job': "map floors",
    'work_size': 2, 'collaborators': "2", 'is_finished': False}).json()) #уже есть id