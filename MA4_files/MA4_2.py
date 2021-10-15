#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt


def main():
	f = Integer(5)
	cpp_times = []
	py_times = []
	nums = list(range(30,45))
	for n in nums:
		start_cpp = pc()
		f.set(n)
		f.fib()
		end_cpp = pc()

		start_py = pc()
		fib_py(n)
		end_py = pc()

		cpp_times.append(end_cpp - start_cpp)
		py_times.append(end_py - start_py)

	start = pc()
	f.set(47)
	f.fib()
	end = pc()

	print(f'''Calculating fib(47) with python is too slow, but with a complied language like C++,
	the execution takes {end - start} seconds''')

	plt.plot(nums, cpp_times)
	plt.plot(nums, py_times)
	plt.xlabel('n')
	plt.ylabel('Seconds')
	plt.legend(['C++', 'Python'])
	plt.title('Time to calculate fib(n) with compiled and interpreted language')
	plt.savefig('Fibonacci_timing.png')


def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))


if __name__ == '__main__':
	main()