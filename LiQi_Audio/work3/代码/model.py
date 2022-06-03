import torch
import torch.nn as nn
import torch.nn.functional as F


class ConvNet(nn.Module):
    # CNN
    ''''''

    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, 22, 1)
        # torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1)
        # in_channels：输入音频通道数
        # out_channels：输出通道数，这个等于卷积核的数量
        # kernel_size：卷积核大小
        # stride：步长
        self.conv2 = nn.Conv2d(10, 20, 1, 1)
        # 上个卷积网络的out_channels，就是下一个网络的in_channels，所以这里是30
        # out_channels：卷积核数量60
        # 通过一个1*1的卷积 步长为1
        self.conv3 = nn.Conv2d(20, 40, 11, 1)
        self.conv4 = nn.Conv2d(40, 80, 2, 1)
        # 同上
        self.fc1 = nn.Linear(5 * 2 * 80, 800)
        # 全连接层torch.nn.Linear(in_features, out_features)
        # in_features:输入特征维度
        # out_features；输出特征维度

        self.fc2 = nn.Linear(800, 6)
        # 输出维度6分类

    def forward(self, x):
        # print(x.shape)  #输入维度，(N,1,161,101) N为一个batch大小
        x = F.relu(self.conv1(x))  # x = (N,10,140,80)
        x = F.max_pool2d(x, 2, 2)  # x = (N,10,70,40) 池化 降采样
        x = F.relu(self.conv2(x))  # x = (N,20,70,40)
        x = F.relu(self.conv3(x))  # x = (N,40,60,30)
        x = F.max_pool2d(x, 10, 10)  # x=(N,40,6,3)
        x = F.relu(self.conv4(x))  # x = (N,80,5,2)
        x = x.view(-1, 5 * 2 * 80)  # x = (N,10*4*50)

        x = F.sigmoid(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)  # 带log的softmax分类，每段音频返回6个概率


class FcNet(nn.Module):
    # DNN
    def __init__(self):
        super(FcNet, self).__init__()

        self.fc1 = nn.Linear(161 * 101 * 1, 1000)
        # 全连接层torch.nn.Linear(in_features, out_features)
        # in_features:输入特征维度
        # out_features；输出特征维度

        self.fc2 = nn.Linear(1000, 6)
        # 输出维度6分类

    def forward(self, x):
        x = x.view(-1, 161 * 101 * 1)  # x = (N,161*101*1)
        x = F.sigmoid(self.fc1(x))  # x = (N,161*101*1)*(161*101*1,1000)=(N,500)
        x = self.fc2(x)  # x = (N,1000)*(1000,6)=(N,6)
        return F.log_softmax(x, dim=1)  # 带log的softmax分类，每段音频返回6个概率
