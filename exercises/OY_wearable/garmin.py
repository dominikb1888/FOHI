import os, sys, datetime

from garminconnect import Garmin

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
today = datetime.date.today()

api = Garmin(email, password)
api.login()

heartrates = api.get_heart_rates(f'{today.isoformat()}')
bloodoxy = api.get_spo2_data(f'{today.isoformat()}')
breathing = api.get_respiration_data(f'{today.isoformat()}')
print(heartrates, bloodoxy, breathing)
