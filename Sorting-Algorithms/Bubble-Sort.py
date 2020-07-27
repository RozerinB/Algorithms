def bubbleSort(data):
    print("current state:", data)
    for i in range (len(data) -1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

def main():
    list1 = [70, 2, 16, 22, 11, 90]
    bubbleSort(list1)
    print("Result: ", list1)

if __name__ == "__main__":
    main()
