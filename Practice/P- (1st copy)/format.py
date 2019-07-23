
start = int(input())
end = int(input())
step = int(input())
print ("inch", "cm")
for i in range(start, end+1, step):
    result = i * 2.54
    print ('%.1f'%i,"" ,'%.1f'%result)
        
 


