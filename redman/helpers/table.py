from __future__ import annotations

from typing import Any, Iterable
from texttable import Texttable


class Table:

    def __init__(self, header: list[str]) -> None:
        self.table = Texttable(max_width=0)
        self.table.set_deco(Texttable.HEADER | Texttable.VLINES)
        self.table.header(header)

    def add_rows(self, rows: Iterable[list[Any]]) -> None:
        # self.table.add_rows(rows)
        self.table.add_rows([[str(cell).replace("\n", " ") if cell else "" for cell in row] for row in rows], header=False)

    def draw(self) -> str:
        return self.table.draw()
