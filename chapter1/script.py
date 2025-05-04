import requests

def make_requests():
    url = "https://httpstat.us/"
    codes = [101, 200, 305, 400, 500]
    for code in codes:
        try:
            full_url = url + str(code)
            print(f"\n[GET] {full_url}")
            response = requests.get(full_url, timeout = 5)
            status_code = response.status_code

            if 100 <= status_code < 400:
                print(f"Status code: {status_code}\nResponse: {response.text}")
            else:
                raise Exception(f"[ERROR] Status code: {status_code}\nResponse: {response.text}") 
        except Exception as e:
            print(e)


if __name__ == "__main__":
    make_requests()
