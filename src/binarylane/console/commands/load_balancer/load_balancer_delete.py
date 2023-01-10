from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.load_balancer.load_balancer_delete import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Cancel an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_delete"""
        parser.cli_argument(
            "load_balancer_id",
            int,
            description="""The ID of the load balancer to cancel.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return type(None)

    def request(
        self,
        load_balancer_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
