# s = "the sky is blue"
# L = s.split()
# L = " ".join(L[::-1])
# print(L)

# inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]

# # index = inorder.index(postorder[-1])
# # # print(index)
# # print(inorder[0:index], postorder[0:index])

# print(inorder[0:0])

# res = []
# for i in range(5):
#     res.append([1] * (i + 1))
# print(res)

# x = [
#     [2],
#     [3, 4],
#     [6, 5, 7],
#     [4, 1, 8, 3]
# ]
# f = [0] * (len(x) + 1)
# print(f)


# x = [2, 1]
# print(x.index(max(x)))


# a = {1, 2, 3, 4, 5, 6}
# print(a)

class Solution:
    def shell_sort(self, list):
        n = len(list)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = list[i]
                j = i
                while j >= gap and list[j - gap] > temp:
                    list[j] = list[j - gap]
                    j -= gap
                list[j] = temp
            gap = gap // 2
        return list


print(Solution().shell_sort([2, 1, 3, 7, 5, 6, 4]))
