from requests import get

print(get('http://localhost:5000/api/jobs').json())  # Получение всех работ

print(get('http://localhost:5000/api/jobs/1').json()) #Корректное получение одной работы

print(get('http://localhost:5000/api/jobs/10').json()) #неверный id
print(get('http://localhost:5000/api/jobs/два').json()) #строка
