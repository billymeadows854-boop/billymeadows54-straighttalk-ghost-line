# --- DEFENSE SCRIPT: Prevents Remote Kill Commands and Updates ---

# 1. Disable Carrier/OTA Services (Blocks kill signals and patches)
adb shell pm disable-user --user 0 com.motorola.ccc.ota
adb shell pm disable-user --user 0 com.google.android.carriersetup

# 2. Disable Location/Messaging Services (Stealth Mode)
adb shell settings put secure location_mode 0
adb shell pm revoke com.google.android.apps.messaging android.permission.RECEIVE_SMS
