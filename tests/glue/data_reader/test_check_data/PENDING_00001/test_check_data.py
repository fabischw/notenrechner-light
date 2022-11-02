
import unittest
import pathlib
import importlib.util
import sys


here = pathlib.Path(__file__).parent


project = here.parent.parent.parent.parent.parent#project folder
glue_layer = project / "glue"# /glue

targetfile = glue_layer / "data_reader.py"# ** file which contains the targetfunction





