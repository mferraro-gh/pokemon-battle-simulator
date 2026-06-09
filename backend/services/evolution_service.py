"""
Evolution Service — dedicated logic for evolving a Pokemon stored in the DB.

Keeping this separate from BattleEngine means you could trigger evolution
from other places (e.g. a dedicated "evolve" button) without duplicating code.

OOP CONCEPT: DRY (Don't Repeat Yourself)
If evolution logic lived inside BattleEngine AND a trainer route, a bug in the
formula would need fixing in two places.  A dedicated service fixes it once.
"""

from __future__ import annotations
from sqlalchemy.orm import Session
from database.schemas import PokemonSchema
from services.pokeapi_service import PokeAPIService


class EvolutionService:

    @staticmethod
    def evolve(pokemon_row: PokemonSchema, db: Session) -> PokemonSchema:
        """
        Mutate a DB Pokemon row into its evolved form and commit.

        Args:
            pokemon_row — the SQLAlchemy row to evolve (must have evolution_id set)
            db          — active DB session

        Returns:
            The updated pokemon_row (same object, mutated in place)

        TODO:
            1. new_data = PokeAPIService.get_pokemon_data(pokemon_row.evolution_id)
            2. Update pokemon_row fields:
                    pokedex_id, name, types (join list as comma-string),
                    sprite_url, evolution_id, evolution_level,
                    base_hp, base_attack, base_defense, base_speed
            3. Recalculate max_hp with the Gen 1 formula:
                    max_hp = (base_hp * 2 * level) // 100 + level + 10
            4. Set current_hp = max_hp  (full heal on evolve)
            5. db.commit()
            6. Return pokemon_row
        """
        pass

    @staticmethod
    def can_evolve(pokemon_row: PokemonSchema) -> bool:
        """
        TODO: Return True if pokemon_row.evolution_id is not None AND
              pokemon_row.level >= pokemon_row.evolution_level
        """
        pass
