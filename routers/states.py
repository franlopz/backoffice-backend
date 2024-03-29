from api import get_current_active_user
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from pydantic.utils import GetterDict
import peewee
from typing import Any, Dict, List
from crud.state import create_states, get_states
from crud.token import User
from api import get_current_active_user

router_states = APIRouter(
    prefix="/states",
    tags=["states"]
)


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class StatesModel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class ResponseModel(BaseModel):
    __root__: Dict[str, List[str]]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


@router_states.post("/")
def createStates(states: List[StatesModel], current_user: User = Depends(get_current_active_user)):
    temp = []
    for state in states:
        temp.append(state.dict())
    #     print(producto.producto)
    print(temp)
    states = create_states(temp)
    return states


@router_states.get("/", response_model=ResponseModel)
def fetch_states(current_user: User = Depends(get_current_active_user)):
    result = get_states()
    return result
