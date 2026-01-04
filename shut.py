import os
import platform
import time

def shutdown():
    system = platform.system().lower()
    # Ask for confirmation
    confirm = input("Are you sure you want to shut down the computer? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Shutdown cancelled.")
        return

    # Optional delay
    print("Shutting down in 5 seconds... (Press Ctrl+C to cancel)")
    time.sleep(5)

    # Run the shutdown command based on OS
    if "windows" in system:
        os.system("shutdown /s /t 0")  # Windows
    elif "linux" in system or "darwin" in system:  # darwin = macOS
        os.system("sudo shutdown now")  # Linux/macOS
    else:
        print("Unsupported operating system.")

# ✅ Correct way to check if the script is being run directly
if __name__ == "__main__":
    shutdown()
