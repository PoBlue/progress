
def progress_for_time(total_time, time_of_steps, finished_steps):
    """compute progress with time pramas
    @total_time: time in min, such as 10 min
    @time_of_steps
    """
    return (time_of_steps * finished_steps) / total_time * 100

def progress_for_step(total_steps, finished_steps):
    """compute progress with step pramas"""
    return finished_steps / total_steps * 100

# # test progress_for_time
# print(progress_for_time(200, 10, 5))

# # test progress_for_step
# print(progress_for_step(10, 5))
