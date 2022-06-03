import numpy as np
import wave
import matplotlib.pyplot as plt
wlen=512
inc=128
f = wave.open("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Audio\\work2\\音频\\元音1.wav" , "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
wave_data = np.frombuffer(str_data, dtype=np.short)
wave_data = wave_data*1.0/(max(abs(wave_data)))
print(wave_data[:10])
#信号总长度
signal_length=len(wave_data)
#若信号长度小于一个帧的长度，则帧数定义为1。否则，计算帧的总长度。
if signal_length<=wlen:
    nf=1
else:
    nf=int(np.ceil((1.0*signal_length-wlen+inc)/inc))
print(nf)
#所有帧加起来总的铺平后的长度
pad_length=int((nf-1)*inc+wlen)
#不够的长度使用0填补，类似于FFT中的扩充数组操作
zeros=np.zeros((pad_length-signal_length,))
#填补后的信号记为pad_signal
pad_signal=np.concatenate((wave_data,zeros))
#相当于对所有帧的时间点进行抽取，得到nf*nw长度的矩阵
indices=np.tile(np.arange(0,wlen),(nf,1))+np.tile(np.arange(0,nf*inc,inc),(wlen,1)).T
#print(indices[:2])
#将indices转化为矩阵
indices=np.array(indices,dtype=np.int32)
#得到帧信号
frames=pad_signal[indices]
windown=np.hanning(wlen)
d=np.zeros(nf)
x=np.zeros(nf)
time = np.arange(0,nf) * (inc*1.0/framerate)

frames=frames.T
para = np.zeros(frames.shape)
for i in range(nf):
        R = np.correlate(frames[:, i], frames[:, i], 'valid')
        para[:, i] = R
plt.subplot(2, 1, 2)
para=para.T
para = para.flatten()
plt.plot(para,c="g")
plt.show()