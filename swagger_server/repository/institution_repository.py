import logging
from swagger_server.models.Institution import Institution
sql_select = "select * from institution where status = 'A'"
sql_search = "select * from institution where status = 'A' AND id = :institution_id"
class InstitutionRepository:

    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory

    def get_institution(self):
        with self.session_factory() as session:
            rows = session.execute(sql_select)
            return rows

    def get_institution_by_id(self, institution_id):
        with self.session_factory() as session:
            logging.info(f"Consultar Institution por ID: ")
            logging.info(f"Query: {sql_search}")
            logging.info(f"Id: {institution_id}")
            result = session.execute(sql_search, {"institution_id": institution_id})
            row = result.fetchone()
            if row is not None:
                institution = Institution(
                    address=row['address'],
                    created_at=row['created_at'],
                    created_user=row['created_user'],
                    description=row['description'],
                    id=row['id'],
                    name=row['name'],
                    status=row['status'],
                    updated_at=row['updated_at'],
                    updated_user=row['updated_user']
                )
                return institution
            else:
                raise ValueError(f"Institución con ID {institution_id} no encontrada")