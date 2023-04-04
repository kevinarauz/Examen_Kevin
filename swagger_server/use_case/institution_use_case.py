from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData
import logging

class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):
        """
            Lista de instutition
        :return:
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response
        )

        return response

    def get_institution_by_id(self, institution_id):
        """
            Obtiene una institución por su ID
        :param institution_id:
        :return:
        """

        institution = self.institution_repository.get_institution_by_id(institution_id)

        if institution:
            data_response = ResponseInstitutionData(
                id=institution.id,
                name=institution.name,
                description=institution.description,
                address=institution.address,
                created_user=institution.created_user,
                created_at=institution.created_at,
                status=institution.status
            )
            logging.info(f"Update Exitoso: {data_response}")
            response = ResponseInstitution(
                code=200,
                message="proceso exitoso",
                data=data_response
            )
        else:
            response = ResponseInstitution(code=-1, message="no se pudo encontrar la institución")

        return response