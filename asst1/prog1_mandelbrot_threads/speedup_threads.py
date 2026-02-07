import matplotlib.pyplot as plt

threads = [2,3,4,5,6,7,8]

speedup_v1 = [1.92,1.62,2.35,2.38,3.15,3.25,3.82]
speedup_v2 = [1.70,2.22,2.65,3.06,3.49,3.93,4.36]
plt.plot(threads, speedup_v1, marker='o', label='View 1')
plt.plot(threads, speedup_v2, marker='x', label='View 2')
plt.xlabel('Number of Threads')
plt.ylabel('Speedup')
plt.title('Mandelbrot Set Speedup')
plt.grid()
plt.legend()
plt.show()