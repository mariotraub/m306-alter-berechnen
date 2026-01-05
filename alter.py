from datetime import datetime
# Dieses Packages hilft die Differenzen der Daten richtig zu berechnen
from dateutil.relativedelta import relativedelta
import sys


DATE_FORMAT = "%d.%m.%Y"
NOW = datetime.now()


class DateDiff():
    def __init__(self, days: int, rel_delta: relativedelta) -> None:
        self.days: int = days
        self.rel_delta: relativedelta = rel_delta


def read_input() -> list[str]:
    return sys.argv[1:]


def validate_dates(input: list[str]) -> list[datetime]:
    try:
        dates: list[datetime] = []
        for string in input:
            date = datetime.strptime(string, DATE_FORMAT)
            # Überprüfen ob Datum in der Zukunft liegt
            if date > NOW:
               print("Mindestens ein eingegebenes Datum befindet sich in der Zukunft", file=sys.stderr)
               exit(1)
            dates.append(date)
        return dates
    # Wenn dieser Error geworfen wird, ist das Datum im falschen Format
    except ValueError:
        print("Die eingegebenen Daten sind im falschen Format.", file=sys.stderr)
        exit(1)


def get_diffs_to_now(dates: list[datetime]) -> list[DateDiff]:
    return [
        # Alle nötigen Daten werden in einem DateDiff-Objekt gewrapped
        DateDiff(
            (NOW - date).days,
            relativedelta(NOW, date)
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
