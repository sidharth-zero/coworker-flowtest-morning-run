import requests

def main():
    resp = requests.get("https://example.com")
    print(resp.status_code)

if __name__ == "__main__":
    main()
