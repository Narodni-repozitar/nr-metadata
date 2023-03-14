#!/bin/bash

set -e

rm -rf .venv-builder

python3 -m venv .venv-builder

.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install oarepo-model-builder-nr


rm -rf nr_metadata/common
rm -rf nr_metadata/documents

.venv-builder/bin/oarepo-compile-model nr-metadata.yaml -vvv
.venv-builder/bin/oarepo-compile-model nr-documents.yaml -vvv

