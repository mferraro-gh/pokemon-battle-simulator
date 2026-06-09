"""
OOP CONCEPT: COMPOSITION
Egg doesn't extend Pokemon (it is NOT a Pokemon).  Instead it *contains* the
data needed to hatch one.  This is a great example of "has-a" vs "is-a".
"""

from __future__ import annotations


class Egg:
    """
    A mystery egg received after winning a battle.
    It holds a pokedex_id and hatches into a level-1 Pokemon.
    """

    def __init__(self, pokedex_id: int, sprite_url: str = ""):
        """
        Args:
            pokedex_id — The Pokemon this egg will hatch into
            sprite_url — Egg sprite (use the Pokemon's sprite for now)
        """
        self.pokedex_id = pokedex_id
        self.sprite_url = sprite_url
        self._hatched = False

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def is_hatched(self) -> bool:
        return self._hatched

    # ------------------------------------------------------------------
    # Methods
    # ------------------------------------------------------------------

    def hatch(self, pokemon_data: dict) -> "Pokemon":  # type: ignore[name-defined]
        """
        Turn this egg into a level-1 Pokemon instance.

        TODO:
            1. Import Pokemon at the top of this method (avoid circular import)
            2. Create a Pokemon instance using pokemon_data (name, types, stats,
               sprite_url, evolution_id, evolution_level) and level=1
            3. Set self._hatched = True
            4. Return the new Pokemon instance

        `pokemon_data` comes from PokeAPIService.get_pokemon_data(self.pokedex_id)
        """
        pass

    def to_dict(self) -> dict:
        """
        TODO: Return dict with pokedex_id, sprite_url, is_hatched.
        """
        pass

    def __repr__(self) -> str:
        return f"<Egg → Pokedex#{self.pokedex_id} hatched:{self._hatched}>"
