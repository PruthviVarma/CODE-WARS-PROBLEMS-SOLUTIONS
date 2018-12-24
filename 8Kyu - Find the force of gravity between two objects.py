def solution(a, b) :
    # your code goes here
     weight = { 'kg':1, 'g':1/1000, 'mg':1/1000000, 'μg':1/1000000000, 'lb':0.453592 }
     distance={ 'm':1, 'cm':1/100, 'mm':1/1000, 'μm':1/1000000, 'ft':0.3048}
     gravity = 6.67 * 10**(-11)
     total_distance = a[2] * distance[b[2]]
     return (gravity * a[0] * weight[b[0]] * a[1] * weight[b[1]])/(total_distance**2)
