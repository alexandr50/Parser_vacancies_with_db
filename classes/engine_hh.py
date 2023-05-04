import requests as requests


class HeadHunter:
    URL = 'https://api.hh.ru/vacancies'

    def __init__(self, employer_id: str):
        self.employer_id = employer_id
        self.params = {'User-Agent': 'Mozilla/4.0', 'employer_id': self.employer_id, 'page': 0, 'per_pages': 100}

    def get_request(self):
        response = requests.get(self.URL, params=self.params)
        if response.status_code == 200:
            return response.json()

    @staticmethod
    def get_content(vacancy: dict):
        vacancy_id = int(vacancy.get('id'))
        title = vacancy.get('name')

        expierince = vacancy.get('experience').get('name')
        employment = vacancy.get('employment').get('name')
        requirements = vacancy.get('snippet').get('requirements')
        salary = vacancy.get('salary')
        url = vacancy.get('alternate_url')
        if salary:
            correct_salary = None
            if salary.get('from'):
                correct_salary += 'от' + salary.get('from')
            if salary.get('to'):
                correct_salary += ' до' + salary.get('to')
            correct_salary += ' ' + salary.get('currency')
        vacancy_for_save = (vacancy_id, title, expierince, employment, requirements, correct_salary, url)
        return vacancy_for_save

    def get_vacancies(self):
        all_vacancies = []
        cur_page = 0
        while True:
            self.params['page'] = cur_page
            result = self.get_request()
            for item in result.get('items'):
                all_vacancies.append(self.get_content(item))
            cur_page += 1

            if result.get('page') == cur_page:
                return


dct = {'alpha-bank': '80', 'sber': '3529', 'tinkoff': '78638', 'ozon': '2180', 'gazpom': '39305', 'Почта': '4352', 'Яндекс': '1740', 'Metro': '673', 'ВТБ': '4181', 'Северсталь': '6041'}

response = requests.get('https://api.hh.ru/vacancies/',
                        params={'User-Agent': 'Mozilla/4.0', 'employer_id': '2180', 'area': '113', 'per_page': 1,
                                'page': 1})
print(response.json())
for item in response.json()['items']:
    for i, j in item.items():
        print(i, j)
