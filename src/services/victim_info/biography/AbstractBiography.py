from abc import ABC, abstractmethod
import asyncio


class AbstractBiography(ABC):
    instances: list['AbstractBiography'] = []

    def __init__(self):
        AbstractBiography.instances.append(self)

    @abstractmethod
    async def get_biography(self, username: str) -> str:
        raise NotImplementedError("get_biography method is not implemented")