import requests, re, time
from pythonmonkey import eval as js_eval

# Generates a list of fuzzing payloads from a file
def fuzz_list_generator():
    fuzz_list_path = "********************"  # Path to the file containing fuzzing payloads
    fuzz_list = []

    with open(fuzz_list_path, 'r') as file:
        for line in file:
            fuzz_list.append(line.strip())

    return fuzz_list

final_fuzz_list = fuzz_list_generator()

# Creates and sends a GET request to the given URL with the provided cookie
def request_creator(url, cookie):
    headers = {'User-Agent': '********************'}  # User-Agent header for the request

    try:
        response = requests.get(url, headers=headers, cookies=cookie, verify=False, allow_redirects=False)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return response

waf_message = "Transferring to the website..."  # Message indicating the presence of a WAF

# Checks the response for a specific cookie and extracts it if available
def check_cookie_status(response):
    if response.status_code == 200 and waf_message in response.text:
        www_cookie_creator_script = re.findall(r'REGEX_PATTERN', response.text)  # Extract script using regex

        if len(www_cookie_creator_script) != 0:
            print("\n----------------- NEW COOKIE WILL BE GENERATED -----------------\n")
            return js_eval(www_cookie_creator_script[0])  # Evaluate JavaScript to generate new cookie
        
    return None

# Creates a cookie dictionary with the given hash string
def cookie_creator(hash_string):
    cookie = {"COOKIE_KEY": hash_string}  # Replace COOKIE_KEY with the actual cookie key
    return cookie

# Extracts and returns the response headers
def check_location_header(response):
    response_header = response.headers
    return response_header

# Main fuzzing function that iterates over the fuzz list and performs requests
def fuzzer():
    target_url = "https://********************/"  # Target URL for fuzzing
    index_min = 0
    index_max = len(final_fuzz_list)
    cookie_0 = ""  # Initial empty cookie

    while index_min < index_max:
        payload = f"{target_url}{final_fuzz_list[index_min]}"
        response = request_creator(payload, cookie_0)
        fuzz_cookie = check_cookie_status(response)

        if fuzz_cookie is not None:
            cookie_0 = cookie_creator(fuzz_cookie)

        fuzz_headers = check_location_header(response)

        if 'Location' in fuzz_headers:
            if fuzz_headers['Location'] != f"/en/{final_fuzz_list[index_min]}/":
                print(f"STATUS CODE: {response.status_code} RESULT: /{final_fuzz_list[index_min]}\n")
        else:
            print(f"STATUS CODE: {response.status_code} RESULT: /{final_fuzz_list[index_min]}\n")

        time.sleep(0.5)
        index_min += 1

fuzzer()
