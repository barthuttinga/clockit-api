import json

from flask import url_for

from app.status import *
from . import AppTestCase


class AuthenticationTestCase(AppTestCase):
    def test_get_token_with_valid_credentials(self):
        url = url_for('_default_auth_request_handler', _external=True)
        headers = {'Content-Type': 'application/json'}
        data = {
            'username': 'joe',
            'password': 'pass',
        }
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )

        data = json.loads(response.data)
        assert HTTP_200_OK == response.status_code
        assert data.get('access_token')

    def test_get_token_with_invalid_credentials(self):
        url = url_for('_default_auth_request_handler', _external=True)
        headers = {'Content-Type': 'application/json'}
        data = {
            'username': 'joe',
            'password': 'nopass',
        }
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )

        data = json.loads(response.data)
        assert HTTP_401_UNAUTHORIZED == response.status_code
        assert data.get('description') == 'Invalid credentials'

    def test_get_protected_resource(self):
        url = url_for('_default_auth_request_handler', _external=True)
        headers = {'Content-Type': 'application/json'}
        data = {
            'username': 'joe',
            'password': 'pass',
        }
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )

        data = json.loads(response.data)
        assert HTTP_200_OK == response.status_code
        assert data.get('access_token')

        url = url_for('api.customers', _external=True)
        headers = {'Authorization': 'JWT ' + data.get('access_token')}
        response = self.test_client.get(url, headers=headers)

        assert HTTP_200_OK == response.status_code
