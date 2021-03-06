import heapq
def meetingRoom(intervals):
    intervals.sort()
    meeting_rooms = 1
    heap = [intervals[0][1]]
    for start, end in intervals[1:]:
        if heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        meeting_rooms = max(meeting_rooms, len(heap))
    return meeting_rooms

#intervals = [[0,15], [0, 30], [15, 20], [21, 25]]
intervals = [[7,10], [2, 4]]
print(meetingRoom(intervals))
