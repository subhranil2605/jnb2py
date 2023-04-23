import os
import json
from typing import AnyStr, Dict, Any, List

from models.cell_model import Cell
from utils import write_to_a_file

NEW_LINE_CHARACTER = "\n"


class Converter:
    def __init__(self, nb_file_path: str) -> None:
        self.nb_file_path: str = nb_file_path

    def convert_to_py(self, file_name: str, dest_path: str) -> None:
        """ h """

        try:
            # all the cells from the notebook
            cells = self._parse_notebook().get("cells")

            # convert all the cells into Cell object
            all_cells: List[Cell] = [Cell(**cell) for cell in cells]

            code = ""
            for cell in all_cells:
                if cell.cell_type == "code":
                    for source_line in cell.source:
                        if not source_line.endswith(NEW_LINE_CHARACTER):
                            code += source_line + NEW_LINE_CHARACTER
                        else:
                            code += source_line

            write_to_a_file(content=code, file_name=file_name, dest_path=dest_path)

        except Exception as e:
            print(str(e))

    def _parse_notebook(self) -> Dict[str, Any]:

        try:
            # getting the notebook data, which is in JSON format
            notebook_data: AnyStr = self._get_data_from_notebook()

            # parse JSON string to dictionary
            notebook_dict: Dict[str, Any] = json.loads(notebook_data)

            return notebook_dict

        except Exception as e:
            print(str(e))

    def _get_data_from_notebook(self) -> AnyStr:

        try:
            with open(self.nb_file_path, "r") as f_obj:
                data: AnyStr = f_obj.read()
            return data

        except Exception as e:
            print(str(e))