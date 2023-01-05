from string import octdigits
from psychopy import monitors
import numpy as np
from metabci.brainstim.paradigm import OC, paradigm
from metabci.brainstim.framework_kent import Experiment
# from functools import partial

if __name__=='__main__':
    mon = monitors.Monitor(
            name='primary_monitor', 
            width=59.6, distance=60,    # width 显示器尺寸cm; distance 受试者与显示器间的距离 
            verbose=False
        )
    mon.setSizePix([1920, 1080])        # 显示器的分辨率
    win_size=np.array([1920, 1080])
    # mon.setSizePix([3840, 2160])        # 显示器的分辨率
    # win_size=np.array([3840, 2160])
    mon.save()
    bg_color_warm = np.array([0, 0, 0])
    # esc/q退出开始选择界面
    ex = Experiment(
        monitor=mon, 
        bg_color_warm=bg_color_warm,    # 范式选择界面背景颜色[-1~1,-1~1,-1~1]
        screen_id=0,
        win_size=win_size,              # 范式边框大小(像素表示)，默认[1920,1080]
        is_fullscr=True,                # True全窗口,此时win_size参数默认屏幕分辨率
        record_frames=False,
        disable_gc=False,
        process_priority='normal',
        use_fbo=False
    )
    win = ex.get_window()

    '''
    Object Control
    '''
    
    fps = 120                                                   # 屏幕刷新率
    text_pos = (0.0, -320.0)                                       # 提示文本位置
    left_pos = [[-350, 0.0]]                                    # 左手位置
    right_pos = [[350, 0.0]]                                    # 右手位置
    tex_color = 2*np.array([179, 45, 0])/255-1                  # 提示文本颜色
    normal_color = [[-0.8,-0.8,-0.8]]                          # 默认颜色
    image_color = [[1,1,1]]                                     # 提示或开始想象颜色
    symbol_height = 100                                         # 提示文本的高度
    n_Elements = 1                                              # 左右手各一个
    stim_length = 350                                           # 长度
    stim_width = 350                                            # 宽度
    basic_OC = OC(win=win)
    basic_OC.config_color(refresh_rate=fps, text_pos=text_pos, left_pos=left_pos, right_pos=right_pos, tex_color=tex_color, 
                          normal_color=normal_color, image_color=image_color, symbol_height=symbol_height, n_Elements=n_Elements, 
                          stim_length=stim_length, stim_width=stim_width)
    basic_OC.config_response()

    bg_color = np.array([-1, -1, -1])                           # 背景颜色
    display_time = 0.5                                            # 范式开始1s的warm时长
    rest_time = 0.5                                               # 提示后的休息时长
    index_time = 1.5                                              # 提示时长，转移视线
    image_time = 4                                              # 想象时长
    response_time = 2                                           # 在线反馈    
    port_addr = 12544 #  0xdefc                                 # 开采集主机端口
    # port_addr = None  #  0xdefc                                 # 关采集主机端口
    # nrep = 2                                                   # block数目
    lsl_source_id =  'meta_online_worker'                       # source id
    online = False # True                                       # 在线实验的标志
    
    nrep = 10                                                   # rep数目


    # for block in range(nBlocks):
        # , take a few long breath, and press space or enter when ready.
    # text = "Object Control about to start...".format(block+1, nBlocks)
    text = "Object Control about to start..."
    ex.register_paradigm(text, paradigm, VSObject=basic_OC, bg_color=bg_color, display_time=display_time, index_time=index_time, 
                        rest_time=rest_time, response_time=response_time, port_addr=port_addr, nrep=nrep, image_time=image_time, 
                        pdim='oc',lsl_source_id=lsl_source_id, online=online)
    ex.run()