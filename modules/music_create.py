import numpy as np
import scipy.io.wavfile as wav

def create_silent_audio(duration_seconds, sample_rate=44100):
    """
    Создает пустую звуковую дорожку заданной длительности
    
    Параметры:
    duration_seconds (int/float): длительность в секундах
    sample_rate (int): частота дискретизации (по умолчанию 44100 Гц)
    """
    # Создаем массив нулей нужной длины
    samples = np.zeros(int(duration_seconds * sample_rate), dtype=np.int16)
    
    # Записываем в WAV файл
    wav.write('static/media/silent_audio.wav', sample_rate, samples)
    print(f"Создан файл silent_audio.wav длительностью {duration_seconds} секунд")

if __name__ == '__main__':
    # Пример использования:
    duration = float(15)
    create_silent_audio(duration)
