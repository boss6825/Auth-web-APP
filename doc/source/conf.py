# -*- coding: utf-8 -*-
#
# Authomatic documentation build configuration file, created by
# sphinx-quickstart on Thu Feb  7 16:09:00 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import datetime
import pkg_resources

# # If extensions (or modules to document with autodoc) are in another directory,
# # add these directories to sys.path here. If the directory is relative to the
# # documentation root, use os.path.abspath to make it absolute, like shown here.

# # pymodules = sys.path.index('/usr/lib/pymodules/python2.7')
# #
# # sys.path.pop(pymodules)

# import google


# GOOGLE_PATH = os.path.split(google.__file__)[0]
# GAE_SDK_PATH = os.path.join(GOOGLE_PATH, '..')
# GAE_SDK_LIB_PATH = os.path.join(GAE_SDK_PATH, 'lib')

# sys.path[0:0] = [
#     os.path.abspath('.'),
#     os.path.abspath('../../'),
#     os.path.abspath('_themes/foundation-sphinx-theme'),
#     os.path.join(GAE_SDK_LIB_PATH, 'webapp2-2.5.2'),
#     os.path.join(GAE_SDK_LIB_PATH, 'yaml-3.10'),
# ]

rst_prolog = """

.. |django| replace:: Django
.. _django: http://djangoproject.org/

.. |pyramid| replace:: Pyramid
.. _pyramid: http://www.pylonsproject.org/

.. |webob| replace:: WebOb
.. _webob: http://webob.org/

.. |werkzeug| replace:: Werkzeug
.. _werkzeug: http://werkzeug.pocoo.org/

.. |flask| replace:: Flask
.. _flask: http://flask.pocoo.org/

.. |gae| replace:: Google App Engine
.. _gae: https://developers.google.com/appengine/

.. |webapp2| replace:: Webapp2
.. _webapp2: http://webapp-improved.appspot.com/

.. |oauth2| replace:: OAuth 2.0
.. _oauth2: http://oauth.net/2/

.. |oauth1| replace:: OAuth 1.0a
.. _oauth1: http://oauth.net/core/1.0a/

.. |openid| replace:: OpenID
.. _openid: http://openid.net/

.. |gae_users_api| replace:: Google App Engine Users API
.. _gae_users_api: https://developers.google.com/appengine/docs/python/users/

.. |jquery| replace:: jQuery
.. _jquery: http://jquery.com/

.. |pyopenid| replace:: python-openid
.. _pyopenid:
.. _python-openid: http://pypi.python.org/pypi/python-openid/

.. |classmethod| replace:: Must be a classmethod!

.. |async| replace:: The internal implementation of the future pattern is quite naive. Use with caution!

.. |provider-class| replace:: provider class
.. _provider-class: providers


.. |no-csrf| replace:: This provider doesn't support CSRF protection!

"""

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "foundation_sphinx_theme",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Authomatic"
this_year = datetime.date.today().year
copyright = u"2013-{0}, Peter Hudec and the Authomatic Project Community".format(
    this_year
)

# TODO: Put version in one place.

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pkg_resources.get_distribution("Authomatic").version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["examples/twitter-localhost.rst", "examples/**/authomatic/**/*"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "monokai"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = "foundation"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

MOTTO = u"""
<span>Authomatic</span><br />
is a <em>framework agnostic</em> library<br />
for <em>Python</em> web applications<br />
with a <em>minimalistic</em> but <em>powerful</em> interface<br />
which simplifies <em>authentication</em> of users<br />
by third party providers like <em>Facebook</em> or <em>Twitter</em><br />
through standards like <em>OAuth</em> and <em>OpenID</em>.
"""

html_theme_options = {
    "logo_screen": "img/authomatic.svg",
    "stylesheet": "css/authomatic.css",
    "favicon": "img/favicon.ico",
    "motto": MOTTO,
    "seo_description": (
        "Simple yet powerful authorization / authentication "
        "client library for Python WEB applications."
    ),
    "base_url": "https://authomatic.github.io/authomatic",
    "opengraph_image": "img/authomatic-seo.gif",
    "google_analytics_id": "UA-40554445-4",
    "social_buttons": True,
    "facebook_app_id": "249464911861131",
    "twitter_id": "AuthomaticPy",
    "author": "Peter Hudec",
    "author_link": "https://peterhudec.com",
    "copyright_year": "2014",
    "google_plus_id": "117034840853387702598",
    "github_user": "authomatic",
    "github_repo": "authomatic",
    "github_ribbon_image": "img/github-ribbon-right.png",
    "flattr_id": "peterhudec",
}

intersphinx_mapping = {
    "flask": ("http://flask.pocoo.org/docs/", None),
    "python": ("https://docs.python.org/2.7", None),
    "django": (
        "https://docs.djangoproject.com/en/dev/",
        "https://docs.djangoproject.com/en/dev/_objects/",
    ),
    "webapp2": ("https://webapp2.readthedocs.io/en/latest/", None),
    "werkzeug": ("http://werkzeug.pocoo.org/docs/", None),
    "pyramid": ("https://docs.pylonsproject.org/en/latest/", None),
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ["_themes/foundation-sphinx-theme"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Authomatic {0}".format(version)

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "Authomaticdoc"

autodoc_member_order = "bysource"
autoclass_content = "both"

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "Authomatic.tex",
        u"Authomatic Documentation",
        "Peter Hudec et al",
        "manual",
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then top-level headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        "index",
        "authomatic",
        u"Authomatic Documentation",
        [u"Peter Hudec", u"Authomatic Project Community"],
        1,
    )
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Authomatic",
        u"Authomatic Documentation",
        u"Peter Hudec",
        "Authomatic",
        "One line description of project.",
        "Miscellaneous",
    )
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'
