import os

import pytest
import dotenv

from gectaro_api_client import GectaroApiClient
import json_template.jsons as json_template

dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')
URL = os.getenv('URL')


@pytest.fixture(scope='session')
def api_client():
    client = GectaroApiClient(auth_token=TOKEN, base_url=URL)
    return client


@pytest.fixture(scope='function')
def prepare_and_delete_resource_request(api_client):
    project_id = api_client.user_demo_project_id
    resource_requests_json = json_template.RESOURCE_REQUEST_SHORT
    resource_requests_json['project_tasks_resource_id'] = 12708774
    resource_requests_json['is_over_budget'] = 1
    response = api_client.create_resource_request(project_id, resource_requests_json)
    response_json = response.json()
    yield response_json['id']
    api_client.delete_resource_request(project_id, response_json['id'])


@pytest.fixture(scope='function')
def create_resource_request_fixture(api_client):
    project_id = api_client.user_demo_project_id
    resource_requests_json = json_template.RESOURCE_REQUEST_SHORT
    resource_requests_json['project_tasks_resource_id'] = 12708774
    resource_requests_json['is_over_budget'] = 1
    response = api_client.create_resource_request(project_id, resource_requests_json)
    response_json = response.json()
    yield response_json['id']


