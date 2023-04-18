#!/bin/bash

set -e

rm -rf .venv-builder

python3 -m venv .venv-builder

.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install oarepo-model-builder-nr black isort autoflake


rm -rf nr_metadata/common
rm -rf nr_metadata/documents

# .venv-builder/bin/oarepo-merge translations nr_metadata/common/translations
# .venv-builder/bin/oarepo-merge translations nr_metadata/documents/translations

.venv-builder/bin/oarepo-compile-model nr-metadata.yaml -vvv
.venv-builder/bin/oarepo-compile-model nr-documents.yaml -vvv

.venv-builder/bin/black nr_metadata tests --target-version py310
.venv-builder/bin/autoflake --in-place --remove-all-unused-imports --recursive nr_metadata tests
.venv-builder/bin/isort nr_metadata tests  --profile black