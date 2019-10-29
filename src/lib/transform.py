import collections

# window_segment segments a datastructure such that every segment is of equal
# length by accumulating a sliding window. Example: [1,2,3] -> [[1,2], [2,3]]
# 
# params:
#    data - n dimensional list like data structure
#    segment_length - int
# 
# example:
#    >>> data = list(range(0,4))
#    >>> seg_len = 3
#    >>> window_segment(data, seg_len)
#    [[0, 1, 2], [1, 2, 3]]
# 
#    >>> data = list(range(0,4))
#    >>> seg_len = 5
#    >>> window_segment(data, seg_len)
#    [[0, 1, 2, 3]]
def window_segment(data, segment_length):
    # if data is a single element list or an empty list it is returned 
    # unmodified.
    if len(data)<=1:
        return data
    
    if len(data)<=segment_length:
        return [data]
    
    segments = []
    
    # deque is a ring buffer. Using this data structure over a normal list 
    # allows strict control over the length of the segment without having to
    # manage messy index handling.
    deque = collections.deque(maxlen=segment_length)

    for row in data:
        
        deque.append(row)
        
        # since deque is a ring buffer the only point in this loop that the 
        # length will not be equal to segment_length is for the first
        # segment_length - 1 steps. This conditional is to allow those first
        # steps to accumulate to the desired length
        if len(deque) == segment_length:
            
            # before deque can be appended to the accumulator it must be 
            # converted to another type of container. This forces python to 
            # copy the the contents of the ring buffer. Otherwise it is 
            # accumulate references to the ring buffer. After this loop 
            # completes those references will point to the same place in 
            # memory.
            segments.append(list(deque))
            
    return segments

def window_aggregate(segments):
    if len(segments) < 1:
        return segments
    
    # There is a special case when the single element list will contain a list
    # of all the data. This case occurs when the segmenter is asked to segment
    # an n length structure into segments that are n elements long or longer.
    # when that is the case the inner list is unwrapped and returned.
    if len(segments) == 1:
        us = segments[0] # unwrapped segment
        
        if type(us) == type(list()):
            return us
        
        return segments
        
    # TODO: document this transformation
    head = [s[0] for s in segments[:-1]]
    tail = segments[-1]
    return head + tail