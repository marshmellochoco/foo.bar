from fractions import Fraction
def solution(pegs):
    # Why do excessive work???
    if len(pegs) == 1:
        return [-1, -1]
        
    rad = calculateFirstRadius(pegs)

    # If the first radius is less then 2, 
    # the last radius will be less than 1 which is invalid
    if rad < 2:
        return [-1, -1]

    # Checking if any peg violates the laws of physics
    currentRad = rad
    for i in range(0, len(pegs)-2):
        nextRad = pegs[i+1] - pegs[i] - currentRad
        if currentRad < 1 or nextRad < 1:
            return [-1,-1]
        currentRad = nextRad
    return [rad.numerator, rad.denominator]

def calculateFirstRadius(pegs):
    # Calculate the radius of the first peg according to the formula
    isEven = True if len(pegs) % 2 == 0 else False
    tempRad = -pegs[0] + pegs[len(pegs)-1] if isEven else -pegs[0] -pegs[len(pegs)-1]
    if len(pegs) > 2:
        for i in range(1, len(pegs)-1):
            tempRad += 2 * pegs[i] * (-1)**(i+1)
    return Fraction(2 * (float(tempRad)/3 if isEven else tempRad)).limit_denominator()


# Test if it is working properly
print("yep" if solution([4,30,50]) == [12, 1] else "nope")


"""
r0/2 = rN (last peg has half radius compare to the first peg to achieve 2x RPM)
r:radius, p:center position of peg

3 Pegs (N=3)                |   4 Pegs (N=4)                    |   5 Pegs (N=5)
r1 + r2 = p2 - p1           |   r3 + r4 = p4 - p3               |   r4 + r5 = p5 - p4
r2 + r3 = p3 - p2           |   From 1:                         |   From 2:
                            |   r1 = p2-p1-p3+p2+r3             |   r1 = -p1+2p2-2p3+p4-r4
r1 = p2-p1-r2               |      = p2-p1-p3+p2+(p4-p3-r4)     |      = -p1+2p2-2p3+p4-(p5-p4-r5)
   = p2-p1-(p3-p2-r3)       |      = 2p2-p1-2p3+p4-r4 ---2      |      = -p1+2p2-2p3+p4-p5+p4+r5
   = p2-p1-p3+p2+r3 ---1    |      = -p1+2p2-2p3+p4-r1/2 ---3   |      = -p1+2p2-2p3+2p4-p5+r1/2
   = p2-p1-p3+p2+r1/2       |   2r1= 2(-p1+2p2-2p3+p4)-r1       |   2r1= 2(-p1+2p2-2p3+2p4-p5)+r1
2r1= 2(-p1+2p2-p3)+r1       |   3r1= 2(-p1+2p2-2p3+p4)          |   r1 = 2(-p1+2p2-2p3+2p4-p5)
r1 = 2(-p1+2p2-p3)          |   r1 = 2(-p1+2p2-2p3+p4)/3            

Conclusion:
r1 = 2(-p1+2p2-2p3+2p4...-pNOdd)      where N is odd
r1 = 2(-p1+2p2-2p3+2p4...+pNEven)/3   where N is even

"""
