# -*- coding: utf-8 -*-

# Shared options for our test configuration
extensions = [
    'restructuredWeb',
    # 'restructuredWeb.configuration_block',
    # 'restructuredWeb.javascript',
    # 'restructuredWeb.css',
    # 'restructuredWeb.twitter',
    # 'restructuredWeb.youtube',
]

# We override layout.html to a blank page for testing
templates_path = ['_templates']

# Configuration Block option
highlight_language = 'default'

# Configuration Block option
config_block = {
    # http://pygments.org/docs/lexers/#lexers-for-python-and-related-languages
    'shell': 'Shell',
}

# For 1.4
html_use_smartypants = False

# Configuration block option - default highlight language
# highlight_language = 'default'

# ┌───────────────────────────────────────────────────────────────────────────┐
# │ Codepen                                                                   │
# └───────────────────────────────────────────────────────────────────────────┘
codepen_theme = 'dark'

# ┌───────────────────────────────────────────────────────────────────────────┐
# │ Google Adsense Config                                                     │
# └───────────────────────────────────────────────────────────────────────────┘

# Adsense config
adsense_client_id = 'ca-pub-XXXXXXXXXXX'

# Named Slots
adsense_slots = {
    'blog-footer': '123456789',
    'post-inline': '987654321',
    'sidebar-skyscraper': '111111111',
}

# Add a default slot if no argument is passed
adsense_default_slot = 'post-inline'
