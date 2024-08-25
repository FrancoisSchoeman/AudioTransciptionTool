import argparse
import speech_recognition as sr
from pydub import AudioSegment


def parse_arguments():
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Convert audio file to text.')
    parser.add_argument('-i', '--input', required=True, help='Input audio file path.')
    return parser.parse_args()


def convert_to_wav(audio_file_path):
    """
    Converts an audio file to WAV format if it is not already in that format.

    Args:
        audio_file_path (str): The path to the input audio file.

    Returns:
        str: The path to the WAV file.
    """
    wav_file_path = 'converted_audio.wav'
    if ".wav" not in audio_file_path:
        print(f"Converting {audio_file_path} to WAV format...")
        sound = AudioSegment.from_file(audio_file_path)
        sound.export(wav_file_path, format="wav")
        print(f"Conversion complete. Saved WAV file as {wav_file_path}")
        return wav_file_path
    else:
        return audio_file_path


def transcribe_audio(final_file_path):
    """
    Transcribes the audio from a WAV file to text using Google's speech recognition API.

    Args:
        final_file_path (str): The path to the WAV file.
    """
    recognizer = sr.Recognizer()
    print(f"Loading audio file {final_file_path} for transcription...")
    with sr.AudioFile(final_file_path) as audio_file:
        audio_data = recognizer.record(audio_file)

    print("Transcribing audio to text...")
    try:
        text = recognizer.recognize_google(audio_data)
        print("\nTranscription:")
        print(text)
        print()
    except sr.UnknownValueError:
        print("\nSorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"\nCould not request results: {e}")


def main():
    """
    Main function to orchestrate the conversion and transcription process.
    """
    args = parse_arguments()
    final_file_path = convert_to_wav(args.input)
    transcribe_audio(final_file_path)

if __name__ == "__main__":
    main()