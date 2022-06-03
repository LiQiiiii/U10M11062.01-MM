img = imread('test_gray.jpg');

%RGB=imread('test_original.jpg');
%I = rgb2gray(RGB);
%imwrite(I,'test_gray.jpg');

%imgdct=my_dct(img);%ֱ�Ӷ�������DCT�任          %ʵ��2ʹ�õĴ��룬ʵ��2ʱȡ��ע�͸����
%imgidct=my_idct(imgdct);%ֱ�Ӷ�������IDCT�任    %ʵ��2ʹ�õĴ��룬ʵ��2ʱȡ��ע�͸����

fun1=@(block_struct) my_dct(block_struct.data);%ʵ��1&3ʹ�õĴ��룬ʵ��1&3ʱȡ��ע�͸����
fun2=@(block_struct) my_idct(block_struct.data);%ʵ��1&3ʹ�õĴ��룬ʵ��1&3ʱȡ��ע�͸����
fun3=@(block_struct) ex3(block_struct.data);   %ʵ��3ʹ�õĴ��룬ʵ��3ʱȡ��ע�͸����

imgdct = blockproc(img,[8,8],fun1);%�ֿ飬����DCT�任       %ʵ��1&3ʹ�õĴ��룬ʵ��1&3ʱȡ��ע�͸����
imgdct=blockproc(imgdct,[8,8],fun3);%��ex3������DCT�任��ľ������������޸���������           %ʵ��3ʹ�õĴ��룬ʵ��3ʱȡ��ע�͸����
imgidct = blockproc(imgdct,[8,8],fun2);%�ֿ飬����IDCT�任  %ʵ��1&3ʹ�õĴ��룬ʵ��1&3ʱȡ��ע�͸����

figure (1)
imshow(img);
title('ԭʼͼ��')

figure(2)
A=uint8(imgdct);
imshow(A);
title('DCT�任ͼ��');

figure(3)
B=uint8(imgidct);
imshow(B);
title('DCT��任ͼ��');
f=RMSE(img,imgidct)             %������������
snr=SNR(img,uint8(imgidct))     %������������
