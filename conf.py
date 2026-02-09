project = "reqs-test"

extensions = [
    "sphinxcontrib.plantuml",
    "sphinx_needs",
]

exclude_patterns = [
    "_build",
    ".venv",
    ".venv/**",
    "venv",
    "venv/**",
    "Thumbs.db",
    ".DS_Store",
]

html_theme = "furo"
html_static_path = ["_static"]

# Force light theme (Furo defaults to auto based on user preference).
html_css_files = [
    "force-light.css",
]
html_js_files = [
    "force-light.js",
]


needs_types = [
    {
        "directive": "project",
        "title": "Project",
        "prefix": "P_",  # prefix for auto-generated IDs
        "style": "rectangle", # style for the type in diagrams
        "color": "#BFD8D2", # color for the type in diagrams
    },
    {
        "directive": "reg-req",
        "title": "Regulatory requirement",
        "prefix": "RR_",  # prefix for auto-generated IDs
        "style": "rectangle",
        "color": "#77AB54",
    },
    {
        "directive": "req",
        "title": "Requirement",
        "prefix": "R_",  # prefix for auto-generated IDs
        "style": "rectangle",
        "color": "#F8D7A1",
    },
    {
        "directive": "spec",
        "title": "Specification",
        "prefix": "S_",  # prefix for auto-generated IDs
        "style": "rectangle",
        "color": "#D6EAF8",
    },
]

needs_extra_options = [
    "legislation",
]
