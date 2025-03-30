from duty_plan_handler import parse_duties_json, get_own_duties
from login_handler import get_login
import os

if __name__ == '__main__':

    uname = os.environ['UNAME']
    pwd = os.environ['PWD']

    login_credentials = get_login(uname,pwd)

    selve_duties = parse_duties_json(get_own_duties(login_credentials))
    print( selve_duties)

    # plan = parse_duty_plan_json(get_duty_plan_json(login_credentials,'2025-02-03', '2025-02-11'))
    # print(plan)
