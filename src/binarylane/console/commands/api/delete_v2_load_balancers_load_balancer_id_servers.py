from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.load_balancers.delete_v2_load_balancers_load_balancer_id_servers import sync_detailed
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.server_ids_request import ServerIdsRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_load_balancers as api_get_v2_load_balancers
import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    load_balancer_id: int
    json_body: ServerIdsRequest

    def __init__(self, load_balancer_id: int, json_body: ServerIdsRequest) -> None:
        self.load_balancer_id = load_balancer_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/LoadBalancers/paths/~1v2~1load_balancers~1%7Bload_balancer_id%7D~1servers/delete"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def lookup_load_balancer_id(ref: str) -> Union[None, int]:
            return api_get_v2_load_balancers.Command(self._context).lookup(ref)

        mapping.add(
            PrimitiveAttribute(
                "load_balancer_id",
                int,
                required=True,
                option_name=None,
                metavar="load_balancer",
                description="""The ID or name of the load balancer for which servers should be removed.""",
                lookup=lookup_load_balancer_id,
            )
        )

        json_body = mapping.add_json_body(ServerIdsRequest)

        def lookup_server_id(ref: str) -> Union[None, int]:
            return api_get_v2_servers.Command(self._context).lookup(ref)

        json_body.add(
            PrimitiveAttribute(
                "server_ids",
                List[int],
                required=True,
                option_name=("servers", "server-ids"),
                metavar="servers",
                description="""A list of server ID or names.""",
                lookup=lookup_server_id,
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            load_balancer_id=request.load_balancer_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
