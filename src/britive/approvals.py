class Approvals():
    def __init__(self, britive) -> None:
        self.britive = britive
        self.base_url = f'{self.britive.base_url}/v1/approvals'

    def __review(self, decision : bool, request_id : str) -> dict:
        """for internal use"""
        params = {}
        if decision:
            params['approveRequest' ] = 'yes'
        else:
            params['approveRequest' ] = 'no'
        return self.britive.patch(f'{self.base_url}/{request_id}', params=params)

    def approve(self, request_id: str) -> dict:
        """
        Approves a request with requestID.

        :param request_id: ID of the request you want to approve.
        :return: None
        """

        return self.__review(True, request_id)

    def reject(self, request_id: str) -> dict:
        """
        Rejects a request with requestID.

        :param request_id: ID of the request you want to reject.
        :return: None
        """

        return self.__review(False, request_id)

    def get(self, request_id: str) -> dict:
        """
        Provides details of given request.

        :param request_id: ID of the request.
        :return: Details of specified request.
        """

        return self.britive.get(f'{self.base_url}/{request_id}')

    def list(self, filter : str = None) -> list:
        """
        Return the list of requests.

        :param filter: The filter that can filter the list requests. The supported operators are 'eq' and 'co'.
        :return: list of requests
        """

        params = {
            'requestType' : 'myApprovals',
            'filter' : filter,
            'consumer': 'papservice',
        }

        return self.britive.get(self.base_url, params=params)
