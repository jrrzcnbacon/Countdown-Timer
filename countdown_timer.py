import time

def countdown(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"Time Remaining: {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("\nTime's up! \a")  # \a sounds a beep on some systems

if __name__ == "__main__":
    try:
        mins = int(input("Enter minutes: "))
        secs = int(input("Enter seconds: "))
        countdown(mins, secs)
    except ValueError:
        print("Please enter valid integers for minutes and seconds.")
