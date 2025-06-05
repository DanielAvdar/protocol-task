import json
from dataclasses import dataclass
from typing import Dict

from protocol_task.protocol_class import ProtocolTask as ProtocolTask, ProtocolTaskInit as ProtocolTaskInit


@dataclass
class MyTaskClassInit:  # type: ProtocolTaskInit
    """
    This is an example task class that implements the ProtocolTask class.
    """

    task_param1: str
    task_param2: int

    def execute_task(
        self,
    ) -> Dict:
        return dict(task_param1=self.task_param1, task_param2=self.task_param2)

    def save_artifact(self, artifact: Dict, path: str) -> None:
        with open(path, "w") as f:
            json.dump(artifact, f)


@dataclass
class MyTaskClass(MyTaskClassInit):  # type: ProtocolTask
    task_param3: str

    def execute_task(self, artifact: Dict) -> Dict:
        artifact["task_param3"] = self.task_param3
        return artifact

    def load_artifact(self, path: str) -> Dict:
        with open(path, "r") as f:
            return json.load(f)
