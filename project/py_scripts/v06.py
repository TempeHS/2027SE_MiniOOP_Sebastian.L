from lib.audio_notification import Audio_Notification


def test_audio():
    audio = Audio_Notification(27)
    audio.warning_on()
    print("Audio notification")


test_audio()
