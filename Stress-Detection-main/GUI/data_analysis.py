import pandas as pd
import os
import numpy as np
import soundfile as sf
import librosa
import csv

isStressed = False
def func(filepath):
    def trimm(data):
        data_trimmed, _ = librosa.effects.trim(data, top_db=20)
        return data_trimmed

    def pitch(data, samplingRate, pitch_factor):
        return librosa.effects.pitch_shift(y=data, sr=samplingRate, n_steps=pitch_factor)

    # feature extraction (mfcc, delta, double-delta, chroma)

    def extract_features(filename):
        with sf.SoundFile(filename) as soundFile:
            x = soundFile.read(dtype="float64")
            sampleRate = soundFile.samplerate
            res = np.array([])

            x = trimm(x)
            x = pitch(x, sampleRate, 3)

            stft = np.abs(librosa.stft(x))

            # for mfcc
            mfccs = np.mean(librosa.feature.mfcc(y=x, sr=sampleRate, n_mfcc=13).T, axis=0)
            res = np.hstack((res, mfccs))

            # for delta
            delta_mfcc = librosa.feature.delta(mfccs)
            res = np.hstack((res, delta_mfcc))

            # for double-delta
            delta2_mfcc = librosa.feature.delta(mfccs, order=2)
            res = np.hstack((res, delta2_mfcc))

            # for chroma
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sampleRate).T, axis=0)
            res = np.hstack((res, chroma))

            # for mel spectrogram
            melSpec = np.mean(librosa.feature.melspectrogram(y=x, sr=sampleRate).T, axis=0)
            res = np.hstack((res, melSpec))

            # for contrast
            contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sampleRate).T, axis=0)
            res = np.hstack((res, contrast))

            # for tonnetz
            tonnetz = np.mean(librosa.feature.tonnetz(y=x, sr=sampleRate).T, axis=0)
            res = np.hstack((res, tonnetz))

        return res

    X_test= []
    testing = extract_features(filepath)
    X_test.append(testing)
    X_test_df = pd.DataFrame(X_test, columns=[f"feat_{i}" for i in range(192)])
    print(X_test_df)
    X_test_df.to_csv('testing.csv')
    import joblib
    def predict(data):
        data = pd.read_csv('testing.csv')
        data = np.array(data)
        print(data.shape)
        clf = joblib.load('model.sav')
        ans = clf.predict(data)
        print(ans[0][0])
        return ans
    isStressed = predict(X_test_df) >= 0.5
    import ran
    ran.nacho(isStressed)
func('data/aud.wav')