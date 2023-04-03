#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/gnab/remark/wiki
import argparse
import os
import sys
import webbrowser
import tempfile
from os import popen
from jinja2 import Template
from pathlib import Path

DEFAULT_CSS = """   body { font-family: 'Droid Serif'; }
    h1, h2, h3 {
      font-family: 'Yanone Kaffeesatz';
      font-weight: normal;
    }
    .remark-code, .remark-inline-code { font-family: 'Ubuntu Mono'; }

    blockquote {
      font-style: italic;
      font-size: 80%;
      background-color: lightgrey;
    }

    a {
      text-decoration: none;
      font-size: 100%;
    }

    tiny {
      font-family: 'Droid Serif';
      font-size: 10px!important;
    }

    .remark-slide-number {
      font-size: 10pt;
      margin-bottom: -11.6px;
      margin-right: 10px;
      color: #e0e0e0; /* white */
      opacity: 1; /* default: 0.5 */
    }
"""


HTML_TEMPLATE = """<!DOCTYPE html>
<html>
  <head>
    <title>{{title}}</title>
    <meta charset="utf-8">
    <style>
      @import url(https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz);
      @import url(https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic);
      @import url(https://fonts.googleapis.com/css?family=Ubuntu+Mono:400,700,400italic);
      {{css}}
    </style>
  </head>
  <body>
    <textarea id="source">
{{markdown}}
    </textarea>
    <script src="https://remarkjs.com/downloads/remark-latest.min.js">
    </script>
    <script>
    var slideshow = remark.create();
    </script>
  </body>
</html>"""


as_reload = """tell application "Safari"
    activate
    tell window 1
        set presiTab to first tab whose name = "{}"
        if current tab is not presiTab then set current tab to presiTab
        -- tell presiTab to do JavaScript "location.reload();"
        tell application "System Events"
            tell process "Safari"
                keystroke "r" using {{command down}}
            end tell
        end tell
    end tell
end tell
"""

as_tab_is_open = """tell application "Safari"
    activate
    tell window 1
        set presiTab to first tab whose name = "{}"
        if current tab is not presiTab then set current tab to presiTab
    end tell
end tell

presiTab
"""


def show_in_browser(presi_file, tab_name=None):
    if sys.platform == "darwin":
        cmd = "osascript -e '" + as_tab_is_open.format(tab_name) + "'"
        tab_id_str = popen(cmd).read().strip()
        if tab_id_str:
            # reload the tab
            cmd = "osascript -e '" + as_reload.format(tab_name) + "'"
            popen(cmd)
        else:
            webbrowser.get("safari").open_new_tab(f"file://{presi_file}")
    else:
        webbrowser.open_new_tab(presi_file)

def filter_comments_from_source(markdown_str):
    to_be_removed = []
    start_idx = None
    markdown_lines = markdown_str.split("\n")
    for idx, line in enumerate(markdown_lines):
        if line.startswith("<!--"):
            start_idx = idx
        elif start_idx and line.endswith("-->"):
            end_idx = idx
            to_be_removed.append((start_idx, end_idx))
            start_idx = end_idx = None
    for s, e in reversed(to_be_removed):
        del markdown_lines[s : e + 1]
    markdown_str = "\n".join(markdown_lines)

    return markdown_str


def generate_html_slides(markdown_str, out_file):
    title = Path(args.input_file_path).stem.title()
    template = Template(HTML_TEMPLATE)
    presi_html = template.render(css=DEFAULT_CSS, markdown=markdown_str, title=title)

    print(f"Generating {out_file}")
    with open(out_file, "w") as fp:
        fp.write(presi_html)

    return title


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert markdown file to remark.ks presentation.")
    parser.add_argument(
        "--preview", help="Opens/reloads a preview of the presentation in Safari", default=False, action="store_true"
    )
    parser.add_argument("input_file_path", type=Path, help="Path to the input markdown file.")
    parser.add_argument(
        "output_file_path",
        type=Path,
        nargs="?",
        default=tempfile.NamedTemporaryFile(suffix=".html").name,
        help="Path to the created presentation.",
    )
    args = parser.parse_args()

    with open(args.input_file_path) as fp:
        markdown_str = fp.read()

    filter_comments_from_source(markdown_str)
    tab_title = generate_html_slides(markdown_str, args.output_file_path)
    print(tab_title)
    if args.preview:
        show_in_browser(f"file://{os.path.abspath(args.output_file_path)}", tab_title)
