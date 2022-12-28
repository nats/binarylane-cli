from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.action_response import ActionResponse
from ...models.change_manage_offsite_backup_copies import ChangeManageOffsiteBackupCopies
from ...models.problem_details import ProblemDetails
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    server_id: int,
    *,
    client: Client,
    json_body: ChangeManageOffsiteBackupCopies,
) -> Dict[str, Any]:
    url = "{}/v2/servers/{server_id}/actions#ChangeManageOffsiteBackupCopies".format(
        client.base_url, server_id=server_id
    )

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
    json_body: ChangeManageOffsiteBackupCopies,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Management of Offsite Backup Copies

     This is used to alter whether old offsite backups will be removed when the replacement upload is
    complete if offsite backups have been selected and a custom offsite location is used.

    Args:
        server_id (int): The target server id.
        json_body (ChangeManageOffsiteBackupCopies): Change the Management of Offsite Backup
            Copies

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
    json_body: ChangeManageOffsiteBackupCopies,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Management of Offsite Backup Copies

     This is used to alter whether old offsite backups will be removed when the replacement upload is
    complete if offsite backups have been selected and a custom offsite location is used.

    Args:
        server_id (int): The target server id.
        json_body (ChangeManageOffsiteBackupCopies): Change the Management of Offsite Backup
            Copies

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
    json_body: ChangeManageOffsiteBackupCopies,
) -> Response[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Management of Offsite Backup Copies

     This is used to alter whether old offsite backups will be removed when the replacement upload is
    complete if offsite backups have been selected and a custom offsite location is used.

    Args:
        server_id (int): The target server id.
        json_body (ChangeManageOffsiteBackupCopies): Change the Management of Offsite Backup
            Copies

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
    json_body: ChangeManageOffsiteBackupCopies,
) -> Optional[Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]]:
    """Change the Management of Offsite Backup Copies

     This is used to alter whether old offsite backups will be removed when the replacement upload is
    complete if offsite backups have been selected and a custom offsite location is used.

    Args:
        server_id (int): The target server id.
        json_body (ChangeManageOffsiteBackupCopies): Change the Management of Offsite Backup
            Copies

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