import nmap


def scanport(ip):
    nm = nmap.PortScannerAsync()
    result = nm.scan(hosts=ip,arguments='-sP')
    print(result)
    return result


scanport('172.16.60.14')