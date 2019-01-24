#!/bin/python

import argparse
import os
import time

from auth import TOKEN_FILENAME, test_api_token, token_file_path
from datetime import datetime, timedelta
from todoist.api import TodoistAPI

def due_today_count(api):
    dueToday = 0
    for item in api.state['items']:
        dueDate = item['due_date_utc']
        completed = item['checked']
        if dueDate is not None:
            dueDate = dueDate[:15]
            dueTimestamp = datetime.strptime(dueDate, '%a %d %b %Y')
            today = datetime.today()

            if (today - dueTimestamp).total_seconds() > 0 and not completed:
                dueToday += 1

    return dueToday

def due_this_week(api):
    dueThisWeek = 0
    for item in api.state['items']:
        dueDate = item['due_date_utc']
        completed = item['checked']
        if dueDate is not None:
            dueDate = dueDate[:15]
            dueTimestamp = datetime.strptime(dueDate, '%a %d %b %Y')
            today = datetime.today()
            thisWeek = today + timedelta(weeks=1)

            if (thisWeek - dueTimestamp).total_seconds() > 0 and not completed:
                dueThisWeek += 1

    return dueThisWeek

def print_loop(api, prefix, weekly):
    REFRESH_RATE = 5

    while True:
        api.sync()

        dueToday = due_today_count(api)

        if weekly:
            dueThisWeek = due_this_week(api)

            output = f'{dueToday} {prefix} {dueThisWeek}'
        else:
            output = f'{prefix} {dueToday}'

        print(output, flush=True)
        time.sleep(REFRESH_RATE)

def load_api():
    filepath = token_file_path(TOKEN_FILENAME)

    if not os.path.isfile(filepath):
        print(f'API Token file \'{TOKEN_FILENAME}\' missing. Run \'python auth.py\'')
        exit(1)

    with open(filepath) as file:
        token = file.read()

    if not test_api_token(token):
        print('Bad API token. Run \'python auth.py\'')
        exit(1)

    return TodoistAPI(token)

def main():
    ICON = '\uf058'

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prefix', default=ICON)
    parser.add_argument('-w', '--weekly', action='store_true')
    args = parser.parse_args()

    api = load_api()

    print_loop(api, args.prefix, args.weekly)


if __name__ == "__main__":
    main()
