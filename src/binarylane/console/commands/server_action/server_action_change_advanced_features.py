from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.server_action.server_action_change_advanced_features import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.advanced_feature import AdvancedFeature
from binarylane.models.change_advanced_features import ChangeAdvancedFeatures
from binarylane.models.change_advanced_features_type import ChangeAdvancedFeaturesType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.video_device import VideoDevice
from binarylane.models.vm_machine_type import VmMachineType
from binarylane.types import UNSET, Unset

from binarylane.console import cli
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-advanced-features"

    @property
    def description(self):
        return """Change the Advanced Features of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-advanced-features"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeAdvancedFeaturesType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled-advanced-features",
            dest="enabled_advanced_features",
            type=Union[Unset, None, List[AdvancedFeature]],
            required=False,
            description="""Do not provide or set to null to keep existing advanced features. Provide an empty array to disable all advanced features, otherwise provide an array with selected advanced features. If provided, any currently enabled advanced features that aren't included will be disabled.""",
        )

        parser.cli_argument(
            "--processor-model",
            dest="processor_model",
            type=Union[Unset, None, str],
            required=False,
            description="""Do not provide or set to null to keep existing processor model.""",
        )

        parser.cli_argument(
            "--automatic-processor-model",
            dest="automatic_processor_model",
            type=Union[Unset, None, bool],
            required=False,
            description="""Set to true to use best available processor model. If this is provided the processor_model property must not be provided.""",
            action=cli.BooleanOptionalAction,
        )

        parser.cli_argument(
            "--machine-type",
            dest="machine_type",
            type=Union[Unset, None, VmMachineType],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| pc_i440_fx_1_point_5 | PC I440 FX 1.5 |
| pc_i440_fx_2_point_11 | PC I440 FX 2.11 |
| pc_i440_fx_4point_1 | PC I440 FX 4.1 |
| pc_i440_fx_4point_2 | PC I440 FX 4.2 |
| pc_i440_fx_5point_0 | PC I440 FX 5.0 |
| pc_i440_fx_5point_1 | PC I440 FX 5.1 |

""",
        )

        parser.cli_argument(
            "--automatic-machine-type",
            dest="automatic_machine_type",
            type=Union[Unset, None, bool],
            required=False,
            description="""Set to true to use best available machine type. If this is provided the machine_type property must not be provided.""",
            action=cli.BooleanOptionalAction,
        )

        parser.cli_argument(
            "--video-device",
            dest="video_device",
            type=Union[Unset, None, VideoDevice],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| cirrus-logic | Cirrus Logic GD5446 |
| standard | Standard VGA with VESA 2.0 extensions |
| virtio | Virtio VGA (800x600) |
| virtio-wide | Virtio VGA (1600x900) |

""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeAdvancedFeaturesType,
        enabled_advanced_features: Union[Unset, None, List[AdvancedFeature]] = UNSET,
        processor_model: Union[Unset, None, str] = UNSET,
        automatic_processor_model: Union[Unset, None, bool] = UNSET,
        machine_type: Union[Unset, None, VmMachineType] = UNSET,
        automatic_machine_type: Union[Unset, None, bool] = UNSET,
        video_device: Union[Unset, None, VideoDevice] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeAdvancedFeatures(
                type=type,
                enabled_advanced_features=enabled_advanced_features,
                processor_model=processor_model,
                automatic_processor_model=automatic_processor_model,
                machine_type=machine_type,
                automatic_machine_type=automatic_machine_type,
                video_device=video_device,
            ),
        )
        return page_response.status_code, page_response.parsed