import os


def write_to_a_file(content: str, file_name: str, dest_path: str) -> None:
    with open(os.path.join(dest_path, file_name), "w") as f_obj:
        f_obj.write(content)
