from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_change_partner import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_partner import ChangePartner
from binarylane.models.change_partner_type import ChangePartnerType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-partner"

    @property
    def description(self) -> str:
        return """Add, Update or Remove a Partner Server for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_change-partner"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangePartnerType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--partner-server-id",
            Union[Unset, None, int],
            dest="partner_server_id",
            required=False,
            description="""Leave this null to remove the server partnership. The partner server must be in the same region as the target server.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangePartnerType,
        partner_server_id: Union[Unset, None, int] = UNSET,
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
            json_body=ChangePartner(
                type=type,
                partner_server_id=partner_server_id,
            ),
        )
        return page_response.status_code, page_response.parsed
