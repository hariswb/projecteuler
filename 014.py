import datetime

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.get_next(self.data) 
        self.length = 0

    def get_next(self, data):
        if data == 1:
            return None

        if data % 2 == 0:
            return int(data/2)

        return 3*data+1

    def set_length(self, length):
        self.length = length

record = {
    1: Node(1)
}


def generate(init):
    global run
    l = []
    temp = Node(init)

    while True:
        if record.get(temp.data):
            temp = record.get(temp.data)
            closest_length = temp.length 
            for count, key in enumerate(l):
                record[key].set_length(len(l)-count + closest_length)

            break

        l.append(temp.data)
        record[temp.data] = temp
        temp = Node(temp.next)

def check_record():
    print("======================")
    for key, item in record.items():
        print(key, item.length)


start = datetime.datetime.now()

for i in range(2,1000001):
    generate(i)

longest = record[1]

for key, node in record.items():
    if node.length > longest.length:
        longest = node

print("result", longest.__dict__)
print("time", datetime.datetime.now() - start)
