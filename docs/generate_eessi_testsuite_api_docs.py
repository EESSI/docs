"""
Generate the code reference pages.
Based off https://mkdocstrings.github.io/recipes/#automatic-code-reference-pages
"""

import os

from pathlib import Path

import mkdocs_gen_files

TEST_SUITE = "test-suite/test-suite"
CI = os.getenv('CI')

if not os.path.isdir(TEST_SUITE):
    if CI:
      raise FileNotFoundError(f"Error: {TEST_SUITE} does not exist. Please clone the eessi/test-suite in a test-suite dir.")
    else:
      print(f"Warning: {TEST_SUITE} does not exist. Ignoring this for a non-CI documentation build, but you could clone the eessi/test-suite in a test-suite dir to build the test suite API docs.")

# build a navigation for the menu and a dictionary of navigations for each section
nav = mkdocs_gen_files.Nav()

# Loop through all python files in test-suite/eessi
for path in sorted(Path(f"{TEST_SUITE}/eessi/").rglob("*.py")):
    # Get the relative filename, without .py suffix
    module_path = path.relative_to(TEST_SUITE).with_suffix("")

    # define the corresponding (relative) markdown filename
    doc_path = path.relative_to(TEST_SUITE).with_suffix(".md")

    # Specify the full corresponding markdown filename, including a testsuite_api subdir
    # so that we don't have these API docs scattered in the root of the EESSI docs repo
    full_doc_path = Path("testsuite_api/", doc_path)

    # If something is an __init__, use the directory name as the name of the python module instead of the filename
    parts = list(module_path.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    # Skip the __main__, if there is one. This is not part of the API
    elif parts[-1] == "__main__":
        continue

    # Add an entry for this module to the navigation
    nav[parts] = doc_path.as_posix()

    # Create the markdown file
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        # identifier is something like eessi.foo.bar
        identifier = ".".join(parts)
        fd.write(f"::: {identifier}")

    # This maps the generated .md file to the source .py, so that you can have an "Edit on GitHub" button
    # that links to the Python code
    mkdocs_gen_files.set_edit_path(full_doc_path, path)

    # Create the api/summary.md file and write the full navigation tree into it so it can be used as a site sidebar
with mkdocs_gen_files.open("testsuite_api/summary.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
