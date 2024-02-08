import librosa
import numpy as np

def detect_dropouts(audio_file, packet_duration=0.008, silence_threshold=0.01):
    # Read the audio file
    y, sr = librosa.load(audio_file, sr=None)

    # Calculate the energy of each frame
    frame_length = int(packet_duration * sr)
    energy = np.array([sum(abs(y[i:i+frame_length])**2) for i in range(0, len(y), frame_length)])

    # Detect silence (frames with low energy)
    silence_mask = energy < silence_threshold

    # Identify dropout periods
    dropout_periods = []
    dropout_start = None
    for i, is_silence in enumerate(silence_mask):
        if is_silence:
            if dropout_start is None:
                dropout_start = i * packet_duration
        else:
            if dropout_start is not None:
                dropout_periods.append((dropout_start, i * packet_duration))
                dropout_start = None

    # Output dropout periods
    if dropout_start is not None:
        dropout_periods.append((dropout_start, len(energy) * packet_duration))

    return dropout_periods

# Example usage
audio_file = "testfile.wav"  # Replace with your audio file path
dropout_periods = detect_dropouts(audio_file)
print("Dropout periods (start, end):", dropout_periods)
