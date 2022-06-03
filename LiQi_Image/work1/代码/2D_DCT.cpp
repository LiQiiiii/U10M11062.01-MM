#define _CRT_SECURE_NO_WARNINGS
#define _CRT_NONSTDC_NO_DEPRECATE
#include <iostream>
#include <memory.h>
#include <math.h>
#include <time.h>
#include <iomanip>
using namespace std;
#define PI (3.1415926)  
#define N (8)   /* 当前切成8x8的块进行DCT变换 */
int WIDTH = 512, HEIGHT = 512;
int MAT_SIZE = 512;
float DCT_Mat[512][512]; //定于变换矩阵
float DctMap[512][512];  //输入矩阵，计算结束后为输出矩阵
float DctMapTmp[512][512];  //矩阵运算时用的中间矩阵
/*
*读取像素
*/
void readFile()
{
    freopen("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Image\\work1\\数据\\testimg.txt", "r", stdin);
    for (int i = 0; i < 512; i++)
    {
        for (int j = 0; j < 512; j++)
        {
            cin >> DctMap[i][j];
        }
    }
}

void TransMat()
{
    int i, j;
    float a;

    for (i = 0; i < MAT_SIZE; i++)
    {
        for (j = 0; j < MAT_SIZE; j++)
        {
            a = 0;
            if (i == 0)
            {
                a = sqrt((float)1 / MAT_SIZE);
            }
            else
            {
                a = sqrt((float)2 / MAT_SIZE);
            }
            DCT_Mat[i][j] = a * cos((j + 0.5) * PI * i / MAT_SIZE); //变换矩阵
        }
    }
}

void DCT()
{
    float t = 0;
    int i, j, k;
    for (i = 0; i < MAT_SIZE; i++)  //相当于A*I
    {
        for (j = 0; j < MAT_SIZE; j++)
        {
            t = 0;
            for (k = 0; k < MAT_SIZE; k++)
            {
                t += DCT_Mat[i][k] * DctMap[k][j]; //矩阵的乘法，DCT_Mat的第i行乘DctMap的第j列
            }
            DctMapTmp[i][j] = t;
        }
    }
    for (i = 0; i < MAT_SIZE; i++)  //相当于（A*I）后再*A‘
    {
        for (j = 0; j < MAT_SIZE; j++)
        {
            t = 0;
            for (k = 0; k < MAT_SIZE; k++)
            {
                t += DctMapTmp[i][k] * DCT_Mat[j][k];
            }
            DctMap[i][j] = t;
        }
    }
}

int main(int argc, char* argv[])
{
    readFile();
    TransMat();
    DCT();
    freopen("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Image\\work1\\数据\\data2.txt", "w", stdout);
    for (int i = 0; i < MAT_SIZE; i++)
    {
        for (int j = 0; j < MAT_SIZE; j++)
        {
            cout << DctMap[i][j] << "\t";
        }
        cout << endl;
    }
}