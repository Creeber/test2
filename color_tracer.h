#ifndef color_tracer_H
#define color_tracer_H

#include "zf_common_headfile.h"
// ɫ��ʶ�����ο�����
//  https://blog.csdn.net/niruxi0401/article/details/119685347

#define IMG_X               0               // ͼƬx����
#define IMG_Y               0               // ͼƬy����
#define IMG_W               SCC8660_W - 1   // ͼƬ���
#define IMG_H               SCC8660_H - 1   // ͼƬ�߶�

//#define ALLOW_FAIL_PER      10              // �ݴ��ʣ�û1<<ALLOW_FAIL_PER�����������һ������㣬�ݴ���Խ��Խ����ʶ�𣬵�������Խ��
//#define ITERATE_NUM         5               // ������������������Խ��ʶ��Խ��ȷ����������Խ��
extern uint8 ALLOW_FAIL_PER;                  // �ݴ��ʣ�û1<<ALLOW_FAIL_PER�����������һ������㣬�ݴ���Խ��Խ����ʶ�𣬵�������Խ��
extern uint8 ITERATE_NUM;                     // ������������������Խ��ʶ��Խ��ȷ����������Խ��
//#define CONDI_H_RANGE       60              // �趨ɫ��궨����ɫ��Χ��  �� set_color_target_condi ������ʹ��
//#define CONDI_S_RANGE       80              // �趨ɫ��궨�ĶԱȶȷ�Χ���� set_color_target_condi ������ʹ��
//#define CONDI_L_RANGE       50              // �趨ɫ��궨�����ȷ�Χ��  �� set_color_target_condi ������ʹ��
extern uint8 CONDI_H_RANGE;   // �趨ɫ��궨����ɫ��Χ��  �� set_color_target_condi ������ʹ��
extern uint8 CONDI_S_RANGE;   // �趨ɫ��궨�ĶԱȶȷ�Χ���� set_color_target_condi ������ʹ��
extern uint8 CONDI_L_RANGE;   // �趨ɫ��궨�����ȷ�Χ��  �� set_color_target_condi ������ʹ��

#define min3v(v1, v2, v3)   ((v1)>(v2)? ((v2)>(v3)?(v3):(v2)):((v1)>(v3)?(v3):(v1)))
#define max3v(v1, v2, v3)   ((v1)<(v2)? ((v2)<(v3)?(v3):(v2)):((v1)<(v3)?(v3):(v1)))
#define SWAPBYTE(h) ((((uint16_t)h << 8)&0xFF00) | ((uint16_t)h >> 8))

//#define WHITE_UP		(120)
//#define WHITE_DOWN		(0)
//#define RED_UP			(255)
//#define RED_DOWN		(185)
//#define BLUE_UP			(175)
//#define BLUE_DOWN		(125)
extern uint8 WHITE_UP;
extern uint8 WHITE_DOWN;
extern uint8 RED_UP;
extern uint8 RED_DOWN;
extern uint8 BLUE_UP;
extern uint8 BLUE_DOWN;

#define is_white(color)	((color>=WHITE_DOWN && color<=WHITE_UP)?1:0)
#define is_red(color)	((color>=RED_DOWN && color<=RED_UP)?1:0)
#define is_blue(color)	((color>=BLUE_DOWN && color<=BLUE_UP)?1:0)

typedef struct{
    unsigned char           h_min;          // Ŀ����Сɫ��
    unsigned char           h_max;          // Ŀ�����ɫ��

    unsigned char           s_min;          // Ŀ����С���Ͷ�
    unsigned char           s_max;          // Ŀ����󱥺Ͷ�

    unsigned char           l_min;          // Ŀ����С����
    unsigned char           l_max;          // Ŀ���������

    unsigned int            width_min;      // Ŀ����С���
    unsigned int            hight_min;      // Ŀ����С�߶�

    unsigned int            width_max;      // Ŀ�������
    unsigned int            hight_max;      // Ŀ�����߶�
}target_condi_struct;                       // �ж�ΪĿ�������

typedef struct{
    unsigned int            x;              // Ŀ���x����
    unsigned int            y;              // Ŀ���y����
    unsigned int            w;              // Ŀ��Ŀ��
    unsigned int            h;              // Ŀ��ĸ߶�
}result_struct;                             // ʶ����

typedef struct{
    unsigned char           red;            // [0,255]
    unsigned char           green;          // [0,255]
    unsigned char           blue;           // [0,255]
}color_rgb_struct;                          // RGB��ʽ��ɫ

typedef struct{
    unsigned char           hue;            // [0,240]
    unsigned char           saturation;     // [0,240]
    unsigned char           luminance;      // [0,240]
}color_hsl_struct;                          // HSL��ʽ��ɫ

typedef struct{
    unsigned int            x_start;        // ����x��ʼλ��
    unsigned int            x_end;          // ����x����λ��
    unsigned int            y_start;        // ����y��ʼλ��
    unsigned int            y_end;          // ����y����λ��
}search_area_struct;                        // ����

extern target_condi_struct target_color_condi;  // ɫ����ɫ��ֵ��Ϣ
extern result_struct target_pos_out;            // Ŀ��λ����Ϣ

extern color_rgb_struct rgb;	// ȫ�� RGB �ṹ��
extern color_hsl_struct hsl;	// ȫ�� HSL �ṹ��

extern color_rgb_struct center_rgb;
extern color_hsl_struct center_hsl;

// ɫ��׷�ٺ���
int     color_trace             (const target_condi_struct *condition,result_struct *resu);
// ����ɫ��Ŀ����ֵ����
void    set_color_target_condi  (uint16 rgb565_data, target_condi_struct* condition);

void rgbtohsl(const color_rgb_struct* rgb, color_hsl_struct* hsl);
void pixel_rgbtohsl(uint16* pointer);
#endif

