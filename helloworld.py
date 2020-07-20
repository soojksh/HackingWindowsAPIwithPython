#Hello World Windows API Style.

# Import the required module to handle Windows API Calls
import ctypes

# Grab a handle to User32.dll & kernel32.dll
user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

# Win API Call
# int MessageBoxA(
# HWND hWnd,
# LPCTSTR lpText,
# LPCTSTR lpCaption,
# UINT, uType
# );

# Setting Up The Params
hWnd = None
lpText = "Hello World"
lpCaption = "Hello Friend"
uType = 0x00000001

# Calling the Windows API Call
response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

#Check the Errors.
error = k_handle.GetLastError()
if error != 0:
    print("Error Code: (0)".format(error))
    exit(1)
    
#Check what the User Clicked.
if response == 1:
    print("User Clicked OK!")
    
elif response == 2:
    print("User Exited!")


