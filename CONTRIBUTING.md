# Contributing

Contributions are welcome, and they are greatly appreciated!

## Types of Contributions

### Report Bugs

Report bugs in the github issues.

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs.

### Implement Features

Look through the GitHub issues for features.

### Submit Feedback

The best way to send feedback is to file an issue in github issues.

If you are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.

## Get Started

Ready to contribute? Here's how to set up this repo for local development.

1. Fork the repo on GitHub.
2. Clone your fork locally:

    ```bash
    git clone git@github.com:your_name_here/repo_name.git
    ```

3. Create a branch for local development:

    ```bash
    git checkout -b name-of-your-bugfix-or-feature
    ```

   Now you can make your changes locally.

4. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox:

    ```bash
    flake8 repo_name tests
    python setup.py test or pytest
    ```

5. Commit your changes and push your branch to GitHub:

    ```bash
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

6. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated.
3.Put your new functionality into a function with a docstring, and add the feature to the list in README.md.
