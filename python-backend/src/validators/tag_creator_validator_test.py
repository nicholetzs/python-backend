from src.validators.tag_creator_validator import tag_creator_validator
from src.erros.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError

# teste unitário
class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    req = MockRequest(json={"product_code":"12345"})
    tag_creator_validator(req)

def test_tag_creator_validator_with_error():
    req = MockRequest(json={"product_code":12345}) #esse fica errado mesmo

    try:
        tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
