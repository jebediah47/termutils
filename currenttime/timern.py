from datetime import datetime
import pytz

green_time = pytz.timezone("Etc/Greenwich")
datetime_GREEN = datetime.now(green_time)
print("Greenwich time:", datetime_GREEN.strftime("%H:%M:%S"))

now = datetime.now()
timern = now.strftime("%H:%M:%S")
print("Current time:", timern)
