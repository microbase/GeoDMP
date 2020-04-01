import requests
import argparse


def login_and_process(id, pw, next):
    # ログインに必要な情報
    URL = "http://3.113.131.37:8000/accounts/login/"
    ID = str(id)
    PASS = str(pw)
    NEXT = next

    session = requests.session()
    res = session.get(URL)
    print(res)
    csrf = session.cookies['csrftoken']

    login_info = {
        "csrfmiddlewaretoken": csrf,
        "username": ID,
        "password": PASS,
        "next": NEXT,
    }

    response = session.post(URL, data=login_info, headers=dict(Referer=URL))

    return response


def latlon_to_income(id, pw, lat, lon):
    next = "http://3.113.131.37:8000/highincome_api/latloninput/result?input_lon={}&input_lat={}&input_radius={}".format(
        lon, lat, rad)

    responce = login_and_process(id, pw, next)

    print(responce.json())


def latlon_to_railline(id, pw, lat, lon):
    next = "http://3.113.131.37:8000/highincome_api/latloninput_railline/result?input_lon={}&input_lat={}&input_radius={}".format(
        lon, lat, rad)

    responce = login_and_process(id, pw, next)

    print(responce.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--id', type=str, required=True)
    parser.add_argument('-p', '--pw', type=str, required=True)
    parser.add_argument('-m', '--mode', type=str, required=True,
                        help='Please input mode. lti : latlon to income, ltr : latlon to raillineassessment')
    parser.add_argument('-lat', '--latitude', type=float, required=False)
    parser.add_argument('-lon', '--longitude', type=float, required=False)
    parser.add_argument('-r', '--radius', type=float, required=False)

    args = parser.parse_args()
    id = args.id
    pw = args.pw
    mode = args.mode
    lat = args.latitude
    lon = args.longitude
    rad = args.radius

    if mode == "lti":
        latlon_to_income(id, pw, lat, lon, rad)

    elif mode == "ltr":
        latlon_to_railline(id, pw, lat, lon, rad)
