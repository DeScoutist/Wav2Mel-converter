#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Или 'Qt5Agg'
import matplotlib.pyplot as plt

# Загрузка данных из файла .npy
data = np.load('mels/45.npy')

# Создание графика
plt.figure(figsize=(10, 4))
plt.imshow(data, aspect='auto', origin='lower')

# Показ графика
plt.show()