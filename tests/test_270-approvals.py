from .cache import * # will also import some globals like `britive`
from britive.britive import Britive
from random import randint

britive = Britive()

def test_get(cached_approval):
    response = britive.approvals.get(cached_approval['requestId'])
    assert isinstance(response, dict)
    assert "requestId" in response.keys()

def test_list(cached_approval):
    response = britive.approvals.list()
    assert isinstance(response, list)
    assert len(response) > 0
    assert isinstance(response[0], dict)

def test_review(cached_approval):
    britive.approvals.approve(cached_approval['requestId'])
    assert britive.approvals.get(cached_approval['requestId'])['status'] == 'APPROVED'
