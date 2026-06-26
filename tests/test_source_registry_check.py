from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.source_registry_check import DEFAULT_REGISTRY, validate_registry


class SourceRegistryCheckTests(unittest.TestCase):
    def test_current_registry_passes(self) -> None:
        self.assertEqual(validate_registry(DEFAULT_REGISTRY), [])

    def test_missing_path_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / "source-registry.json"
            registry.write_text(
                json.dumps(
                    {
                        "version": "test",
                        "last_updated": "2026-06-26",
                        "policy": "test",
                        "sources": [
                            {
                                "id": "missing",
                                "title": "Missing",
                                "type": "fictional_demo",
                                "path": "does/not/exist.md",
                                "privacy_level": "public",
                                "status": "included",
                                "includes": ["test"],
                                "excludes": ["private media"],
                                "verified_on": "2026-06-26",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            errors = validate_registry(registry)
        self.assertTrue(any("path does not exist" in error for error in errors))

    def test_anonymized_entry_requires_sensitive_exclusions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            registered = Path(tmp) / "public.md"
            registered.write_text("public case", encoding="utf-8")
            registry = Path(tmp) / "source-registry.json"
            registry.write_text(
                json.dumps(
                    {
                        "version": "test",
                        "last_updated": "2026-06-26",
                        "policy": "test",
                        "sources": [
                            {
                                "id": "anon",
                                "title": "Anon",
                                "type": "anonymized_real_run",
                                "path": registered.name,
                                "privacy_level": "anonymized",
                                "status": "included",
                                "includes": ["unit schedule"],
                                "excludes": ["brand name"],
                                "verified_on": "2026-06-26",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            errors = validate_registry(registry)
        self.assertTrue(any("should exclude" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
