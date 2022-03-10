import csv
import os
from urllib.parse import urlparse

import jinja2
import requests


loader = jinja2.FileSystemLoader(searchpath="./templates/")
env = jinja2.Environment(loader=loader)


def main():
    """
    Update profile/README.md with the latest data.
    """
    # Download the latest bylines
    r = requests.get("https://raw.githubusercontent.com/biglocalnews/bylines/main/bylines.csv")
    with open("bylines.csv", 'w') as fh:
        fh.write(r.text)

    # Read in the data
    byline_list = list(csv.DictReader(open("./bylines.csv", 'r')))

    # Parse the domains
    for by in byline_list:
        u = urlparse(by['url']).netloc
        by['domain'] = ".".join(u.split(".")[-2:])

    # Render the template
    template = env.get_template("README.md")
    md = template.render(byline_list=byline_list)

    # Write out the README
    with open("./profile/README.md", "w") as fh:
        fh.write(md)

    os.unlink("bylines.csv")


if __name__ == "__main__":
    main()
