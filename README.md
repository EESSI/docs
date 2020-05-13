## Documentation for the European Environment for Scientific Software Installations (EESSI)

Welcome to the repository that hosts the **[EESSI](https://github.com/EESSI)** documentation, see https://eessi.github.io/docs.

## Basic info

* contents are located in ``docs/`` subdirectory

* [Markdown](https://daringfireball.net/projects/markdown) is used as syntax


## Getting started

This documentation is rendered via [MkDocs](https://www.mkdocs.org/),
which makes it very easy to preview the result of the changes you make locally.

* First, install ``mkdocs``:

        pip install mkdocs-material mkdocs-git-revision-date-localized-plugin

* Build the documentation:

        make

  or:

        mkdocs build

* Test the documentation (make sure there are no issues):

        make test

  or:

        mkdocs build --strict

* Start the MkDocs built-in dev-server to preview the documentation as you work on it:

        make preview

  or:

        mkdocs serve

  Visit http://127.0.0.1:8000 to see the local live preview of the changes you make.

* If you prefer building a static preview you can use ``make``,
  which should result in a ``site/`` subdirectory that contains the rendered documentation.


## Automatic updates

The rendered version of this documentation at https://eessi.github.io/docs
is automatically updated on every push to the ``master`` branch,
thanks to the GitHub Actions workflow defined in
[``.github/workflows/deploy.yml``](https://github.com/EESSI/docs/blob/master/.github/workflows/deploy.yml).

The [``gh-pages``](https://github.com/EESSI/docs/tree/gh-pages) branch in this repository contains the rendered version.

https://eessi.github.io/docs will only be updated if the tests pass,
see GitHub Actions workflow defined in
[``.github.workflows/test.yml``](https://github.com/EESSI/docs/blob/master/.github/workflows/test.yml).

**Note**: **do *not* change the files in the ``gh-pages`` branch directly!**

All your changes will be lost the next time the ``master`` branch is updated...
