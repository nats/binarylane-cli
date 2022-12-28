from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.action_response import ActionResponse
from ...models.change_port_blocking import ChangePortBlocking
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    json_body: ChangePortBlocking,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}/actions#ChangePortBlocking".format(client.base_url, server_id=server_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    if response.status_code == 200:
        response_200 = ActionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == 400:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())

        return response_422
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    server_id: int,
    *,
    client: Client,
    json_body: ChangePortBlocking,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Port Blocking for a Server

     Port blocking is a security feature. In the majority of cases when a server is hacked, the attacker
    will then use the server to either send spam or perform brute-force authentication attacks against
    other servers on the internet.
    This is used to enable or disable blocking of outgoing connections for email, SSH and Remote Desktop
    (TCP ports 22, 25, and 3389).


    Args:
        server_id (int): The target server id.
        json_body (ChangePortBlocking): Change the Port Blocking for a Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    server_id: int,
    *,
    client: Client,
    json_body: ChangePortBlocking,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Port Blocking for a Server

     Port blocking is a security feature. In the majority of cases when a server is hacked, the attacker
    will then use the server to either send spam or perform brute-force authentication attacks against
    other servers on the internet.
    This is used to enable or disable blocking of outgoing connections for email, SSH and Remote Desktop
    (TCP ports 22, 25, and 3389).


    Args:
        server_id (int): The target server id.
        json_body (ChangePortBlocking): Change the Port Blocking for a Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return sync_detailed(
        server_id=server_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    server_id: int,
    *,
    client: Client,
    json_body: ChangePortBlocking,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Port Blocking for a Server

     Port blocking is a security feature. In the majority of cases when a server is hacked, the attacker
    will then use the server to either send spam or perform brute-force authentication attacks against
    other servers on the internet.
    This is used to enable or disable blocking of outgoing connections for email, SSH and Remote Desktop
    (TCP ports 22, 25, and 3389).


    Args:
        server_id (int): The target server id.
        json_body (ChangePortBlocking): Change the Port Blocking for a Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        server_id=server_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    server_id: int,
    *,
    client: Client,
    json_body: ChangePortBlocking,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Port Blocking for a Server

     Port blocking is a security feature. In the majority of cases when a server is hacked, the attacker
    will then use the server to either send spam or perform brute-force authentication attacks against
    other servers on the internet.
    This is used to enable or disable blocking of outgoing connections for email, SSH and Remote Desktop
    (TCP ports 22, 25, and 3389).


    Args:
        server_id (int): The target server id.
        json_body (ChangePortBlocking): Change the Port Blocking for a Server

    Returns:
        Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]
    """

    return (
        await asyncio_detailed(
            server_id=server_id,
            client=client,
            json_body=json_body,
        )
    ).parsed