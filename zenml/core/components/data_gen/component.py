from typing import Text, Dict, Any, Optional

from tfx.dsl.components.base.base_component import BaseComponent
from tfx.dsl.components.base.executor_spec import ExecutorClassSpec
from tfx.types import standard_artifacts, Channel
from tfx.types.component_spec import ComponentSpec, ExecutionParameter, \
    ChannelParameter

from zenml.core.components.data_gen.constants import DATA_SPLIT_NAME
from zenml.core.components.data_gen.executor import DataExecutor
from zenml.core.standards.standard_keys import StepKeys


class DataGenSpec(ComponentSpec):
    PARAMETERS = {
        StepKeys.SOURCE: ExecutionParameter(type=Text),
        StepKeys.ARGS: ExecutionParameter(type=Dict[Text, Any]),
    }
    INPUTS = {}
    OUTPUTS = {
        DATA_SPLIT_NAME: ChannelParameter(type=standard_artifacts.Examples)
    }


class DataGen(BaseComponent):
    SPEC_CLASS = DataGenSpec
    EXECUTOR_SPEC = ExecutorClassSpec(DataExecutor)

    def __init__(self,
                 source: Text,
                 source_args: Dict[Text, Any],
                 instance_name: Optional[Text] = None,
                 examples: Optional[ChannelParameter] = None):
        """
        Interface for all DataGen components, the main component responsible
        for reading data and converting to TFRecords. This is how we handle
        versioning data for now.

        Args:
            source:
            source_args:
            schema:
            instance_name:
            examples:
            enable_cache:
        """
        examples = examples or Channel(type=standard_artifacts.Examples)

        # Initiate the spec and create instance
        spec = self.SPEC_CLASS(source=source,
                               args=source_args,
                               examples=examples)

        super(DataGen, self).__init__(spec=spec,
                                      instance_name=instance_name)
