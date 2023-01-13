from __future__ import annotations

from http import HTTPStatus
from typing import Dict, List, Optional, Tuple, Union

from binarylane.api.server.server_data_usage_list import sync_detailed
from binarylane.client import Client
from binarylane.models.data_usages_response import DataUsagesResponse
from binarylane.models.links import Links

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "server_id",
            "expires",
            "transfer_gigabytes",
            "current_transfer_usage_gigabytes",
            "transfer_period_end",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "server_id": """The ID of the server that this data transfer usage refers to.""",
            "expires": """The date and time in ISO8601 format that the current billing period expires.""",
            "transfer_gigabytes": """The included data transfer for this server in this period in GB.""",
            "current_transfer_usage_gigabytes": """The used data transfer for this server in this period in GB.
If you have more than one server, please see our data pooling policy: this value may include excess data transfer used by other servers or may have 'offloaded' excess data transfer to other servers with spare capacity.""",
            "transfer_period_end": """The date and time in ISO8601 format that the data transfer limit period ended (if it is completed) or when it will end (if this is the current period).""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch all Current Data Usage (Transfer) for All Servers"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_data-usage_list"""

    @property
    def ok_response_type(self) -> type:
        return DataUsagesResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, DataUsagesResponse]]:

        # HTTPStatus.OK: DataUsagesResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[DataUsagesResponse] = None

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

            assert isinstance(page_response.parsed, DataUsagesResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.data_usages += page_response.parsed.data_usages

        return status_code, response
