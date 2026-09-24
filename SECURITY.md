# Security Policy

## Supported Versions

CloudPulse is currently in early development. Security fixes are applied to the latest version of the main branch.

| Version | Supported |
| --- | --- |
| 0.1.x | Yes |
| Older versions | No |

## Reporting a Vulnerability

Please do not publish suspected security vulnerabilities in a public GitHub issue.

Instead, contact the project maintainer privately with:

- a description of the vulnerability
- steps required to reproduce it
- the potential impact
- affected CloudPulse version or commit
- any suggested mitigation, if known

Please avoid including passwords, API keys, authentication tokens, or other sensitive credentials in reports.

## Response Process

After receiving a report, the maintainer will attempt to reproduce and evaluate the issue before discussing a fix or disclosure.

Confirmed vulnerabilities should be addressed before detailed public disclosure whenever practical.

## Security Considerations

CloudPulse sends HTTP or HTTPS requests to endpoints supplied by the user. Contributors should carefully consider URL handling, network failures, redirects, timeouts, and the accidental exposure of sensitive information when proposing new monitoring features.
