import datetime
import time
import pygame

def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error:
        print("Error: Could not load or play the audio file.")

def set_alarm():
    try:
        alarm_input = input("Enter the time for the alarm in HH:MM format: ")
        alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M")
        return alarm_time.time()
    except ValueError:
        print("Please enter a valid time in HH:MM format.")
        return set_alarm()


def run_alarm_clock(alarm_time):
    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time:
            play_audio(r'#audio file')
            break
        else:
            time.sleep(1)  # Check every 1 seconds for the alarm time

def main():
    print("Welcome to the Python Alarm Clock!")
    print("Set your alarm time.")
    alarm_time = set_alarm()
    print(f"Alarm set for {alarm_time.strftime('%H:%M')}")

    run_alarm_clock(alarm_time)




# if __name__ == "__main__":
#     # Replace 'your_audio_file_path.wav' with the path to your audio file (e.g., 'alarm_sound.wav')
#     audio_file_path = 'your_audio_file_path.wav'  # Update this with your audio file path
#     play_audio(audio_file_path)


if __name__ == "__main__":
    print(datetime.datetime.now().time())
    main()