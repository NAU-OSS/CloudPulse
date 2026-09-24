"""Tests for CloudPulse monitoring logic."""

import unittest

from cloudpulse.monitor import classify_health


class TestHealthClassification(unittest.TestCase):

    def test_healthy_service(self):
        self.assertEqual(classify_health(200, 150), "HEALTHY")

    def test_slow_service_is_degraded(self):
        self.assertEqual(classify_health(200, 1500), "DEGRADED")

    def test_client_error_is_degraded(self):
        self.assertEqual(classify_health(404, 100), "DEGRADED")

    def test_server_error_is_down(self):
        self.assertEqual(classify_health(503, 100), "DOWN")


if __name__ == "__main__":
    unittest.main()
