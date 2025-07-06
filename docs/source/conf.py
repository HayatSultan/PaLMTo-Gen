# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# Allow sphinx to discover library path
sys.path.insert(0, os.path.abspath('../palmto_gen'))


project = 'PaLMTo_gen'
copyright = '2025, Hayat Sultan'
author = 'Hayat Sultan'
release = '0.3b3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",   # Auto-generate documentation from docstrings
    "sphinx.ext.viewcode",  # Adds links to source code in doc
    "sphinx.ext.napoleon",  # Support for Google or Numpy style docstring
    "myst_parser",          # Parse markdown files
    
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Source file parsers
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
