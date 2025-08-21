from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import schemas, crud, database, practice
from database import SessionLocal, engine, Base
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Library API"
      )
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)
@app.get("/authors/", response_model=list[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db=db)
@app.post("/book/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)
@app.get("/book/", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)