#define _CRT_SECURE_NO_WARNINGS
#define _CRT_NONSTDC_NO_DEPRECATE
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int PIXEL[256];
int NUMPIXEL=0;
double HISTOGRAM[256];
double SUM_HISTOGRAM[256];
int  CHANGE_PIXEL[256];
void refreshPIXEL()
{
    for (int i=0; i <=255; i++)
    {
        PIXEL[i] = 0;
    }
}

void countNUMPIXEL()
{
    for (int i=0; i <=255; i++)
    {
        if (PIXEL[i] != 0)
        {
            NUMPIXEL=NUMPIXEL+PIXEL[i];
        }
    }


}
int main()
{
    FILE* fp1 = NULL;
    FILE* fp2 = NULL;
    int middle = 0;
    refreshPIXEL();
    freopen("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Image\\work1\\数据\\testimg.txt", "r" , stdin);
    while (1)
    {
        cin >> middle;
        if (middle >= 0)
        {                  
            PIXEL[middle]++;
        }    


        else break;
    }
    countNUMPIXEL();
	int i=0;
	int j=0;
    for (i = 0; i <= 255; i++)
    {
        HISTOGRAM[i] =( PIXEL[i]*1.000) / (NUMPIXEL*1.0000);
    }
    for (i = 1; i <= 255; i++)
    {
        SUM_HISTOGRAM[i] = HISTOGRAM[i] + SUM_HISTOGRAM[i - 1];
    }
    for (i = 1; i <= 255; i++)
    {
        CHANGE_PIXEL[i] = SUM_HISTOGRAM[i] * 255.0000;
    }
    middle = 0;
    freopen("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Image\\work1\\数据\\testimg.txt", "r" , stdin);
    freopen("C:\\Users\\61060\\Desktop\\NPU-LQ\\大三上\\多媒体\\LiQi_Image\\work1\\数据\\data.txt", "w", stdout);
    int change_len=1;
    for (i = 1; i <= 512; i++)
    {
        for (j = 1; j <= 512; j++)
        {
            cin >> middle;
            cout << CHANGE_PIXEL[middle]<<"\t";
        }
        cout << endl;
   }
    return 0;
}

