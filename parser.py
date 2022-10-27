import requests
import csv

print('Выгрузка списка релизов из репозитория на GitHub')

owner = input('Введите логин владельца: ')
repo = input('Введите название репозитория: ')
token = input('Введите ваш токен GitAPI: ')

url = 'https://api.github.com/repos/%s/%s/releases?per_page=100' % (owner, repo)
aut = 'Bearer %s' % token

params = dict(Accept='application/vnd.github+json', Authorization=aut)

response = requests.request('GET', url, headers=params)
data = response.json()

header_csv = [
    'Номер релиза',
    'Дата',
    'Название',
    'Описание'
]

file_name = '%s-%s-releases.csv' % (owner, repo)
result_file = open(file_name, 'w', encoding='UTF=8')

writer = csv.writer(result_file)
writer.writerow(header_csv)

for i in range(len(data)):
    row = [data[i]["tag_name"], data[i]["published_at"], data[i]["name"], data[i]["body"]]
    writer.writerow(row)

result_file.close()

print('Конец')
