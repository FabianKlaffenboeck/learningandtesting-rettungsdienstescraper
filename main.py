from data_objects import Duty
import paho.mqtt.client as paho
from duty_plan_handler import parse_duties_json, get_own_duties
from login_handler import get_login
import os
import json
import time

if __name__ == '__main__':

    uname = os.environ['UNAME']
    pwd = os.environ['PWD']

    rate = int(os.environ['RATE'])

    mqtt_addr = os.environ['MQTT_ADDR']
    mqtt_topic = os.environ['MQTT_TOPIC']
    mqtt_pw = os.environ['MQTT_PW']
    mqtt_uname = os.environ['MQTT_UNAME']

    if uname is None or pwd is None:
        raise Exception('Please set environment variables UNAME and PWD')

    if rate <= 0:
        raise Exception("rate must be positive")

    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.username_pw_set(mqtt_uname, mqtt_pw)
    client.connect(mqtt_addr, 1883)

    while True:
        login_credentials = get_login(uname, pwd)
        selve_duties = parse_duties_json(get_own_duties(login_credentials))
        data = json.dumps([obj.__dict__ for obj in selve_duties])
        print(data)
        client.publish(mqtt_topic, payload=data, qos=1)
        time.sleep(rate)

    # plan = parse_duty_plan_json(get_duty_plan_json(login_credentials,'2025-02-03', '2025-02-11'))
    # print(plan)
