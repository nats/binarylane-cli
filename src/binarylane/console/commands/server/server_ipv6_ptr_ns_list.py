from __future__ import annotations

from http import HTTPStatus
from typing import Optional, Tuple, Union

from binarylane.api.server.server_ipv6_ptr_ns_list import sync_detailed
from binarylane.client import Client
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.reverse_name_servers_response import ReverseNameServersResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch all Existing IPv6 Name Server Records"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_ipv6-ptr-ns_list"""

    @property
    def ok_response_type(self) -> type:
        return ReverseNameServersResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ReverseNameServersResponse]]:

        # HTTPStatus.OK: ReverseNameServersResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[ReverseNameServersResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, ReverseNameServersResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.reverse_nameservers += page_response.parsed.reverse_nameservers

        return status_code, response
