x,y,w,h = map(int,input().split())

distance_to_left = x
distance_to_bottom=y
distance_to_right=w-x
distance_to_top= h-y

min_distance = distance_to_left

if(min_distance>distance_to_bottom):
    min_distance=distance_to_bottom

if(min_distance>distance_to_right):
    min_distance=distance_to_right

if(min_distance>distance_to_top):
    min_distance=distance_to_top

print(min_distance)