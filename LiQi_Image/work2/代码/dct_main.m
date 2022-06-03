img = imread('test_gray.jpg');

%RGB=imread('test_original.jpg');
%I = rgb2gray(RGB);
%imwrite(I,'test_gray.jpg');

%imgdct=my_dct(img);%直接对整个作DCT变换          %实验2使用的代码，实验2时取消注释该语句
%imgidct=my_idct(imgdct);%直接对整个作IDCT变换    %实验2使用的代码，实验2时取消注释该语句

fun1=@(block_struct) my_dct(block_struct.data);%实验1&3使用的代码，实验1&3时取消注释该语句
fun2=@(block_struct) my_idct(block_struct.data);%实验1&3使用的代码，实验1&3时取消注释该语句
fun3=@(block_struct) ex3(block_struct.data);   %实验3使用的代码，实验3时取消注释该语句

imgdct = blockproc(img,[8,8],fun1);%分块，再作DCT变换       %实验1&3使用的代码，实验1&3时取消注释该语句
imgdct=blockproc(imgdct,[8,8],fun3);%用ex3函数对DCT变换后的矩阵处理，保留有限个交流分量           %实验3使用的代码，实验3时取消注释该语句
imgidct = blockproc(imgdct,[8,8],fun2);%分块，再作IDCT变换  %实验1&3使用的代码，实验1&3时取消注释该语句

figure (1)
imshow(img);
title('原始图象')

figure(2)
A=uint8(imgdct);
imshow(A);
title('DCT变换图象');

figure(3)
B=uint8(imgidct);
imshow(B);
title('DCT逆变换图象');
f=RMSE(img,imgidct)             %计算均方根误差
snr=SNR(img,uint8(imgidct))     %计算均方信噪比
