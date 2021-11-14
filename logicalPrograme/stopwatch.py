'''
@Author : Avinash Jadhav
@Date : 2021-11-12
@Last Modify by : Avinash Jadhav
@Title : print stop watch
'''

import time


class StopWatch:

    try:
        def time_convert(sec):
            '''
                   @Description : time_convert function if convert time into sec, minutes, hour
                   @Parameter   : parameter is only one that is sec
                   @return      : - '''
            mins = sec // 60
            sec = sec % 60
            hours = mins // 60
            mins = mins % 60
            print("Time Used = {0}:{1}:{2}".format(int(hours), int(mins), sec))

        input("Press Enter to start")
        start_time = time.time()

        input("Press Enter to stop")
        end_time = time.time()

        time_lapsed = end_time - start_time
        time_convert(time_lapsed)

    except Exception as e:

        print(e)