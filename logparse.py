import datetime

def compute_time_diff_seconds(start, end):
    format = "%b %d %H:%M:%S:%f"
    start_time = datetime.datetime.strptime(start, format)
    end_time = datetime.datetime.strptime(end, format)
    return (end_time - start_time).total_seconds()

def get_next_event(filename):
    with open(filename, "r") as datafile:
        for line in datafile:
            if "dut : Device State :" in line:
                line = line.strip()
                action = line.split()[-1]
                timestamp = line[:19]
                yield (action, timestamp)
