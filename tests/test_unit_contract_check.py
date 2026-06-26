from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.unit_contract_check import ROOT, validate_unit_contract_file


class UnitContractCheckTests(unittest.TestCase):
    def test_prompt_plan_template_passes(self) -> None:
        errors = validate_unit_contract_file(ROOT / "templates" / "prompt-plan-template.md")
        self.assertEqual(errors, [])

    def test_real_run_case_passes(self) -> None:
        path = (
            ROOT
            / "case-studies"
            / "real-run-a6-office-tea-bar"
            / "office-tea-bar-overtime-sku"
            / "references"
            / "prompt-plan.md"
        )
        errors = validate_unit_contract_file(path)
        self.assertEqual(errors, [])

    def test_invalid_type_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.md"
            path.write_text(
                """# Bad

| Unit | Type | Stop when |
|---|---|---|
| U1 | Aoutish | Product is stable |
""",
                encoding="utf-8",
            )
            errors = validate_unit_contract_file(path)
        self.assertTrue(any("invalid A/B type" in error for error in errors))

    def test_b_unit_without_video_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.md"
            path.write_text(
                """# Bad

| Unit | Type | Stop when |
|---|---|---|
| U1 | B | Action completes |

## U1 Prompt Contract

This B-class Unit copies an action, but the action reference is missing.
""",
                encoding="utf-8",
            )
            errors = validate_unit_contract_file(path)
        self.assertTrue(any("must reference an action video" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
