import librosa
y, sr = librosa.load('t1.wav', sr=None)
y_16k = librosa.resample(y, sr, 16000)
librosa.output.write_wav('t1-16.wav', y_16k, 16000)
y_8k = librosa.resample(y, sr, 8000)
librosa.output.write_wav('t1-8.wav', y_16k, 8000)

