import pytest

from objects_schema import ResourceRequests, validate_json
import json_template.jsons as json_template


def test_get_project_resource_requests_status(api_client):
    """Снабжение: Заявки - Получить список заявок
    Тест 1 (Позитивный) - Проверка статуса запроса"""
    response = api_client.get_project_resource_requests_by_project_id(api_client.user_demo_project_id)
    assert response.status_code == 200


def test_get_project_resource_requests_schema(api_client):
    """Снабжение: Заявки - Получить список заявок
    Тест 2 (Позитивный) - Проверка корректной схемы ответа"""
    response = api_client.get_project_resource_requests_by_project_id(api_client.user_demo_project_id)
    for schema in response.json():
        assert validate_json(schema, ResourceRequests)


def test_get_project_resource_requests_unavailable_project_id(api_client):
    """Снабжение: Заявки - Получить список заявок
    Тест 3 (Негативный) - Проверка ввода недоступного проекта
    TODO: добавить проверку что проект номер не существует"""
    response = api_client.get_project_resource_requests_by_project_id(api_client.user_demo_project_id * 7)
    response_json = response.json()
    assert response.status_code == 404
    assert response_json == json_template.UNAVAILABLE_PROJECT_NUMBER


def test_get_project_resource_requests_long_project_id(api_client):
    """Снабжение: Заявки - Получить список заявок
    Тест 4 (Негативный) - Проверка длинного номера проекта"""
    response = api_client.get_project_resource_requests_by_project_id(api_client.user_demo_project_id * 1000000000000)
    response_json = response.json()
    assert response.status_code == 500
    assert response_json == json_template.LONG_PROJECT_NUMBER


def test_get_resource_request_by_id_status(api_client):
    """Снабжение: Заявки - Получить данные заявки (По ИД заявки)
    Тест 1 (Позитивный) - Проверка статуса запроса"""
    resource_request_id = \
        api_client.get_project_resource_requests_by_project_id(api_client.user_demo_project_id).json()[0]['id']
    response = api_client.get_resource_request_by_resource_request_id(api_client.user_demo_project_id,
                                                                      resource_request_id)
    assert response.status_code == 200


def test_get_resource_request_by_id_schema(api_client):
    """Снабжение: Заявки - Получить данные заявки (По ИД заявки)
    Тест 2 (Позитивный) - Проверка схемы запроса"""
    resource_request_id = \
        api_client.get_project_resource_requests_by_project_id(api_client.user_demo_project_id).json()[0]['id']
    response = api_client.get_resource_request_by_resource_request_id(api_client.user_demo_project_id,
                                                                      resource_request_id)
    assert validate_json(response.json(), ResourceRequests)


def test_get_resource_request_by_id_wrong_resource_request_id(api_client):
    """Снабжение: Заявки - Получить данные заявки (По ИД заявки)
    Тест 3 (Негативный) - Проверка ввода неправильного ИД заявки
    TODO: Сделать 100 процентный вариант для неправильного ИД заявки"""
    response = api_client.get_resource_request_by_resource_request_id(api_client.user_demo_project_id, 11223344)
    assert response.json() == json_template.WRONG_RESOURCE_REQUEST


def test_get_resource_request_by_id_wrong_project_id(api_client):
    """Снабжение: Заявки - Получить данные заявки (По ИД заявки)
    Тест 4 (Негативный) - Проверка ввода неправильного проектного номера"""
    resource_request_id = \
        api_client.get_project_resource_requests_by_project_id(api_client.user_demo_project_id).json()[0]['id']
    response = api_client.get_resource_request_by_resource_request_id(11223344, resource_request_id)
    assert response.json() == json_template.UNAVAILABLE_PROJECT_NUMBER


def test_get_resource_requests_by_company_id_status(api_client):
    """Снабжение: Заявки - Получить список заявок (По ИД компании)
    Тест 1 (Позитивный) - Проверка статуса запроса"""
    response = api_client.get_resource_requests_by_company_id(api_client.user_company_id)
    assert response.status_code == 200


