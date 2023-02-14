from http import HTTPStatus

import allure

from const import urls
from utils.assertions import Assertions
from utils.base_case import BaseCase
from utils.my_requests import MyRequests


@allure.epic('User editing cases')
class TestUserEdit(BaseCase):
    @allure.description('This test checks the ability to edit a newly created user')
    def test_edit_just_created_user(self):
        # REGISTRATION
        registration_data = self.prepare_registration_data()
        auth_respose = MyRequests.post(
            url=urls.REGISTRATION_SLUG, data=registration_data)

        Assertions.assert_code_status(auth_respose, HTTPStatus.OK)
        Assertions.assert_json_has_key(auth_respose, 'id')

        email = registration_data['email']
        password = registration_data['password']
        user_id = self.get_json_value(auth_respose, 'id')

        # LOGIN
        auth_sid, token, _ = (
            self.create_session(email=email, password=password)
        )

        # EDIT
        new_name = 'changed name'
        edit_response = MyRequests.put(
            url=urls.EDIT_USER_SLUG.format(user_id),
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={'firstName': new_name}
        )

        Assertions.assert_code_status(edit_response, HTTPStatus.OK)

        # GET
        edit_response = MyRequests.get(
            url=urls.EDIT_USER_SLUG.format(user_id),
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
        )

        Assertions.assert_json_by_value(
            edit_response,
            'firstName',
            new_name,
            'Wrong name of the user after edit'
        )
