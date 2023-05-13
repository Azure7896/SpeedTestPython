import resolver
import speedtest as st
import os
import requests
import socket


class Speed:
    server = st.Speedtest()
    jsonTestInfo = server.get_best_server()

    def __init__(self):
        pass

    @classmethod
    def get_test_info(cls):
        return Speed.jsonTestInfo.items()

    @classmethod
    def check_download(cls):
        down = Speed.server.download()
        down = down / 1000000
        return down

    @classmethod
    def check_upload(cls):
        upload = Speed.server.upload()
        upload = upload / 1000000
        return upload

    @classmethod
    def check_ping(cls):
        ping = Speed.server.results.ping
        return ping


class IpChecker:

    def __init__(self):
        pass

    @classmethod
    def get_ip_addresses(cls):
        return os.system("ipconfig")

    @classmethod
    def get_public_ip_address(cls):
        return str(requests.get('https://checkip.amazonaws.com').text.strip())


class PortChecker:

    def __init__(self):
        pass

    @classmethod
    def port_check(cls, port_number):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect(("127.0.0.1", port_number))
            return True
        except:
            return False


class DnsChecker:

    def __init__(self):
        pass

    @classmethod
    def resolve_name_to_ip(cls, name):
        return socket.gethostbyname(name)

    @classmethod
    def resolve_ip_to_name(cls, ip_address):
        return socket.gethostbyaddr(ip_address)
