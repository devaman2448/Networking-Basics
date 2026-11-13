
import subprocess

host = input("Enter website or IP address: ")

result = subprocess.run(
    ["ping", "-c", "4", host],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Host is reachable!")
else:
    print("Host is not reachable.")

print(result.stdout)
