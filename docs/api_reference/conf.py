import os
import sys

sys.path.insert(0, os.path.abspath("."))


# -- Project information --------
project = "Ragrank"
copyright = "2024, Izam Mohammed"
author = "Izam Mohammed"
release = "0.0.7"


# -- General configuration ---------

extensions = [
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinxext.opengraph",
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_title = "ragrank 🎯"
html_favicon = "./_static/favicon.ico"
html_static_path = ["_static"]
language = "en"

# open graph configuration
ogp_site_url = "https://api-ragrank.readthedocs.io/"
ogp_image = "https://raw.githubusercontent.com/Auto-Playground/ragrank/main/docs/docs/_static/imgs/ragrank_dark.png"
ogp_description_length = 300
ogp_type = "article"

ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
]

ogp_enable_meta_description = True
