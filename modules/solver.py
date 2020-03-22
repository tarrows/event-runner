from dataclasses import dataclass
from typing import Dict


@dataclass
class Material:
    material_id: int
    name: str


@dataclass
class Quest:
    name: str
    income: Dict[int, int]
    consumption: int


@dataclass
class Reward:
    name: str
    count: int
    material_id: int
    require: int


@dataclass
class Solver:
    """
    solve Ax >= y
    """
    def solve(self):
        pass
