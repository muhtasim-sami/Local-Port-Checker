import requests, subprocess as sb
cmd = "Get-NetTCPConnection -State Listen  | select -ExpandProperty LocalPort | sort -Unique"

def shell(cmd):
    return sb.run(["powershell","-Command",cmd],capture_output=True, text=True)

ports = shell(cmd).stdout.split(sep='\n')
print("open ports are : \n", ports)

for port in ports:
    try:
        response = requests.get(f"http://127.0.0.1:{port}/apex", timeout=5)
        if response.headers['Server'] == 'Oracle XML DB/Oracle Database':
            print(f"Port {port} is running oracle db")
    except :
        pass

