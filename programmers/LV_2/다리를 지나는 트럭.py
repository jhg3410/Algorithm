def solution(bridge_length, weight, truck_weights):
    answer = 0
    last_truck = []
    crossing_truck = []
    now_weight = 0 
    length = len(truck_weights)

    while len(last_truck)!= length:
        print(answer,last_truck,crossing_truck,truck_weights)
        answer += 1
        if truck_weights:
            for cross in crossing_truck:
                cross[1] += 1
            for cross in crossing_truck:
                if cross[1] == bridge_length:
                    crossing_truck.remove(cross)
                    now_weight -= cross[0]
                    last_truck.append(cross[0])
            if now_weight+truck_weights[0] <= weight:
                tmp = truck_weights.pop(0)
                crossing_truck.append([tmp,0])
                now_weight += tmp
            
        else:
            for cross in crossing_truck:
                cross[1] += 1
            for cross in crossing_truck:    
                if cross[1] == bridge_length:
                    crossing_truck.remove(cross)
                    now_weight -= cross[0]
                    last_truck.append(cross[0])
    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]	
print(solution(bridge_length,weight,truck_weights))
