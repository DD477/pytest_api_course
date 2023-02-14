from http import HTTPStatus

import allure

from const import urls
from utils.assertions import Assertions
from utils.base_case import BaseCase
from utils.my_requests import MyRequests


@allure.epic('Registration cases')
class TestUserRegistration(BaseCase):
    @allure.description('This test checks user registration')
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post(url=urls.REGISTRATION_SLUG, data=data)

        Assertions.assert_code_status(response, HTTPStatus.OK)
        Assertions.assert_json_has_key(response, 'id')

    @allure.description('This test checks user registration with existing email')
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        expected_content = "Users with email '{}' already exists"
        data = self.prepare_registration_data(email)
        response = MyRequests.post(url=urls.REGISTRATION_SLUG, data=data)

        Assertions.assert_code_status(response, HTTPStatus.BAD_REQUEST)
        assert (
            response.content.decode('utf-8') == expected_content.format(email)
        ), (
            f'Unexpected response content {response.content}'
        )
