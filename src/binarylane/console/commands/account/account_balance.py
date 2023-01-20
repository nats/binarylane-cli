from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.account.account_balance import sync_detailed
from binarylane.models.balance_response import BalanceResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners import CommandRunner


class CommandRequest:
    pass


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "balance"

    @property
    def description(self) -> str:
        return """Fetch Current Balance Information"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return BalanceResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, BalanceResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: BalanceResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
