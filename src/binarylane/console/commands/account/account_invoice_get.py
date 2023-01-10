from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.account.account_invoice_get import sync_detailed
from binarylane.client import Client
from binarylane.models.invoice_response import InvoiceResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Invoice"""

    def configure(self, parser):
        """Add arguments for account_invoice_get"""
        parser.cli_argument(
            "invoice_id",
            int,
            description="""The ID of the invoice to fetch.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return InvoiceResponse

    def request(
        self,
        invoice_id: int,
        client: Client,
    ) -> Union[Any, InvoiceResponse, ProblemDetails]:

        page_response = sync_detailed(
            invoice_id=invoice_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
