from requests import JSONDecodeError, Response


class Assertions:
    @staticmethod
    def assert_json_by_value(
        response: Response,
        name: str,
        expected_value: str,
        error_message: str
    ):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, (
                f'Response is not in JSON. Response text is "{response.text}"'
            )
        assert name in response_as_dict, (
            f'Response does not have a key {name}'
        )
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name: str):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, (
                f'Response is not in JSON. Response text is "{response.text}"'
            )
        assert name in response_as_dict, (
            f'Response does not have a key {name}'
        )

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, (
                f'Response is not in JSON. Response text is "{response.text}"'
            )
        for name in names:
            assert name in response_as_dict, (
                f'Response does not have a key {name}'
            )

    @staticmethod
    def assert_json_has_not_key(response: Response, name: str):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, (
                f'Response is not in JSON. Response text is "{response.text}"'
            )
        assert name not in response_as_dict, (
            f'Response JSON should not have a key {name}. But it is present'
        )

    @staticmethod
    def assert_code_status(response: Response, expected_code_status):
        assert response.status_code == expected_code_status, (
            f'Unexpected status code. Expected: {expected_code_status}. '
            f'Actual: {response.status_code}.'
        )
