import requests
r = requests.get("https://simpledebit.gocardless.io/health_check")
print(r)
print(r.status_code, r.reason)
