# Change Log

All changes to the package starting with v2.8.1 will be logged here.

## v2.18.0 [2023-03-27]
#### What's New
* Support for tag membership rules.

#### Enhancements
* Allow the creation of external tags (tags associated with an identity provider) using a non-SCIM identity.

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None


## v2.17.0 [2023-03-14]
#### What's New
* Workload API coverage (create workload federation identity providers and map to service identities) `workload`
* System Policies coverage `system.policies`
* System Roles coverage `system.roles`
* System Permissions coverage `system.permissions`

#### Enhancements
* Add custom attribute coverage to users and service identities

#### Bug Fixes
* None

#### Dependencies
* For dev/test removed the pin on `pytest` which was causing issues with newer versions of python

#### Other
* None

### DEPRECATION NOTICE

#### `policies.py`

This python file only holds one method `build`. The remainder of the system policy logic has been created
in `system.policies` so as not to cause confusion with secrets manager and profile policies.

In the next major release, `policies.py` will be retired. As of release `2.17.0` the `polices.build` method
simply calls `system.policies.build`. 

## v2.16.0 [2023-03-02]
#### What's New
* Natively support Azure Managed Identity OIDC authentication for workload federation.

#### Enhancements
* None

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.15.1 [2023-02-16]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
* Added missing API call `profiles.get_scopes()`

#### Dependencies
* None

#### Other
* None

## v2.15.0 [2023-02-06]
#### What's New
* Added two new APIs for managing single environment scope changes for a profile
  * `profiles.add_single_environment_scope()`
  * `profiles.remove_single_environment_scope()`

#### Enhancements
* None

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.14.2 [2023-01-27]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
* In `poilicies.build()` properly handle when lists are empty

#### Dependencies
* None

#### Other
* None

## v2.14.1 [2023-01-24]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
* In `profile.poilicies.build()` support the now available `validFor` approval parameter via method parameter `access_validity_time`.

#### Dependencies
* None

#### Other
* None

## v2.14.0 [2023-01-18]
#### What's New
* Added Bitbucket as an OIDC federation provider so that the needed logic for authenticating to Britive via Bitbucket pipelines is abstracted away from the caller.

#### Enhancements
* None

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.13.0 [2023-01-06]
#### What's New
* Ability to pass a callback function to the following `my_access` methods which will report progress of the process.
  * `checkout`
  * `checkout_by_name`
  * `request_approval`
  * `request_approval_by_name`

#### Enhancements
* None

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.12.4 [2023-01-04]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
> **_NOTE:_**  This is a pre-release feature. It is being published in anticipation of upcoming features being released to production. This functionality will not yet work in production environments.
* Properly handle use case of long term (IAM User) vs. temporary credentials (AssumeRole/Federation) in the AWS Federation Provider

#### Dependencies
* None

#### Other
* None

## v2.12.3 [2022-12-12]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
* Fix bug when catching JSON decode exceptions when decoding `requests` response - catching the more generic `ValueError` instead of a specific JSON decode error
> **_NOTE:_**  This is a pre-release feature. It is being published in anticipation of upcoming features being released to production. This functionality will not yet work in production environments.
* Remove port from tenant name in the AWS provider

#### Dependencies
* None

#### Other
* Allow disabling TLS/SSL verification for local development work by setting environment variable `export BRITIVE_NO_VERIFY_SSL=true`

## v2.12.2 [2022-11-28]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
> **_NOTE:_**  This is a pre-release feature. It is being published in anticipation of upcoming features being released to production. This functionality will not yet work in production environments.
* Fix issue with AWS provider when injecting the tenant name into the AWS sigv4 signed request

#### Dependencies
* None

#### Other
* None

## v2.12.1 [2022-11-17]
#### What's New
* None

#### Enhancements
> **_NOTE:_**  This is a pre-release feature. It is being published in anticipation of upcoming features being released to production. This functionality will not yet work in production environments.
* Allow caller to specify duration/expiration time of tokens generated by the AWS federation provider 

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.12.0 [2022-11-16]
#### What's New
> **_NOTE:_**  This is a pre-release feature. It is being published in anticipation of upcoming features being released to production. This functionality will not yet work in production environments.
* Support for workload identity federation providers 

#### Enhancements
* None

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.11.2 [2022-11-01]
#### What's New
* None

#### Enhancements
* Reduce number of API calls required to checkout a profile

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.11.1 [2022-10-24]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
* Allow local machine DNS resolution (e.g. /etc/hosts) for tenant URL check

#### Dependencies
* None

#### Other
* None

## v2.11.0 [2022-10-18]
#### What's New
* Support for Secrets Manager APIs
  * Vaults
  * Password Policies
  * Secrets
  * Policies
  * Static Secret Templates
  * Resources
  * Folders
* Support for Notification Medium APIs

#### Enhancements
* Allow the use of a port number in a tenant URL

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.10.0 [2022-10-06]
#### What's New
* None

#### Enhancements
* Allow for non `*.britive-app.com` tenants. Default to `britive-app.com` if no valid URL is provided (for backwards compatibility)

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.9.0 [2022-09-30]
#### What's New
* Exponential backoff logic added to all API calls.

#### Enhancements
* Add `filter_expression` to `britive.reports.run()` to allow filtering the results as required by the caller.

#### Bug Fixes
* None

#### Dependencies
* None

#### Other
* None

## v2.8.1 [2022-09-22]
#### What's New
* None

#### Enhancements
* None

#### Bug Fixes
* Fixes an issue with `britive.audit_logs.query()` pagination. The last page of results is now included.
* Fixes an issue with `britive.reports.run()` pagination. The last page of results is now included.
* Fixes an issue with `britive.reports.run()` results being truncated to a maximum of 1000 records when `csv=False`. This was due to how the API handles JSON results vs. CSV results. Now the results are always obtained in CSV format from the API and then converted to a list of dictionaries if `csv=False`.

#### Dependencies
* None

#### Other
* None
