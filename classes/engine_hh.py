

import requests as requests



class HeadHunter:
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self, employer_id: str):
        self.employer_id = employer_id
        self.params = {'User-Agent': 'Mozilla/4.0', 'employer_id': self.employer_id, 'page': 0, 'per_pages': 100}

    def get_request(self):
        response = requests.get(self.URL, params=self.params)
        if response.status_code == 200:
            return response.json().get('items')

    @staticmethod
    def get_content(vacancy: dict):
        vacancy_id = int(vacancy.get('id'))
        title = vacancy.get('name')
        company_name = vacancy.get('employer').get('name')
        expierince = vacancy.get('experience').get('name')
        employment = vacancy.get('employment').get('name')
        requirements = vacancy.get('snippet').get('requirements')
        salary = vacancy.get('salary')
        url = vacancy.get('alternate_url')
        if salary:
            pass


    def get_vacancies(self):
        all_vacancies = []
        cur_page = 0
        while True:
            self.params['page'] = cur_page
            result = self.get_request()
            for item in result:
                all_vacancies.append(self.get_content(item))
            cur_page += 1




dct = {'alpha-bank': '80', 'sber': '', 'tinkoff': '78638'}


response = requests.get('https://api.hh.ru/vacancies/', params={'User-Agent': 'Mozilla/4.0', 'employer_id': '78638', 'area': '113', 'per_page': 1, 'page': 0})
print(response.status_code)
for item in response.json()['items']:
    for i, j in item.items():
        print(i, j)