import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions
from const import urls


class TestUserGet(BaseCase):
    def test_get_user_detalis_not_auth(self):
        response = requests.get(url=urls.EDIT_USER_SLUG.format(2))

        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_not_key(response, 'email')
        Assertions.assert_json_has_not_key(response, 'firstName')
        Assertions.assert_json_has_not_key(response, 'lastName')

    def test_get_user_detalis_auth_as_same_user(self):
        email = 'vinkotov@example.com',
        password = '1234',
        auth_sid, token, user_id_from_auth_endpoints = (
            self.create_session(email=email, password=password)
        )

        check_response = requests.get(
            url=urls.EDIT_USER_SLUG.format(user_id_from_auth_endpoints),
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        expected_fields = ('username', 'email', 'firstName', 'lastName')
        Assertions.assert_json_has_keys(check_response, expected_fields)
