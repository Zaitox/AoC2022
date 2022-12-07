import csv
framesize = 4
framesize_message = 14

def check_frame_is_start(frame):
    for c in frame:
        if frame.count(c) > 1:
            return False
    return True

with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    buf = csv_reader.__next__()[0]
    
    for i in range(framesize, len(buf)+1):
        frame = buf[i-framesize:i]
        if check_frame_is_start(frame):
            print(f'found start {i}:{frame}')
            break

    print(f'buf len {len(buf)}')
    print(f'stack: done')
    
with open('input.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    buf = csv_reader.__next__()[0]
    
    for i in range(framesize_message, len(buf)+1):
        frame = buf[i-framesize_message:i]
        if check_frame_is_start(frame):
            print(f'found start {i}:{frame}')
            break


