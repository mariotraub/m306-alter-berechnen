from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys


DATE_FORMAT = "%d.%m.%Y"


class DateDiff():
    def __init__(self, days: int, rel_delta: relativedelta) -> None:
        self.days: int = days
        self.rel_delta: relativedelta = rel_delta


def read_input() -> list[str]:
    return sys.argv[1:]


def validate_dates(input: list[str]) -> list[datetime]:
    try:
        return [
            datetime.strptime(date, DATE_FORMAT) for date in input
        ]
    except ValueError:
        print("Die eingegebenen Daten sind nicht valide.", file=sys.stderr)
        exit(1)


def get_diffs_to_now(dates: list[datetime]) -> list[DateDiff]:
    now = datetime.now()

    return [
        DateDiff(
            (now - date).days,
            relativedelta(now, date)
        ) for date in dates
    ]



def print_diffs(diffs: list[DateDiff]):
    for diff in diffs:
        years = diff.rel_delta.years
        months = diff.rel_delta.months
        days = diff.rel_delta.days

        total_days = diff.days
        print(f"Das Alter ist {years} Jahre {months} Monate und {days} Tage, das sind {total_days} Tage")


if __name__ == "__main__":
    input = read_input()
    dates = validate_dates(input)
    diffs = get_diffs_to_now(dates)
    print_diffs(diffs) 
