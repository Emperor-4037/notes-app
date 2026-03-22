from typing import Generic, Type, TypeVar, Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    
    def __init__(self, model : Type[ModelType], session : AsyncSession):
        self.model = model
        self.session = session

    async def create(self, obj : ModelType) -> ModelType:
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def get_by_id(self, obj_id : int) -> Optional[ModelType]:
        return await self.session.get(self.model, obj_id)


    async def get_all(self) -> Sequence[ModelType]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()
    
    async def delete(self, obj : ModelType) -> bool:
        await self.session.delete(obj)
        await self.session.commit()
        return True

    async def update(self, obj : ModelType, data : dict) -> ModelType:
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        
        await self.session.commit()
        await self.session.refresh(obj)
        return obj
    