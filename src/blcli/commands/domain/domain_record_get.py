from typing import Any, Type, Union

from ...client.api.domain.domain_record_get import sync_detailed
from ...client.client import Client
from ...client.models.domain_record_response import DomainRecordResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Existing Domain Record"""

    def configure(self, parser):
        """Add arguments for domain_record_get"""
        parser.cli_argument(
            "domain_name",
            type=str,
            description="""The domain name for which the record should be fetched.""",
        )
        parser.cli_argument(
            "record_id",
            type=int,
            description="""The ID of the record to fetch.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return DomainRecordResponse

    def request(
        self,
        domain_name: str,
        record_id: int,
        client: Client,
    ) -> Union[Any, DomainRecordResponse, ProblemDetails]:

        page_response = sync_detailed(
            domain_name=domain_name,
            record_id=record_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
