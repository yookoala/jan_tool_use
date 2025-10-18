import json
from pygments import highlight, lexers, formatters

def pretty_print(obj):
    """
    Pretty print a JSON object.
    """
    formatted_json = json.dumps(obj, sort_keys=True, indent=4)
    print(highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter()))
