from pydantic import BaseModel

class EditAsset(BaseModel):
  title_birg: str 
  title_pair_give: str 
  title_pair_get: str 
  pair_give: str 
  pair_get: str 