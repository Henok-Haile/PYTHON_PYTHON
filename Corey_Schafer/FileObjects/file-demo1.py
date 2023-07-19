# File objects

with open('HENOK.jpg', 'rb') as rf:
    with open('HENOK_copy.jpg', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)