import itertools

costs = {'A': 1, 'B': 3, 'C': 4, 'D': 6, 'E': 8, 'F': 9}
combinations = itertools.combinations('ABCDEF', 2)

famous_result = 'None'
famous_validation = 100000

for it in combinations:
    temp_result = str(it)
    cost = costs[it[0]] + costs[it[1]]
    available = 'ABCDEF'.strip(''.join(it))
    #print 'available: ' + available
    meta = ''.join(it)
    #print 'meta: ' + meta
    print str(it) + ' idzie, zostaje available - krok 1'
    for it2 in itertools.combinations(meta, 1):
        print str(it2) + ' wraca - krok 2'
        temp_result2 = temp_result + str(it2)
        available2 = available + (''.join(it2))
        #print 'available2: ' + available2
        meta2 = meta.strip(''.join(it2))
        #print 'meta2: ' + meta2
        cost2 = cost + costs[it2[0]]
        for it3 in itertools.combinations(available2, 2):
            print str(it3) + ' idzie, zostaje available - krok 3'
            temp_result3 = temp_result2 + str(it3)
            available3 = available2.strip(''.join(it3))
            meta3 = meta2 + (''.join(it3))
            cost3 = cost2 + costs[it3[0]] + costs[it3[1]]
            for it4 in itertools.combinations(meta3, 1):
                #wraca B - krok 4
                temp_result4 = temp_result3 + str(it4)
                available4 = available3 + (''.join(it4))
                meta4 = meta3.strip(''.join(it4))
                cost4 = cost3 + costs[it4[0]]
                for it5 in itertools.combinations(available4, 2):
                    #EF idzie, zostaje available - krok 5
                    temp_result5 = temp_result4 + str(it5)
                    available5 = available4.strip(''.join(it5))
                    meta5 = meta4 + (''.join(it5))
                    cost5 = cost4 + costs[it5[0]] + costs[it5[1]]
                    for it6 in itertools.combinations(meta5, 1):
                        #wraca C - krok 6
                        temp_result6 = temp_result5 + str(it6)
                        available6 = available5 + (''.join(it6))
                        meta6 = meta5.strip(''.join(it6))
                        cost6 = cost5 + costs[it6[0]]
                        for it7 in itertools.combinations(available6, 2):
                            #BC idzie, zostaje available - krok 7
                            temp_result7 = temp_result6 + str(it7)
                            available7 = available6.strip(''.join(it7))
                            meta7 = meta6 + (''.join(it7))
                            cost7 = cost6 + costs[it7[0]] + costs[it7[1]]
                            for it8 in itertools.combinations(meta7, 1):
                                #B wraca - krok 8
                                temp_result8 = temp_result7 + str(it8)
                                available8 = available7 + (''.join(it8))
                                meta8 = meta7.strip(''.join(it8))
                                cost8 = cost7 + costs[it8[0]]
                                ### only 2 left, send them through bridge
                                #########################################
                                #                                       #
                                temp_result9 = temp_result8 + str(available8)
                                cost9 = cost8 + costs[available[0]] + costs[available[1]]
                                meta9 = meta + (''.join(available))
                                available9 = ''
                                if (cost9 < famous_validation):
                                    famous_validation = cost9
                                    famous_result = temp_result9
    #print ' '

print famous_validation
print famous_result
