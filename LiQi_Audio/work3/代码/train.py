from __future__ import print_function
import torch
import torch.nn.functional as F
from torch.autograd import Variable

def train(loader, model, optimizer, epoch, cuda, log_interval, verbose=True):
    model.train() #进入训练模式
    for batch_idx, (data, target) in enumerate(loader):
        if cuda: #使用GPU加速
            data, target = data.cuda(), target.cuda()
        with torch.no_grad():
            data, target = Variable(data), Variable(target)
        optimizer.zero_grad() #梯度归零
        print(data.shape)
        output = model(data) #输出的维度[N,6] 这里的data是函数的forward参数x
        train_loss = F.nll_loss(output, target) #loss求的平均数，除以batch
        # 单分类交叉熵损失函数，一段音频里只能有一个类别，输入input的需要softmax
        train_loss.backward()
        optimizer.step()
        if verbose:
            if batch_idx % log_interval == 0:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(loader.dataset),
                       100. * batch_idx / len(loader), train_loss.item()))
        return train_loss

def test(loader, model, cuda, Accuracy_list, verbose=True):
    model.eval()
    test_loss = 0
    correct = 0

    for data, target in loader:
        if cuda:
            data, target = data.cuda(), target.cuda()
        with torch.no_grad():
            data, target = Variable(data), Variable(target)
        output = model(data)
        test_loss += F.nll_loss(output, target, reduction='sum').data.item()  # sum up batch loss
        pred = output.data.max(1, keepdim=True)[1]  # get the index of the max log-probability
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(loader.dataset)

    Accuracy_list.append(100 * correct / (len(loader.dataset)))

    if verbose:
        print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
            test_loss, correct, len(loader.dataset), 100. * correct / len(loader.dataset)))
    return test_loss
