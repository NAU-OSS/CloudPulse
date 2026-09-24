"""Core monitoring functionality for CloudPulse."""

from dataclasses import dataclass
from time import perf_counter
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


@dataclass
class HealthResult:
    """Represents the result of a service health check."""

    url: str
    status_code: int | None
    latency_ms: float | None
    status: str
    error: str | None = None


def classify_health(status_code: int, latency_ms: float) -> str:
    """Classify a service as healthy, degraded, or down."""

    if status_code >= 500:
        return "DOWN"

    if status_code >= 400 or latency_ms >= 1000:
        return "DEGRADED"

    return "HEALTHY"


def check_service(url: str, timeout: float = 5.0) -> HealthResult:
    """Check one HTTP/HTTPS service and measure its response time."""

    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    request = Request(
        url,
        headers={"User-Agent": "CloudPulse/0.1"},
        method="GET",
    )

    started = perf_counter()

    try:
        with urlopen(request, timeout=timeout) as response:
            latency_ms = (perf_counter() - started) * 1000
            status_code = response.getcode()

            return HealthResult(
                url=url,
                status_code=status_code,
                latency_ms=latency_ms,
                status=classify_health(status_code, latency_ms),
            )

    except HTTPError as exc:
        latency_ms = (perf_counter() - started) * 1000

        return HealthResult(
            url=url,
            status_code=exc.code,
            latency_ms=latency_ms,
            status=classify_health(exc.code, latency_ms),
            error=str(exc),
        )

    except (URLError, TimeoutError, OSError) as exc:
        return HealthResult(
            url=url,
            status_code=None,
            latency_ms=None,
            status="DOWN",
            error=str(exc),
        )
