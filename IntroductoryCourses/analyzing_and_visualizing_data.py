# Analyzing and Visualizing Data
import numpy as np

data = np.loadtxt(
    fname="C:/Users/hrach/Desktop/Denovo Sciences/OxRSE_training/IntroductoryCourses/data/inflammation-01.csv",
    delimiter=",")

print(data)

print(type(data))

print(data.dtype)

print(type(data[0, 0]))

print(data.shape)

print("first value in data:", data[0, 0])

print("middle value in data:", data[30, 20])

print(data[0:4, 0:10])

print(data[5:10, 0:10])

print(data[:3, 36:])

# Selecting every nth item
print(data[::3, ::2].shape)
print(data[0:10:3, 0:10:2])

# Analyzing data
print(np.mean(data))

import time

print(time.ctime())

maxval, minval, stdval = np.max(data), np.min(data), np.std(data)

print("maximum inflammation:", maxval)
print("minimum inflammation:", minval)
print("standard inflammation:", stdval)

patient_0 = data[0, :]  # 0 on the first axis (rows), everything on the second (columns)
print("maximum inflammation for patient 0:", np.max(patient_0))
print("maximum inflammation for patient 2:", np.max(data[2, :]))

print(np.mean(data, axis=0))
print(np.mean(data, axis=0).shape)

print(np.mean(data, axis=1))
print(np.mean(data, axis=1).shape)

element = "oxygen"
print("first three characters:", element[:3])
print("last three characters:", element[-3:])

print(data[3:3, 4:4].shape)
print(data[3:3, :].shape)

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("A = ")
print(A)

B = np.hstack((A, A))
print("B = ")
print(B)

C = np.vstack((A, A))
print("C = ")
print(C)

D = np.hstack((A[:, :1], A[:, -1:]))
print("D = ")
print(D)

D = np.delete(A, 1, 1)
print("D = ")
print(D)

patient3_week1 = data[3, :7]
print("patient3_week1 =", patient3_week1)
print(np.diff(patient3_week1))
print(np.diff(data, axis=1))
print(np.max(np.absolute(np.diff(data, axis=1)), axis=1))

## Visualizing data
import matplotlib.pyplot as plt

image = plt.imshow(data)
plt.show()

ave_inflammation = np.mean(data, axis=0)
ave_plot = plt.plot(ave_inflammation)
plt.show()

max_plot = plt.plot(np.max(data, axis=0))
plt.show()

min_plot = plt.plot(np.min(data, axis=0))
plt.show()

## Multiple figure plots
fig = plt.figure(figsize=(3.0, 10.0))

axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

ave_data = np.mean(data, axis=0)
axes1.set_ylabel("average")
axes1.plot(ave_data, drawstyle="steps-mid")
axes1.set_ylim(np.min(ave_data), np.max(ave_data) * 1.1)

max_data = np.max(data, axis=0)
axes2.set_ylabel("max")
axes2.plot(max_data, drawstyle="steps-mid")
axes2.set_ylim(np.min(max_data), np.max(max_data) * 1.1)

min_data = np.min(data, axis=0)
axes3.set_ylabel("min")
axes3.plot(min_data, drawstyle="steps-mid")
axes3.set_ylim(np.min(min_data), np.max(min_data) * 1.1)

fig.tight_layout()

plt.savefig("inflammation.png")
plt.show()

std_inflammation = np.std(data, axis=0)
plt.plot(std_inflammation)
plt.show()
