# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from datetime import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CfA Git Users'
now = datetime.now()
author = 'Center for Astrophysics | Harvard & Smithsonian'
copyright = "{}, {}".format(now.year, author)
version = '1.0'
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['requirements.txt']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_title = "CfA Git Users Documentation"
html_static_path = ['_static']
html_css_files = ['css/mod_theme.css']

# -- Options for LaTeX PDF output --------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}