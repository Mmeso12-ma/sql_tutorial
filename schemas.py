from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str
    bio: str | None = None
    nationality: str | None = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    published_year: int | None = None
    available: bool = True

class BookCreate(BookBase):
    author_id: int

class Book(BookBase):
    id: int
    author: Author

    class Config:
        orm_mode = True