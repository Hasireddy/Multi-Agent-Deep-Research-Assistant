from pydantic import BaseModel, Field

class SubQuestion(BaseModel):
    id: int = Field(default=0,ge=0,description="stable index for referring to subquestion")
    question: str = Field(min_length=1, description="single searchable question")
    rationale: str = Field(default="", description="One line on why answering this helps")


class PlanResponse(BaseModel):
    sub_questions: list[SubQuestion] = Field(description="Three to five focussed sub questions")


