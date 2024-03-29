from api import get_current_active_user
from crud.cities import create_cities
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from pydantic.utils import GetterDict
import peewee
from typing import Any, List
from crud.token import User

router_cities = APIRouter(
    prefix="/cities",
    tags=["cities"]
)


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class CitiesModel(BaseModel):
    id: int
    stateId: int
    name: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


@router_cities.post("/")
def createCities(cities: List[CitiesModel], current_user: User = Depends(get_current_active_user)):
    temp = []
    for city in cities:
        temp.append(city.dict())
    #     print(producto.producto)
    print(temp)
    create_cities(temp)
    return
