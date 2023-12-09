from abc import ABC, abstractmethod
import pickle
from typing import Any


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource='') -> None:
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def __dump(self) -> None:
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))
        
    def __load(self) -> None:
        self.__cache = pickle.load(open(self.__datasource, 'rb'))
        
    def add(self, key, obj) -> None:
        self.__cache[key] = obj
        self.__dump()
        
    def get(self, key) -> Any:
        return self.__cache[key]
    
    def remove(self, key) -> None:
        self.__cache.pop(key)
        self.__dump()
        
    def get_all(self) -> list:
        return self.__cache.values()