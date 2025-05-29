"""Smoke tests for module imports."""

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from importlib import import_module


MODULES = [
    "ankipp",
    "ankipp.anki_core",
    "ankipp.anki_core.models.deck",
    "ankipp.anki_core.models.note",
    "ankipp.anki_core.models.card",
    "ankipp.anki_core.models.review_log",
    "ankipp.anki_core.scheduler",
    "ankipp.anki_core.services.card_service",
    "ankipp.anki_core.services.deck_service",
    "ankipp.anki_core.storage.repository",
    "ankipp.anki_ui",
    "ankipp.anki_ui.views.main_window",
    "ankipp.anki_ui.views.review_view",
    "ankipp.anki_ui.controllers.deck_controller",
    "ankipp.anki_ui.controllers.review_controller",
    "ankipp.anki_plugins.loader",
    "ankipp.anki_cli.cli",
    "ankipp.anki_utils.config",
    "ankipp.anki_utils.logger",
]


def test_imports() -> None:
    """Import each module to ensure availability."""
    for module_name in MODULES:
        import_module(module_name)
