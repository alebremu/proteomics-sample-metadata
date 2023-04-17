# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_asciidoc', # Add the asciidoc extension here
]

# Add any other configuration settings you need here

# -- Options for asciidoc output -------------------------------------------

# Set the output format to HTML (default is DocBook)
asciidoc_output_format = 'html'

# Set the path to your adoc files
asciidoc_files = ['README.adoc']

# Add any other asciidoc-specific configuration settings you need here