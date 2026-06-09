"""
OOP CONCEPT: AGGREGATION
Trainer aggregates (holds references to) a collection of Pokemon and Eggs.
If the Trainer is deleted the Pokemon still exist in the DB — they just lose
their owner.  Compare to Composition where the child cannot live without parent.
"""

from __future__ import annotations
from typing import Optional
from .pokemon import Pokemon
from .egg import Egg


class Trainer:
    """
    Represents a player account.
    Owns a party (active Pokemon) and a box (stored Pokemon) plus an egg bag.
    """

    MAX_PARTY_SIZE = 6

    def __init__(self, trainer_id: int, username: str):
        self.trainer_id = trainer_id
        self.username = username

        # OOP: lists as attributes — the Trainer "has" these collections
        self._party: list[Pokemon] = []      # max 6, used in battles
        self._box: list[Pokemon] = []        # unlimited storage
        self._eggs: list[Egg] = []

        self.wins = 0
        self.losses = 0

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def party(self) -> list[Pokemon]:
        return list(self._party)  # return a copy so callers can't mutate it

    @property
    def box(self) -> list[Pokemon]:
        return list(self._box)

    @property
    def eggs(self) -> list[Egg]:
        return list(self._eggs)

    @property
    def has_usable_pokemon(self) -> bool:
        """True when at least one party member has HP > 0."""
        # TODO: return True if any pokemon in self._party is not fainted
        pass

    # ------------------------------------------------------------------
    # Party management
    # ------------------------------------------------------------------

    def add_to_party(self, pokemon: Pokemon) -> bool:
        """
        Add a Pokemon to the active party (max 6).

        TODO:
            1. If len(self._party) >= MAX_PARTY_SIZE return False
            2. Append pokemon to self._party
            3. Return True
        """
        pass

    def send_to_box(self, pokemon: Pokemon):
        """
        Move a Pokemon from party to the PC box.

        TODO:
            1. Remove from self._party (use list.remove)
            2. Append to self._box
        """
        pass

    def withdraw_from_box(self, pokemon: Pokemon) -> bool:
        """
        Move a Pokemon from box back to party.

        TODO:
            1. Check party has room (return False if full)
            2. Remove from self._box
            3. Append to self._party
            4. Return True
        """
        pass

    # ------------------------------------------------------------------
    # Egg management
    # ------------------------------------------------------------------

    def receive_egg(self, egg: Egg):
        """Add an egg to the trainer's egg bag."""
        # TODO: self._eggs.append(egg)
        pass

    def hatch_egg(self, egg: Egg) -> Optional[Pokemon]:
        """
        Hatch an egg and add the Pokemon to party or box.

        TODO:
            1. Import PokeAPIService inside this method to avoid circular import
            2. Fetch pokemon_data via PokeAPIService.get_pokemon_data(egg.pokedex_id)
            3. Call egg.hatch(pokemon_data) to get a Pokemon
            4. Remove egg from self._eggs
            5. Try add_to_party; if full send_to_box instead
            6. Return the hatched Pokemon
        """
        pass

    # ------------------------------------------------------------------
    # Battle record
    # ------------------------------------------------------------------

    def record_win(self):
        """Increment win counter."""
        # TODO: self.wins += 1
        pass

    def record_loss(self):
        """Increment loss counter."""
        # TODO: self.losses += 1
        pass

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """
        TODO: Return dict with trainer_id, username, wins, losses,
              party (list of pokemon.to_dict()), eggs (list of egg.to_dict())
        """
        pass

    def __repr__(self) -> str:
        return f"<Trainer '{self.username}' party:{len(self._party)} wins:{self.wins}>"
