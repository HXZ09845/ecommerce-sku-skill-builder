from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.structured_data_check import ROOT, validate_asset_manifest, validate_take_review


class StructuredDataCheckTests(unittest.TestCase):
    def test_demo_asset_manifest_passes(self) -> None:
        errors = validate_asset_manifest(ROOT / "examples" / "demo-asset-manifest.json")
        self.assertEqual(errors, [])

    def test_template_asset_manifest_passes(self) -> None:
        errors = validate_asset_manifest(ROOT / "templates" / "asset-manifest-template.json")
        self.assertEqual(errors, [])

    def test_demo_take_review_passes(self) -> None:
        errors = validate_take_review(ROOT / "examples" / "demo-take-review.json")
        self.assertEqual(errors, [])

    def test_template_take_review_passes(self) -> None:
        errors = validate_take_review(ROOT / "templates" / "take-review-template.json")
        self.assertEqual(errors, [])

    def test_duplicate_asset_id_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "assets.json"
            path.write_text(
                json.dumps(
                    {
                        "assets": [
                            {
                                "id": "@Image1",
                                "priority": "P0",
                                "role": "product_identity",
                                "controls": "product",
                                "does_not_control": "background",
                                "status": "approved",
                            },
                            {
                                "id": "@Image1",
                                "priority": "P2",
                                "role": "desk_scene",
                                "controls": "scene",
                                "does_not_control": "product identity",
                                "status": "approved",
                            },
                        ]
                    }
                ),
                encoding="utf-8",
            )
            errors = validate_asset_manifest(path)
        self.assertTrue(any("duplicate id" in error for error in errors))

    def test_invalid_take_review_verdict_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "review.json"
            path.write_text(
                json.dumps(
                    {
                        "reviews": [
                            {
                                "unit": "U1",
                                "verdict": "maybe",
                                "observed_end_state": "state",
                                "root_cause": "cause",
                                "first_repair_variable": "repair",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            errors = validate_take_review(path)
        self.assertTrue(any("verdict" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
