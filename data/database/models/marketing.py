import sqlalchemy
from ..db_session import SqlAlchemyBase


class Marketing_Data(SqlAlchemyBase):
    __tablename__ = 'marketing'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    Advertising_Category = sqlalchemy.Column(sqlalchemy.Text, nullable=True, unique=True)
    Costs = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Leads = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Leads_Final = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Leads_Not_Called = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Сost_Per_Lead = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Сost_Per_Lead_Final = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    deals = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Agreement_Epe_or_Collection = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Additional_Services = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Upsells = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Deals_BFLA = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Percent_Lead_to_LeadFinal = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    Percent_LeadFinal_to_Agreement_Epe_or_Collection = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    Cost_Deal_Epe_or_Collection = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
