from typing import Any, Dict, List, Union

from ...client.api.image.image_list import sync_detailed
from ...client.client import Client
from ...client.models.image_query_type import ImageQueryType
from ...client.models.images_response import ImagesResponse
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "type",
            "public",
            "min_disk_size",
            "size_gigabytes",
            "status",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this image.""",
            "name": """The name of this image.""",
            "type": """
| Value | Description |
| ----- | ----------- |
| custom | An image uploaded by a user. |
| snapshot | A snapshot. Snapshot creation is not currently supported so only distribution images will have this value. |
| backup | A backup of a server. |

""",
            "public": """A public image is available to all users. A private image is available only to the account that created the image.""",
            "regions": """The slugs of the regions where the image is available for use.""",
            "min_disk_size": """For a distribution image this is the minimum disk size in GB required to install the operating system. For a backup image this is the minimum total disk size in GB required to restore the backup.""",
            "size_gigabytes": """For a distribution image this is the disk size used in GB by the operating system on initial install. For a backup image this is the size of the compressed backup image in GB.""",
            "tags": """Tags are not currently supported and this will always be an empty array.""",
            "status": """
| Value | Description |
| ----- | ----------- |
| NEW | The image is new. |
| available | The image is available for use. |
| pending | The image is pending and is not yet available for use. |
| deleted | The image has been deleted and is no longer available for use. |

""",
            "distribution_info": """""",
            "distribution": """If this is an operating system image, this is the name of the distribution. If this is a backup image, this is the name of the distribution the server is using.""",
            "full_name": """If this is an operating system image, this is the name and version of the distribution. If this is a backup image, this is the name and version of the distribution the server is using.""",
            "slug": """If this is an operating system image this is a slug which may be used as an alternative to the ID as a reference.""",
            "created_at": """If this is a backup image this is the date and time in ISO8601 format when the image was created.""",
            "description": """A description that may provide further details or warnings about the image.""",
            "error_message": """If the image creation failed this may provide further information.""",
            "min_memory_megabytes": """This is minimum memory in MB necessary to support this operating system (or the base operating system for a backup image).""",
            "distribution_surcharges": """""",
            "backup_info": """""",
        }

    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List All Images"""

    def configure(self, parser):
        """Add arguments for image_list"""

        parser.cli_argument(
            "--type",
            dest="type",
            type=Union[Unset, None, ImageQueryType],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| distribution | Base operating system images. |
| application | Operating system images that include pre-installed applications. This option is not currently supported, operating system images with pre-installed applications are listed under 'distribution'. |
| backup | A backup image of a server. |

""",
        )
        parser.cli_argument(
            "--private",
            dest="private",
            type=Union[Unset, None, bool],
            required=False,
            description="""None""",
        )
        parser.cli_argument(
            "--tag-name",
            dest="tag_name",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        client: Client,
        type: Union[Unset, None, ImageQueryType] = UNSET,
        private: Union[Unset, None, bool] = UNSET,
        tag_name: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, ImagesResponse, ValidationProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: ImagesResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                type=type,
                private=private,
                tag_name=tag_name,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.images += page_response.parsed.images

        return response
