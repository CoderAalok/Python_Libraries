import numpy as np
import matplotlib.pyplot as plt

x = np.array(([1,2,9],
              [2,3,4]))

y = np.array(([2,3,8],
              [4,6,7]))
plt.grid()
plt.plot(x,y, marker='o')
plt.title('First time use')
plt.show()

# print(x.dtype)
# # print(dir(np))
# xy = np.append(x, [0,3,4,5,6])
# np.append
# print(x)

# print(x+y)
# print(x*y)
# print(x-y)
# print(x/y)
# print(x//y)
# print(x%y)
# ===========================================================================

# find identity matrix(2*2 matrix)
# if x[0][0] == x[1][1] == 1 and x[0][1] == x[1][0] == 0 :
#     print("This is an identity matrix.")
# else:
#     print('This is not an identity matrix.')

# is_identity = True
# for r in range(len(x)):
#     for c in range(len(x[0])):
#         if (r==c and x[r][c]!=1) or (r!=c and x[r][c]!=0):
#             is_identity = False
# if is_identity:
#         print("This is an identity matrix.")
# else:
#     print('This is not an identity matrix.')
# ===========================================================================

# if np.array_equal(x,np.identity(len(x))):
#     print(True)
# else:
#     print(False)
# ===========================================================================

# row,col = x.shape
# print(f"Row: {row}\nColumn: {col}")

# # print(x[1][::-1])
# # append all array combine into one
# print(np.append(x[0],[1,2]))
# # Concatenate into array within array
# print(np.concatenate((x,[[2,4]])))

