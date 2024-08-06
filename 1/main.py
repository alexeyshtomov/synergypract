A = [6, -5, 6, -1, -6, -4, -5, 3]
N = len(A)

max_index = 0
min_index = 0

for i in range(N):
    if A[i] > A[max_index]:
        max_index = i
    if A[i] < A[min_index]:
        min_index = i

if min_index > max_index:
    min_index, max_index = max_index, min_index

sum_negative = 0

for i in range(min_index + 1, max_index):
    if A[i] < 0:
        sum_negative += A[i]


print('Результат:', sum_negative)
