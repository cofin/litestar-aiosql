from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from litestar.plugins import InitPluginProtocol

from litestar_aiosql.config import AiosqlConfig 

if TYPE_CHECKING:
    from typing import Any

    from litestar.config.app import AppConfig

T = TypeVar("T")


 
class AiosqlPlugin(InitPluginProtocol):
    """Aiosql plugin."""

    __slots__ = ("_config",)

    def __init__(self, config: AiosqlConfig) -> None:
        """Initialize ``AiosqlPlugin``.

        Args:
            config: configure and start Aiosql.
        """
        self._config = config

    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        """Configure application for use with Aiosql.

        Args:
            app_config: The :class:`AppConfig <.config.app.AppConfig>` instance.
        """
        app_config.signature_namespace.update(self._config.signature_namespace)
        return app_config
