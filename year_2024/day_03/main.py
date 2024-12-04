import re


if __name__ == '__main__':

    with open('input') as file:
        data = "".join(file.readlines())

        data = data+"don't()"


        start = 0
        result = []
        
        while start < len(data):

            res = re.search(r"don't\(\)", data[start:])

            result += re.findall(r"mul\((\d+),(\d+)\)", data[start:start+res.start()])

            next_ = re.search(r"do\(\)", data[start+res.end():])
            if next_ is None:
                break

            start += next_.end()+res.end()
            

        # Part II
        print(sum(int(a)*int(b) for a, b in result))



        result = re.findall(r"mul\((\d+),(\d+)\)", data)

        # Part I
        print(sum(int(a)*int(b) for a, b in result))