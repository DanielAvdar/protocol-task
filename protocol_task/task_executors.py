from dataclasses import dataclass
from typing import Union

from ml_orchestrator.artifacts import Artifact, Input, Output

from protocol_task.protocol_class import ProtocolTask, ProtocolTaskInit


@dataclass
class TaskExecutorMeta:
    """
    task_params: json serializable dictionary
    task_module: str - module path to the task class. for example: 'protocol_task_example.tasks.MyTaskClass'
    """

    task_params: dict
    task_module: str

    @staticmethod
    def _fetch_module_component(module_path) -> type(Union[ProtocolTask, ProtocolTaskInit]):
        components = module_path.split(".")
        mod = __import__(components[0])
        if len(components) == 1:
            return mod
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    @property
    def task_instance(
        self,
    ) -> Union[ProtocolTask, ProtocolTaskInit]:
        """
        Load the task module.
        """
        task_class = self._fetch_module_component(self.task_module)
        task_instance = task_class(**self.task_params)
        return task_instance


@dataclass
class ArtifactTaskExecutor(TaskExecutorMeta):
    input_artifact: Input[Artifact]
    output_artifact: Output[Artifact]

    def execute(
        self,
    ) -> None:
        tp: ProtocolTask = self.task_instance
        input_artifact = tp.load_artifact(self.input_artifact.path)
        output_artifact = tp.execute_task(input_artifact)
        tp.save_artifact(output_artifact, self.output_artifact.path)


@dataclass
class ArtifactTaskInitExecutor(TaskExecutorMeta):
    output_artifact: Output[Artifact]

    def execute(
        self,
    ) -> None:
        tp: ProtocolTaskInit = self.task_instance
        output_artifact = tp.execute_task()
        tp.save_artifact(output_artifact, self.output_artifact.path)
