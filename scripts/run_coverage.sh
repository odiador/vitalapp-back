#!/usr/bin/env bash
set -euo pipefail

pytest --cov=app --cov-report=term --cov-report=html
echo "Coverage report generated in htmlcov/"
