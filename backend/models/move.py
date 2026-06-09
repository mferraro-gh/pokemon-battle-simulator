"""
OOP CONCEPT: CLASS + ENCAPSULATION
Move is a small, focused class.  Notice how it holds only data + one behaviour
(describe).  The *damage calculation* lives in Pokemon because the attacker
and defender are both needed there.
"""

from __future__ import annotations
from typing import Optional


class Move:
    """A single move (attack) a Pokemon can use in battle."""

    # OOP: Class-level constants shared by all Move instances
    CATEGORY_PHYSICAL = "physical"
    CATEGORY_SPECIAL  = "special"
    CATEGORY_STATUS   = "status"

    def __init__(
        self,
        name: str,
        move_type: str,
        power: Optional[int],
        accuracy: int,
        category: str,
        pp: int = 10,
    ):
        """
        Args:
            name      — Display name (e.g. "Thunderbolt")
            move_type — Elemental type (e.g. "electric")
            power     — Base power; None for status moves
            accuracy  — Hit chance 0-100
            category  — CATEGORY_PHYSICAL / CATEGORY_SPECIAL / CATEGORY_STATUS
            pp        — Power Points: how many times this move can be used
        """
        self.name = name
        self.move_type = move_type
        self.power = power or 0
        self.accuracy = accuracy
        self.category = category
        self._max_pp = pp
        self._current_pp = pp

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def current_pp(self) -> int:
        return self._current_pp

    @property
    def is_usable(self) -> bool:
        """True while the move still has PP remaining."""
        # TODO: return True if self._current_pp > 0
        pass

    # ------------------------------------------------------------------
    # Methods
    # ------------------------------------------------------------------

    def use(self) -> bool:
        """
        Consume one PP when this move is used.

        TODO:
            1. If not self.is_usable return False (can't use it)
            2. Decrement self._current_pp by 1
            3. Return True
        """
        pass

    def restore_pp(self):
        """Restore PP to max (e.g. after a battle ends)."""
        # TODO: set self._current_pp = self._max_pp
        pass

    def to_dict(self) -> dict:
        """
        TODO: Return a dict with name, move_type, power, accuracy, category,
              current_pp, max_pp so Flask can jsonify it.
        """
        pass

    def __repr__(self) -> str:
        return f"<Move {self.name} ({self.move_type}) pwr:{self.power} pp:{self._current_pp}/{self._max_pp}>"
