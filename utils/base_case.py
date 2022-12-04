from datetime import datetime as dt
from typing import Optional

from requests import Response

from const import urls
from utils.assertions import Assertions
from utils.my_requests import MyRequests


class BaseCase:
    def get_cookie(self, response: Response, cookie_name: str):
        assert cookie_name in response.cookies, (
            f'Cannot fine cookie with a name {cookie_name} '
            'in the last response'
        )
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name: str):
        assert header_name in response.headers, (
            f'Cannot find header with a name {header_name} '
            'in the lase response'
        )
        return response.headers[header_name]

    def get_json_value(self, response: Response, name: str):
        response_as_dict = Assertions.assert_response_in_json_format(response)
        assert name in response_as_dict, (
            f'Response does not have a key {name}'
        )
        return response_as_dict[name]

    def create_session(self, email: str, password: str):
        data = {
            'email': email,
            'password': password
        }
        response = MyRequests.post(url=urls.LOGIN_SLUG, data=data)
        auth_sid = self.get_cookie(response, 'auth_sid')
        token = self.get_header(response, 'x-csrf-token')
        user_id = self.get_json_value(
            response, 'user_id'
        )
        return auth_sid, token, user_id

    def prepare_registration_data(self, email: Optional[str] = None):
        if email is None:
            base_part = 'test'
            domain = 'example.com'
            random_part = dt.now().strftime('%m%d%Y%H%M%S')
            email = f'{base_part}{random_part}@{domain}'

        return {
            'password': '1234',
            'username': 'test_username',
            'firstName': 'test_first_name',
            'lastName': 'test_last_name',
            'email': email
        }
