from abc import ABC, abstractmethod

from engine.model.calliope import Calliope
from engine.model.thovex import Thovex
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.glissade import Glissade

class CarFactory:
    @staticmethod
    def get_Calliope(last_service_date, current_mileage, last_service_mileage, indicator_warning):
        return Calliope(last_service_date, current_mileage, last_service_mileage, indicator_warning)

    @staticmethod
    def get_Thovex(last_service_date, current_mileage, last_service_mileage, indicator_warning):
        return Thovex(last_service_date, current_mileage, last_service_mileage, indicator_warning)

    @staticmethod
    def get_Palindrome(last_service_date, current_mileage, last_service_mileage, indicator_warning):
        return Palindrome(last_service_date, current_mileage, last_service_mileage, indicator_warning)
    @staticmethod
    def get_Rorschach(last_service_date, current_mileage, last_service_mileage, indicator_warning):
        return Rorschach(last_service_date, current_mileage, last_service_mileage, indicator_warning)
    @staticmethod
    def get_Glissade(last_service_date, current_mileage, last_service_mileage, indicator_warning):
        return Glissade(last_service_date, current_mileage, last_service_mileage, indicator_warning)
