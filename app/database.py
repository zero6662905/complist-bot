import json
from typing import Optional


def get_data(file_path: str, components_id: Optional[int] = None) -> list[dict]:
    with open(file_path, "r") as fp:
        data = json.load(fp)

        if components_id != None and components_id<len(data):
            return data[components_id]
        return data