from sqlalchemy.orm import Session
import schemas
import database
import practice
def get_authors(db:Session):
    return db.query(practice.Author).all()

def create_author(db:Session, author:schemas.AuthorCreate):
    db_author = practice.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
def get_books(db:Session):
    return db.query(practice.Book).all()
def create_book(db:Session, book:schemas.BookCreate):
    db_book = practice.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book