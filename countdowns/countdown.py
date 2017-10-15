import datetime
import sys


def str_to_date(str_dt):
    """
    Converts string to date -- must be in YYYY-MM-DD format
    :param dt:
    :return:
    """

    return datetime.datetime.strptime(str_dt, '%Y-%m-%d').date()


def check_date_valid(possible_date):
    """
    Checks if date is valid
    :param possible_date: needs to be in YYYY-MM-DD format otherwise it won't work
    :return:
    """

    is_good_date = False

    if type(possible_date) == str and str_to_date(possible_date):       # it's a string and can be converted to date
        tested_date = str_to_date(possible_date)
        is_good_date = True

    elif type(possible_date) == datetime.date:
        tested_date = possible_date
        is_good_date = True

    else:
        is_good_date = False
        tested_date = None

    return is_good_date, tested_date


def check_end_date_bigger(start_dt, end_dt):
    """
    Checks to see that end_dt is greater (more in the future) than start_dt
    :param start_dt:
    :param end_dt:
    :return:
    """

    is_logical = False

    if type(start_dt) == str:
        start_dt = str_to_date(start_dt)

    if type(end_dt) == str:
        end_dt = str_to_date(end_dt)

    if end_dt > start_dt:
        is_logical = True

    if not is_logical:
        print("THAT DOESN'T EVEN MAKE SENSE; CHECK YOUR DATES: start = {} & end = {}".format(start_dt, end_dt))

    return is_logical


def diff_between_dates(start_dt, end_dt):
    """
    Calculates the delta between the dates
    :param start_dt: date obj
    :param end_dt: date obj
    :return: time delta in days, weeks, days post the week, months
    """
    days_between = (end_dt - start_dt).days
    weeks_between, days_after_week = round(days_between/7), (days_between%7)
    months_between = ((end_dt.year - start_dt.year) * 12) + (end_dt.month - start_dt.month)

    return days_between, weeks_between, days_after_week, months_between


def main():

    if len(sys.argv) == 3:    # start and end dates provided
        start_dt = sys.argv[1]
        end_dt = sys.argv[2]

    elif len(sys.argv) == 2:     # only end date provided, assume today is start date
        start_dt = datetime.date.today()
        end_dt = sys.argv[1]

    else:
        print("""Provide either an end date to calculate the time delta between today and then
        OR provide start and end dates to calculate the time deltas between them.""")

    # calculate things now....

    # start
    valid_start_date, start_date = check_date_valid(start_dt)

    # end
    valid_end_date, end_date = check_date_valid(end_dt)

    # valid dates and calculation is logical
    if valid_start_date and valid_end_date and check_end_date_bigger(start_date, end_date):
        days, weeks, weeks_post_days, months = diff_between_dates(start_date, end_date)

        output_msg = """
        START DATE: {}
        END DATE: {}

        --- COUNTDOWN ---
        IN DAYS: {}
        IN WEEKS: {} (and {} days)
        IN MONTHS: {}
        """.format(start_date, end_date,days, weeks, weeks_post_days, months)

        print(output_msg)


main()
