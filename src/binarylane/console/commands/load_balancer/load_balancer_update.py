from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.load_balancer.load_balancer_update import sync_detailed
from binarylane.client import Client
from binarylane.models.algorithm_type import AlgorithmType
from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.health_check import HealthCheck
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.sticky_sessions import StickySessions
from binarylane.models.update_load_balancer_request import UpdateLoadBalancerRequest
from binarylane.models.update_load_balancer_response import UpdateLoadBalancerResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "update"

    @property
    def description(self):
        return """Update an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_update"""
        parser.cli_argument(
            "load_balancer_id",
            int,
            description="""The ID of the load balancer to update.""",
        )

        parser.cli_argument(
            "--name",
            str,
            dest="name",
            required=True,
            description="""The hostname of the load balancer.""",
        )

        parser.cli_argument(
            "--algorithm",
            Union[Unset, None, AlgorithmType],
            dest="algorithm",
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| round_robin | Each request will be sent to one of the nominated servers in turn. |
| least_connections | Each request will be sent to the server with the least existing connections. This option is not currently supported. |

""",
        )

        parser.cli_argument(
            "--forwarding-rules",
            Union[Unset, None, List[ForwardingRule]],
            dest="forwarding_rules",
            required=False,
            description="""The rules that control which traffic the load balancer will forward to servers in the pool. Leave null to accept a default "HTTP" only forwarding rule.""",
        )

        parser.cli_argument(
            "--health-check",
            Union[Unset, None, HealthCheck],
            dest="health_check",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--sticky-sessions",
            Union[Unset, None, StickySessions],
            dest="sticky_sessions",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--redirect-http-to-https",
            Union[Unset, None, bool],
            dest="redirect_http_to_https",
            required=False,
            description="""Redirect HTTP traffic received by the load balancer to HTTPS. This is not currently supported.""",
            action=BooleanOptionalAction,
        )

        parser.cli_argument(
            "--enable-proxy-protocol",
            Union[Unset, None, bool],
            dest="enable_proxy_protocol",
            required=False,
            description="""Enable the PROXY protocol on the load balancer. This is not currently supported.""",
            action=BooleanOptionalAction,
        )

        parser.cli_argument(
            "--enable-backend-keepalive",
            Union[Unset, None, bool],
            dest="enable_backend_keepalive",
            required=False,
            description="""Use HTTP keepalive connections to servers in the load balancer pool. This is not currently supported.""",
            action=BooleanOptionalAction,
        )

        parser.cli_argument(
            "--server-ids",
            Union[Unset, None, List[int]],
            dest="server_ids",
            required=False,
            description="""A list of server IDs to assign to this load balancer.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return UpdateLoadBalancerResponse

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        name: str,
        algorithm: Union[Unset, None, AlgorithmType] = UNSET,
        forwarding_rules: Union[Unset, None, List[ForwardingRule]] = UNSET,
        health_check: Union[Unset, None, HealthCheck] = UNSET,
        sticky_sessions: Union[Unset, None, StickySessions] = UNSET,
        redirect_http_to_https: Union[Unset, None, bool] = UNSET,
        enable_proxy_protocol: Union[Unset, None, bool] = UNSET,
        enable_backend_keepalive: Union[Unset, None, bool] = UNSET,
        server_ids: Union[Unset, None, List[int]] = UNSET,
    ) -> Union[Any, ProblemDetails, UpdateLoadBalancerResponse, ValidationProblemDetails]:

        page_response = sync_detailed(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=UpdateLoadBalancerRequest(
                name=name,
                algorithm=algorithm,
                forwarding_rules=forwarding_rules,
                health_check=health_check,
                sticky_sessions=sticky_sessions,
                redirect_http_to_https=redirect_http_to_https,
                enable_proxy_protocol=enable_proxy_protocol,
                enable_backend_keepalive=enable_backend_keepalive,
                server_ids=server_ids,
            ),
        )
        return page_response.status_code, page_response.parsed
