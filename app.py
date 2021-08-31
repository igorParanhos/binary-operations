from store.services import check_is_opened_today
from store.models import DayOfTheWeek, Store


def main():
    print('Starting Application...')

    store = Store(opened_days=DayOfTheWeek.MONDAY | DayOfTheWeek.TUESDAY)

    print(store)
    print(DayOfTheWeek.MONDAY)
    print(check_is_opened_today(store, 1))

if __name__ == '__main__':
    main()