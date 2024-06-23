import requests


class GectaroApiClient:
    def __init__(self, base_url, auth_token):
        self.session = requests.Session()
        self.session.headers = {"Authorization": auth_token}
        self.session.verify = False
        self.base_url = base_url
        self.user_demo_project_id = self._get_demo_project_id()
        self.user_company_id = self.get_companies().json()[0]['id']

    def get_current_user(self):
        """Авторизация - Получить текущего пользователя"""
        return self.session.get(f"{self.base_url}/users/current")

    def get_companies(self):
        """Компании - Получить список компаний"""
        return self.session.get(f"{self.base_url}/companies")

    def get_company_projects_list(self, company_id: int):
        """Проекты - Получить список проектов"""
        return self.session.get(f"{self.base_url}/companies/{company_id}/projects")

    def get_project_resource_requests_by_project_id(self, project_id: int):
        """Снабжение: Заявки - Получить список заявок (По ИД проект)"""
        return self.session.get(f"{self.base_url}/projects/{project_id}/resource-requests")

    def get_resource_request_by_resource_request_id(self, project_id: int, resource_request_id: int):
        """Снабжение: Заявки - Получить данные заявки (По ИД заявки)"""
        return self.session.get(f"{self.base_url}/projects/{project_id}/resource-requests/{resource_request_id}")

    def _get_demo_project_id(self):
        """Функция для получения ИД проекта пользователя"""
        company_id = self.get_companies().json()[0]['id']
        project_id = self.get_company_projects_list(company_id).json()[0]['id']
        return project_id

    def get_resource_requests_by_company_id(self, company_id: int):
        """Снабжение: Заявки - Получить список заявок (По ИД компании)"""
        return self.session.get(f"{self.base_url}/companies/{company_id}/resource-requests")

    def create_resource_by_project_id(self, project_id: int, resource_json: dict):
        """По ТЗ запрос на создание заявки"""
        return self.session.post(f"{self.base_url}/projects/{project_id}/resources", data=resource_json)

    def create_resource_by_task_id(self, task_id: int, resource_json: dict):
        """Сметы - Добавить ресурс в работу"""
        return self.session.post(f"{self.base_url}/tasks/{task_id}/resources", resource_json)

    def create_resource_request(self, project_id: int, resource_request_json):
        """Снабжение: Заявки - Добавить заявку"""
        return self.session.post(f"{self.base_url}/projects/{project_id}/resource-requests", data=resource_request_json)

    def create_task(self, company_id: int, task_json: dict):
        """Создать задачу"""
        return self.session.post(f"{self.base_url}/companies/{company_id}/issues", data=task_json)

    def delete_resource_request(self, project_id: int, resource_request_id: int):
        return self.session.delete(f"{self.base_url}/projects/{project_id}/resource-requests/{resource_request_id}")

    def edit_resource_request(self, project_id: int, resource_request_id: int, edited_field: dict):
        return self.session.put(f"{self.base_url}/projects/{project_id}/resource-requests/{resource_request_id}",
                                data=edited_field)
