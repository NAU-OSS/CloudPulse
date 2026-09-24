# CloudPulse Roadmap

CloudPulse is a lightweight open-source CLI for checking website and API health, latency, and availability.

This roadmap describes the current direction of the project. Priorities may change as contributors discuss issues, submit pull requests, and identify new use cases.

## Current Foundation — v0.1

CloudPulse currently supports:

- HTTP and HTTPS endpoint checks
- HTTP status reporting
- response latency measurement
- HEALTHY, DEGRADED, and DOWN classifications
- multiple endpoints in a single command
- a summary of service health
- automated unit tests
- GitHub Actions CI across supported Python versions

## Near-Term Goals

Current public issues define the immediate roadmap:

- #1 Validate that `--timeout` is greater than zero
- #2 Make the degraded latency threshold configurable
- #3 Add JSON output for automation and scripting

Additional near-term improvements may include:

- improved network error messages
- stronger edge-case test coverage
- clearer CLI behavior
- improved exit codes for automation

## Future Ideas

Potential future directions include:

- configuration files for groups of endpoints
- repeated monitoring at configurable intervals
- response-history summaries
- API response expectations
- additional machine-readable output formats

These are ideas, not guaranteed features.

## Project Scope

CloudPulse is intended to remain a lightweight terminal-first monitoring tool.

It is not intended to replace full observability platforms.

New features should provide clear value without making the core unnecessarily complex.

## Community Influence

Contributors can influence the roadmap by:

- opening issues
- describing real monitoring problems
- discussing design options
- reviewing pull requests
- submitting focused changes

Major roadmap work should normally be connected to a GitHub issue so design decisions and progress remain visible.
