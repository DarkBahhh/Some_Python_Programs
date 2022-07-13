import datetime
import sys

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

def extract_data(filename):
    time_on_started = None
    errs = []
    total_time_on = 0
    for action, timestamp in get_next_event(filename):
        if "ERR" == action:
            errs.append(timestamp)
        elif ("ON" == action) and (not time_on_started):
            time_on_started = timestamp
        elif ("OFF" == action) and time_on_started:
            time_on = compute_time_diff_seconds(time_on_started, timestamp)
            total_time_on += time_on
            time_on_started = None
    return total_time_on, errs

if __name__ == "__main__":
    total_time_on, errs = extract_data(sys.argv[1])
    print("The device was ON during {} seconds.".format(total_time_on))
    if errs:
        print("Timestamp for error event:")
        for err in errs:
            print("\t{}".format(err))
    else:
        print("No error found.")