def test_get_resource_requests_by_company_id_schema(api_client):
    """Снабжение: Заявки - Получить список заявок (По ИД компании)
    Тест 2 (Позитивный) - Проверка JSON схемы + соответствие аналогичному запросу с project_id"""
    response = api_client.get_resource_requests_by_company_id(api_client.user_company_id)
    for schema in response.json():
        assert validate_json(schema, ResourceRequests)

    project_id = api_client.user_demo_project_id
    project_resource_requests_by_project_id_json = api_client.get_project_resource_requests_by_project_id(
        project_id).json()
    assert response.json() == project_resource_requests_by_project_id_json


def test_get_resource_requests_by_company_id_wrong_company_id(api_client):
    """Снабжение: Заявки - Получить список заявок (По ИД компании)
    Тест 3 (Негативный) - Проверка ввода неправильного ИД компании"""
    response = api_client.get_resource_requests_by_company_id(11223344)
    assert response.status_code == 400
    assert response.json() == json_template.WRONG_COMPANY_ID


def test_get_resource_requests_by_company_id_wrong_(api_client):
    """Снабжение: Заявки - Получить список заявок (По ИД компании)
    Тест 4 (Негативный) - Проверка ввода не Integer"""
    response = api_client.get_resource_requests_by_company_id('COMPANY_ID')
    assert response.status_code == 404
    assert response.json() == json_template.PAGE_NOT_FOUND


def test_create_resource_request_only_requirement_fields(api_client):
    """Снабжение: Заявки - Добавить заявку
        Тест 1(Позитивный) - Проверка создания при заполнении обязательных полей
        TODO: сделать получение ИД задачи"""
    project_id = api_client.user_demo_project_id
    resource_requests_json = json_template.RESOURCE_REQUEST_SHORT
    resource_requests_json['project_tasks_resource_id'] = 12708774
    response = api_client.create_resource_request(project_id, resource_requests_json)
    response_json = response.json()
    assert response.status_code == 201
    assert validate_json(response_json, ResourceRequests)

    created_resource_request_json = api_client.get_resource_request_by_resource_request_id(project_id,
                                                                                           response_json['id']).json()
    user_id = api_client.get_current_user().json()['id']
    assert response_json['project_tasks_resource_id'] == str(created_resource_request_json['project_tasks_resource_id'])
    assert response_json['user_id'] == created_resource_request_json['user_id'] == user_id
    api_client.delete_resource_request(project_id, response_json['id'])


def test_create_resource_request_all_fields(api_client):
    """Снабжение: Заявки - Добавить заявку
        Тест 2(Позитивный) - Проверка создания при заполнении всех полей
        TODO: сделать получение ИД задачи"""
    project_id = api_client.user_demo_project_id
    resource_requests_json = json_template.RESOURCE_REQUEST_SHORT
    resource_requests_json['project_tasks_resource_id'] = 12708774
    resource_requests_json['batch_number'] = 2
    resource_requests_json['is_over_budget'] = 1
    response = api_client.create_resource_request(project_id, resource_requests_json)
    response_json = response.json()
    assert response.status_code == 201
    assert validate_json(response_json, ResourceRequests)
    created_resource_request_json = api_client.get_resource_request_by_resource_request_id(project_id,
                                                                                           response_json['id']).json()
    assert response_json['is_over_budget'] == created_resource_request_json['is_over_budget'] == 1
    api_client.delete_resource_request(project_id, response_json['id'])


def test_create_resource_request_not_all_requirements_field(api_client):
    """Снабжение: Заявки - Добавить заявку
        Тест 3(Негативный) - Проверка отправки запроса без обязательных полей
        TODO: сделать получение ИД задачи"""
    project_id = api_client.user_demo_project_id
    resource_requests_json = json_template.RESOURCE_REQUEST_SHORT
    requirement_fields = ["project_tasks_resource_id", "volume", "cost", "needed_at"]
    for field in requirement_fields:
        resource_requests_json_temp = resource_requests_json.copy()
        resource_requests_json_temp['project_tasks_resource_id'] = 12708774
        resource_requests_json_temp['batch_number'] = 2
        resource_requests_json_temp['is_over_budget'] = 1
        del resource_requests_json_temp[field]
        response = api_client.create_resource_request(project_id, resource_requests_json_temp)
        assert response.status_code == 422
        assert response.json()[0] == json_template.RESOURCE_REQUEST_FILLING_ERRORS[field]



