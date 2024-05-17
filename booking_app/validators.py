from django.contrib import messages
from datetime import datetime

def validate_booking_range(request, start_date, end_date):
  if start_date > end_date:
    messages.error(request, "Please make the drop off date after the pick up date")
    return False
  if start_date <= datetime.now():
    messages.error(request, "Choose a date in the future")
    return False
  return True
