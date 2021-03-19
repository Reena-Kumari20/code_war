def count_positives_sum_negatives(arr):
    i=0
    count=0
    sum=0
    while i<len(arr):
        if arr[i]>0:
            count=count+1
        elif arr[i]==0:
            pass
        else:
            sum=sum+arr[i]
        i=i+1
    return([count,sum])