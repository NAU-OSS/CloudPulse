# CloudPulse

[![CloudPulse CI](https://github.com/NAU-OSS/CloudPulse/actions/workflows/ci.yml/badge.svg)](https://github.com/NAU-OSS/CloudPulse/actions/workflows/ci.yml)

> A lightweight, open-source command-line tool for checking website and API health, response latency, and availability.

CloudPulse gives developers and system administrators a fast way to inspect the health of multiple HTTP/HTTPS services directly from a terminal.

The project intentionally uses the Python standard library so that new contributors can understand, run, test, and extend the code without installing a large dependency stack.

## Why CloudPulse?

Developers often need a quick answer to a basic operational question: Are my services actually responding?

Large observability platforms provide extensive monitoring, but they can be unnecessary when someone simply wants to check several endpoints from a terminal.

CloudPulse focuses on this smaller problem.

It currently reports:

- HTTP response status
- request latency
- health classification
- multiple endpoints in a single command
- a final service-health summary

## Health Classification

CloudPulse currently uses three states:

- `HEALTHY`: HTTP status below 400 and latency below 1000 ms.
- `DEGRADED`: HTTP 4xx response or latency of at least 1000 ms.
- `DOWN`: HTTP 5xx response, timeout, connection failure, or similar network failure.

These thresholds are intentionally simple in the first release and may become configurable in future versions.

## Requirements

- Python 3.10 or newer recommended
- Internet access when checking remote services

CloudPulse currently has no third-party runtime dependencies.

## Getting Started

Clone this repository and enter the project directory.

    git clone https://github.com/NAU-OSS/CloudPulse.git
    cd CloudPulse

Run CloudPulse against one endpoint:

    python3 -m cloudpulse https://example.com

Check several endpoints together:

    python3 -m cloudpulse https://github.com https://example.com

Change the network timeout:

    python3 -m cloudpulse https://example.com --timeout 2

## Running Tests

CloudPulse uses Python unittest for its automated test suite.

    python3 -m unittest discover -s tests -v

## Project Structure

- `cloudpulse/monitor.py` performs HTTP checks and health classification.
- `cloudpulse/reporter.py` formats monitoring results.
- `cloudpulse/cli.py` provides the command-line interface.
- `cloudpulse/__main__.py` enables `python -m cloudpulse`.
- `tests/` contains automated tests.

## Project Goals

CloudPulse aims to remain useful while also being approachable to people making their first open-source contribution.

Potential future improvements include:

- configurable latency thresholds
- JSON output
- configuration-file support
- repeated monitoring intervals
- response-history tracking
- uptime statistics
- additional automated tests
- improved terminal reporting

Major features should be discussed in GitHub issues before implementation so design decisions remain visible to the community.

## Open Source Philosophy

CloudPulse follows several principles:

1. Keep the core understandable.
2. Prefer useful behavior over unnecessary complexity.
3. Document important technical decisions.
4. Welcome documentation, testing, design, and code contributions.
5. Discuss significant development publicly through issues and pull requests.

## Contributing

Contributions are welcome. A dedicated contribution guide, code of conduct, issue templates, and pull request template are being maintained as part of the project community infrastructure.

## Project Status

CloudPulse is currently an early-stage open-source project. Interfaces and behavior may evolve as contributors propose improvements.

## Maintainer

CloudPulse was started by Paul Revanth Madasu within the Northern Arizona University NAU-OSS organization.

## License

CloudPulse is distributed under the MIT License. See [LICENSE](LICENSE) for details.


## Community and Project Documents

- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Roadmap](ROADMAP.md)
- [Governance](GOVERNANCE.md)
- [License](LICENSE)
