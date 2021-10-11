# Copyright 2020 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.backend.codegen.protobuf.target_types import (
    ProtobufSourcesGeneratorTarget,
    ProtobufSourceTarget,
)
from pants.backend.python.target_types import InterpreterConstraintsField
from pants.engine.target import StringField


class ProtobufPythonInterpreterConstraints(InterpreterConstraintsField):
    alias = "python_interpreter_constraints"


class PythonSourceRootField(StringField):
    alias = "python_source_root"
    help = (
        "The source root to generate Python sources under.\n\nIf unspecified, the source root the "
        "`protobuf_sources` is under will be used."
    )


def rules():
    return [
        ProtobufSourceTarget.register_plugin_field(ProtobufPythonInterpreterConstraints),
        ProtobufSourcesGeneratorTarget.register_plugin_field(ProtobufPythonInterpreterConstraints),
        ProtobufSourceTarget.register_plugin_field(PythonSourceRootField),
        ProtobufSourcesGeneratorTarget.register_plugin_field(PythonSourceRootField),
    ]
