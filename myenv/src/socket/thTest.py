import time
def inc_func1():
	i = 0
	while True:
		print("inc_func1() i : %d" % i)
		time.sleep(1)
		i += 1

def inc_func2():
	i = 0
	while True:
		print("inc_func2() i : %d" % i)
		i += 1
		time.sleep(1)

if __name__ == '__main__':
	inc_func1()
	inc_func2()
