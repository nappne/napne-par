# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NAPNE IFRN Parnamirim'
copyright = '2025, NAPNE'
author = 'NAPNE'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.mermaid',
]

# MyST parser configuration
myst_enable_extensions = [
    "linkify",
    "colon_fence",
    "deflist",
    "tasklist",
    "html_admonition",
    "html_image",
]

# Support for both .rst and .md files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# Theme options for Furo
html_theme_options = {
    "sidebar_hide_name": False,
}

# BiTeX configuration
bibtex_bibfiles = ['references.bib']
