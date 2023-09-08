# DNS ENUM
import  requests
host_name = input("Enter Host Name: ")
sub_domains = open("domains.txt","r").read().split("\n")

for sub in sub_domains:
    url1=f"https://{sub}.{host_name}"
    url2=f"http://{sub}.{host_name}"
    try:
        requests.get(url1)
        print(f"[+] Discorverd SubDomain: {url1}")
        requests.get(url2)
        print(f"[+] Discorverd SubDomain: {url2}")
    except requests.ConnectionError:
        pass