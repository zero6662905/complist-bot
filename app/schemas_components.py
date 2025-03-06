from pydantic import BaseModel


class components(BaseModel):
    title: str
    desc: str
    url: str