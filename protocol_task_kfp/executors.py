# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


def artifacttaskexecutor(
    task_params: dict,
    task_module: str,
    input_artifact: Input[Artifact],
    output_artifact: Output[Artifact],
):
    from protocol_task.task_executors import ArtifactTaskExecutor

    comp = ArtifactTaskExecutor(
        task_params=task_params,
        task_module=task_module,
        input_artifact=input_artifact,
        output_artifact=output_artifact,
    )
    comp.execute()


def artifacttaskinitexecutor(
    task_params: dict,
    task_module: str,
    output_artifact: Output[Artifact],
):
    from protocol_task.task_executors import ArtifactTaskInitExecutor

    comp = ArtifactTaskInitExecutor(
        task_params=task_params,
        task_module=task_module,
        output_artifact=output_artifact,
    )
    comp.execute()
