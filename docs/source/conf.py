# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Zetabot'
# copyright = '2021, Graziella'
author = 'Zetabank'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_id': 'UA-17821189-2',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
}

def setup(app):
    app.add_stylesheet("css/toc_custom.css")
# -- Referencing
numfig = True

# -- Options for EPUB output
epub_show_urls = 'footnote'
