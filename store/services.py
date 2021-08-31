from .models import DayOfTheWeek, Store


def check_is_opened_today(store: Store, day_of_the_week: int):
    return DayOfTheWeek[day_of_the_week] in store.opened_days
