# A Program to create reusable date utility functions for date manipulation and formatting

from datetime import datetime, timedelta


def current_date():
    return datetime.now().date()


def days_from_today(days):
    return current_date() + timedelta(days=days)


def format_date(date):
    return date.strftime("%d-%m-%Y")
