/*********************************************************************************************************************
* MCX Vision Opensourec Library ����MCX Vision ��Դ�⣩��һ�����ڹٷ� SDK �ӿڵĵ�������Դ��
* Copyright (c) 2024 SEEKFREE ��ɿƼ�
* 
* ���ļ��� MCX Vision ��Դ���һ����
* 
* MCX Vision ��Դ�� ��������
* �����Ը��������������ᷢ���� GPL��GNU General Public License���� GNUͨ�ù������֤��������
* �� GPL �ĵ�3�棨�� GPL3.0������ѡ��ģ��κκ����İ汾�����·�����/���޸���
* 
* ����Դ��ķ�����ϣ�����ܷ������ã�����δ�������κεı�֤
* ����û�������������Ի��ʺ��ض���;�ı�֤
* ����ϸ����μ� GPL
* 
* ��Ӧ�����յ�����Դ���ͬʱ�յ�һ�� GPL �ĸ���
* ���û�У������<https://www.gnu.org/licenses/>
* 
* ����ע����
* ����Դ��ʹ�� GPL3.0 ��Դ���֤Э�� �����������Ϊ���İ汾
* �������Ӣ�İ��� libraries/doc �ļ����µ� GPL3_permission_statement.txt �ļ���
* ��ӭ��λʹ�ò����������� ���޸�����ʱ���뱣����ɿƼ��İ�Ȩ����������������
* 
* �ļ�����          main
* ��˾����          �ɶ���ɿƼ����޹�˾
* �汾��Ϣ          �鿴 libraries/doc �ļ����� version �ļ� �汾˵��
* ��������          MDK 5.38a
* ����ƽ̨          MCX Vision
* ��������          https://seekfree.taobao.com/
* 
* �޸ļ�¼
* ����              ����                ��ע
* 2024-04-21        ZSY            first version
********************************************************************************************************************/
#include "zf_model_process.h"
#if defined(__cplusplus)
extern "C" // mian�ļ���C++�ļ��������Ҫ����C���Ե�ͷ�ļ�������Ҫʹ��extern "C"
{
#endif /* __cplusplus */ 
#include "zf_common_headfile.h"
#include "color_tracer.h"
#include "Uart.h"
#include "Camera.h"
#include "Menu.h"
	#include "micro_time.h"

// ���µĹ��̻��߹����ƶ���λ�����ִ�����²���
// ��һ�� �ر��������д򿪵��ļ�
// �ڶ��� project->clean  �ȴ��·�����������

// ���İ������������Ҫ�ֶ���λ������
// ���İ������������Ҫ�ֶ���λ������
// ���İ������������Ҫ�ֶ���λ������.
    
// ����������к�ģ���ϵ�Core����˸��˵�����������HardFault������Ҫ����Ƿ�������Խ�磬����û�г�ʼ��������ʱ��û�����õ����
    
// *************************** ���̲���˵�� ***************************
// 1.ʹ��DAP����������ģ��,��IPS2.0��Ļ�嵽ģ���ϣ�ע�����ŷ���
// 
// 2.MCX Vision���ر����̣�
// 
// 3.��λ���İ壨��Ҫ�ֶ���λ�� 
// 
// 4.��Ļ����ʾʵʱͼ�񲢿��ɫ��Ŀ�꣬ͨ���������Ը�����Ļ������ɫ�л�ʶ��ɫ��

// **************************** �������� ****************************

uint8 mcx_param_init_flag;	// MCX ������ʼ����־λ��1 Ϊ��ʼ���ɹ���

// LED״̬ö��
enum 
{
    LED_ON = 0,
    LED_OFF = 1
}led_state_enum;

// LED���ƺ궨��
#define LED_WHITE(x)    gpio_set_level(gpio_led_white,  (uint8)x)

uint8 led_flag;

// LED �����Ŷ���
gpio_struct gpio_led_white =    {GPIO2, 11u};	

// KEY���Ŷ���
gpio_struct gpio_key_1 =        {GPIO4, 2u};
gpio_struct gpio_key_2 =        {GPIO4, 3u};

int main(void)
{
    // ʱ�Ӻ͵��Դ���-����4��ʼ��
    zf_board_init();
    // �û�����-����5��ʼ��
    user_uart_init();
    // ��ʱ300ms
    system_delay_ms(300);
    // ʹ��C++�����޷�ʹ��printf������ʹ��zf_debug_printf��zf_user_printf���
    zf_debug_printf("debug_uart_init_finish\r\n");  // ʹ�õ��Դ���-����4��������
//    zf_user_printf("user_uart_init_finish\r\n");  // ʹ���û�����-����5��������

    // ��ʼ������
    gpio_init(gpio_key_1, GPI, 0, PULL_UP);
	gpio_init(gpio_key_2, GPI, 0, PULL_UP);
	// LED ��ʼ��
	gpio_init(gpio_led_white, GPO, 0, PULL_UP);
    // ��Ļ��ʼ��
    ips200_init();
    // ����ͷ��ʼ��
    scc8660_init();
	
    while (1)
    {
        if(scc8660_finish)
        {
            scc8660_finish = 0;
			
			// ����ɫ������ֵ�İ���
            if(!gpio_get_level(gpio_key_1))
			{
				// ͨ��ͼ��������������ɫ��ʶ����ֵ
                set_color_target_condi((*((uint16*)g_camera_buffer + SCC8660_H/2 * SCC8660_W + SCC8660_W/2)), &target_color_condi);
				
				#if IS_SHOW_PARAM
				// ��ȡ��ǰ��Ļ�������ص�� HSL ֵ����ʾ���˵���
				uint16 byte = *(scc8660_image + SCC8660_H/2 * SCC8660_W + SCC8660_W/2);
				center_rgb.red   = (unsigned char)((SWAPBYTE(byte) & 0xf800) >> 8);
				center_rgb.green = (unsigned char)((SWAPBYTE(byte) & 0x07e0) >> 3);
				center_rgb.blue  = (unsigned char)((SWAPBYTE(byte) & 0x001f) << 3);
				rgbtohsl(&center_rgb, &center_hsl);
				
				menu_show();
				#endif
			}
			
			// ���� LED ������İ���
			if(!gpio_get_level(gpio_key_2)) led_flag =~led_flag;
			if(led_flag) LED_WHITE(LED_OFF);
			else LED_WHITE(LED_ON);
			
			#if IS_SHOW_SCC8660
            ips200_show_scc8660((uint16_t*)g_camera_buffer);
			#endif
			
			// ɫ����
            if(color_trace(&target_color_condi, &target_pos_out))
            {
				od_result.x1 = target_pos_out.x - target_pos_out.w/2;
				od_result.y1 = target_pos_out.y - target_pos_out.h/2;
				od_result.x2 = target_pos_out.x + target_pos_out.w/2;
				od_result.y2 = target_pos_out.y + target_pos_out.h/2;
				
				// �ж������Ƿ��������ڣ����ڵĻ���������
				if(box_in_saidao())
				{
					judge_corner();
					user_result_uart_send();
					
					zf_debug_printf("x1:%d,y1:%d,x2:%d,y2:%d\r\n", od_result.x1, od_result.y1, od_result.x2, od_result.y2);
				}
				
				#if IS_SHOW_SCC8660
				// ��Ļ��ʾ����
				// ���Ŀ������
                ips200_draw_line((target_pos_out.x - target_pos_out.w/2), (target_pos_out.y - target_pos_out.h/2), (target_pos_out.x + target_pos_out.w/2), (target_pos_out.y - target_pos_out.h/2), 0x0000);
                ips200_draw_line((target_pos_out.x - target_pos_out.w/2), (target_pos_out.y - target_pos_out.h/2), (target_pos_out.x - target_pos_out.w/2), (target_pos_out.y + target_pos_out.h/2), 0x0000);
                ips200_draw_line((target_pos_out.x - target_pos_out.w/2), (target_pos_out.y + target_pos_out.h/2), (target_pos_out.x + target_pos_out.w/2), (target_pos_out.y + target_pos_out.h/2), 0x0000);
                ips200_draw_line((target_pos_out.x + target_pos_out.w/2), (target_pos_out.y - target_pos_out.h/2), (target_pos_out.x + target_pos_out.w/2), (target_pos_out.y + target_pos_out.h/2), 0x0000);
				#endif
            }
			
			#if IS_SHOW_SCC8660
			// ����Ļ������
			ips200_draw_line(SCC8660_W/2-10, SCC8660_H/2, SCC8660_W/2+10, SCC8660_H/2, 0x0000);
			ips200_draw_line(SCC8660_W/2, SCC8660_H/2-10, SCC8660_W/2, SCC8660_H/2+10, 0x0000);
			
			// ��Ŀ����������
//			ips200_draw_line(0, (od_result.y1+od_result.y2)/2, SCC8660_W-1, (od_result.y1+od_result.y2)/2, 0x0000);
//			ips200_draw_line((od_result.x1+od_result.x2)/2, 0, (od_result.x1+od_result.x2)/2, SCC8660_H-1, 0x0000);
			#endif
			
			// ���ڷ���
			if(mcx_param_init_flag)
			{
				mcx_param_init_flag=0;
				mcx_send_buffer[0] = HEADER_FOOTER_NUM+DATA_SIZE_FLAG_NUM+2;
				mcx_send_buffer[1] = PARAM_INIT_BYTE;
				mcx_send_buffer[2] = 1;	// ��ʼ���ɹ�
				user_uart_send(mcx_send_buffer, 2+DATA_SIZE_FLAG_NUM);
				
				#if IS_SHOW_PARAM
				menu_show();
				#endif
			}
        }
    }
}

// **************************** �������� ****************************
#if defined(__cplusplus)
}
#endif /* __cplusplus */