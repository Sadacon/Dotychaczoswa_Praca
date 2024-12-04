import platform
from platform import python_version_tuple

python_version = " ".join(platform.python_version_tuple())

print("------ Python Information ------")
print(f"Implementation: {platform.python_implementation()}")
print(f"(Version): {python_version_tuple}")
print("------ Platform Information ------")
print(f"Operation system: {platform.system()}")
print(f"OS version: {platform.version()}")
print(f"OS release: {platform.release()}")
print(f"Machine type: {platform.machine()}")
print(f"Node name: {platform.node()}")