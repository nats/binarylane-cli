from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_reboot import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.reboot import Reboot
from binarylane.models.reboot_type import RebootType
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "reboot"

    @property
    def description(self):
        return """Request a Server Perform a Reboot"""

    def configure(self, parser):
        """Add arguments for server-action_reboot"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=RebootType,
            required=True,
            description="""None""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: RebootType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Reboot(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed