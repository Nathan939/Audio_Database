import matplotlib.pyplot as plot
from scipy.io import wavfile
from pydub import AudioSegment
from glob import glob
import os

def wavfiles2spec():
    hotwords = [x[0] for x in os.walk('audio\\')]
    hotwords.pop(0)

    for files in hotwords:
        try:
            os.makedirs("monos/" + files.split("\\")[-1])
        except OSError:
            print("Couldn't create directorie")

        try:
            os.makedirs("specto/" + files.split("\\")[-1])
        except OSError:
            print("Couldn't create directorie")

        audio_files = glob(files + '/*.wav')
        for audio in audio_files:
            sound = AudioSegment.from_wav(audio)
            sound = sound.set_channels(1)
            new_audio_path = "monos/" + files.split("\\")[-1] + '/' + audio.split('\\')[-1]
            sound.export(new_audio_path, format="wav")

            name_file = ("specto/" + files.split("\\")[-1] + '/' + audio.split('\\')[-1]).replace(".wav", ".jpg")
            # graph_spectrogram(new_audio_path, name_file)
            
            # Read the wav file (mono)
            samplingFrequency, signalData = wavfile.read(new_audio_path)

            # Plot the signal read from wav file
            plot.figure(figsize=(9.04, 5.98), dpi=100)
            plot.specgram(signalData,Fs=samplingFrequency)
            plot.axis('off')
            plot.savefig(name_file, format='jpg', bbox_inches='tight')
            print("Exported", name_file)
            plot.close('all')

wavfiles2spec()