@pytest.mark.parametrize(["key", "value"], [("project_tasks_resource_id", 'abc'), ("volume", 'abv'), ("cost", "abv"),
                                            ("needed_at", 'abc')])
def test_create_resource_request_non_existent_field_value(api_client, key, value):
    """Снабжение: Заявки - Добавить заявку
        Тест 4(Негативный) - Проверка неправильности заполнения полей
        TODO: сделать получение ИД задачи"""
    project_id = api_client.user_demo_project_id
    resource_requests_json = json_template.RESOURCE_REQUEST_SHORT.copy()
    resource_requests_json['project_tasks_resource_id'] = 12708774
    resource_requests_json[key] = value
    response = api_client.create_resource_request(project_id, resource_requests_json)
    assert response.status_code == 422
    assert response.json()[0] == json_template.RESOURCE_REQUEST_FIELD_TYPE_ERRORS[key]


@pytest.mark.parametrize(['key', 'value'], [("volume", 111), ("cost", 222), ("batch_number", 333)])
def test_edit_resource_request_with_one_field(api_client, prepare_and_delete_resource_request, key, value):
    """Снабжение: Заявки - Изменить данные заявки
        Тест 1(Позитивный) - Проверка изменения полей по очереди"""
    resource_request_id = prepare_and_delete_resource_request
    project_id = api_client.user_demo_project_id
    edited_field = {key: value}
    response = api_client.edit_resource_request(project_id, resource_request_id, edited_field)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json[key] == str(value)


def test_edit_resource_request_with_all_field(api_client, prepare_and_delete_resource_request):
    """Снабжение: Заявки - Изменить данные заявки
        Тест 2(Позитивный) - Проверка изменения всех полей?"""
    resource_request_id = prepare_and_delete_resource_request
    project_id = api_client.user_demo_project_id

    edited_fields = {"volume": 123, "cost": 321, "batch_number": 345, "batch_parent_request_id": 758,
                     "is_over_budget": 0, "created_at": 122222111,
                     "needed_at": 123123123}
    response = api_client.edit_resource_request(project_id, resource_request_id, edited_fields)
    response_json = response.json()
    assert response.status_code == 200
    for field in edited_fields:
        if field == 'is_over_budget':
            assert response_json['is_over_budget'] == json_template.IS_OVER_BUDGET_CONVERTER[
                edited_fields["is_over_budget"]]
            continue
        assert response_json[field] == str(edited_fields[field])


@pytest.mark.parametrize(['project_id', 'resource_request_id'], [(9999999999, "correct"), ("correct", 9999999999)],
                         ids=["wrong_project_id", "wrong_resource_request_id"])
def test_edit_resource_request_with_one_correct_field(api_client, prepare_and_delete_resource_request, project_id,
                                                      resource_request_id):
    """Снабжение: Заявки - Изменить данные заявки
        Тест 3(Негативный) - Отправка запроса с некорректными обязательными полями"""
    edited_field = {"volume": 111}
    if project_id == "correct":
        project_id = api_client.user_demo_project_id
    elif resource_request_id == "correct":
        resource_request_id = prepare_and_delete_resource_request
    response = api_client.edit_resource_request(project_id, resource_request_id, edited_field)
    assert response.status_code == 500


@pytest.mark.parametrize(['project_id', 'resource_request_id'], [("123ab2", "correct"), ("correct", "123ab2")],
                         ids=["string_project_id", "string_resource_request_id"])
