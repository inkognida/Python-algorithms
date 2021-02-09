
print('x', 'y', 'w', 'z', ' ', 'f')
for x in 0,1:
    for y in 0,1: 
        for w in 0,1: 
            for z in 0,1: 
                f = x or y or w or z and not(z) #example function
                if int(f) == 1: 
                    print(x,y,w,z, ' ', int(f))
