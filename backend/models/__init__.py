# Expose all models from one place so routes can do:
#   from models import Pokemon, Trainer, Battle, Egg, Move

from .pokemon import Pokemon
from .move import Move
from .trainer import Trainer
from .battle import Battle, BattleRound
from .egg import Egg

__all__ = ["Pokemon", "Move", "Trainer", "Battle", "BattleRound", "Egg"]
