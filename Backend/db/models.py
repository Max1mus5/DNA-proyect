from sqlalchemy import Column, String, Integer
from db.database import Base

class DnaSequence(Base):
    __tablename__ = 'dna_sequences'
    
    id = Column(Integer, primary_key=True, index=True)
    sequence = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
