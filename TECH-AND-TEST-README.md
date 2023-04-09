# Python Britive SDK

This repo will hold the python code that wraps the Britive API so downstream python applications/scripts
can consume a native Python library.

## Python Version Support
We use `typing` in this package so a requirement is Python 3.5 or greater - https://docs.python.org/3/library/typing.html.
Use of {**dict1, **dict2} exists in profiles.py and that also requires Python 3.5 or greater.
`requests` package will stop supporting 3.6 in 2022 so we should bump to only supporting Python 3.7 and up


## Production Use
Install requirements.

~~~
pip install -r requirements.txt
~~~


## Building

Steps from here: https://packaging.python.org/en/latest/tutorials/packaging-projects/

Inside the existing virtualenv...

~~~
python -m pip install --upgrade build
python -m build
~~~

We will now have a new `/dist` directory containing a `.tar.gz` tarball and `whl` wheel. The wheel is considered
a "built distribution" meaning it is compiled for various OSes and architectures. In our case this is a pure Python
implementation so the wheel is for all OSes and architectures (`-py3-none-any.whl`).

## Github Actions
There are 2 Github Actions in play that publish to PyPI.

1. Trigger off of a push to the `develop` branch. Will deploy to test PyPI.
2. Trigger off of a new release being published. Will deploy to real PyPI.


## Testing
Install requirements.

~~~
pip install -r requirements/dev.txt
~~~

This library is using `tox` for true package testing. `tox` will install the package distribution in a virtual
environment and then run the tests (using `pytest`) inside of that clean environment. This ensures that the packaging
process itself is also working as expected.

To run just execute `tox` on the command line or if you want to clean the environment `tox -r` which will
rebuild the entire virtualenv. There are some issues with pytest caching that have been found so cleaning the virtualenv
helps clear that up.

`pytest` is being used to test the SDK. Run the following commands in order to test the full library.

These below tests/commands should only be run during local development when iterating quickly (more like unit testing). 
`tox` should be used when possible to test the full end-to-end process (more like integration testing).

If you do want to run these outside of `tox` you will need to set this environment variable so that we can do some
PATH magic in `tests/__init__.py`.

~~~
export BRITIVE_UNIT_TESTING=true
~~~

You will also need other environment variables.

* The AWS account that will be used to create test applications/environments/etc. This is being added as an 
environment variable, so it is not hardcoded into the tests and stored in the repo as a result.

Note that this AWS account will need 2 IAM resources.

* Identity Provider: name of BritivePythonApiWrapperTesting-{tenant}
* Role: name of britive-integration-role-{tenant}

where {tenant} is the lowercase tenant and is also what is set below in the BRITIVE_TENANT env var

~~~
export BRITIVE_API_TOKEN=...
export BRITIVE_TENANT=...
export BRITIVE_TEST_ENV_ACCOUNT_ID=<12 digit AWS account id>
~~~

If you want to skip running a scan (and waiting a long time for the results) you can set

~~~
export BRITIVE_TEST_IGNORE_SCAN=true
~~~

And then all the API calls that are reliant on a scan to occur will be ignored. This may be useful when you just
want to an internal end-to-end process vs. integrating with a cloud service provider.

Then run these in order or as required.

~~~
pytest tests/test_005-identity_attributes.py -v
pytest tests/test_010-users.py -v
pytest tests/test_020-tags.py -v
pytest tests/test_030-service_identities.py -v
pytest tests/test_040-service_identity_tokens.py -v
pytest tests/test_050-applications.py -v
pytest tests/test_060-environment_groups.py -v
pytest tests/test_070-environments.py -v
pytest tests/test_080-scans.py -v  # warning - this one will take a while since it initiates a real scan
pytest tests/test_090-accounts.py -v # note - a scan must first be completed
pytest tests/test_100-permissions.py -v # note - a scan must first be completed
pytest tests/test_110-groups.py -v # note - a scan must first be completed
pytest tests/test_130-profiles.py -v
pytest tests/test_140-task_services.py -v
pytest tests/test_150-tasks.py -v
pytest tests/test_160-security_policies.py -v
pytest tests/test_170-saml.py -v
pytest tests/test_180-api_tokens.py -v
pytest tests/test_190-audit_logs.py -v
pytest tests/test_200-reports.py -v
pytest tests/test_210-identity_providers.py -v
pytest tests/test_215-workload.py -v
pytest tests/test_220-my_access.py -v
pytest tests/test_230-notifications.py -v
pytest tests/test_240-secrets_manager.py -v
pytest tests/test_250-my_secrets.py -v
pytest tests/test_260-notification_mediums.py -v
pytest tests/test_270-system_policies.py -v
pytest tests/test_280_system_actions.py -v
pytest tests/test_290_system_consumers.py -v
pytest tests/test_300-system_roles.py -v
pytest tests/test_310-system_permissions.py -v

pytest tests/test_990-delete_all_resources.py -v
~~~

Or you can simply run `pytest -v` to test everything all at once. The above commands however allow you to halt
testing to fix issues that might arise.

## Secrets Manager Testing

Since the admin API actions for Secrets Manager are not yet built into this Python API Wrapper then
some manual setup has to occur in the tenant used for testing. Specifically these tests will need at
least 1 secret available to the calling user/service identity and one of those secrets has to be named
"/Test".

This will change once the admin API actions are built into this package as we can then programmatically create
the vault and secrets before testing the britive.my_secrets functionality.
