import datetime

def compute_time_diff_seconds(start, end):
    format = "%b %d %H:%M:%S:%f"
    start_time = datetime.datetime.strptime(start, format)
    end_time = datetime.datetime.strptime(end, format)
    return (end_time - start_time).total_seconds()
