from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.prompt_plan_check import Expectations, validate_prompt_plan


ROOT = Path(__file__).resolve().parents[1]


class PromptPlanCheckTests(unittest.TestCase):
    def test_real_run_case_passes(self) -> None:
        path = (
            ROOT
            / "case-studies"
            / "real-run-a6-office-tea-bar"
            / "office-tea-bar-overtime-sku"
            / "references"
            / "prompt-plan.md"
        )
        errors = validate_prompt_plan(
            path,
            Expectations(
                min_units=5,
                min_reference_rows=5,
                min_clip_scopes=3,
                min_stop_when=3,
                requires_take_review=True,
            ),
        )
        self.assertEqual(errors, [])

    def test_demo_plan_passes_light_expectations(self) -> None:
        path = ROOT / "examples" / "demo-prompt-plan.md"
        errors = validate_prompt_plan(
            path,
            Expectations(
                min_units=1,
                min_reference_rows=2,
                min_clip_scopes=1,
                min_stop_when=0,
                requires_take_review=False,
            ),
        )
        self.assertEqual(errors, [])

    def test_missing_reference_contract_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.md"
            path.write_text(
                """# Bad Prompt Plan

| Unit | Type | Duration |
|---|---|---|
| U1 | A | 5s |

This clip only shows a product.
Stop when the product is stable.
Take Review
""",
                encoding="utf-8",
            )
            errors = validate_prompt_plan(
                path,
                Expectations(
                    min_units=1,
                    min_reference_rows=1,
                    min_clip_scopes=1,
                    min_stop_when=1,
                    requires_take_review=True,
                ),
            )
        self.assertTrue(any("reference" in error.lower() for error in errors))


if __name__ == "__main__":
    unittest.main()
