from glob import glob
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


notebook_list = glob("./*.ipynb")
ep = ExecutePreprocessor()

for notebook in notebook_list:
    with open(notebook) as notebook_file:
        nb = nbformat.read(notebook_file, as_version=4)
        ep.preprocess(nb)