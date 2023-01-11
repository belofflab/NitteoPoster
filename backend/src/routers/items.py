from fastapi import APIRouter
from src.schemas import EditAsset
router = APIRouter()


@router.post('/item')
async def create_item(item: EditAsset): 
    print(item)
    return {'answer': 'ok'}