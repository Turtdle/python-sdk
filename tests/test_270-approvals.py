from .cache import * # will also import some globals like `britive`
from britive.britive import Britive
from random import randint

britive = Britive()

def random_str_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))


"""
Current way to find the user who is executing the tests;
Replace by a better way if possible
"""
temp_token = britive.api_tokens.create(name = 'Temporary token for approvals testing')
current_user = britive.users.get_by_name(temp_token['createdBy'])


checkout_SI = britive.service_identities.create(
    name = "Approvals Test Checkout " + random_str_with_N_digits(5),
)
britive_requester = Britive(token=checkout_SI['token'])
policy = britive.profiles.policies.build(
    name = 'Approval Test Policy ' + random_str_with_N_digits(5),
    service_identities=checkout_SI['id'],
    approver_users=current_user['id']
)
t = britive.profiles.policies.create(cached_profile['id'], policy)
response = britive_requester.my_access.request_approval_by_name(
    cached_profile['name'],
    cached_environment['name'],
    justification='approvals test'
)

cached_approvals = britive.approvals.get(response['id'])

def test_get(cached_approval):
    response = britive.approvals.get(cached_approval['requestId'])
    assert isinstance(response, dict)
    assert "requestId" in response.keys()

def test_list():
    response = britive.approvals.list()
    assert isinstance(response, list)
    assert len(response) > 0
    assert isinstance(response[0], dict)

def test_review(cached_approval):
    britive.approvals.approve(cached_approval['requestId'])
    assert britive.approvals.get(cached_approval['requestId'])['status'] == 'APPROVED'


