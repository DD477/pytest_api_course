import requests
from http import HTTPStatus

from lib.base_case import BaseCase
from lib.assertions import Assertions
from const import urls


class TestUserRegistration(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = requests.post(url=urls.REGISTRATION_SLUG, data=data)

        Assertions.assert_code_status(response, HTTPStatus.OK)
        Assertions.assert_json_has_key(response, 'id')

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        expected_content = "Users with email '{}' already exists"
        data = self.prepare_registration_data(email)
        response = requests.post(url=urls.REGISTRATION_SLUG, data=data)

        Assertions.assert_code_status(response, HTTPStatus.BAD_REQUEST)
        assert (
            response.content.decode('utf-8') == expected_content.format(email)
        ), (
            f'Unexpected response content {response.content}'
        )
