from abc import ABC, abstractmethod

from engine.model.calliope import Calliope
from engine.model.thovex import Thovex
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.glissade import Glissade

from datetime import datetime
date = datetime.today().date()

class CarFactory:
    @staticmethod
    def get_Calliope(last_service_date=date, current_mileage=0, last_service_mileage=0, indicator_warning=False, tyreSensorArray=[0, 0, 0, 0]):
        return Calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning, tyreSensorArray=tyreSensorArray)

    @staticmethod
    def get_Thovex(last_service_date=date, current_mileage=0, last_service_mileage=0, indicator_warning=False, tyreSensorArray=[0, 0, 0, 0]):
        return Thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning, tyreSensorArray=tyreSensorArray)

    @staticmethod
    def get_Palindrome(last_service_date=date, current_mileage=0, last_service_mileage=0, indicator_warning=False, tyreSensorArray=[0, 0, 0, 0]):
        return Palindrome(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning, tyreSensorArray=tyreSensorArray)
    @staticmethod
    def get_Rorschach(last_service_date=date, current_mileage=0, last_service_mileage=0, indicator_warning=False, tyreSensorArray=[0, 0, 0, 0]):
        return Rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning, tyreSensorArray=tyreSensorArray)
    @staticmethod
    def get_Glissade(last_service_date=date, current_mileage=0, last_service_mileage=0, indicator_warning=False, tyreSensorArray=[0, 0, 0, 0]):
        return Glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage, indicator_warning=indicator_warning, tyreSensorArray=tyreSensorArray)
