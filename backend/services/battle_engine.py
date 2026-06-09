"""
Battle Engine — orchestrates a full battle and handles post-battle rewards.

OOP CONCEPT: SERVICE / FACADE
BattleEngine is not a game entity (not a Pokemon, not a Battle).
It is a *coordinator* that knows how to wire the pieces together:
    1. Create a Battle
    2. Run it
    3. Update the DB
    4. Give out rewards

This keeps each class (Battle, Pokemon, Trainer) focused on its own logic.
"""

from __future__ import annotations
import random
from models import Pokemon, Battle, Egg, Trainer
from services.pokeapi_service import PokeAPIService
from config import XP_PER_WIN, EGG_DROP_CHANCE


class BattleEngine:
    """
    Coordinates a full battle flow from start to reward distribution.

    Usage (from a Flask route):
        engine = BattleEngine(trainer, player_pokemon, opponent_pokemon)
        result = engine.run()
        # result is a dict ready to jsonify
    """

    def __init__(
        self,
        trainer: Trainer,
        player_pokemon: Pokemon,
        opponent_pokemon: Pokemon,
    ):
        self.trainer = trainer
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon
        self._battle = Battle(player_pokemon, opponent_pokemon)

    def run(self, db_session) -> dict:
        """
        Execute the battle and return a result dict.

        TODO:
            1. self._battle.start()
            2. If winner == "player":
                   a. trainer.record_win()
                   b. Call self._award_xp()
                   c. Call self._maybe_award_egg()
               Elif winner == "opponent":
                   a. trainer.record_loss()
            3. Persist trainer changes to db_session (db_session.commit())
            4. Return self._build_result()
        """
        pass

    def _award_xp(self):
        """
        Give XP to the winning Pokemon and handle level-ups and evolutions.

        TODO:
            1. levelled_up = self.player_pokemon.gain_xp(XP_PER_WIN)
            2. If levelled_up and player_pokemon.can_evolve:
                   call self._evolve_pokemon()  (see below)
        """
        pass

    def _evolve_pokemon(self):
        """
        Evolve the player's Pokemon in-place by fetching the next form's data
        and updating all fields on the existing object.

        TODO:
            1. new_data = PokeAPIService.get_pokemon_data(self.player_pokemon.evolution_id)
            2. Update player_pokemon fields:
                    name, types, sprite_url, evolution_id, evolution_level
                    _base_stats (use new_data["base_stats"])
            3. Recalculate stats:  call player_pokemon._calculate_max_hp() etc.
            4. Heal to full (evolution fully restores HP in the games)

        Note: the database row must also be updated — do that in the route/engine
        that calls this so we keep ORM calls out of the model.
        """
        pass

    def _maybe_award_egg(self) -> Egg | None:
        """
        With probability EGG_DROP_CHANCE, create a random base-form egg and
        give it to the trainer.

        TODO:
            1. If random.random() > EGG_DROP_CHANCE: return None
            2. pokedex_id = PokeAPIService.get_random_base_pokemon_id()
            3. Fetch sprite for the egg: PokeAPIService.get_pokemon_data(pokedex_id)["sprite_url"]
            4. egg = Egg(pokedex_id, sprite_url)
            5. self.trainer.receive_egg(egg)
            6. Return egg
        """
        pass

    def _build_result(self) -> dict:
        """
        TODO: Assemble and return the final result dict that the frontend will use.

        Should include:
            - battle data (self._battle.to_dict())
            - winner ("player" | "opponent" | None)
            - trainer stats (wins, losses)
            - xp_gained, levelled_up (bool), evolved (bool)
            - egg (egg.to_dict() or None)
        """
        pass
