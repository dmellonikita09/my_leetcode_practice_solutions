def meetingRoom(intervals):
    #0--5--10--15--20--25--30
    intervals.sort()
    last_end = -1
    for start, end in intervals:
        if last_end <= start:
            last_end = end
        else:
            return False
    return True
intervals = [[7,10], [2, 4]]
print(meetingRoom(intervals))
#TC o(nlogn)
#SC o(1)