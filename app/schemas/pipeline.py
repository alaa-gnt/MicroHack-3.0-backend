from pydantic import BaseModel
from typing import List, Optional

class PipelineResponse(BaseModel):
    id: str
    status: str

    class Config:
        from_attributes = True
