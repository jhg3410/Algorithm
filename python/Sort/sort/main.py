import bubble_sort
import insertion_sort
import selection_sort
import shell_sort
import timeit

# A = [10,20,30,40,90,80,70,60,50]    # 어느정도 정렬이 되어있는 배열
A = [90,80,70,60,50,40,30,20,10]    # 정렬이 전혀 되어있지않은 배열
n = len(A)
start_time = timeit.default_timer()
print("정렬된 배열 :",bubble_sort.bubble_sort(A,n))
print("버블정렬의 시간은 : ",timeit.default_timer()-start_time)
start_time = timeit.default_timer()
print("정렬된 배열 :",selection_sort.selection_sort(A,n))
print("선택정렬의 시간은 : ",timeit.default_timer()-start_time)
start_time = timeit.default_timer()
print("정렬된 배열 :",insertion_sort.insertion_sort(A,n))
print("삽입정렬의 시간은 : ",timeit.default_timer()-start_time)
start_time = timeit.default_timer()
print("정렬된 배열 :",shell_sort.shell_sort(A,n))
print("쉘 정렬의  시간은 : ",timeit.default_timer()-start_time)