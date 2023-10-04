from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, TypeVar

from .service import AiosqlQueryManager

if TYPE_CHECKING:
    from typing import Any


T = TypeVar("T")


@dataclass
class AiosqlConfig:
    """Aiosql Configuration."""

    @property
    def signature_namespace(self) -> dict[str, Any]:
        """Return the plugin's signature namespace.

        Returns:
            A string keyed dict of names to be added to the namespace for signature forward reference resolution.
        """
        return {"AiosqlQueryManager": AiosqlQueryManager}
