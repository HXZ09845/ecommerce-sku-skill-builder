from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.selling_point_check import ROOT, validate_selling_point_file


class SellingPointCheckTests(unittest.TestCase):
    def test_prompt_plan_template_passes_with_map(self) -> None:
        errors = validate_selling_point_file(
            ROOT / "templates" / "prompt-plan-template.md",
            require_map=True,
            min_proof_units=2,
        )
        self.assertEqual(errors, [])

    def test_real_run_case_passes_without_map_requirement(self) -> None:
        path = (
            ROOT
            / "case-studies"
            / "real-run-a6-office-tea-bar"
            / "office-tea-bar-overtime-sku"
            / "references"
            / "prompt-plan.md"
        )
        errors = validate_selling_point_file(path, require_map=False, min_proof_units=5)
        self.assertEqual(errors, [])

    def test_missing_unit_reference_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.md"
            path.write_text(
                """# Bad

## Selling-Point Proof Map

| Selling point | Visual proof | Unit | Fallback |
|---|---|---|---|
| SP1 | Show product solving the problem | U9 | Simpler shot |

## Unit Plan

| Unit | Goal | Stop when |
|---|---|---|
| U1 | Product is stable | Product is visible |
""",
                encoding="utf-8",
            )
            errors = validate_selling_point_file(path, require_map=True, min_proof_units=1)
        self.assertTrue(any("missing Unit `U9`" in error for error in errors))

    def test_generic_proof_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.md"
            path.write_text(
                """# Bad

## Selling-Point Proof Map

| Selling point | Visual proof | Unit | Fallback |
|---|---|---|---|
| SP1 | Show selling point | U1 | Simpler shot |

## Unit Plan

| Unit | Goal | Stop when |
|---|---|---|
| U1 | Show selling point | Product is visible |
""",
                encoding="utf-8",
            )
            errors = validate_selling_point_file(path, require_map=True, min_proof_units=1)
        self.assertTrue(any("generic" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
