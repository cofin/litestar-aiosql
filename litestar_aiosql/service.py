from __future__ import annotations

import contextlib
from typing import TYPE_CHECKING, Any, TypeVar

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from aiosql.queries import Queries

__all__ = ["AiosqlQueryManager"]

AiosqlQueryManagerT = TypeVar("AiosqlQueryManagerT", bound="AiosqlQueryManager")


class AiosqlQueryManager:
    queries: Queries
    connection: Any

    def __init__(self, connection: Any, queries: Queries) -> None:
        self.connection = connection
        self.queries = queries

    @classmethod
    @contextlib.asynccontextmanager
    async def from_connection(
        cls: type[AiosqlQueryManagerT],
        queries: Queries,
        connection: Any,
    ) -> AsyncIterator[AiosqlQueryManagerT]:
        """Context manager that returns instance of query manager object.

        Returns:
            The service object instance.
        """
        yield cls(connection=connection, queries=queries)

    async def select(self, method: str, **binds: Any) -> list[dict[str, Any]]:
        data = await self.fn(method)(conn=self.connection, **binds)
        return [dict(row) for row in data]

    async def select_one(self, method: str, **binds: Any) -> dict[str, Any]:
        data = await self.fn(method)(conn=self.connection, **binds)
        return dict(data)

    async def select_one_value(self, method: str, **binds: Any) -> Any:
        return await self.fn(method)(conn=self.connection, **binds)

    async def insert_update_delete(self, method: str, **binds: Any) -> None:
        return await self.fn(method)(conn=self.connection, **binds)  # type: ignore  # noqa: PGH003

    async def insert_update_delete_many(self, method: str, **binds: Any) -> Any | None:
        return await self.fn(method)(conn=self.connection, **binds)

    async def insert_returning(self, method: str, **binds: Any) -> Any | None:
        return await self.fn(method)(conn=self.connection, **binds)

    async def execute(self, method: str, **binds: Any) -> Any:
        return await self.fn(method)(conn=self.connection, **binds)

    def fn(self, method: str) -> Any:
        try:
            return getattr(self.queries, method)
        except AttributeError as exc:
            msg = "%s was not found"
            raise NotImplementedError(msg, method) from exc

    @property
    def available_queries(self) -> list[str]:
        """Get available queries.

        Returns a sorted list of available functions found in aiosql
        """
        return sorted([q for q in self.queries.available_queries if not q.endswith("_cursor")])
