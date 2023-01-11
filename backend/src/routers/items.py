from fastapi import APIRouter
router = APIRouter()


@router.post('/item')
async def create_item(item): 
    print(item)
    return {'answer': 'ok'}