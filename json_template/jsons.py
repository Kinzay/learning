import json

UNAVAILABLE_PROJECT_NUMBER = {'name': 'Not Found', 'message': 'Выбранный проект недоступен.', 'code': 75120,
                              'status': 404}
LONG_PROJECT_NUMBER = {"name": "Internal Server Error", "message": "Возникла внутренняя ошибка сервера.", "code": 0,
                       "status": 500}
RESOURCE_REQUEST_SHORT = {"project_tasks_resource_id": 123, "volume": 100, "cost": 99, "needed_at": 1719091652}
WRONG_RESOURCE_REQUEST = {'code': 0,
                          'message': 'Запрошенная заявка на ресурс не найдена.',
                          'name': 'Not Found',
                          'status': 404}
WRONG_COMPANY_ID = {'code': 65410,
                    'message': 'Сущность Company не найдена.',
                    'name': 'Bad Request',
                    'status': 400}
PAGE_NOT_FOUND = {'name': 'Not Found', 'message': 'Страница не найдена.', 'code': 0, 'status': 404}
RESOURCE_SHORT = {"project_id": 2, "type": 3, "name": "test"}
TASK_SHORT = {"company_id": 2, "name": 'test', "description": "test description"}
RESOURCE_REQUEST_FILLING_ERRORS = {
    "project_tasks_resource_id": {'field': 'project_tasks_resource_id', 'message': 'Необходимо заполнить «Ресурс».'},
    "volume": {'field': 'volume', 'message': 'Необходимо заполнить «Количество».'},
    "cost": {'field': 'cost', 'message': 'Необходимо заполнить «Цена, шт».'},
    "needed_at": {'field': 'needed_at', 'message': 'Необходимо заполнить «Дата востребования».'}}
RESOURCE_REQUEST_FIELD_TYPE_ERRORS = {
    "project_tasks_resource_id": {'field': 'project_tasks_resource_id',
                                  'message': 'Значение «Ресурс» должно быть целым числом.'},
    "volume": {'field': 'volume', 'message': 'Значение «Количество» должно быть числом.'},
    "cost": {'field': 'cost', 'message': 'Значение «Цена, шт» должно быть числом.'},
    "needed_at": {'field': 'needed_at', 'message': 'Значение «Дата востребования» должно быть целым числом.'}}
IS_OVER_BUDGET_CONVERTER = {0: False, 1: True}
RESOURCE_REQUEST_NOT_EXIST = {'code': 0,
                              'message': 'Запрошенная заявка на ресурс не найдена.',
                              'name': 'Not Found',
                              'status': 404}
RESOURCE_REQUEST_CANT_DELETE_IS_OVER_BUDGET = {'name': 'Unprocessable entity',
                                               'message': 'Запрещено удалять заявки на заказы сверх бюджета.',
                                               'code': 0, 'status': 422}
TASK_RESOURCE_NOT_FOUND = {'code': 0,
                           'message': 'not_found_project_task_resource',
                           'name': 'Not Found',
                           'status': 404}
