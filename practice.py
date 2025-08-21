from sqlalchemy import Integer, String
from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    bio = Column(String, nullable=True)
    nationality = Column(String, nullable=True)
    books = relationship("Book", back_populates="author")
class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    published_year = Column(Integer, nullable=True)
    
    available = Column(Boolean, default=True)
class BookAuthor(Base):
    __tablename__ = "book_author"
    book_id = Column(Integer, ForeignKey("book.id"), primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.id"), primary_key=True)
    book = relationship("Book", back_populates="authors")
    author = relationship("Author", back_populates="books")
    books = relationship("Book", secondary="book_author", back_populates="authors")
    authors = relationship("Author", secondary="book_author", back_populates="books")