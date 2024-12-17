# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NFL Analysis'
copyright = '2024, Sedona Dettwiler and Ethan Beckstead'
author = 'Sedona Dettwiler and Ethan Beckstead'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              'myst_parser',
              'sphinx.ext.githubpages']

templates_path = ['myst_parser']
source_suffix = {'.rst': 'restructuredtext',
'.md': 'markdown',
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
