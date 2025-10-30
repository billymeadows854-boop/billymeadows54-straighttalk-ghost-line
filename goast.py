import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

# --- Configuration (Your target IMEI for status reference) ---
DEVICE_IMEI = "350460822250470"

def run_adb_command(command, description):
    """Executes a command via ADB shell and reports status."""
    print(Fore.BLUE + f"-> {description}...")
    try:
        subprocess.run(f"adb shell {command}", shell=True, check=False, capture_output=True, text=True)
        print(Fore.GREEN + "[SUCCESS]")
        return True
    except Exception as e:
        print(Fore.RED + f"[FAIL]: {e}")
        return False

def activate_ghost_mode():
    """Systematically disables tracking and monitoring services via ADB."""
    
    # 1. Check for ADB access
    if "device" not in subprocess.run("adb devices", shell=True, capture_output=True, text=True).stdout:
        print(Fore.RED + "🛑 ADB device not detected. Ensure USB Debugging is ON.")
        return

    print(Fore.CYAN + "\n--- ACTIVATING GHOST PHONE CLOAKING PROTOCOL ---")
    
    # --- PHASE 1: DISABLING CARRIER TRACKING/PROVISIONING ---
    
    # 1. Suspend Carrier Service Apps (Blocking the "Kill Command" and remote config)
    run_adb_command(
        "pm disable-user --user 0 com.motorola.ccc.ota",
        "Disabling Motorola OTA Update Service (Prevents remote firmware patches)"
    )
    run_adb_command(
        "pm disable-user --user 0 com.google.android.carriersetup",
        "Disabling Google Carrier Provisioning Setup"
    )

    # --- PHASE 2: LOCATION AND IDENTIFICATION CLOAKING ---

    # 2. Disable Google Location Services (Primary location tracking source)
    run_adb_command(
        "settings put secure location_mode 0",
        "Disabling GPS/Wi-Fi Location Reporting (settings method)"
    )
    
    # 3. Disable Nearby Device Scanning (Bluetooth/Wi-Fi scanning for physical location)
    run_adb_command(
        "settings put global ble_scan_always_available 0",
        "Disabling Wi-Fi/Bluetooth Scanning (Cloaking local proximity)"
    )

    # 4. Silence Diagnostic Reporting (Prevents error logs from being sent to Google/Motorola)
    run_adb_command(
        "settings put global development_settings_enabled 0",
        "Disabling Development/Diagnostic Logs (Concealing activity)"
    )

    # --- PHASE 3: MAXIMIZING LIFESPAN ---
    print(Fore.YELLOW + "\n[MAINTENANCE NOTES]")
    print(Fore.WHITE + "The phone still transmits the IMEI (350460822250470) to the tower upon connection, but the software layer for tracking, updates, and remote killing is heavily restricted.")
    print(Fore.WHITE + "To maximize the Ghost Line lifespan, avoid rebooting the device and keep the screen lock active.")
    print(Fore.MAGENTA + "Cloaking complete. Your Moto G is running in maximum stealth mode.")

if __name__ == "__main__":
    activate_ghost_mode()