# This file was auto-generated by Fern from our API Definition.

import os
import typing

import httpx

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import ClientEnvironment


class BaseCohere:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : ClientEnvironment
        The environment to use for requests from the client. from .environment import ClientEnvironment



        Defaults to ClientEnvironment.PRODUCTION



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 300 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from cohere.client import Client

    client = Client(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ClientEnvironment = ClientEnvironment.PRODUCTION,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("CO_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 300 if httpx_client is None else None
        if token is None:
            raise ApiError(body="The client must be instantiated be either passing in token or setting CO_API_KEY")
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )


class AsyncBaseCohere:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : ClientEnvironment
        The environment to use for requests from the client. from .environment import ClientEnvironment



        Defaults to ClientEnvironment.PRODUCTION



    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 300 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from cohere.client import AsyncClient

    client = AsyncClient(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ClientEnvironment = ClientEnvironment.PRODUCTION,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("CO_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 300 if httpx_client is None else None
        if token is None:
            raise ApiError(body="The client must be instantiated be either passing in token or setting CO_API_KEY")
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: ClientEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
