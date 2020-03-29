from dataclasses import dataclass
from typing import Dict, List


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


class Solver:
    """
    solve Ax >= y
    """
    def solve(self):
        pass

    @classmethod
    def from_items(cls, materials: List[Material], quests: List[Quest], rewards: List[Reward]):
        """create solver with varidation"""
        pass
