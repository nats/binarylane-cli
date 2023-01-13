from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_add_disk import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.add_disk import AddDisk
from binarylane.models.add_disk_type import AddDiskType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "add-disk"

    @property
    def description(self) -> str:
        return """Create an Additional Disk for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_add-disk"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            AddDiskType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--size-gigabytes",
            int,
            dest="size_gigabytes",
            required=True,
            description="""The size of the new disk in GB. The server must have at least this much unallocated storage space.""",
        )

        parser.cli_argument(
            "--description",
            Union[Unset, None, str],
            dest="description",
            required=False,
            description="""An optional description for the disk. If this is null a default description will be added. Submit an empty string to prevent the default description being added.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: AddDiskType,
        size_gigabytes: int,
        description: Union[Unset, None, str] = UNSET,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=AddDisk(
                type=type,
                size_gigabytes=size_gigabytes,
                description=description,
            ),
        )
        return page_response.status_code, page_response.parsed
