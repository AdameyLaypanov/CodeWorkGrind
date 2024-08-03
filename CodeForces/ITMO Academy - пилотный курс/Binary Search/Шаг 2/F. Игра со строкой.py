def can_form_p_after_removing_k(t, p, a, k):
    n = len(t)
    m = len(p)

    removed = [False] * n
    for i in range(k):
        removed[a[i] - 1] = True

    p_index = 0
    for i in range(n):
        if not removed[i]:
            if t[i] == p[p_index]:
                p_index += 1
                if p_index == m:
                    return True
    return False


def max_letters_to_remove(t, p, a):
    left, right = 0, len(t)

    while left < right:
        mid = (left + right + 1) // 2
        if can_form_p_after_removing_k(t, p, a, mid):
            left = mid
        else:
            right = mid - 1

    return left


# Пример использования
t = input().strip()
p = input().strip()
a = list(map(int, input().strip().split()))

print(max_letters_to_remove(t, p, a))
