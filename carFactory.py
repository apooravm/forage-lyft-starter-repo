from abc import ABC, abstractmethod

from engine.model.calliope import Calliope
from engine.model.thovex import Thovex
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.glissade import Glissade

class CarFactory:
    @staticmethod
    def get_Calliope(last_service_date=0, current_mileage=0, last_service_mileage=0, indicator_warning=False):
        return Calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning)

    @staticmethod
    def get_Thovex(last_service_date=0, current_mileage=0, last_service_mileage=0, indicator_warning=False):
        return Thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning)

    @staticmethod
    def get_Palindrome(last_service_date=0, current_mileage=0, last_service_mileage=0, indicator_warning=False):
        return Palindrome(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning)
    @staticmethod
    def get_Rorschach(last_service_date=0, current_mileage=0, last_service_mileage=0, indicator_warning=False):
        return Rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning)
    @staticmethod
    def get_Glissade(last_service_date=0, current_mileage=0, last_service_mileage=0, indicator_warning=False):
        return Glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning)