def test_edit_resource_request_with_wrong_field_types(api_client, prepare_and_delete_resource_request, project_id,
                                                      resource_request_id):
    """Снабжение: Заявки - Изменить данные заявки
        Тест 4(Негативный) - Отправка запроса с некорректными обязательными полями"""
    edited_field = {"volume": 111}
    if project_id == "correct":
        project_id = api_client.user_demo_project_id
    elif resource_request_id == "correct":
        resource_request_id = prepare_and_delete_resource_request
    response = api_client.edit_resource_request(project_id, resource_request_id, edited_field)
    assert response.status_code == 404


def test_delete_resource_request_correct_request(api_client, create_resource_request):
    """Снабжение: Заявки - Удалить заявку
        Тест 1(Позитивный) - Проверка выполнения запроса"""
    project_id = api_client.user_demo_project_id
    resource_request_id = create_resource_request_fixture
    response = api_client.delete_resource_request(project_id, resource_request_id)
    assert response.status_code == 204
    assert response.url == f'{api_client.base_url}/projects/{project_id}/resource-requests/{resource_request_id}'


def test_delete_resource_request_check_deleted(api_client, create_resource_request_fixture):
    """Снабжение: Заявки - Удалить заявку
        Тест 2(Позитивный) - Проверка что заявка не находится"""
    project_id = api_client.user_demo_project_id
    resource_request_id = create_resource_request_fixture
    api_client.delete_resource_request(project_id, resource_request_id)
    check_resource_request_exists = api_client.get_resource_request_by_resource_request_id(project_id,
                                                                                           resource_request_id)
    assert check_resource_request_exists.json() == json_template.RESOURCE_REQUEST_NOT_EXIST


def test_delete_resource_request_cant_delete_over_budget(api_client, create_resource_request_fixture):
    """Снабжение: Заявки - Удалить заявку
        Тест 3(Позитивный) - Проверка, что не удаляется заявка с is_over_budget False"""
    project_id = api_client.user_demo_project_id
    resource_request_id = create_resource_request_fixture
    edited_field = {"is_over_budget": 0}
    api_client.edit_resource_request(project_id, resource_request_id, edited_field)
    response = api_client.delete_resource_request(project_id, resource_request_id)
    assert response.json() == json_template.RESOURCE_REQUEST_CANT_DELETE_IS_OVER_BUDGET


@pytest.mark.parametrize(['project_id', 'resource_request_id'], [(999999999, "correct"), ("correct", 999999999)],
                         ids=["wrong project_id", "wrong resource_request_id"])
def test_delete_resource_request_correct_request(api_client, create_resource_request_fixture, project_id, resource_request_id):
    """Снабжение: Заявки - Удалить заявку
        Тест 4 (Негативный) - Проверка выполнения запроса при несуществующих значений полей"""
    if project_id == "correct":
        project_id = api_client.user_demo_project_id
    elif resource_request_id == "correct":
        resource_request_id = create_resource_request_fixture
    response = api_client.delete_resource_request(project_id, resource_request_id)
    assert response.status_code == 404
    if project_id == 999999999:
        assert response.json() == json_template.UNAVAILABLE_PROJECT_NUMBER
    elif resource_request_id == 999999999:
        assert response.json() == json_template.TASK_RESOURCE_NOT_FOUND


@pytest.mark.parametrize(['project_id', 'resource_request_id'], [("123ab2", "correct"), ("correct", "True")],
                         ids=["string project_id", "string resource_request_id"])
def test_delete_resource_request_wrong_field_type(api_client, create_resource_request_fixture, project_id, resource_request_id):
    """Снабжение: Заявки - Удалить заявку
        Тест 4 (Негативный) - Проверка выполнения запроса при неправильных типах полей"""
    if project_id == "correct":
        project_id = api_client.user_demo_project_id
    elif resource_request_id == "correct":
        resource_request_id = create_resource_request_fixture
    response = api_client.delete_resource_request(project_id, resource_request_id)
    assert response.status_code == 404
    assert response.json() == json_template.PAGE_NOT_FOUND
