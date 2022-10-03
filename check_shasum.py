p = open('/home/carman/Downloads/produced.sha')
produced_sha = p.read()

o = open('/home/carman/Downloads/original.sha')
original_sha = o.read()

for i in range(len(original_sha)):
    if original_sha[i] != produced_sha[i]:
        print('Error: The Checksum Failed')
        break
else:
    print('Checksum is completed. No Modification has been detected')