from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import insert
from database.models.UrlsModel import UrlsModel
from database.models.ContractorModel import ContractorModel


class Connection(object):
    def __init__(self):
        self.engine = create_engine(
            'mysql+pymysql://root:@localhost:3306/buildzoom')

    def setUrl(self, item):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        url = session.query(UrlsModel).filter_by(url=item['url']).first()

        if not url:
            url = UrlsModel()
            url.url = item['url']
            url.status = item['status']

        try:
            session.add(url)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

    def setContractor(self, item):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        contractor = session.query(ContractorModel).filter_by(
            url=item['url']).first()

        if not contractor:
            contractor = ContractorModel()
            contractor.url = item['url']
        contractor.name = item['name']
        contractor.description = item['description']
        contractor.category = item['category']
        contractor.rating = item['rating']
        contractor.rating_buildzoom = item['rating_buildzoom']
        contractor.phone = item['phone']
        contractor.email = item['email']
        contractor.website = item['website']
        contractor.is_licensed = item['is_licensed']
        contractor.license_info = item['license_info']
        contractor.insured_value = item['insured_value']
        contractor.bond_value = item['bond_value']
        contractor.street_address = item['street_address']
        contractor.city = item['city']
        contractor.state = item['state']
        contractor.zipcode = item['zipcode']
        contractor.full_address = item['full_address']
        contractor.image = item['images'][0]['path']
        contractor.info_updated_at = item['info_updated_at']
        contractor.employee = item['employee']
        contractor.work_preferences = item['work_preferences']
        contractor.updated_at = text('now()')

        try:
            session.add(contractor)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

    def getUrl(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        url = session.query(UrlsModel).filter_by(status=0).first()
        session.close()
        return url

    def changeUrlStatus(self, id, status):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        url = session.query(UrlsModel).filter_by(id=id).first()
        url.status = status

        try:
            session.add(url)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return
