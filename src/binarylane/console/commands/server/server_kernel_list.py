from __future__ import annotations

from http import HTTPStatus
from typing import Dict, List, Optional, Tuple, Union

from binarylane.api.server.server_kernel_list import sync_detailed
from binarylane.client import Client
from binarylane.models.kernels_response import KernelsResponse
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this kernel.""",
            "name": """This name of this kernel.""",
            "version": """The version (if any) of this kernel.""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List all Available Kernels for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_kernel_list"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server for which kernels should be listed.""",
        )

    @property
    def ok_response_type(self) -> type:
        return KernelsResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, KernelsResponse, ProblemDetails]]:

        # HTTPStatus.OK: KernelsResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[KernelsResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=server_id,
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, KernelsResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.kernels += page_response.parsed.kernels

        return status_code, response
