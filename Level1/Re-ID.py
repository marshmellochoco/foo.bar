class solution:
    def solution(num):
        max = 68000
        primeStr = ""
        ''' Debug
        for i in range(max):
            if i % 5000 == 0:
                print("Running: " + str(i))
                print("Success: " + str(len(primeStr)))
                print()
        '''
           if i > 1:
                for j in range(2, i):
                    if i % j == 0 or i % 2 == 0:
                        break
                else:
                    primeStr += str(i)

            if len(primeStr) >= 32000 or len(primeStr) >= num+5:
                break
        return str(primeStr[num:num+5])


print(solution.solution(3))