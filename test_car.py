import unittest
from datetime import datetime

# from engine.model.calliope import Calliope
# from engine.model.glissade import Glissade
# from engine.model.palindrome import Palindrome
# from engine.model.rorschach import Rorschach
# from engine.model.thovex import Thovex

from carFactory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.get_Calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.get_Calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 3000
        last_service_mileage = 0

        car = CarFactory.get_Calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.get_Calliope(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyreSensorArray = [0.1, 0.1, 0.5, 0.1]
        car = CarFactory.get_Calliope(tyreSensorArray=tyreSensorArray)
        self.assertFalse(car.needs_service())

    def test_tyre_should_be_serviced(self):
        tyreSensorArray = [1, 1, 1, 0.9]
        car = CarFactory.get_Calliope(tyreSensorArray=tyreSensorArray)
        self.assertTrue(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.get_Glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        warning_light = False

        car = CarFactory.get_Glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        warning_light = False

        car = CarFactory.get_Glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        warning_light = False

        car = CarFactory.get_Glissade(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyreSensorArray = [0.1, 0.1, 0.5, 0.1]
        car = CarFactory.get_Glissade(tyreSensorArray=tyreSensorArray)
        self.assertFalse(car.needs_service())

    def test_tyre_should_be_serviced(self):
        tyreSensorArray = [0.1, 0.1, 1, 0.1]
        car = CarFactory.get_Glissade(tyreSensorArray=tyreSensorArray)
        self.assertTrue(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        car = CarFactory.get_Palindrome(last_service_date=last_service_date, indicator_warning=warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        car = CarFactory.get_Palindrome(last_service_date=last_service_date, indicator_warning=warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = CarFactory.get_Palindrome(last_service_date=last_service_date, indicator_warning=warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = CarFactory.get_Palindrome(last_service_date=last_service_date, indicator_warning=warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyreSensorArray = [0.1, 0.1, 0.5, 0.1]
        car = CarFactory.get_Palindrome(tyreSensorArray=tyreSensorArray)
        self.assertFalse(car.needs_service())

    def test_tyre_should_be_serviced(self):
        tyreSensorArray = [0.1, 0.1, 1, 0.1]
        car = CarFactory.get_Palindrome(tyreSensorArray=tyreSensorArray)
        self.assertTrue(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.get_Rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.get_Rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.get_Rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory.get_Rorschach(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyreSensorArray = [0.1, 0.1, 0.5, 0.1]
        car = CarFactory.get_Rorschach(tyreSensorArray=tyreSensorArray)
        self.assertFalse(car.needs_service())

    def test_tyre_should_be_serviced(self):
        tyreSensorArray = [1, 1, 1, 0.9]
        car = CarFactory.get_Rorschach(tyreSensorArray=tyreSensorArray)
        self.assertTrue(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.get_Thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.get_Thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.get_Thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.get_Thovex(last_service_date=last_service_date, current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyreSensorArray = [0.1, 0.1, 0.5, 0.1]
        car = CarFactory.get_Thovex(tyreSensorArray=tyreSensorArray)
        self.assertFalse(car.needs_service())

    def test_tyre_should_be_serviced(self):
        tyreSensorArray = [1, 1, 1, 0.9]
        car = CarFactory.get_Thovex(tyreSensorArray=tyreSensorArray)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()