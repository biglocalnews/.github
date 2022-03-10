import csv

import jinja2
import requests


loader = jinja2.FileSystemLoader(searchpath="./templates/")
env = jinja2.Environment(loader=loader)


def main():
    """
    Update profile/README.md with the latest data.
    """
    # Download the latest bylines

    # Read in the data
    byline_list = []

    # Render the template
    template = env.get_template("README.md")
    md = template.render(byline_list=byline_list)

    # Write out the README
    with open("./profile/README.md", "w") as fh:
        fh.write(md)


if __name__ == "__main__":
    main()
