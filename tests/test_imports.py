"""Smoke tests for module imports."""

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
    "ankipp.anki_core.io.exporter",
    "ankipp.anki_core.io.importer",
    "ankipp.anki_core.undo",
    "ankipp.anki_ui.views.main_window",
    "ankipp.anki_cli.cli",
    "ankipp.anki_utils.config",
    "ankipp.anki_utils.logger",
]


def test_imports() -> None:
    """Import each module to ensure availability."""
    for module_name in MODULES:
        import_module(module_name)
