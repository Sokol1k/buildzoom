from sqlalchemy import Column, String, Integer, Float, Boolean, JSON, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base


class ContractorModel(declarative_base()):
    __tablename__ = 'contractor'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    url = Column('url', String, nullable=False, unique=True, index=True)
    description = Column('description', String)
    category = Column('category', String)
    rating = Column('rating', Float)
    rating_buildzoom = Column('rating_buildzoom', Integer)
    phone = Column('phone', String)
    email = Column('email', String)
    website = Column('website', String)
    is_licensed = Column('is_licensed', Boolean, default=False)
    license_info = Column('license_info', JSON)
    insured_value = Column('insured_value', String)
    bond_value = Column('bond_value', String)
    street_address = Column('street_address', String)
    city = Column('city', String)
    state = Column('state', String)
    zipcode = Column('zipcode', String)
    full_address = Column('full_address', String)
    image = Column('image', String)
    info_updated_at = Column('info_updated_at', String)
    employee = Column('employee', JSON)
    work_preferences = Column('work_preferences', JSON)
    create_at = Column('create_at', TIMESTAMP,
                       server_default=text('now()'), nullable=False)
    updated_at = Column('updated_at', TIMESTAMP,
                        server_default=text('now()'), server_onupdate=text('now()'), nullable=False)
