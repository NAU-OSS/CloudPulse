# Contributing to CloudPulse

Thank you for your interest in contributing to CloudPulse.

CloudPulse is an open-source command-line service health monitor. Contributions are welcome from developers, students, technical writers, testers, and anyone interested in improving lightweight service monitoring.

## Ways to Contribute

You can contribute by:

- reporting bugs
- suggesting new features
- improving documentation
- adding or improving tests
- improving terminal output
- improving error handling
- proposing monitoring features
- reviewing pull requests

Small contributions are welcome. You do not need to implement a major feature to participate.

## Before You Start

Before beginning a significant change:

1. Search existing GitHub issues to see whether the topic has already been discussed.
2. Open a new issue if no relevant discussion exists.
3. Explain the problem or proposed improvement clearly.
4. Wait for discussion when the change affects major project behavior or architecture.

Small documentation fixes and minor corrections may be submitted directly as pull requests.

## Development Setup

CloudPulse requires Python 3.10 or newer.

Clone the repository:

    git clone https://github.com/NAU-OSS/CloudPulse.git
    cd CloudPulse

Create a virtual environment if desired:

    python3 -m venv .venv
    source .venv/bin/activate

Install the project in editable mode:

    python3 -m pip install -e .

Verify the CLI:

    cloudpulse https://example.com

You can also run CloudPulse without installing it:

    python3 -m cloudpulse https://example.com

## Running Tests

Run the complete test suite before submitting a pull request:

    python3 -m unittest discover -s tests -v

A contribution should not intentionally break existing tests.

New behavior should include tests when practical.

## Branches

Create a focused branch for your work instead of developing directly on `main`.

Examples:

    git switch -c feature/config-file
    git switch -c fix/timeout-handling
    git switch -c docs/improve-readme

Keep each branch focused on one logical change.

## Commit Messages

Use short, descriptive commit messages that explain the purpose of the change.

Examples:

    Add configurable latency threshold
    Improve timeout error reporting
    Document local development setup
    Add tests for degraded responses

Avoid vague messages such as `update`, `changes`, or `fix stuff`.

## Pull Requests

A good pull request should:

- describe what changed
- explain why the change is useful
- reference a related issue when applicable
- remain focused on one problem
- include tests for new behavior when practical
- update documentation when behavior changes
- pass the existing test suite

Reviewers may request changes before a pull request is merged. Code review is intended to improve both the contribution and the project.

## Reporting Bugs

When reporting a bug, include as much useful information as possible:

- CloudPulse version or commit
- Python version
- operating system
- command that produced the problem
- expected behavior
- actual behavior
- relevant error output
- steps needed to reproduce the issue

Do not include passwords, API keys, authentication tokens, or other sensitive information.

## Feature Requests

Feature requests should explain the problem being solved rather than only proposing an implementation.

Useful feature requests describe:

- the use case
- current limitation
- expected behavior
- possible alternatives
- examples when appropriate

## Project Design Principles

Contributions should generally support CloudPulse's core goals:

1. Keep the command-line experience simple.
2. Keep the core implementation understandable.
3. Prefer Python standard-library functionality when reasonable.
4. Provide useful failure messages.
5. Keep monitoring behavior predictable and testable.
6. Avoid unnecessary complexity.
7. Document important behavior and design decisions.

These are guidelines rather than absolute rules. Contributors may propose changes to them through GitHub issues.

## Community Expectations

Be respectful and constructive when participating in issues, pull requests, and reviews.

Technical disagreement is welcome. Personal attacks, harassment, and discriminatory behavior are not.

All participants are expected to follow the project's Code of Conduct.

## Security Issues

Please do not publicly disclose a vulnerability before maintainers have had an opportunity to review it.

Security reporting instructions are documented in `SECURITY.md`.

## Questions

If you are unsure whether an idea belongs in CloudPulse, open a GitHub issue and start a discussion.

Contributing to an open-source project includes more than writing code. Thoughtful questions, documentation improvements, testing, issue reports, and reviews are all valuable contributions.

## Code Style and Formatting

CloudPulse is written in Python and aims to keep the codebase simple and readable.

When contributing code:

- follow standard Python conventions and PEP 8 where practical
- use four spaces for indentation
- choose clear and descriptive names for functions, variables, and modules
- keep functions focused on a single responsibility
- avoid unnecessary dependencies and complexity
- add comments when they explain reasoning that is not obvious from the code
- keep changes focused on the issue or feature being addressed
- preserve compatibility with the Python versions tested by the project

Before submitting a pull request, contributors should run the complete test suite and verify that the command-line interface still works as expected.

## Documentation Standards

Documentation is considered an important part of CloudPulse.

Contributors should:

- update the README when user-facing behavior, installation, or usage changes
- document new command-line options and provide examples when appropriate
- keep documentation clear, concise, and consistent with the actual behavior of the project
- update tests and related documentation when behavior changes
- use Markdown for project documentation
- link to related issues or pull requests when useful for understanding a change

Documentation-only contributions are welcome and should follow the same review process as code changes.
