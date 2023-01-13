from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.vpc.vpc_update import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.models.update_vpc_request import UpdateVpcRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.vpc_response import VpcResponse
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return """Update an Existing VPC"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for vpc_update"""
        parser.cli_argument(
            "vpc_id",
            int,
            description="""The target vpc id.""",
        )

        parser.cli_argument(
            "--name",
            str,
            dest="name",
            required=True,
            description="""A name to help identify this VPC.""",
        )

        parser.cli_argument(
            "--route-entries",
            Union[Unset, None, List[RouteEntryRequest]],
            dest="route_entries",
            required=False,
            description="""The route entries that control how network traffic is directed through the VPC environment.""",
        )

    @property
    def ok_response_type(self) -> type:
        return VpcResponse

    def request(
        self,
        vpc_id: int,
        client: Client,
        name: str,
        route_entries: Union[Unset, None, List[RouteEntryRequest]] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails, VpcResponse]]:

        # HTTPStatus.OK: VpcResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            vpc_id=vpc_id,
            client=client,
            json_body=UpdateVpcRequest(
                name=name,
                route_entries=route_entries,
            ),
        )
        return page_response.status_code, page_response.parsed
