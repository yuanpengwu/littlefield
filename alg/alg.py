from littlefield import Littlefield
import login
import time


def calculate_station1_R(session, time_frame, thre_dict):
    assert isinstance(session, Littlefield)
    assert isinstance(time_frame, int)
    R1_queue_l = session.station1.queue_size()
    R1_utilization_l = session.station1.utilization()
    print("At time = ", time_frame, " , R1 queue size = ", R1_queue_l[time_frame])
    print("At time = ", time_frame, " , R1 utilization = ", R1_utilization_l[time_frame])
    if R1_queue_l[time_frame][1] > thre_dict['queue_th'] and \
            R1_utilization_l[time_frame][1] > thre_dict['util_th']:
        print('Warning: Station1 MIGHT need to increase at least one machine !!')
        if time_frame > 0 and R1_utilization_l[time_frame-1][1] > thre_dict['util_th']-0.2: # check previous time frame
            print('Warning: Station1 MUST increase at least one machine !!')

def calculate_station2_R(session, time_frame, thre_dict):
    assert isinstance(session, Littlefield)
    assert isinstance(time_frame, int)
    R2_queue_l = session.station2.queue_size()
    R2_utilization_l = session.station2.utilization()
    print("At time = ", time_frame, " , R2 queue size = ", R2_queue_l[time_frame])
    print("At time = ", time_frame, " , R2 utilization = ", R2_utilization_l[time_frame])
    if R2_queue_l[time_frame][1] > thre_dict['queue_th'] and \
            R2_utilization_l[time_frame][1] > thre_dict['util_th']:
        print('Warning: Station2 MIGHT need to increase at least one machine !!')
        if time_frame > 0 and R2_utilization_l[time_frame - 1][1] > thre_dict['util_th']-0.2:  # check previous time frame
            print('Warning: Station2 MUST increase at least one machine !!')

def calculate_station3_R(session, time_frame, thre_dict):
    assert isinstance(session, Littlefield)
    assert isinstance(time_frame, int)
    R3_queue_l = session.station3.queue_size()
    R3_utilization_l = session.station3.utilization()
    print("At time = ", time_frame, " , R3 queue size = ", R3_queue_l[time_frame])
    print("At time = ", time_frame, " , R3 utilization = ", R3_utilization_l[time_frame])
    if R3_queue_l[time_frame][1] > thre_dict['queue_th'] and \
            R3_utilization_l[time_frame][1] > thre_dict['util_th']:
        print('Warning: Station3 MIGHT need to increase at least one machine !!')
        if time_frame > 0 and R3_utilization_l[time_frame - 1][1] > thre_dict['util_th']-0.2:  # check previous time frame
            print('Warning: Station3 MUST increase at least one machine !!')



def backtest(session_id):
    obj = Littlefield('group6', 'coronado91', session_id)
    th_dict = {
        'queue_th' : 100,
        'util_th' : 0.99
    }
    for ind in range(260):
        calculate_station1_R(obj, ind, th_dict)
        calculate_station2_R(obj, ind, th_dict)
        calculate_station3_R(obj, ind, th_dict)

def backtest_throughput_rate(session_id):
    obj = Littlefield('group6', 'coronado91', session_id)



if  __name__ == '__main__':
    #url = "http://op.responsive.net/Littlefield"
    #R1_capacity = 5*60
    #R3_capacity = 15*60

    url = "http://op.responsive.net/lt/ucsd2"
    username = 'group6'
    password = 'coronado91'
    opener = login.Login(username,password,url)
    web_driver = opener.process()
    time.sleep(3)
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    cookies = web_driver.get_cookie('JSESSIONID')
    print(cookies['value'])


    backtest(cookies['value'])