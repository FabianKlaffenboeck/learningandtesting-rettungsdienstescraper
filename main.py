from data_objects import Duty
from duty_plan_handler import parse_duties_json, get_own_duties
from login_handler import get_login
import os
import json
import time

if __name__ == '__main__':

    uname = os.environ['UNAME']
    pwd = os.environ['PWD']
    rate = int(os.environ['RATE'])

    if uname is None or pwd is None:
        raise Exception('Please set environment variables UNAME and PWD')

    if rate <= 0:
        raise Exception("rate must be positive")

    while True:
        login_credentials = get_login(uname, pwd)
        selve_duties = parse_duties_json(get_own_duties(login_credentials))
        print(json.dumps([obj.__dict__ for obj in selve_duties]))
        time.sleep(rate)

    # plan = parse_duty_plan_json(get_duty_plan_json(login_credentials,'2025-02-03', '2025-02-11'))
    # print(plan)
