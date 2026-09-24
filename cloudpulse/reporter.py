"""Terminal reporting utilities for CloudPulse."""

from cloudpulse.monitor import HealthResult


def format_result(result: HealthResult) -> str:
    """Convert a health result into a readable terminal line."""

    status_icons = {
        "HEALTHY": "[OK]",
        "DEGRADED": "[WARN]",
        "DOWN": "[DOWN]",
    }

    icon = status_icons.get(result.status, "[?]")
    code = str(result.status_code) if result.status_code is not None else "N/A"

    if result.latency_ms is None:
        latency = "N/A"
    else:
        latency = f"{result.latency_ms:.0f} ms"

    return (
        f"{icon:<7} {result.url:<40} "
        f"HTTP {code:<4} {latency:<10} {result.status}"
    )
