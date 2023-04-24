from jnb2py import Converter

file_name = "example_test.py"
output_path = ""
converter = Converter("notebooks/temp.ipynb")

converter.convert_to_py(file_name, output_path)

