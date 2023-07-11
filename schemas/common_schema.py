from pydantic import BaseModel as SCBaseModel


class CommonSchema(SCBaseModel):
    title: str
    message: str
    type: str
