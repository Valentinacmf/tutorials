# flake8: noqa
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath("./"))

from fugue import __version__
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = "Fugue Tutorials"
version = __version__
copyright = "2020, Han Wang"  # noqa: A001
author = "Han Wang"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode",
              "sphinx.ext.autodoc", "sphinx_rtd_theme",
              "nbsphinx","sphinx.ext.mathjax"]

nbsphinx_execute = 'never'

nbsphinx_toctree = {
  "maxdepth": 2
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["docs/_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "python"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["venv"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["docs/_static"]
html_logo = "docs/_static/logo_blue.svg"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'style_nav_header_background': '#264263', 
    # "light_css_variables": {
    #     "color-brand-primary": "red",
    #     "color-brand-content": "#CC3333",
    #     "color-admonition-background": "orange",
    # },
    "light_css_variables": {
        "color-brand-primary": "#254262",
        "color-brand-content": "#254262",
        "color-api-highlight-on-target": "#6081a6",
    },
    # always use light theme, taken from Pandera
    # https://github.com/pradyunsg/furo/blob/main/src/furo/assets/styles/variables/_index.scss
    "dark_css_variables": {
        "color-foreground-primary": "black",
        "color-foreground-secondary": "#5a5c63",
        "color-foreground-muted": "#72747e",
        "color-foreground-border": "#878787",
        "color-background-primary": "white",
        "color-background-secondary": "#f8f9fb",
        "color-background-hover": "#efeff4ff",
        "color-background-hover--transparent": "#efeff400",
        "color-background-border": "#eeebee",
        "color-admonition-background": "transparent",
        "color-api-highlight-on-target": "#e5fff5",
    },
}

source_suffix = ['.ipynb']

master_doc = "README"
