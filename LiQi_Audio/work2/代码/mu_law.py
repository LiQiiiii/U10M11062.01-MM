import wave
import numpy as np
import matplotlib.pyplot as plt


def mu_law(x, mu=255):
    x = np.clip(x, -1, 1)
    x_mu = np.sign(x) * np.log(1 + mu*np.abs(x))/np.log(1 + mu)
    return ((x_mu + 1)/2 * mu).astype('int16')


def get_wave_data():
    # 采用只读的方式读取wav文件，并将其保存到f中
    f = wave.open("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Audio\\work2\\音频\\元音1.wav", "rb")
    # 获取所有参数
    params = f.getparams()
    # 以原频率进行采样采样，获取bytes
    str_data = f.readframes(f.getnframes())
    # 转成二字节数组形式（每个采样点占两个字节）
    wave_data = np.frombuffer(str_data, dtype=np.short)
    f.close()

    ret = [mu_law(x / 2 ** 15) for x in wave_data]
    ret = np.array(ret,dtype=np.uint8)
    write_back(ret)
    plt.figure(figsize=(8,8))
    plt.subplot(211)
    plt.title("befroe")
    plt.plot(wave_data)  #转化前
    plt.subplot(212)
    plt.title("after")
    plt.plot(ret)  #转化后
    plt.savefig("p2mu_law.png")
    plt.show()

def write_back(wave_data):
    f = wave.open("元音out.wav", "wb")
    # 设置通道数
    f.setnchannels(1)
    #  设置采样宽度为8bit
    f.setsampwidth(1)
    # 采样率
    f.setframerate(8000)
    f.writeframes(wave_data)
    f.close()

if __name__ == '__main__':
   get_wave_data()
