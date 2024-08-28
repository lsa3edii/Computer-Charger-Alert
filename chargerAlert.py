import psutil
import winsound
import ctypes
# import time
from threading import Timer

def beep_alert():
    winsound.Beep(1000, 500)  # Frequency 1000 Hz, Duration 500 ms

def check_battery_status():
    battery = psutil.sensors_battery()
    return battery.power_plugged

def hide_console():
    # Hide the console window
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def monitor_battery(previous_status):
    current_status = check_battery_status()
    if current_status != previous_status:
        beep_alert()
        previous_status = current_status

    # Re-set the timer for the next check
    Timer(0.1, monitor_battery, [previous_status]).start()

# def main():
#     print("Running...")
#     previous_status = check_battery_status()
#     while True:
#         time.sleep(0.1)  # Check every 0.1 seconds
#         current_status = check_battery_status()
#         if current_status != previous_status:
#             beep_alert()
#             previous_status = current_status

def main():
    print("Running...")
    initial_status = check_battery_status()
    monitor_battery(initial_status)

if __name__ == "__main__":
    hide_console()
    main()
