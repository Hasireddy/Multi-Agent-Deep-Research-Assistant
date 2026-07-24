from pydantic import BaseModel, Field

class SearchResultSchema(BaseModel):
    subquestion_id: int = Field(default=0,ge=0,description="stable index for referring the subquestion")
    url: str = Field(min_length=1, description="single searched question url")
    title: str = Field(min_length=1, description="title of searched result")
    content: str = Field(min_length=1, description="Content of the result")
