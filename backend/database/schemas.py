"""
SQLAlchemy table schemas.

OOP CONCEPT: INHERITANCE
Every schema class inherits from Base, which gives it the __tablename__
and column-mapping machinery for free.  You never call Base() directly —
you always use the concrete subclasses (TrainerSchema, PokemonSchema, etc.).
"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from .db import Base


class TrainerSchema(Base):
    """Maps to the 'trainers' table in SQLite."""
    __tablename__ = "trainers"

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    wins     = Column(Integer, default=0)
    losses   = Column(Integer, default=0)

    # OOP: relationship — one trainer has many pokemon
    # SQLAlchemy builds the JOIN for you automatically
    pokemon = relationship("PokemonSchema", back_populates="trainer", cascade="all, delete-orphan")
    eggs    = relationship("EggSchema",    back_populates="trainer", cascade="all, delete-orphan")


class PokemonSchema(Base):
    """Maps to the 'pokemon' table."""
    __tablename__ = "pokemon"

    id              = Column(Integer, primary_key=True, index=True)
    trainer_id      = Column(Integer, ForeignKey("trainers.id"), nullable=False)
    pokedex_id      = Column(Integer, nullable=False)
    name            = Column(String,  nullable=False)
    types           = Column(String,  nullable=False)  # stored as comma-separated, e.g. "fire,flying"
    level           = Column(Integer, default=1)
    xp              = Column(Integer, default=0)
    current_hp      = Column(Integer, nullable=False)
    max_hp          = Column(Integer, nullable=False)
    sprite_url      = Column(String,  default="")
    evolution_id    = Column(Integer, nullable=True)
    evolution_level = Column(Integer, nullable=True)
    in_party        = Column(Boolean, default=True)   # False = in the PC box

    # Base stats (denormalised for simplicity)
    base_hp      = Column(Integer, nullable=False)
    base_attack  = Column(Integer, nullable=False)
    base_defense = Column(Integer, nullable=False)
    base_speed   = Column(Integer, nullable=False)

    trainer = relationship("TrainerSchema", back_populates="pokemon")

    # ------------------------------------------------------------------
    # TODO: add a helper method that converts this DB row into a Pokemon
    #       model object so routes don't have to do the mapping manually.
    #
    # def to_model(self) -> Pokemon:
    #     from models import Pokemon
    #     return Pokemon(
    #         pokedex_id  = self.pokedex_id,
    #         name        = self.name,
    #         types       = self.types.split(","),
    #         base_stats  = { "hp": self.base_hp, ... },
    #         level       = self.level,
    #         sprite_url  = self.sprite_url,
    #         ...
    #     )
    # ------------------------------------------------------------------


class EggSchema(Base):
    """Maps to the 'eggs' table."""
    __tablename__ = "eggs"

    id         = Column(Integer, primary_key=True, index=True)
    trainer_id = Column(Integer, ForeignKey("trainers.id"), nullable=False)
    pokedex_id = Column(Integer, nullable=False)
    sprite_url = Column(String,  default="")
    is_hatched = Column(Boolean, default=False)

    trainer = relationship("TrainerSchema", back_populates="eggs")


class BattleLogSchema(Base):
    """Stores a summary of each battle for the history screen."""
    __tablename__ = "battle_logs"

    id                  = Column(Integer, primary_key=True, index=True)
    trainer_id          = Column(Integer, ForeignKey("trainers.id"), nullable=False)
    player_pokemon_name = Column(String)
    opponent_name       = Column(String)
    result              = Column(String)   # "win" | "loss" | "draw"
    rounds_played       = Column(Integer)
    # TODO: store the full round log as JSON string if you want replay functionality
