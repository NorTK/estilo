# Configuration file for the Sphinx documentation builder.
# Guía de Estilo de Documentación para NorTK
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Guía de Estilo de Documentación para NorTK'
copyright = '2026, NorTK: Infraestructura Crítica y Soberanía Digital'
author = 'NorTK'

version = '0.1.0'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# Activar bloques todo para desarrollo
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/logo.svg'
html_css_files = [
    'css/nortk.css',
]

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
    'style_external_links': True,
}

html_show_sourcelink = False
html_copy_source = False
