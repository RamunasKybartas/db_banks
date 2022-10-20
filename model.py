# Padaryti programą, kurį leistų įvesti asmenis, bankus, asmenims priskirti sąskaitas bankuose.

# Asmuo turi vardą, pavardę, asmens kodą, tel. numerį.
# Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
# Sąskaita turi numerį, balansą, priskirtą asmenį ir banką
# Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose bankuose
# Padaryti duomenų bazės schemą (galima ją parodyti dėstytojui).
# Sukurti programą su UI konsolėje, kuri leistų įvesti asmenis, bankus, sąskaitas.
#  Leistų vartotojui peržiūrėti savo sąskaitas ir jų informaciją, pridėti arba nuimti iš jų pinigų. 
#  Taip pat leistų bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų informaciją.

# def create_object(object_class, **kwargs):
#     obj = object_class(**kwargs)
#     session.add(obj)
#     session.commit()
#     return obj

from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///saskaitos.db')
Base = declarative_base()


class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    asmens_kodas = Column("Asmens kodas", Integer, unique=True)
    el_pastas = Column("El. pašto adresas", String)
    saskaitos = relationship ("Saskaita", back_populates="asmuo")

    def __repr__(self):
        return f"{self.id}: {self.vardas} {self.pavarde}, {self.asmens_kodas}, {self.el_pastas}"

class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    adresas = Column("Adresas", String)
    banko_kodas = Column("Banko kodas", Integer)
    swift_kodas = Column("SWIFT kodas", String)
    saskaitos = relationship("Saskaita", back_populates = "bankas")

    def __repr__(self):
        return f"{self.id}: {self.pavadinimas}, {self.adresas}, {self.banko_kodas}, {self.swift_kodas}"

class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key=True)
    numeris = Column("Sąskaitos numeris", Integer)
    balansas = Column("Pinigų balansas", Float)
    asmuo_id = Column("asmuo_id", Integer, ForeignKey('asmuo.id'))
    asmuo = relationship("Asmuo", back_populates = "saskaitos")
    bankas_id = Column("bankas_id", Integer, ForeignKey('bankas.id'))
    bankas = relationship("Bankas", back_populates = "saskaitos")

    def __repr__(self):
        return f"{self.id}: {self.numeris}, {self.balansas}, {self.asmuo}, {self.bankas}"


Base.metadata.create_all(engine)