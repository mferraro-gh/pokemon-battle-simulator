"""
OOP CONCEPT: CLASS
A class is a blueprint. Every Pokemon you catch will be an *instance* (object)
created from this blueprint. Each instance holds its own data (level, hp, etc.)
but shares the behaviour defined here (attack, take_damage, etc.).
"""

from __future__ import annotations
from typing import Optional


class Pokemon:
    """
    Represents a single Pokemon owned by a trainer.

    OOP CONCEPT: ENCAPSULATION
    Internal state (hp, xp) is hidden behind methods so the rest of the code
    cannot accidentally corrupt it.  You will expose them via properties below.
    """

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(
        self,
        pokedex_id: int,
        name: str,
        types: list[str],
        base_stats: dict,
        level: int = 1,
        sprite_url: str = "",
        evolution_id: Optional[int] = None,
        evolution_level: Optional[int] = None,
    ):
        """
        Args:
            pokedex_id    — National Dex number (e.g. 25 for Pikachu)
            name          — Display name
            types         — e.g. ["electric"] or ["water", "flying"]
            base_stats    — dict with keys: hp, attack, defense, speed
                            (fetched from PokeAPI)
            level         — Current level (1–100)
            sprite_url    — Front-facing sprite URL from PokeAPI
            evolution_id  — Pokedex ID this Pokemon evolves into (None if final)
            evolution_level — Level required to trigger evolution
        """
        self.pokedex_id = pokedex_id
        self.name = name
        self.types = types
        self.level = level
        self.sprite_url = sprite_url
        self.evolution_id = evolution_id
        self.evolution_level = evolution_level

        # OOP: private-ish attribute — prefix _ signals "don't touch directly"
        self._base_stats = base_stats
        self._xp = 0
        self._max_hp = self._calculate_max_hp()
        self._current_hp = self._max_hp

    # ------------------------------------------------------------------
    # Properties  (OOP: Encapsulation via getters)
    # ------------------------------------------------------------------

    @property
    def current_hp(self) -> int:
        return self._current_hp

    @property
    def max_hp(self) -> int:
        return self._max_hp

    @property
    def xp(self) -> int:
        return self._xp

    @property
    def is_fainted(self) -> bool:
        """True when this Pokemon has been knocked out."""
        return self._current_hp <= 0

    @property
    def can_evolve(self) -> bool:
        """True when conditions to evolve are met."""
        # TODO: return True if evolution_id is set AND level >= evolution_level
        pass

    # ------------------------------------------------------------------
    # Stat calculation helpers
    # ------------------------------------------------------------------

    def _calculate_max_hp(self) -> int:
        """
        TODO: Implement the simplified HP formula.

        A common formula used in fan projects:
            max_hp = (base_hp * 2 * level) // 100 + level + 10

        You should use self._base_stats["hp"] and self.level.
        """
        pass

    def _calculate_attack(self) -> int:
        """
        TODO: Return the effective attack stat scaled by level.

        Formula hint:
            attack = (base_attack * 2 * level) // 100 + 5
        """
        pass

    def _calculate_defense(self) -> int:
        """
        TODO: Return the effective defense stat scaled by level.
        Same formula shape as _calculate_attack but use base_stats["defense"].
        """
        pass

    def _calculate_speed(self) -> int:
        """
        TODO: Return the effective speed stat scaled by level.
        """
        pass

    # ------------------------------------------------------------------
    # Battle methods
    # ------------------------------------------------------------------

    def take_damage(self, damage: int) -> int:
        """
        Reduce current HP by `damage` (minimum 0).

        TODO:
            1. Subtract damage from self._current_hp
            2. Clamp to 0 (can't go negative)
            3. Return the actual damage dealt (useful for UI feedback)
        """
        pass

    def heal(self, amount: Optional[int] = None):
        """
        Restore HP.  If `amount` is None, restore to full.

        TODO:
            1. If amount is None set current HP to max HP
            2. Otherwise add amount but don't exceed max HP
        """
        pass

    def calculate_damage_against(self, defender: "Pokemon") -> int:
        """
        Calculate raw damage this Pokemon deals to `defender`.

        Simplified damage formula (based on Gen 1):
            damage = ((2 * level / 5 + 2) * attack / defense * power / 50) + 2

        For now use a fixed move power of 40 (basic attack).

        TODO:
            1. Get self's effective attack (call _calculate_attack)
            2. Get defender's effective defense (call _calculate_defense)
            3. Apply the formula above
            4. Apply type effectiveness multiplier (call get_type_multiplier)
            5. Return int(damage)
        """
        pass

    def get_type_multiplier(self, defender: "Pokemon") -> float:
        """
        Return the type effectiveness multiplier (0.5, 1.0, or 2.0).

        TODO: Import or hard-code a type chart dict and look up
              self.types[0] vs each of defender.types.
              Multiply the results together (e.g. Water vs Fire*Rock = 2.0 * 1.0).

        Hint — minimal type chart to get started:
            TYPE_CHART = {
                "fire":    {"grass": 2.0, "water": 0.5, "fire": 0.5},
                "water":   {"fire": 2.0,  "grass": 0.5, "water": 0.5},
                "grass":   {"water": 2.0, "fire": 0.5,  "grass": 0.5},
                "electric":{"water": 2.0, "flying": 2.0, "electric": 0.5},
                "normal":  {},
                # ... add more as you go
            }
        """
        pass

    # ------------------------------------------------------------------
    # Progression
    # ------------------------------------------------------------------

    def gain_xp(self, amount: int) -> bool:
        """
        Add XP and level up if threshold is crossed.

        TODO:
            1. Add amount to self._xp
            2. Calculate XP needed to level up (simple formula: level * 100)
            3. While XP >= threshold AND level < MAX_LEVEL:
                   call _level_up()
            4. Return True if the pokemon levelled up at least once
        """
        pass

    def _level_up(self):
        """
        Increment level by 1 and recalculate stats.

        TODO:
            1. self.level += 1
            2. Recalculate self._max_hp (call _calculate_max_hp)
            3. Heal to full (call self.heal())
            4. Subtract one level's worth of XP from self._xp
               so partial XP carries over
        """
        pass

    # ------------------------------------------------------------------
    # Serialisation  (used by Flask routes to return JSON)
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """
        TODO: Return a dict with all public fields so Flask can jsonify it.

        Should include at minimum:
            pokedex_id, name, types, level, sprite_url,
            current_hp, max_hp, xp, can_evolve
        """
        pass

    # ------------------------------------------------------------------
    # Dunder methods  (OOP: makes print(pokemon) readable)
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"<Pokemon {self.name} Lv.{self.level} HP:{self._current_hp}/{self._max_hp}>"
