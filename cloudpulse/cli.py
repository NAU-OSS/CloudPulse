"""Command-line interface for CloudPulse."""

import argparse

from cloudpulse.monitor import check_service
from cloudpulse.reporter import format_result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cloudpulse",
        description="Monitor website and API health from your terminal.",
    )

    parser.add_argument(
        "urls",
        nargs="+",
        help="One or more websites or API endpoints to monitor.",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Request timeout in seconds (default: 5).",
    )

    return parser


def main() -> None:
    args = build_parser().parse_args()

    print()
    print("CloudPulse Service Health Report")
    print("=" * 78)

    healthy = 0
    degraded = 0
    down = 0

    for url in args.urls:
        result = check_service(url, timeout=args.timeout)
        print(format_result(result))

        if result.status == "HEALTHY":
            healthy += 1
        elif result.status == "DEGRADED":
            degraded += 1
        else:
            down += 1

    print("=" * 78)
    print(
        f"Summary: {healthy} healthy | "
        f"{degraded} degraded | {down} down"
    )


if __name__ == "__main__":
    main()
