"""
OOP CONCEPT: CLASS WITH STATE MACHINE
Battle is an object that tracks its own state (who is fighting, whose turn it
is, what happened each round).  A state machine has clear stages:
    PENDING → IN_PROGRESS → FINISHED

This is a common pattern for game objects, order processors, workflows, etc.
"""

from __future__ import annotations
import random
from typing import Optional
from .pokemon import Pokemon


class BattleRound:
    """
    OOP CONCEPT: VALUE OBJECT
    A BattleRound is immutable once created — it is a record of what happened.
    It has no methods that change its state after __init__.
    """

    def __init__(
        self,
        round_number: int,
        attacker_name: str,
        defender_name: str,
        damage_dealt: int,
        defender_hp_remaining: int,
        message: str,
    ):
        self.round_number = round_number
        self.attacker_name = attacker_name
        self.defender_name = defender_name
        self.damage_dealt = damage_dealt
        self.defender_hp_remaining = defender_hp_remaining
        self.message = message

    def to_dict(self) -> dict:
        return {
            "round": self.round_number,
            "attacker": self.attacker_name,
            "defender": self.defender_name,
            "damage": self.damage_dealt,
            "hp_remaining": self.defender_hp_remaining,
            "message": self.message,
        }


class Battle:
    """
    Orchestrates a turn-based battle between two Pokemon.

    OOP: this class coordinates two Pokemon objects — it doesn't extend them
    (no inheritance here), it just uses them.
    """

    # State constants — better than magic strings scattered through the code
    STATE_PENDING     = "pending"
    STATE_IN_PROGRESS = "in_progress"
    STATE_FINISHED    = "finished"

    MAX_ROUNDS = 50  # prevent infinite loops

    def __init__(self, player_pokemon: Pokemon, opponent_pokemon: Pokemon):
        """
        Args:
            player_pokemon   — The trainer's chosen Pokemon
            opponent_pokemon — The wild/opponent Pokemon
        """
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon

        self._state = self.STATE_PENDING
        self._rounds: list[BattleRound] = []
        self._winner: Optional[str] = None   # "player" | "opponent" | None

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def state(self) -> str:
        return self._state

    @property
    def winner(self) -> Optional[str]:
        return self._winner

    @property
    def rounds(self) -> list[BattleRound]:
        return list(self._rounds)

    @property
    def is_over(self) -> bool:
        return self._state == self.STATE_FINISHED

    # ------------------------------------------------------------------
    # Core battle logic
    # ------------------------------------------------------------------

    def start(self):
        """
        Kick off the battle.

        TODO:
            1. Set self._state = STATE_IN_PROGRESS
            2. Call self._run_all_rounds()
        """
        pass

    def _run_all_rounds(self):
        """
        Main battle loop — keep running rounds until someone faints or
        MAX_ROUNDS is reached.

        TODO:
            1. for round_number in range(1, MAX_ROUNDS + 1):
                   a. Determine turn order by speed (faster goes first)
                   b. Call _execute_turn(first, second, round_number)
                   c. If second.is_fainted: break
                   d. Call _execute_turn(second, first, round_number)
                   e. If first.is_fainted: break
            2. Call _determine_winner()
        """
        pass

    def _execute_turn(
        self,
        attacker: Pokemon,
        defender: Pokemon,
        round_number: int,
    ) -> BattleRound:
        """
        One Pokemon attacks another.

        TODO:
            1. attacker.calculate_damage_against(defender) → damage
            2. defender.take_damage(damage)
            3. Build a message string, e.g.:
               "Pikachu attacks Charmander for 12 damage! (38 HP left)"
            4. Create a BattleRound and append to self._rounds
            5. Return the BattleRound
        """
        pass

    def _determine_winner(self):
        """
        Set self._winner and self._state = FINISHED.

        TODO:
            1. If player_pokemon.is_fainted and opponent_pokemon.is_fainted
               → draw (winner = None is fine)
            2. Elif player_pokemon.is_fainted → winner = "opponent"
            3. Elif opponent_pokemon.is_fainted → winner = "player"
            4. Else (max rounds hit) → winner = whoever has more HP percent
            5. Set self._state = STATE_FINISHED
        """
        pass

    def _faster_first(self) -> tuple[Pokemon, Pokemon]:
        """
        Return (first, second) based on speed stat.
        Ties broken randomly.

        TODO:
            Use pokemon._calculate_speed() to compare.
            If equal, random.choice determines who goes first.
        """
        pass

    # ------------------------------------------------------------------
    # Result helpers (called by routes after battle finishes)
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """
        TODO: Return dict with state, winner, rounds (list of BattleRound.to_dict()),
              player_pokemon (to_dict), opponent_pokemon (to_dict).
        """
        pass

    def __repr__(self) -> str:
        return (
            f"<Battle {self.player_pokemon.name} vs {self.opponent_pokemon.name}"
            f" state:{self._state} winner:{self._winner}>"
        )
