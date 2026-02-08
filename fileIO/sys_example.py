import sys

print("Python version", sys.version)
print("Version info.", sys.version_info)
print("Platform:", sys.platform)
print("Executable path:", sys.executable)
print("Module search paths:", sys.path)
print("Current module name:", __name__)
print("File encoding:", sys.getdefaultencoding())
print("Argument list:", sys.argv)
if len(sys.argv) < 2:
    print("No additional arguments provided.")
    sys.exit(1)
else:
    print("Additional arguments:", sys.argv[1:])
print("Ok, got", sys.argv[1], "as the first argument.")