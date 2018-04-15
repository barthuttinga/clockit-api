import json

from flask import url_for

from clockit_api.status import *
from . import AppTestCase


class ModelsTestCase(AppTestCase):
    def test_list_customers(self):
        token = self.get_token('joe', 'pass')
        url = url_for('api.customers', _external=True)
        headers = {'Authorization': 'JWT ' + token}
        response = self.test_client.get(url, headers=headers)
        assert HTTP_200_OK == response.status_code

    def test_create_customer(self):
        token = self.get_token('joe', 'pass')
        url = url_for('api.customers', _external=True)
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
        }
        data = {'name': 'New customer'}
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )
        assert HTTP_201_CREATED == response.status_code

    def test_create_customer_without_name(self):
        token = self.get_token('joe', 'pass')
        url = url_for('api.customers', _external=True)
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
        }
        data = {}
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )
        data = json.loads(response.data)
        assert HTTP_400_BAD_REQUEST == response.status_code
        assert data['name'] == ['Missing data for required field.']

    def test_list_projects(self):
        token = self.get_token('joe', 'pass')
        url = url_for('api.projects', _external=True)
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
        }
        response = self.test_client.get(url, headers=headers)
        data = json.loads(response.data)

        assert HTTP_200_OK == response.status_code
        for elm in data:
            assert sorted(elm.keys()) == ['created_at', 'customer', 'id',
                                          'name']
            # assert elm['customer'] == 1

    def test_create_project(self):
        token = self.get_token('joe', 'pass')
        url = url_for('api.projects', _external=True)
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
        }
        data = {'name': 'New project',
                'customer': {"id": 1, "name": "New customer"}}
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )

        assert HTTP_201_CREATED == response.status_code
        assert data['name'] == 'New project'
        assert data['customer']['id'] == 1

    def test_create_customer_project(self):
        token = self.get_token('joe', 'pass')
        url = url_for('api.customer_projects', id=1, _external=True)
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
        }
        data = {'name': 'New project'}
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )
        data = json.loads(response.data)

        assert HTTP_201_CREATED == response.status_code
        assert data['name'] == 'New project'
        assert data['customer']['id'] == 1

    def test_list_customer_projects(self):
        token = self.get_token('joe', 'pass')
        url = url_for('api.customer_projects', id=1, _external=True)
        headers = {
            'Authorization': 'JWT ' + token,
            'Content-Type': 'application/json',
        }
        response = self.test_client.get(
            url,
            headers=headers
        )
        data = json.loads(response.data)

        assert HTTP_200_OK == response.status_code
        assert len(data) == 4
        for elm in data:
            assert sorted(elm.keys()) == ['created_at', 'id', 'name']
