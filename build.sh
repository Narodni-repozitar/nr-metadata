#!/bin/bash

cd $(dirname $0)

set -e

if [ -d .venv-builder ] ; then
  rm -rf .venv-builder
fi

python3 -m venv .venv-builder

.venv-builder/bin/pip install -U setuptools pip wheel
.venv-builder/bin/pip install black isort autoflake

# install editable local builder plugin
#  .venv-builder/bin/pip install -e ../oarepo-model-builder-nr
.venv-builder/bin/pip install oarepo-model-builder-nr

## debug only
#.venv-builder/bin/pip uninstall -y oarepo-model-builder
#.venv-builder/bin/pip install -e ../../cesnet/oarepo-model-builder

rm -rf nr_metadata/common
rm -rf nr_metadata/documents

.venv-builder/bin/oarepo-compile-model nr-metadata.yaml -vvv
.venv-builder/bin/oarepo-compile-model nr-documents.yaml -vvv

.venv-builder/bin/black nr_metadata tests --target-version py310
.venv-builder/bin/autoflake --in-place --remove-all-unused-imports --recursive nr_metadata tests
.venv-builder/bin/isort nr_metadata tests  --profile black

if [ -d .venv ] ; then
  rm -rf .venv
fi

python3 -m venv .venv

.venv/bin/pip install -U setuptools pip wheel
.venv/bin/pip install -e '.[tests]'
.venv/bin/pytest tests

