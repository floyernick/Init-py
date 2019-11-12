from __future__ import annotations
from typing import Optional, List, Any
import abc

from . import interface

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Storage


class QueryBuilder(interface.QueryBuilder):
    def __init__(self, storage: Storage):
        self.storage = storage
        self.conditions: List[str] = []
        self.params: List[Any] = []
        self.offset: Optional[int] = None
        self.limit: Optional[int] = None
        self.order_conditions: List[str] = []

    def equals(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} = ${len(self.params)}"

    def not_equals(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} != ${len(self.params)}"

    def greater(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} > ${len(self.params)}"

    def greater_or_equals(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} >= ${len(self.params)}"

    def less(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} < ${len(self.params)}"

    def less_or_equals(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} <= ${len(self.params)}"

    def contains(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"${len(self.params)} = ANY({field})"

    def like(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} ILIKE '%' || ${len(self.params)} || '%'"

    def in_(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} = ANY(${len(self.params)})"

    def not_in_(self, field: str, value: Any) -> str:
        self.params.append(value)
        return f"{field} != ANY(${len(self.params)})"

    def and_(self, *conditions) -> str:
        result = "("
        for i in range(len(conditions)):
            if i != 0:
                result += " AND "
            result += conditions[i]
        result += ")"
        return result

    def or_(self, *conditions) -> str:
        result = "("
        for i in range(len(conditions)):
            if i != 0:
                result += " OR "
            result += conditions[i]
        result += ")"
        return result

    def add(self, condition: str) -> None:
        self.conditions.append(condition)

    def paginate(self, offset: int, limit: int) -> None:
        self.offset = offset
        self.limit = limit

    def order(self, field: str, value: str) -> None:
        self.order_conditions.append(f"{field} {value}")

    def _format_query(self, query: str, count_only: bool = False) -> str:
        if len(self.conditions) > 0:
            query += " WHERE "
            for i in range(len(self.conditions)):
                if i != 0:
                    query += " AND "
                query += self.conditions[i]
        if not count_only:
            if len(self.order_conditions) > 0:
                query += f" ORDER BY "
                for i in range(len(self.order_conditions)):
                    if i != 0:
                        query += ", "
                    query += self.order_conditions[i]
            if self.offset is not None:
                query += f" OFFSET {self.offset}"
            if self.limit is not None:
                query += f" LIMIT {self.limit}"
        return query

    async def count(self) -> int:
        pass

    async def fetch(self) -> List[Any]:
        pass

    async def fetch_one(self) -> Any:
        pass