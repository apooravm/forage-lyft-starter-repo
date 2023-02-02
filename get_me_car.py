from carFactory import CarFactory
from datetime import datetime

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 1)

c1 = CarFactory().get_Calliope(last_service_date, 90000, 1)

print(c1.needs_service())
