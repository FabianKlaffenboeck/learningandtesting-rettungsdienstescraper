import requests
import re
import json

def get_login(uname, pwd):
    data = {
        "client": "RKOOE",
        "login": uname,
        "password": pwd,
    }

    session = requests.Session()
    session.post(
        'https://dienstplan.o.roteskreuz.at/login.php',
        data=data,
    )

    session_id = session.cookies.get("PHPSESSID")

    response = requests.get(
        'https://dienstplan.o.roteskreuz.at',
        cookies={'PHPSESSID': session_id},
    )

    match = re.search(r"\{.*?\}",
                      re.search(r"\$.ajaxSetup\(\{\s*headers:\s*\{.*?\}\s*\}\s*\);", response.content.decode()).group(
                          0)).group(0)

    ajex_cred = re.sub(re.escape("{ headers: "), "", match).replace("'", '"')

    ajex_header=json.loads(ajex_cred)

    return [session_id, ajex_header]
