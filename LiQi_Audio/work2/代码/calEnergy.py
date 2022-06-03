import wave
import numpy as np
import numpy as np
import pylab
import pylab as pl

def calEnergy(wave_data) :
    energy = []
    sum = 0
    for i in range(len(wave_data)) :
        sum = sum + (int(wave_data[i]) * int(wave_data[i]))
        if (i + 1) % 256 == 0 :
            energy.append(sum)
            sum = 0
        elif i == len(wave_data) - 1 :
            energy.append(sum)
    return energy

f = wave.open("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Audio\\work2\\音频\\清音1.wav" , "rb")
# getparams() 一次性返回所有的WAV文件的格式信息
params = f.getparams()
# nframes 采样点数目
nchannels, sampwidth, framerate, nframes = params[:4]
# readframes() 按照采样点读取数据
str_data = f.readframes(nframes)            # str_data 是二进制字符串

# 以上可以直接写成 str_data = f.readframes(f.getnframes())

# 转成二字节数组形式（每个采样点占两个字节）
wave_data = np.frombuffer(str_data, dtype = np.short)
print( "采样点数目：" + str(len(wave_data)))          #输出应为采样点数目
f.close()
# 计算每一帧的能量 256个采样点为一帧

energy = calEnergy(wave_data)
print(energy)

time = np.arange(0, len(wave_data)) * (1.0 / framerate)
time2 = np.arange(0, len(energy)) * (len(wave_data) / len(energy) / framerate)
pl.subplot(211)
pl.plot(time, wave_data)
pl.ylabel("Amplitude")
pl.subplot(212)
pl.plot(time2, energy)
pl.ylabel("short energy")
pl.xlabel("time (seconds)")
pl.show()

# print("短时能量：",energy)