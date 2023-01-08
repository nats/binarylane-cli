from typing import Any, Type

from ...client.api.domain.domain_refresh_nameserver_cache import sync_detailed
from ...client.client import Client
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "refresh-nameserver-cache"

    @property
    def description(self):
        return """Refresh Cached Nameserver Domain Records"""

    def configure(self, parser):
        """Add arguments for domain_refresh-nameserver-cache"""

    @property
    def ok_response_type(self) -> Type:
        return type(None)

    def request(
        self,
        client: Client,
    ) -> Any:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
