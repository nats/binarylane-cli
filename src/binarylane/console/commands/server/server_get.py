from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_get import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.server_response import ServerResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_get"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server to fetch.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ServerResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ServerResponse]]:

        # HTTPStatus.OK: ServerResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
