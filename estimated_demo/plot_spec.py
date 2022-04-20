import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import librosa
import librosa.display
import os
import pydub

from pathlib import Path

NFFT = 1022
HOP_LENGTH = 256
TARGET_SAMPLING_RATE = 16384
wav_files = Path('.').rglob('*.wav')
for file in wav_files:
    file_path = file.as_posix()
    """
    if ('mod' in file_path) or (('6Ws1WKA4z2k_0_35_to_0_48' in file_path) \
            or ('cttFanV0o7c_0_07_to_2_44' in file_path) \
            or ('pRh9rKd2j64_0_15_to_0_55' in file_path) \
            or ('sEnTMgzw8ow_1_5_to_2_07' in file_path) \
            or ('sEnTMgzw8ow_1_29_to_1_47' in file_path) \
            or ('sEnTMgzw8ow_2_38_to_2_53' in file_path) \
            or ('tcol' in file_path) \
            or ('vyu3HU3XWi4_2_04_to_2_14' in file_path)):
            """
    if ('mod' in file_path):
        file_name = os.path.basename(file_path)
        folder_path = os.path.dirname(file_path)
        output_path = os.path.join(folder_path, file_name[:-4] + '.png')
        y, sr = librosa.load(file_path, sr=16384)
        sound = pydub.AudioSegment.from_wav(file_path)
        sound.export(file_path[:-4]+'.mp3', format="mp3")

        stft = librosa.stft(y, n_fft=NFFT, hop_length=HOP_LENGTH)
        D = librosa.amplitude_to_db(np.absolute(stft),
                                    ref=np.max)
        librosa.display.specshow(D, sr=sr, hop_length=HOP_LENGTH, x_axis='time', cmap='Reds', y_axis='linear')
        plt.ylabel(None)
        plt.xlabel(None)
        plt.savefig(output_path, bbox_inches='tight')
        #plt.show()
