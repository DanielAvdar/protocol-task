from typing import (
    Any,
    Protocol,
)


class ProtocolTask(Protocol):
    """
    The execution flow of a task is as follows:
    1. Load an artifact from a path.
    2. Execute the task on the artifact.
    3. Save the artifact to a path.
    for example:
    p_task=ProtocolTask(**params)
    input_artifact = p_task.load_artifact(input_path)
    output_artifact = p_task.execute_task(input_artifact)
    p_task.save_artifact(output_artifact, output_path)
    """

    def load_artifact(self, path: str) -> Any: ...
    def execute_task(self, artifact: Any) -> Any: ...
    def save_artifact(self, artifact: Any, path: str) -> None: ...


class ProtocolTaskInit(Protocol):
    """
    The execution flow of a task is as follows:
    1. Load an artifact from a path.
    2. Execute the task on the artifact.
    3. Save the artifact to a path.
    for example:
    p_task=ProtocolTask(**params)
    input_artifact = p_task.load_artifact(input_path)
    output_artifact = p_task.execute_task(input_artifact)
    p_task.save_artifact(output_artifact, output_path)
    """

    def execute_task(
        self,
    ) -> Any: ...
    def save_artifact(self, artifact: Any, path: str) -> None: ...
