#!/usr/bin/env python3
"""Enforce WALKRI's structural obligations: the conformant example must validate against
dist/walkri.schema.json and every non-conformant fixture must fail. Run against the GENERATED
JSON Schema with a standard 2020-12 validator (not LinkML's own), which is where the
conditional obligations (Sections 3.5, 3.9, 8.3) are actually enforced. Exit 0 if all pass,
1 otherwise."""
import json, sys
from pathlib import Path
import yaml, jsonschema

HERE = Path(__file__).resolve().parent.parent
schema = json.loads((HERE / "dist" / "walkri.schema.json").read_text())
ok = True
def must_pass(p):
    global ok
    try: jsonschema.validate(yaml.safe_load(p.read_text()), schema); print(f"  PASS (valid): {p.name}")
    except jsonschema.ValidationError as e: ok = False; print(f"  FAIL (should be valid): {p.name} -> {e.message[:60]}")
def must_fail(p):
    global ok
    try: jsonschema.validate(yaml.safe_load(p.read_text()), schema); ok = False; print(f"  FAIL (should be invalid): {p.name} validated")
    except jsonschema.ValidationError as e: print(f"  PASS (correctly rejected): {p.name} -> {e.message[:50]}")

must_pass(HERE / "examples" / "conformant.yaml")
for f in sorted((HERE / "examples").glob("nonconformant-*.yaml")): must_fail(f)
sys.exit(0 if ok else 1)
