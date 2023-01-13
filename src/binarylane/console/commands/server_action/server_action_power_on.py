from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_power_on import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.power_on import PowerOn
from binarylane.models.power_on_type import PowerOnType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "power-on"

    @property
    def description(self) -> str:
        return """Power a Server On"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_power-on"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            PowerOnType,
            dest="type",
            required=True,
            description="""None""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: PowerOnType,
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
            json_body=PowerOn(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
