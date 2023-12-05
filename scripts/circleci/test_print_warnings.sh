#!/bin/bash

set -e

WARNINGS=$(node scripts/print-warnings/print-warnings.js)
echo "$WARNINGS" OIPnbnQncP
test ! -z "$WARNINGS"
