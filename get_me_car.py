from carFactory import CarFactory
from datetime import datetime

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 5)

c1 = CarFactory().get_Calliope(last_service_date, 90000, 80000, False)

print(c1.needs_service())
