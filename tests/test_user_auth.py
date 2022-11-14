import pytest

from const import urls
from utils.assertions import Assertions
from utils.base_case import BaseCase
from utils.my_requests import MyRequests


class TestUserAuth(BaseCase):
    exclude_params = [
        ('no cookie'),
        ('no token'),
    ]

    def setup_method(self):
        email = 'vinkotov@example.com',
        password = '1234',
        self.auth_sid, self.token, self.user_id_from_auth_endpoints = (
            self.create_session(email=email, password=password)
        )

    def test_user_auth(self):
        check_response = MyRequests.get(
            url=urls.GET_IS_AUTH_SLUG,
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid': self.auth_sid}
        )
        Assertions.assert_json_by_value(
            check_response,
            'user_id',
            self.user_id_from_auth_endpoints,
            '''User id from auth endpoint is not equal
            to user id from check endpoint'''

        )

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_check_auth(self, condition):
        match condition:
            case 'no cookie':
                check_response = MyRequests.get(
                    url=urls.GET_IS_AUTH_SLUG,
                    headers={'x-csrf-token': self.token},
                )
            case 'no token':
                check_response = MyRequests.get(
                    url=urls.GET_IS_AUTH_SLUG,
                    cookies={'auth_sid': self.auth_sid}
                )
        Assertions.assert_json_by_value(
            check_response,
            'user_id',
            0,
            f'User is authorized with condition {condition}'

        )
