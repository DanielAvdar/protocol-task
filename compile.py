from pathlib import Path

from ml_orchestrator import FunctionParser

from protocol_task.task_executors import ArtifactTaskExecutor, ArtifactTaskInitExecutor


def parse_components(file_path: str) -> None:
    parser = FunctionParser()
    comp_list = [
        ArtifactTaskExecutor,
        ArtifactTaskInitExecutor,
    ]
    parser.parse_components_to_file(comp_list, file_path)


if __name__ == "__main__":
    # file_path = Path(__file__).parent / "components.py"
    file_path = Path(__file__).parent / "protocol_task_kfp" / "executors.py"
    parse_components(file_path.as_posix())
