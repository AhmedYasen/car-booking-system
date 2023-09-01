from apscheduler.schedulers.background import BackgroundScheduler
from src.models.booking import Booking
from datetime import datetime
import logging


def booking_today():
    success, data = Booking().read_by_hire_date(datetime.today())
    logging.info(f"Bookings for Today {datetime.today()}:\n\n{data}")


def report_everyday():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(booking_today, 'cron', hour=1, minute=0)
    scheduler.start()
