#
#  b1 = 1
#  a1~a5,b2~b4 in [1,2,4,5,6,7,8,9] can not be duplicated
#
#   a5 a4 a3 a2 a1
#   -  b4 b3 b2 b1
# -----------------
#   3  3  3  3   3
#
candidates = [1,2,4,5,6,7,8,9]

for a1 in candidates:
    for a2 in [x for x in candidates if x!=a1]:
        for a3 in [x for x in candidates if x != a1 and x!=a2]:
            for a4 in [x for x in candidates if x != a1 and x!=a2 and x!=a3]:
                for a5 in [x for x in candidates if x != a1 and x != a2 and x != a3 and x!=a4]:
                    b1 =3
                    for b2 in [x for x in candidates if x != a1 and x != a2 and x != a3 and x!=a4 and x!=a5]:
                        for b3 in [x for x in candidates if x != a1 and x != a2 and x != a3 and x != a4 and x != a5 and x!=b2]:
                            for b4 in [x for x in candidates if  x != a1 and x != a2 and x != a3 and x != a4 and x != a5 and x != b2 and x!=b3]:
                                a = a1 + a2*10 + a3*100 + a4*1000 + a5*10000
                                b = b1 + b2*10 + b3*100 + b4*1000
                                result = a-b
                                if result == 33333:
                                    print("found solution:",a,b)
                                    
