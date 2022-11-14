def test(method):
    match method:
        case 'GET':
            print(method)
        case 'POST':
            print(method)
        case 'PUT':
            print(method)
        case 'DELETE':
            print(method)
        case _:
            raise Exception(f'Bad HTTP method "{method}" was received')


test(1)