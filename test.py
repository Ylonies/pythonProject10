from requests import get, post

# print(get('http://localhost:5000/api/jobs').json())  # Получение всех работ
#
# print(get('http://localhost:5000/api/jobs/1').json()) #Корректное получение одной работы
#
# print(get('http://localhost:5000/api/jobs/10').json()) #неверный id
# print(get('http://localhost:5000/api/jobs/два').json()) #строка

#
# print(post('http://localhost:5000/api/jobs').json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1, 'job': "deployment of residential modules 1 and 2",
    'work_size': 10, 'collaborators': "2", 'is_finished': False}).json())