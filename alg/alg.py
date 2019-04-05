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
    _orders = []
    _average_order = []
    _average_sum = 0
    ords = obj.completed_jobs.count()
    ord = obj.orders.job_arrivals()
    for ind in range(len(ords[0][2])):
        calculate_station1_R(obj, ind, th_dict)
        calculate_station2_R(obj, ind, th_dict)
        calculate_station3_R(obj, ind, th_dict)
        print("Order at time ", ind, " is ", ord[ind])
        _orders.append(ord[ind][1])
        print("#####################################################")
    for ind, val in enumerate(_orders):
        print(ind, " ,", val)
        if ind <= len(ords[0][2]) - 5:
            _average_order.append(sum(_orders[ind:ind+5])/5)
    print("order 5 day average:")
    print(_average_order)
    # export to a csv file
    import csv
    with open('average_demand.csv', 'w+') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(_average_order)

def backtest_throughput_rate(session_id):
    obj = Littlefield('group6', 'coronado91', session_id)
    th_dict = {
        'queue_th': 100,
        'util_th': 0.90
    }

    ord = obj.orders.job_arrivals()
    rev = obj.completed_jobs.revenues()
    jobs = obj.completed_jobs.count()
    ave_demand = 0
    for ind in range(len(ord)-5, len(ord)):
        calculate_station1_R(obj, ind, th_dict)
        calculate_station2_R(obj, ind, th_dict)
        calculate_station3_R(obj, ind, th_dict)
        print("Order at time ", ind, " is ", ord[ind])
        #print(jobs)

        print("Contract 1 completed jobs for ", ind, " is ", jobs[0][2][ind])
        print("Contract 2 completed jobs for ", ind, " is ", jobs[1][2][ind])
        print("Contract 3 completed jobs for ", ind, " is ", jobs[2][2][ind])
        print("Contract 1 Rev at time ", ind, " is ", rev[0][2][ind])
        print("Contract 2 Rev at time ", ind, " is ", rev[1][2][ind])
        print("Contract 3 Rev at time ", ind, " is ", rev[2][2][ind])
        ave_demand = ave_demand + ord[ind][1]

        print("#####################################################")
    print("Average Demand = ", ave_demand/5)




if  __name__ == '__main__':
    #url = "http://op.responsive.net/Littlefield"
    #R1_capacity = 5*60
    #R3_capacity = 15*60

    #url = "http://op.responsive.net/lt/ucsd2"
    url = 'mit.responsive.net/lt/opscom'
    username = 'radytripler'
    password = 'radymit2019'
    opener = login.Login(username,password,url)
    web_driver = opener.process()
    time.sleep(1)
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    cookies = web_driver.get_cookie('JSESSIONID')
    print(cookies['value'])

#################################################################
    while True:
        #backtest(cookies['value'])
        backtest_throughput_rate(cookies['value'])
        time.sleep(20*60) # refresh every 10 mins
        #keyboard.press(Key.f5)
        #keyboard.release(Key.f5)
        time.sleep(2)
        cookies = web_driver.get_cookie('JSESSIONID')
        print(cookies['value'])