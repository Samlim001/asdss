def game(result,point1,betting):
    bet = betting
    global winlose
    if bet == '':
        winlose = 0
    else:
        open9 = result
        open9_string = "".join(open9)
        bar2 = open9_string.split("-")
        bar = bar2[1]
        bar1 = bar2[0]
        point = point1
        bs = bet.split()
        #-----------------------------------------------
        #----------------中二王-------------------------
        #-----------------------------------------------
        try:
            if "/" in bs[0]:
                bet02 = 0
                bet03 = 0
                bet04 = 0
                bet05 = 0
                bs1 = bs[0].split("/")
                b1 = bs1[1].count("1")
                b2 = bs1[1].count("2")
                b3 = bs1[1].count("3")
                b4 = bs1[1].count("4")
                bt = b1+b2+b3+b4
                if bt == 2:
                    if "-" not in bs[1] and "+" not in bs[1]:
                        bss1 = int(bs[1])
                        y480 = bss1 % 120
                        y100 = bss1 % 100
                        y580 = bss1 % 580
                        y340 = bss1 % 340
                        y1000 = bss1 % 1000
                        if bar in bs1[1]:
                            if y480 == 0 or y100 == 0 or y580 == 0 or y340 == 0 or y1000 == 0:
                                bet02 = bss1/2
                            else:
                                bet02 = bss1*60
                        elif bar not in bs1[0] and bar not in bs1[1]:
                            if y480 == 0 or y100 == 0 or y580 == 0 or y340 == 0 or y1000 == 0:
                                bet02 = bss1*0
                            else:
                                bet02 = bss1*0
                        elif bar in bs1[0]:
                            if y1000 == 0:
                                bet02 = bss1/1000*-1050
                            elif y480 == 0:
                                bet02 = bss1/120*-125
                            elif y100 == 0:
                                bet02 = bss1/100*-105
                            elif y580 == 0:
                                bet02 = bss1/580*-605
                            elif y340 == 0:
                                bet02 = bss1/340*-355
                            else:
                                bet02 = bss1*-125
                    
                    elif "-" in bs[1] and "+" not in bs[1]:
                        bet1 = bs[1].split("-")
                        bet02 = 0
                        if bet1[0] == "60" and "400" in bet1[1]:
                            if "x" in bet1[1]:
                                bss = bet1[1].split("x")
                                bss1 = int(bet1[0])
                                bss2 = int(bss[0])
                                bss3 = int(bss[1])
                                if bar in bs1[1]:
                                    bet02 = (bss1/3+bss2/2)*bss3
                                elif bar not in bs1[0] and bar not in bs1[1]:
                                    bet02 = (bss1/3+bss2*0)*bss3
                                elif bar in bs1[0]:
                                    bet02 = (bss1*-1+bss2*-1-20)*bss3
                            elif "x" not in bet1[1]:
                                bss1 = int(bet1[0])
                                bss2 = int(bet1[1])
                                if bar in bs1[1]:
                                    bet02 = bss1/3+bss2/2
                                elif bar not in bs1[0] and bar not in bs1[1]:
                                    bet02 = bss1/3+bss2*0
                                elif bar in bs1[0]:
                                    bet02 = (bss1*-1+bss2*-1)-20
                        else:
                            bss1 = int(bet1[0])
                            bss2 = int(bet1[1])
                            y4801 = bss1 % 120
                            y480 = bss2 % 120
                            y100 = bss2 % 100
                            y580 = bss2 % 580
                            y340 = bss2 % 340
                            y1000 = bss2 % 1000
                            y90 = bss1 - 90
                            bss1 = int(bet1[0])
                            bss2 = int(bet1[1])
                            if bar in bs1[1]:
                                if y4801 == 0 and y480 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y4801 == 0 and y100 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y4801 == 0 and y580 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y4801 == 0 and y340 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y4801 == 0 and y1000 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y4801 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                    bet02 = bss1/3+bss2*60
                                elif y4801 != 0 and y480 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y4801 != 0 and y100 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y4801 != 0 and y580 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y4801 != 0 and y340 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y4801 != 0 and y1000 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y4801 != 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0 and y90 != 0:
                                    bet02 = bss1*40+bss2*60

                                elif y90 == 0 and y480 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y90 == 0 and y100 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y90 == 0 and y580 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y90 == 0 and y340 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y90 == 0 and y1000 == 0:
                                    bet02 = bss1/3+bss2/2
                                elif y90 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                    bet02 = bss1/3+bss2*60
                                elif y90 != 0 and y480 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y90 != 0 and y100 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y90 != 0 and y580 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y90 != 0 and y340 == 0:
                                    bet02 = bss1*40+bss2/2
                                elif y90 != 0 and y1000 == 0:
                                    bet02 = bss1*40+bss2/2

                            elif bar not in bs1[0] and bar not in bs1[1]:
                                if y4801 == 0 and y480 == 0:
                                    bet02 = bss1/3+bss2*0
                                elif y4801 == 0 and y100 == 0:
                                    bet02 = bss1/3+bss2*0
                                elif y4801 == 0 and y580 == 0:
                                    bet02 = bss1/3+bss2*0
                                elif y4801 == 0 and y340 == 0:
                                    bet02 = bss1/3+bss2*0   
                                elif y4801 == 0 and y1000 == 0:
                                    bet02 = bss1/3+bss2*0   
                                elif y4801 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                    bet02 = bss1/3+bss2*0
                                elif y4801 != 0 and y480 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y4801 != 0 and y100 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y4801 != 0 and y580 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y4801 != 0 and y340 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y4801 != 0 and y1000 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y4801 != 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0 and y90 != 0:
                                    bet02 = bss1*40+bss2*0

                                elif y90 == 0 and y480 == 0:
                                    bet02 = bss1/3+bss2*0
                                elif y90 == 0 and y100 == 0:
                                    bet02 = bss1/3+bss2*0
                                elif y90 == 0 and y580 == 0:
                                    bet02 = bss1/3+bss2*0
                                elif y90 == 0 and y340 == 0:
                                    bet02 = bss1/3+bss2*0   
                                elif y90 == 0 and y1000 == 0:
                                    bet02 = bss1/3+bss2*0   
                                elif y90 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                    bet02 = bss1/3+bss2*0
                                elif y90 != 0 and y480 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y90 != 0 and y100 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y90 != 0 and y580 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y90 != 0 and y340 == 0:
                                    bet02 = bss1*40+bss2*0
                                elif y90 != 0 and y1000 == 0:
                                    bet02 = bss1*40+bss2*0

                            elif bar in bs1[0]:
                                if y4801 == 0 and y1000 == 0:
                                    bet02 = bss1/120*-125+bss2/1000*-1050
                                elif y4801 == 0 and y480 == 0:
                                    bet02 = bss1/120*-125+bss2/120*-125
                                elif y4801 == 0 and y100 == 0:
                                    bet02 = bss1/120*-125+bss2/100*-105
                                elif y4801 == 0 and y580 == 0:
                                    bet02 = bss1/120*-125+bss2/580*-605
                                elif y4801 == 0 and y340 == 0:
                                    bet02 = bss1/120*-125+bss2/340*-355
                                elif y4801 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0:
                                    bet02 = bss1/120*-125+bss2*-125
                                if y4801 != 0 and y1000 == 0 and y90 != 0:
                                    bet02 = bss1*-125+bss2/1000*-1050
                                elif y4801 != 0 and y480 == 0 and y90 != 0:
                                    bet02 = bss1*-125+bss2/120*-125
                                elif y4801 != 0 and y100 == 0 and y90 != 0:
                                    bet02 = bss1*-125+bss2/100*-105
                                elif y4801 != 0 and y580 == 0 and y90 != 0:
                                    bet02 = bss1*-125+bss2/580*-605
                                elif y4801 != 0 and y340 == 0 and y90 != 0:
                                    bet02 = bss1*-125+bss2/340*-355
                                elif y4801 != 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y90 != 0:
                                    bet02 = bss1*-125+bss2*-125

                                if y90 == 0 and y1000 == 0:
                                    bet02 = bss1/90*-95+bss2/1000*-1050
                                elif y90 == 0 and y480 == 0:
                                    bet02 = bss1/90*-95+bss2/120*-125
                                elif y90 == 0 and y100 == 0:
                                    bet02 = bss1/90*-95+bss2/100*-105
                                elif y90 == 0 and y580 == 0:
                                    bet02 = bss1/90*-95+bss2/580*-605
                                elif y90 == 0 and y340 == 0:
                                    bet02 = bss1/90*-95+bss2/340*-355
                                elif y90 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0:
                                    bet02 = bss1/90*-95+bss2*-125

                    elif "-" not in bs[1] and "+" in bs[1]:
                        bet1 = bs[1].split("+")
                        bss1 = int(bet1[0])
                        bss2 = int(bet1[1])
                        y480 = bss2 % 120
                        y100 = bss2 % 100
                        y580 = bss2 % 580
                        y340 = bss2 % 340
                        y1000 = bss2 % 1000
                        y1001 = bss1 % 100
                        if bar in bs1[1]:
                            if y1001 == 0:
                                bet02 = bss1/2+bss2/2
                            elif y480 == 0:
                                bet02 = bss1*60+bss2/2
                            elif y100 == 0:
                                bet02 = bss1*60+bss2/2
                            elif y580 == 0:
                                bet02 = bss1*60+bss2/2
                            elif y340 == 0:
                                bet02 = bss1*60+bss2/2
                            elif y1000 == 0:
                                bet02 = bss1*60+bss2/2
                        elif bar not in bs1[0] and bar not in bs1[1]:
                            if y1001 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y480 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y100 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y580 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y340 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y1000 == 0:
                                bet02 = bss1*0+bss2*0
                        elif bar in bs1[0]:
                            if y1001 == 0 and y1000 == 0:
                                bet02 = bss1/100*-105+bss2/1000*-1050
                            elif y1001 == 0 and y480 == 0:
                                bet02 = bss1/100*-105+bss2/120*-125
                            elif y1001 == 0 and y100 == 0:
                                bet02 = bss1/100*-105+bss2/100*-105
                            elif y1001 == 0 and y580 == 0:
                                bet02 = bss1/100*-105+bss2/580*-605
                            elif y1001 == 0 and y340 == 0:
                                bet02 = bss1/100*-105+bss2/340*-355
                            elif y1000 == 0:
                                bet02 = bss1*-125+bss2/1000*-1050
                            elif y480 == 0:
                                bet02 = bss1*-125+bss2/120*-125
                            elif y100 == 0:
                                bet02 = bss1*-125+bss2/100*-105
                            elif y580 == 0:
                                bet02 = bss1*-125+bss2/580*-605
                            elif y340 == 0:
                                bet02 = bss1*-125+bss2/340*-355

                    elif "-" in bs[1] and "+" in bs[1]:
                        bet1 = bs[1].split("-")
                        if "+" in bet1[1]:
                            bet2 = bet1[1].split("+")
                            bss1 = int(bet1[0])
                            bss2 = int(bet2[0])
                            bss3 = int(bet2[1])
                            y480 = bss3 % 120
                            y100 = bss3 % 100
                            y580 = bss3 % 580
                            y340 = bss3 % 340
                            y1000 = bss3 % 1000
                            if bar in bs1[1]:
                                if y480 == 0:
                                    bet02 = bss1*40+bss2*60+bss3/2
                                elif y100 == 0:
                                    bet02 = bss1*40+bss2*60+bss3/2
                                elif y580 == 0:
                                    bet02 = bss1*40+bss2*60+bss3/2
                                elif y340 == 0:
                                    bet02 = bss1*40+bss2*60+bss3/2
                                elif y1000 == 0:
                                    bet02 = bss1*40+bss2*60+bss3/2
                            elif bar not in bs1[0] and bar not in bs1[1]:
                                if y480 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y100 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y580 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y340 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y1000 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                            elif bar in bs1[0]:
                                if y1000 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/1000*-1050
                                elif y480 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/120*-125
                                elif y100 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/100*-105
                                elif y580 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/580*-605
                                elif y340 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/340*-355

                elif bt == 3:
                    bs2 = bs1[1]
                    wl1 = bs1[0].count(bar)
                    wl2 = bs2[0].count(bar)
                    wl3 = bs2[1].count(bar)
                    wl4 = bs2[2].count(bar) 
                    cc = bs[1].count("-")
                    if bs2[2] != bs2[0] and bs2[2] != bs2[1]:
                        if cc == 1:
                            if "x" not in bs[1]:
                                bet1 = bs[1].split("-")
                                bss1 = int(bet1[0])
                                bss2 = int(bet1[1])
                                bss3 = bss1 + bss2
                                y480 = bss3 % 120
                                y100 = bss3 % 100
                                y460 = bss3 % 460
                                if bar in bs2[0] or bar in bs2[1]:
                                    if y480 == 0:
                                        bet02 = bss1/2
                                    elif y100 == 0:
                                        bet02 = bss1/2
                                    elif y460 == 0:
                                        bet02 = bss1/2
                                    else:
                                        bet02 = 999999
                                elif bar in bs2[2]:
                                    if y480 == 0:
                                        bet02 = bss2*1
                                    elif y100 == 0:
                                        bet02 = bss2*1
                                    elif y460 == 0:
                                        bet02 = bss2*1
                                    else:
                                        bet02 = 999999
                                elif bar in bs1[0]:
                                    if y480 == 0:
                                        bet02 = bss3/120*-125
                                    elif y100 == 0:
                                        bet02 = bss3/100*-105
                                    elif y460 == 0:
                                        bet02 = bss3/460*-480
                                    else:
                                        bet02 = 999999
                            elif "x" in bs[1]:
                                bet1 = bs[1].split("x")
                                bet2 = bet1[0].split("-")
                                x = int(bet1[1])
                                bss1 = int(bet2[0])
                                bss2 = int(bet2[1])
                                bss3 = bss1 + bss2
                                y480 = bss3 % 120
                                y100 = bss3 % 100
                                y460 = bss3 % 460
                                if bar in bs2[0] or bar in bs2[1]:
                                    if y480 == 0:
                                        bet02 = bss1/2*x
                                    elif y100 == 0:
                                        bet02 = bss1/2*x
                                    elif y460 == 0:
                                        bet02 = bss1/2*x
                                    else:
                                        bet02 = 999999
                                elif bar in bs2[2]:
                                    if y480 == 0:
                                        bet02 = bss2*1*x
                                    elif y100 == 0:
                                        bet02 = bss2*1*x
                                    elif y460 == 0:
                                        bet02 = bss2*1*x
                                    else:
                                        bet02 = 999999
                                elif bar in bs1[0]:
                                    if y480 == 0:
                                        bet02 = bss3/120*-125*x
                                    elif y100 == 0:
                                        bet02 = bss3/100*-105*x
                                    elif y460 == 0:
                                        bet02 = bss3/460*-480*x
                                    else:
                                        bet02 = 999999
                        
                        elif cc == 2:
                            if "x" not in bs[1]:
                                bet1 = bs[1].split("-")
                                bss1 = int(bet1[0])
                                bss2 = int(bet1[1])
                                bss3 = int(bet1[2])
                                bss4 = bss2 + bss3
                                y480 = bss4 % 120
                                y100 = bss4 % 100
                                y460 = bss4 % 460
                                y30 = bss1 % 30
                                if bar in bs2[0] or bar in bs2[1]:
                                    if y30 == 0 and y480 == 0:
                                        bet02 = bss2/2
                                        bet03 = bss1/3
                                    elif y30 == 0 and y100 == 0:
                                        bet02 = bss2/2
                                        bet03 = bss1/3
                                    elif y480 == 0 and y30 != 0:
                                        bet02 = bss2/2
                                        bet03 = bss1*40
                                    elif y100 == 0 and y30 != 0:
                                        bet02 = bss2/2
                                        bet03 = bss1*40
                                    elif y30 == 0 and y460 == 0:
                                        bet02 = bss2/2
                                        bet03 = bss1/3
                                    elif y460 == 0 and y30 != 0:
                                        bet02 = bss2/2
                                        bet03 = bss1*40
                                    else:
                                        bet02 = 999999
                                elif bar in bs2[2]:
                                    if y30 == 0 and y480 == 0:
                                        bet02 = bss3*1
                                        bet03 = bss1/3
                                    elif y30 == 0 and y100 == 0:
                                        bet02 = bss3*1
                                        bet03 = bss1/3
                                    elif y480 == 0 and y30 != 0:
                                        bet02 = bss3*1
                                        bet03 = bss1*40
                                    elif y100 == 0 and y30 != 0:
                                        bet02 = bss3*1
                                        bet03 = bss1*40
                                    elif y30 == 0 and y460 == 0:
                                        bet02 = bss3*1
                                        bet03 = bss1/3
                                    elif y460 == 0 and y30 != 0:
                                        bet02 = bss3*1
                                        bet03 = bss1*40
                                    else:
                                        bet02 = 999999
                                elif bar in bs1[0]:
                                    if y30 == 0 and y480 == 0:
                                        bet02 = bss4/120*-125
                                        bet03 = bss1*-1
                                    elif y30 == 0 and y100 == 0:
                                        bet02 = bss4/100*-105
                                        bet03 = bss1*-1
                                    elif y480 == 0 and y30 != 0:
                                        bet02 = bss4/120*-125
                                        bet03 = bss1*-125
                                    elif y100 == 0 and y30 != 0:
                                        bet02 = bss4/100*-105
                                        bet03 = bss1*-125
                                    elif y30 == 0 and y460 == 0:
                                        bet02 = bss4/460*-480
                                        bet03 = bss1*-1
                                    elif y460 == 0 and y30 != 0:
                                        bet02 = bss4/460*-480
                                        bet03 = bss1*-125
                                    else:
                                        bet02 = 999999
                            elif "x" in bs[1]:
                                bet1 = bs[1].split("x")
                                bet2 = bet1[0].split("-")
                                x = int(bet1[1])
                                bss1 = int(bet2[0])
                                bss2 = int(bet2[1])
                                bss3 = int(bet2[2])
                                bss4 = bss2 + bss3
                                y480 = bss4 % 120
                                y100 = bss4 % 100
                                y30 = bss1 % 30
                                y460 = bss4 % 460
                                if bar in bs2[0] or bar in bs2[1]:
                                    if y30 == 0 and y480 == 0:
                                        bet02 = bss2/2*x
                                        bet03 = bss1/3
                                    elif y30 == 0 and y100 == 0:
                                        bet02 = bss2/2*x
                                        bet03 = bss1/3
                                    elif y480 == 0 and y30 != 0:
                                        bet02 = bss2/2*x
                                        bet03 = bss1*40
                                    elif y100 == 0 and y30 != 0:
                                        bet02 = bss2/2*x
                                        bet03 = bss1*40
                                    elif y30 == 0 and y460 == 0:
                                        bet02 = bss2/2*x
                                        bet03 = bss1/3
                                    elif y460 == 0 and y30 != 0:
                                        bet02 = bss2/2*x
                                        bet03 = bss1*40
                                    else:
                                        bet02 = 999999
                                elif bar in bs2[2]:
                                    if y30 == 0 and y480 == 0:
                                        bet02 = bss3*1*x
                                        bet03 = bss1/3
                                    elif y30 == 0 and y100 == 0:
                                        bet02 = bss3*1*x
                                        bet03 = bss1/3
                                    elif y480 == 0 and y30 != 0:
                                        bet02 = bss3*1*x
                                        bet03 = bss1*40
                                    elif y100 == 0 and y30 != 0:
                                        bet02 = bss3*1*x
                                        bet03 = bss1*40
                                    elif y30 == 0 and y460 == 0:
                                        bet02 = bss3*1*x
                                        bet03 = bss1/3
                                    elif y460 == 0 and y30 != 0:
                                        bet02 = bss3*1*x
                                        bet03 = bss1*40
                                    else:
                                        bet02 = 999999
                                elif bar in bs1[0]:
                                    if y30 == 0 and y480 == 0:
                                        bet02 = bss4/120*-125*x
                                        bet03 = bss1*-1
                                    elif y30 == 0 and y100 == 0:
                                        bet02 = bss4/100*-105*x
                                        bet03 = bss1*-1
                                    elif y480 == 0 and y30 != 0:
                                        bet02 = bss4/120*-125*x
                                        bet03 = bss1*-125
                                    elif y100 == 0 and y30 != 0:
                                        bet02 = bss4/100*-105*x
                                        bet03 = bss1*-125
                                    elif y30 == 0 and y460 == 0:
                                        bet02 = bss4/460*-480*x
                                        bet03 = bss1*-1
                                    elif y460 == 0 and y30 != 0:
                                        bet02 = bss4/460*-480*x
                                        bet03 = bss1*-125
                                    else:
                                        bet02 = 999999

                    elif bs2[2] == bs2[0] or bs2[2] == bs2[1]:
                        cc = bs[1].count("-")
                        if cc == 1:
                            bet1 = bs[1].split("-")
                            bss1 = int(bet1[0])
                            bss2 = int(bet1[1])
                            y480 = bss1 % 120
                            y4801 = bss2 % 120
                            y100 = bss1 % 100
                            y1001 = bss2 % 100
                            y1000 = bss1 % 1000
                            y10001 = bss2 % 1000
                            if wl1 == 1:
                                if y480 == 0:
                                    bet02 = bss1/120*-125
                                if y100 == 0:
                                    bet02 = bss1/100*-105
                                if y4801 == 0:
                                    bet03 = bss2/120*-125
                                if y1001 == 0:
                                    bet03 = bss2/100*-105
                                if y1000 == 0:
                                    bet02 = bss1/1000*-1050
                                if y10001 == 0:
                                    bet03 = bss2/1000*-1050
                                if y480 != 0 and y100 != 0 and y1000 != 0:
                                    bet04 = bss1*-125
                                if y4801 != 0 and y1001 != 0 and y10001 != 0:
                                    bet05 = bss2*-125
                            elif wl2 == 1 or wl3 == 1:
                                if wl4 == 1:
                                    if y480 == 0:
                                        bet02 = bss1/2
                                    if y100 == 0:
                                        bet02 = bss1/2
                                    if y4801 == 0:
                                        bet03 = bss2*1
                                    if y1001 == 0:
                                        bet03 = bss2*1
                                    if y1000 == 0:
                                        bet02 = bss1/2
                                    if y10001 == 0:
                                        bet03 = bss2*1
                                    if y480 != 0 and y100 != 0 and y1000 != 0:
                                        bet04 = bss1*60
                                    if y4801 != 0 and y1001 != 0 and y10001 != 0:
                                        bet05 = bss2*120
                                else:
                                    if y480 == 0:
                                        bet02 = bss1/2
                                    if y100 == 0:
                                        bet02 = bss1/2
                                    if y4801 == 0:
                                        bet03 = bss2*0
                                    if y1001 == 0:
                                        bet03 = bss2*0
                                    if y1000 == 0:
                                        bet02 = bss1/2
                                    if y10001 == 0:
                                        bet03 = bss2*0
                                    if y480 != 0 and y100 != 0 and y1000 != 0:
                                        bet04 = bss1*60
                                    if y4801 != 0 and y1001 != 0 and y10001 != 0:
                                        bet05 = bss2*0
                            elif wl2 == 0 and wl3 == 0 and wl1 == 0:
                                if y480 == 0:
                                    bet02 = bss1*0
                                if y100 == 0:
                                    bet02 = bss1*0
                                if y4801 == 0:
                                    bet03 = bss2*0
                                if y1001 == 0:
                                    bet03 = bss2*0
                                if y1000 == 0:
                                    bet02 = bss1*0
                                if y10001 == 0:
                                    bet03 = bss2*0
                                if y480 != 0 and y100 != 0 and y1000 != 0:
                                    bet04 = bss1*0
                                if y4801 != 0 and y1001 != 0 and y10001 != 0:
                                    bet05 = bss2*0

                        if cc == 2:
                            bet1 = bs[1].split("-")
                            bss1 = int(bet1[0])
                            bss2 = int(bet1[1])  
                            bss3 = int(bet1[2])
                            y480 = bss1 % 120    
                            y4801 = bss2 % 120
                            y4802 = bss3 % 120
                            y100 = bss2 % 100
                            y1001 = bss3 % 100
                            y1000 = bss2 % 1000
                            y10001 = bss3 % 1000
                            if wl1 == 1:
                                if y480 == 0:
                                    bet02 = bss1/120*-125
                                if y480 != 0:
                                    bet02 = bss1*-125
                                if y4801 == 0:
                                    bet03 = bss2/120*-125
                                if y100 == 0:
                                    bet03 = bss2/100*-105
                                if y1000 == 0:
                                    bet03 = bss2/1000*-1050
                                if y4801 != 0 and y100 != 0 and y1000 != 0:
                                    bet03 = bss2*-125
                                if y4802 == 0:
                                    bet04 = bss3/120*-125
                                if y1001 == 0:
                                    bet04 = bss3/100*-105
                                if y10001 == 0:
                                    bet04 = bss3/1000*-1050
                                if y4802 != 0 and y1001 != 0 and y10001 != 0:
                                    bet04 = bss3*-125
                            elif wl2 == 1 or wl3 == 1:
                                if wl4 == 1:
                                    if y4801 == 0:
                                        bet03 = bss2/2
                                    if y100 == 0:
                                        bet03 = bss2/2
                                    if y1000 == 0:
                                        bet03 = bss2/2
                                    if y4801 != 0 and y100 != 0 and y1000 != 0:
                                        bet03 = bss2*60
                                    if y480 == 0:
                                        bet02 = bss1/3
                                    if y480 != 0:
                                        bet02 = bss1*40
                                    if y4802 == 0:
                                        bet04 = bss3*1
                                    if y1001 == 0:
                                        bet04 = bss3*1
                                    if y10001 == 0:
                                        bet04 = bss3*1
                                    if y4802 != 0 and y1001 != 0 and y10001 != 0:
                                        bet04 = bss3*120
                                else:
                                    if y4801 == 0:
                                        bet03 = bss2/2
                                    if y100 == 0:
                                        bet03 = bss2/2
                                    if y1000 == 0:
                                        bet03 = bss2/2
                                    if y4801 != 0 and y100 != 0 and y1000 != 0:
                                        bet03 = bss2*60
                                    if y480 == 0:
                                        bet02 = bss1/3
                                    if y480 != 0:
                                        bet02 = bss1*40
                                    if y4802 == 0:
                                        bet04 = bss3*0
                                    if y1001 == 0:
                                        bet04 = bss3*0
                                    if y1001 == 0:
                                        bet04 = bss3*0
                                    if y4802 != 0 and y1001 != 0 and y10001 != 0:
                                        bet04 = bss3*0
                            elif wl2 == 0 and wl3 == 0 and wl1 == 0:
                                if y4801 == 0:
                                    bet03 = bss2*0
                                if y100 == 0:
                                    bet03 = bss2*0
                                if y1000 == 0:
                                    bet03 = bss2*0
                                if y4801 != 0 and y100 != 0 and y1000 != 0:
                                    bet03 = bss2*0
                                if y480 == 0:
                                    bet02 = bss1/3
                                if y480 != 0:
                                    bet02 = bss1*40
                                if y4802 == 0:
                                    bet04 = bss3*0
                                if y1001 == 0:
                                    bet04 = bss3*0
                                if y10001 == 0:
                                    bet04 = bss3*0
                                if y4802 != 0 and y1001 != 0 and y10001 != 0:
                                    bet04 = bss3*0

                elif bt == 1:
                    if "-" not in bs[1] and "+" not in bs[1]:
                        bss1 = int(bs[1])
                        y480 = bss1 % 120
                        y100 = bss1 % 100
                        y580 = bss1 % 580
                        y340 = bss1 % 340
                        y1000 = bss1 % 1000
                        if bar in bs1[1]:
                            if y480 == 0 or y100 == 0 or y580 == 0 or y340 == 0 or y1000 == 0:
                                bet02 = bss1*1
                            else:
                                bet02 = bss1*120
                        elif bar not in bs1[0] and bar not in bs1[1]:
                            if y480 == 0 or y100 == 0 or y580 == 0 or y340 == 0 or y1000 == 0:
                                bet02 = bss1*0
                            else:
                                bet02 = bss1*0
                        elif bar in bs1[0]:
                            if y1000 == 0:
                                bet02 = bss1/1000*-1050
                            elif y480 == 0:
                                bet02 = bss1/120*-125
                            elif y100 == 0:
                                bet02 = bss1/100*-105
                            elif y580 == 0:
                                bet02 = bss1/580*-605
                            elif y340 == 0:
                                bet02 = bss1/340*-355
                            else:
                                bet02 = bss1*-125
                    
                    elif "-" in bs[1] and "+" not in bs[1]:
                        bet1 = bs[1].split("-")
                        bss1 = int(bet1[0])
                        bss2 = int(bet1[1])
                        y4801 = bss1 % 120
                        y480 = bss2 % 120
                        y100 = bss2 % 100
                        y580 = bss2 % 580
                        y340 = bss2 % 340
                        y1000 = bss2 % 1000
                        if bar in bs1[1]:
                            if y4801 == 0 and y480 == 0:
                                bet02 = bss1/3+bss2
                            elif y4801 == 0 and y100 == 0:
                                bet02 = bss1/3+bss2
                            elif y4801 == 0 and y580 == 0:
                                bet02 = bss1/3+bss2
                            elif y4801 == 0 and y340 == 0:
                                bet02 = bss1/3+bss2
                            elif y4801 == 0 and y1000 == 0:
                                bet02 = bss1/3+bss2
                            elif y4801 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                bet02 = bss1/3+bss2*120
                            elif y4801 != 0 and y480 == 0:
                                bet02 = bss1*40+bss2
                            elif y4801 != 0 and y100 == 0:
                                bet02 = bss1*40+bss2
                            elif y4801 != 0 and y580 == 0:
                                bet02 = bss1*40+bss2
                            elif y4801 != 0 and y340 == 0:
                                bet02 = bss1*40+bss2
                            elif y4801 != 0 and y1000 == 0:
                                bet02 = bss1*40+bss2
                            elif y4801 != 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                bet02 = bss1*40+bss2*120
                        elif bar not in bs1[0] and bar not in bs1[1]:
                            if y4801 == 0 and y480 == 0:
                                bet02 = bss1/3+bss2*0
                            elif y4801 == 0 and y100 == 0:
                                bet02 = bss1/3+bss2*0
                            elif y4801 == 0 and y580 == 0:
                                bet02 = bss1/3+bss2*0
                            elif y4801 == 0 and y340 == 0:
                                bet02 = bss1/3+bss2*0
                            elif y4801 == 0 and y1000 == 0:
                                bet02 = bss1/3+bss2*0
                            elif y4801 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                bet02 = bss1/3+bss2*0
                            elif y4801 != 0 and y480 == 0:
                                bet02 = bss1*40+bss2*0
                            elif y4801 != 0 and y100 == 0:
                                bet02 = bss1*40+bss2*0
                            elif y4801 != 0 and y580 == 0:
                                bet02 = bss1*40+bss2*0
                            elif y4801 != 0 and y340 == 0:
                                bet02 = bss1*40+bss2*0
                            elif y4801 != 0 and y1000 == 0:
                                bet02 = bss1*40+bss2*0
                            elif y4801 != 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                bet02 = bss1*40+bss2*0
                        elif bar in bs1[0]:
                            if y4801 == 0 and y1000 == 0:
                                bet02 = bss1/120*-125+bss2/1000*-1050
                            elif y4801 == 0 and y480 == 0:
                                bet02 = bss1/120*-125+bss2/120*-125
                            elif y4801 == 0 and y100 == 0:
                                bet02 = bss1/120*-125+bss2/100*-105
                            elif y4801 == 0 and y580 == 0:
                                bet02 = bss1/120*-125+bss2/580*-605
                            elif y4801 == 0 and y340 == 0:
                                bet02 = bss1/120*-125+bss2/340*-355
                            elif y4801 == 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0 and y1000 != 0:
                                bet02 = bss1/120*-125+bss2*-125
                            elif y4801 != 0 and y1000 == 0:
                                bet02 = bss1*-125+bss2/1000*-1050
                            elif y4801 != 0 and y480 == 0:
                                bet02 = bss1*-125+bss2/120*-125
                            elif y4801 != 0 and y100 == 0:
                                bet02 = bss1*-125+bss2/100*-105
                            elif y4801 != 0 and y580 == 0:
                                bet02 = bss1*-125+bss2/580*-605
                            elif y4801 != 0 and y340 == 0:
                                bet02 = bss1*-125+bss2/340*-355
                            elif y4801 != 0 and y580 != 0 and y100 != 0 and y480 != 0 and y340 != 0:
                                bet02 = bss1*-125+bss2*-125

                    elif "-" not in bs[1] and "+" in bs[1]:
                        bet1 = bs[1].split("+")
                        bss1 = int(bet1[0])
                        bss2 = int(bet1[1])
                        y480 = bss2 % 120
                        y100 = bss2 % 100
                        y580 = bss2 % 580
                        y340 = bss2 % 340
                        y1000 = bss2 % 1000
                        if bar in bs1[1]:
                            if y480 == 0:
                                bet02 = bss1*120+bss2
                            elif y100 == 0:
                                bet02 = bss1*120+bss2
                            elif y580 == 0:
                                bet02 = bss1*120+bss2
                            elif y340 == 0:
                                bet02 = bss1*120+bss2
                            elif y1000 == 0:
                                bet02 = bss1*120+bss2
                        elif bar not in bs1[0] and bar not in bs1[1]:
                            if y480 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y100 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y580 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y340 == 0:
                                bet02 = bss1*0+bss2*0
                            elif y1000 == 0:
                                bet02 = bss1*0+bss2*0
                        elif bar in bs1[0]:
                            if y1000 == 0:
                                bet02 = bss1*-125+bss2/1000*-1050
                            elif y480 == 0:
                                bet02 = bss1*-125+bss2/120*-125
                            elif y100 == 0:
                                bet02 = bss1*-125+bss2/100*-105
                            elif y580 == 0:
                                bet02 = bss1*-125+bss2/580*-605
                            elif y340 == 0:
                                bet02 = bss1*-125+bss2/340*-355
                    elif "-" in bs[1] and "+" in bs[1]:
                        bet1 = bs[1].split("-")
                        if "+" in bet1[1]:
                            bet2 = bet1[1].split("+")
                            bss1 = int(bet1[0])
                            bss2 = int(bet2[0])
                            bss3 = int(bet2[1])
                            y480 = bss3 % 120
                            y100 = bss3 % 100
                            y580 = bss3 % 580
                            y340 = bss3 % 340
                            y1000 = bss3 % 1000
                            if bar in bs1[1]:
                                if y480 == 0:
                                    bet02 = bss1*40+bss2*120+bss3
                                elif y100 == 0:
                                    bet02 = bss1*40+bss2*120+bss3
                                elif y580 == 0:
                                    bet02 = bss1*40+bss2*120+bss3
                                elif y340 == 0:
                                    bet02 = bss1*40+bss2*120+bss3
                                elif y1000 == 0:
                                    bet02 = bss1*40+bss2*120+bss3
                            elif bar not in bs1[0] and bar not in bs1[1]:
                                if y480 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y100 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y580 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y340 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                                elif y1000 == 0:
                                    bet02 = bss1*40+bss2*0+bss3*0
                            elif bar in bs1[0]:
                                if y1000 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/1000*-1050
                                elif y480 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/120*-125
                                elif y100 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/100*-105
                                elif y580 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/580*-605
                                elif y340 == 0:
                                    bet02 = bss1*-125+bss2*-125+bss3/340*-355
                winlose = bet02+bet03+bet04+bet05


            #-----------------------------------------------
            #----------------三王赢-------------------------
            #-----------------------------------------------

            def aa3():
                if "+" not in bet:
                    y90 = int(bs[1]) - 90
                    y120 = int(bs[1]) % 120
                    if y90 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/3
                    elif y120 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/3
                    elif y90 != 0 and y120 != 0:
                        bs1 = int(bs[1])
                        winlose = bs1*40
                if "+" in bet:
                    bs1 = bs[1].split("+")
                    y90 = int(bs1[1]) - 90
                    y120 = int(bs1[1]) % 120
                    if y90 == 0 :
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*40+bs3/3
                    elif y120 == 0 :
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*40+bs3/3
                return winlose

            if bs[0] == "1" and bar == "2":
                winlose = aa3()

            if bs[0] == "1" and bar == "3":
                winlose = aa3()

            if bs[0] == "1" and bar == "4":
                winlose = aa3()

            if bs[0] == "2" and bar == "1":
                winlose = aa3()

            if bs[0] == "2" and bar == "3":
                winlose = aa3()

            if bs[0] == "2" and bar == "4":
                winlose = aa3()

            if bs[0] == "3" and bar == "1":
                winlose = aa3()

            if bs[0] == "3" and bar == "2":
                winlose = aa3()

            if bs[0] == "3" and bar == "4":
                winlose = aa3()

            if bs[0] == "4" and bar == "1":
                winlose = aa3()

            if bs[0] == "4" and bar == "2":
                winlose = aa3()

            if bs[0] == "4" and bar == "3":
                winlose = aa3()

            #-----------------------------------------------
            #----------------三王吃-------------------------
            #-----------------------------------------------

            def eat3():
                if "+" not in bet:
                    y90 = int(bs[1]) - 90
                    y120 = int(bs[1]) % 120
                    if y90 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/90*-95
                    elif y120 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/120*-125
                    elif y90 != 0 and y120 != 0:
                        bs1 = int(bs[1])
                        winlose = bs1*-125
                if "+" in bet:
                    bs1 = bs[1].split("+")
                    y90 = int(bs1[1]) - 90
                    y120 = int(bs1[1]) % 120
                    if y90 == 0 :
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*-125+bs3/90*-95
                    elif y120 == 0 :
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*-125+bs3/120*-125
                return winlose

            if bs[0] == "1" and bar == "1":
                winlose = eat3()

            if bs[0] == "2" and bar == "2":
                winlose = eat3()

            if bs[0] == "3" and bar == "3":
                winlose = eat3()

            if bs[0] == "4" and bar == "4":
                winlose = eat3()

            #-----------------------------------------------
            #----------------冲南输赢-------------------------
            #-----------------------------------------------

            def eat4():
                if "+" not in bet:
                    y120 = int(bs[1]) % 120
                    y90 = int(bs[1]) - 90
                    if y120 == 0:
                        bs1 = int(bs[1])
                        wl = bs1/120*-125
                    elif y90 == 0:
                        bs1 = int(bs[1])
                        wl = bs1/90*-95
                    elif y90 != 0 and y120 != 0:
                        bs1 = int(bs[1])
                        wl = bs1*-125
                elif "+" in bet:
                    bs1 = bs[1].split("+")
                    y120 = int(bs1[1]) % 120
                    y90 = int(bs1[1]) - 90
                    if y120 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        wl = bs2*-125+bs3/120*-125
                    elif y90 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        wl = bs2*-125+bs3/90*-95
                return wl

            def aa4():
                if "+" not in bet:
                    y120 = int(bs[1]) % 120
                    y90 = int(bs[1]) - 90
                    if y120 == 0:
                        bs1 = int(bs[1])
                        wl = bs1/3
                    elif y90 == 0:
                        bs1 = int(bs[1])
                        wl = bs1/3
                    elif y90 != 0 and y120 != 0:
                        bs1 = int(bs[1])
                        wl = bs1*40
                elif "+" in bet:
                    bs1 = bs[1].split("+")
                    y120 = int(bs1[1]) % 120
                    y90 = int(bs1[1]) - 90
                    if y120 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        wl = bs2*40+bs3/3
                    elif y90 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        wl = bs2*40+bs3/3
                return wl

            if bs[0] == "xx":
                if point == "3" or point == "6" or point == "7" or point == "14" or point == "15" or point == "18":
                    winlose = eat4()
                else:
                    winlose = aa4()

            #-----------------------------------------------
            #----------------CROSS-------------------------
            #-----------------------------------------------

            if bs[0] == "x1" or bs[0] == "x2" or bs[0] == "x3" or bs[0] == "x4" or bs[0] == "x5" or bs[0] == "x6":
                bet1 = int(bs[1])
                bs1 = bs[0].split("x")
                bs2 = bs1[1]
                wl = bar1.count(bs2)
                ys1 = bar1[0] == bar1[1]
                ys2 = bar1[0] == bar1[2]
                if wl == 3:
                    winlose = bet1*35
                elif wl == 2:
                    winlose = bet1*23
                elif wl == 1 and ys1 is True:
                    winlose = bet1*12
                elif wl == 1 and ys1 is False:
                    winlose = bet1*11
                elif wl == 0 and ys2 is True:
                    winlose = bet1*-9
                elif wl == 0 and ys1 is True:
                    winlose = bet1*-10
                elif wl == 0 and ys1 is False:
                    winlose = bet1*-11

            #-----------------------------------------------
            #----------------冲南一输赢-------------------------
            #-----------------------------------------------

            def aa5():
                if "+" not in bs[1]:
                    y120 = int(bs[1]) % 120
                    y90 = int(bs[1]) - 90
                    if y120 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/3*2
                    elif y90 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/3*2
                    elif y90 != 0 and y120 != 0:
                        bs1 = int(bs[1])
                        winlose = bs1*80
                elif "+" in bs[1]:
                    bs1 = bs[1].split("+")
                    y120 = int(bs1[1]) % 120
                    y90 = int(bs1[1]) - 90
                    if y120 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*80+bs3/3*2
                    elif y90 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*80+bs3/3*2
                return winlose

            def eat51():
                if "+" not in bs[1]:
                    y120 = int(bs[1]) % 120
                    y90 = int(bs[1]) - 90
                    if y120 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/120*-250
                    elif y90 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/90*-190
                    elif y90 != 0 and y120 != 0:
                        bs1 = int(bs[1])
                        winlose = bs1*-250
                elif "+" in bs[1]:
                    bs1 = bs[1].split("+")
                    y120 = int(bs1[1]) % 120
                    y90 = int(bs1[1]) - 90
                    if y120 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*-250+bs3/120*-250
                    elif y90 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*-250+bs3/90*-190
                return winlose

            def eat5():
                if "+" not in bs[1]:
                    y120 = int(bs[1]) % 120
                    y90 = int(bs[1]) - 90
                    if y120 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/120*-85
                    elif y90 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/90*-65
                    elif y90 != 0 and y120 != 0:
                        bs1 = int(bs[1])
                        winlose = bs1*-85
                elif "+" in bs[1]:
                    bs1 = bs[1].split("+")
                    y120 = int(bs1[1]) % 120
                    y90 = int(bs1[1]) - 90
                    if y120 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*-85+bs3/120*-85
                    elif y90 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2*-85+bs3/90*-65
                return winlose

            if bs[0] == "1xx":
                if point == "3" or point == "6" or point == "7" or point == "14" or point == "15" or point == "18":
                    winlose = eat5()
                elif bar == "1":
                    winlose = eat5()
                else:
                    winlose = aa5()

            if bs[0] == "2xx":
                if bar == "2":
                    if point == "6" or point == "14" or point == "18":
                        winlose = eat51()
                    else:
                        winlose = eat5()
                elif point == "3" or point == "7" or point == "15":
                    winlose = eat5()
                else:
                    winlose = aa5()

            if bs[0] == "3xx":
                if bar == "3":
                    if point == "3" or point == "7" or point == "15":
                        winlose = eat51()
                    else:
                        winlose = eat5()
                elif point == "6" or point == "14" or point == "18":
                    winlose = eat5()
                else:
                    winlose = aa5()

            if bs[0] == "4xx":
                if point == "3" or point == "6" or point == "7" or point == "14" or point == "15" or point == "18":
                    winlose = eat5()
                elif bar == "4":
                    winlose = eat5()
                else:
                    winlose = aa5()

            #-----------------------------------------------
            #----------------13角-------------------------
            #-----------------------------------------------

            def aa6():
                bs1 = int(bs[1])
                winlose = bs1*1
                return winlose

            def eat6():
                y480 = int(bs[1]) % 120
                y100 = int(bs[1]) % 100
                y1000 = int(bs[1]) % 1000
                y580 = int(bs[1]) % 580
                if y1000 == 0:
                    bs1 = int(bs[1])
                    winlose = bs1/1000*-1050
                elif y480 == 0:
                    bs1 = int(bs[1])
                    winlose = bs1/120*-125
                elif y100 == 0:
                    bs1 = int(bs[1])
                    winlose = bs1/100*-105
                elif y580 == 0:
                    bs1 = int(bs[1])
                    winlose = bs1/580*-605
                return winlose

            if bs[0] == "12":
                if bar == "1" or bar == "2":
                    winlose = aa6()
                elif bar == "3" or bar == "4":
                    winlose = eat6()

            if bs[0] == "13":
                if bar == "1" or bar == "3":
                    winlose = aa6()
                elif bar == "2" or bar == "4":
                    winlose = eat6()

            if bs[0] == "14":
                if bar == "1" or bar == "4":
                    winlose = aa6()
                elif bar == "2" or bar == "3":
                    winlose = eat6()

            if bs[0] == "23":
                if bar == "2" or bar == "3":
                    winlose = aa6()
                elif bar == "1" or bar == "4":
                    winlose = eat6()

            if bs[0] == "24":
                if bar == "2" or bar == "4":
                    winlose = aa6()
                elif bar == "1" or bar == "3":
                    winlose = eat6()

            if bs[0] == "34":
                if bar == "3" or bar == "4":
                    winlose = aa6()
                elif bar == "1" or bar == "2":
                    winlose = eat6()

            #-----------------------------------------------
            #----------------131角-------------------------
            #-----------------------------------------------

            def aa7():
                if "-" not in bs[1]:
                    bs1 = int(bs[1])
                    winlose = bs1*2
                elif "-" in bs[1]:
                    bs1 = bs[1].split("-")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    winlose = bs2*1+bs3*2
                return winlose

            def eat7():
                if "-" not in bs[1]:
                    y480 = int(bs[1]) % 120
                    y100 = int(bs[1]) % 100
                    y1000 = int(bs[1]) % 1000
                    y580 = int(bs[1]) % 580
                    if y1000 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/1000*-1050
                    elif y480 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/120*-125
                    elif y100 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/100*-105
                    elif y580 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/580*-605
                elif "-" in bs[1]:
                    bs1 = bs[1].split("-")
                    y480 = int(bs1[0]) % 120
                    y4801 = int(bs1[1]) % 120
                    y580 = int(bs1[0]) % 580
                    y5801 = int(bs1[1]) % 580
                    y100 = int(bs1[0]) % 100
                    y1001 = int(bs1[1]) % 100
                    y1000 = int(bs1[0]) % 1000
                    y10001 = int(bs1[1]) % 1000
                    y1002 = (int(bs1[0])+int(bs1[1])) % 100
                    if y1000 == 0 and y10001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/1000*-1050+bs3/1000*-1050
                    elif y480 == 0 and y4801 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/120*-125+bs3/120*-125
                    elif y100 == 0 and y1001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/100*-105+bs3/100*-105
                    elif y100 == 0 and y10001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/100*-105+bs3/1000*-1050
                    elif y1000 == 0 and y4801 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/1000*-1050+bs3/120*-125
                    elif y1000 == 0 and y1001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/1000*-1050+bs3/100*-105
                    elif y480 == 0 and y10001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/120*-125+bs3/1000*-1050
                    elif y480 == 0 and y1001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/120*-125+bs3/100*-105
                    elif y100 == 0 and y4801 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/100*-105+bs3/120*-125

                    elif y580 == 0 and y1001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/580*-605+bs3/100*-105
                    elif y580 == 0 and y4801 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/580*-605+bs3/120*-125
                    elif y580 == 0 and y5801 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/580*-605+bs3/580*-605
                    elif y580 == 0 and y10001 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/580*-605+bs3/1000*-1050
                    elif y1000 == 0 and y5801 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/1000*-1050+bs3/580*-605
                    elif y100 == 0 and y5801 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = bs2/100*-105+bs3/580*-605

                    elif y1002 == 0:
                        bs2 = int(bs1[0])
                        bs3 = int(bs1[1])
                        winlose = (bs2+bs3)/100*-105
                return winlose

            def ass7():
                if "-" not in bs[1]:
                    bs1 = int(bs[1])
                    winlose = bs1*0
                elif "-" in bs[1]:
                    bs1 = bs[1].split("-")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    winlose = bs2*1+bs3*0
                return winlose

            if bs[0] == "121":
                if bar == "1":
                    winlose = aa7()
                elif bar == "3" or bar == "4":
                    winlose = eat7()
                elif bar == "2":
                    winlose = ass7()

            if bs[0] == "122":
                if bar == "2":
                    winlose = aa7()
                elif bar == "3" or bar == "4":
                    winlose = eat7()
                elif bar == "1":
                    winlose = ass7()

            if bs[0] == "131":
                if bar == "1":
                    winlose = aa7()
                elif bar == "2" or bar == "4":
                    winlose = eat7()
                elif bar == "3":
                    winlose = ass7()

            if bs[0] == "133":
                if bar == "3":
                    winlose = aa7()
                elif bar == "2" or bar == "4":
                    winlose = eat7()
                elif bar == "1":
                    winlose = ass7()

            if bs[0] == "141":
                if bar == "1":
                    winlose = aa7()
                elif bar == "2" or bar == "3":
                    winlose = eat7()
                elif bar == "4":
                    winlose = ass7()

            if bs[0] == "144":
                if bar == "4":
                    winlose = aa7()
                elif bar == "2" or bar == "3":
                    winlose = eat7()
                elif bar == "1":
                    winlose = ass7()

            if bs[0] == "232":
                if bar == "2":
                    winlose = aa7()
                elif bar == "1" or bar == "4":
                    winlose = eat7()
                elif bar == "3":
                    winlose = ass7()

            if bs[0] == "233":
                if bar == "3":
                    winlose = aa7()
                elif bar == "1" or bar == "4":
                    winlose = eat7()
                elif bar == "2":
                    winlose = ass7()

            if bs[0] == "242":
                if bar == "2":
                    winlose = aa7()
                elif bar == "1" or bar == "3":
                    winlose = eat7()
                elif bar == "4":
                    winlose = ass7()

            if bs[0] == "244":
                if bar == "4":
                    winlose = aa7()
                elif bar == "1" or bar == "3":
                    winlose = eat7()
                elif bar == "2":
                    winlose = ass7()

            if bs[0] == "343":
                if bar == "3":
                    winlose = aa7()
                elif bar == "1" or bar == "2":
                    winlose = eat7()
                elif bar == "4":
                    winlose = ass7()

            if bs[0] == "344":
                if bar == "4":
                    winlose = aa7()
                elif bar == "1" or bar == "2":
                    winlose = eat7()
                elif bar == "3":
                    winlose = ass7()

            #-----------------------------------------------
            #----------------大中小-------------------------
            #-----------------------------------------------

            if bs[0] == "b":
                if int(point) <= 10:
                    bs1 = int(bs[1])
                    winlose = bs1*-1
                elif bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                    bs1 = int(bs[1])
                    winlose = bs1*-1
                else:
                    bs1 = int(bs[1])
                    winlose = bs1*1

            if bs[0] == "s":
                if int(point) >= 11:
                    bs1 = int(bs[1])
                    winlose = bs1*-1
                elif bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                    bs1 = int(bs[1])
                    winlose = bs1*-1
                else:
                    bs1 = int(bs[1])
                    winlose = bs1*1

            if bs[0] == "c":
                if int(point) <= 8:
                    bs1 = int(bs[1])
                    winlose = bs1*-1
                elif int(point) >= 13:
                    bs1 = int(bs[1])
                    winlose = bs1*-1
                elif bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                    bs1 = int(bs[1])
                    winlose = bs1*-1
                else:
                    bs1 = int(bs[1])
                    winlose = bs1*1
                
            #-----------------------------------------------
            #----------------大小鱼-------------------------
            #-----------------------------------------------

            if bs[0] == "bf":
                if "x" in bs[1]:
                    bss = bs[1].split("x")
                    bs1 = bss[0].split("-")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    bs4 = int(bss[1])
                    if int(point) <= 8:
                        winlose = (bs2*-1+bs3*-1)*bs4
                    elif bar1 == "111" or bar1 == "222" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                        winlose = (bs2*-1+bs3*-1)*bs4
                    elif int(point) >= 11:
                        if "444" not in bar1 and "555" not in bar1 and "666" not in bar1:
                            winlose = (bs2-bs3)*bs4
                    elif int(point) == 9 or int(point) == 10:
                        winlose = (bs3*3-bs2)*bs4
                else:
                    bs1 = bs[1].split("-")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    if int(point) <= 8:
                        winlose = bs2*-1+bs3*-1
                    elif bar1 == "111" or bar1 == "222" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                        winlose = bs2*-1+bs3*-1
                    elif int(point) >= 11:
                        if "444" not in bar1 and "555" not in bar1 and "666" not in bar1:
                            winlose = bs2-bs3
                    elif int(point) == 9 or int(point) == 10:
                        winlose = bs3*3-bs2


            if bs[0] == "sf":
                if "x" in bs[1]:
                    bss = bs[1].split("x")
                    bs1 = bss[0].split("-")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    bs4 = int(bss[1])
                    if int(point) >= 13:
                        winlose = (bs2*-1+bs3*-1)*bs4
                    elif bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "555" or bar1 == "666":
                        winlose = (bs2*-1+bs3*-1)*bs4
                    elif int(point) <= 10:
                        if "111" not in bar1 and "222" not in bar1 and "333" not in bar1:
                            winlose = (bs2-bs3)*bs4
                    elif int(point) == 11 or int(point) == 12: 
                        winlose = (bs3*3-bs2)*bs4
                else:
                    bs1 = bs[1].split("-")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    if int(point) >= 13:
                        winlose = bs2*-1+bs3*-1
                    elif bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "555" or bar1 == "666":
                        winlose = bs2*-1+bs3*-1
                    elif int(point) <= 10:
                        if "111" not in bar1 and "222" not in bar1 and "333" not in bar1:
                            winlose = bs2-bs3
                    elif int(point) == 11 or int(point) == 12:
                        winlose = bs3*3-bs2
                    
            #-----------------------------------------------
            #----------------千字-------------------------
            #-----------------------------------------------

            def scv(a,c,e):
                if c == 3 and "=" not in a:
                    bcv1 = bar1.count(a[0])
                    bcv2 = bar1.count(a[1])
                    bcv3 = bar1.count(a[2])
                    bcv5 = int(bcv1)+int(bcv2)+int(bcv3)
                    if a[0] == a[1]:
                        if bcv5 == 5:
                            if bar1 == "665" or bar1 == "112":
                                e = e*60
                            else:
                                e = e*50
                        elif bcv5 != 5:
                            e = e*-1
                    elif a[0] != a[1]:
                        if a == bar1:
                            e = e*30
                        elif a != bar1:
                            e = e*-1
                elif c == 4 and "=" not in a:
                    bcv1 = bar1.count(a[0])
                    bcv2 = bar1.count(a[1])
                    bcv3 = bar1.count(a[2])
                    bcv4 = bar1.count(a[3])
                    bcv5 = int(bcv1)+int(bcv2)+int(bcv3)+int(bcv4)
                    q1 = a[0]+a[1]+a[2]
                    q2 = a[0]+a[1]+a[3]
                    q3 = a[0]+a[2]+a[3]
                    q4 = a[1]+a[2]+a[3]
                    if a[0] == a[1] and a[2] == a[3]:#5566   
                        if bcv5 == 6 and bar1[0] == bar1[2]:
                            e = e*-1
                        elif bcv5 == 6:
                            if bar1 == "665" or bar1 == "112":
                                e = e/2*59
                            else:
                                e = e/2*49
                        elif bcv5 != 6:
                            e = e*-1

                    elif a[0] == a[1] and a[2] != a[3] and a[0] == a[2]:#4443
                        q1 = a[0]+a[1]+a[2] #444 
                        q2 = a[1]+a[2]+a[3] #443
                        if q1 == bar1:
                            e = e/2*159
                        elif q2 == bar1:
                            if bar1 == "665" or bar1 == "112":
                                e = e/2*59
                            else:
                                e = e/2*49
                        elif q1 != bar1 and q2 != bar1:
                            e = e*-1
                    
                    elif a[1] == a[2] and a[0] != a[1] and a[1] == a[3]:#3444
                        q1 = a[1]+a[2]+a[3] #444 
                        q2 = a[1]+a[2]+a[0] #443
                        if q1 == bar1:
                            e = e/2*159
                        elif q2 == bar1:
                            if bar1 == "665" or bar1 == "112":
                                e = e/2*59
                            else:
                                e = e/2*49
                        elif q1 != bar1 and q2 != bar1:
                            e = e*-1
                    
                    elif a[0] == a[1] and a[2] != a[3] and a[0] != a[2]:#1123
                        q1 = a[0]+a[1]+a[2] #112
                        q2 = a[0]+a[1]+a[3] #113
                        q3 = a[1]+a[2]+a[3] #123
                        if q3 == bar1:
                            e = e/3*28
                        elif q1 == bar1 or q2 == bar1:
                            if bar1 == "665" or bar1 == "112":
                                e = e/3*58
                            else:
                                e = e/3*48
                        elif q1 != bar1 and q2 != bar1 and q3 != bar1:
                            e = e*-1

                    elif a[0] != a[1] and a[2] != a[3] and a[1] == a[2]:#1223
                        q1 = a[1]+a[2]+a[3] #223
                        q2 = a[1]+a[2]+a[0] #221
                        q3 = a[0]+a[2]+a[3] #123
                        if q3 == bar1:
                            e = e/3*28
                        elif q1 == bar1 or q2 == bar1:
                            if bar1 == "665" or bar1 == "112":
                                e = e/3*58
                            else:
                                e = e/3*48
                        elif q1 != bar1 and q2 != bar1 and q3 != bar1:
                            e = e*-1

                    elif a[0] != a[1] and a[2] == a[3] and a[1] != a[2]:#1233
                        q1 = a[2]+a[3]+a[0] #331
                        q2 = a[2]+a[3]+a[1] #332
                        q3 = a[0]+a[1]+a[2] #123
                        if q3 == bar1:
                            e = e/3*28
                        elif q1 == bar1 or q2 == bar1:
                            if bar1 == "665" or bar1 == "112":
                                e = e/3*58
                            else:
                                e = e/3*48
                        elif q1 != bar1 and q2 != bar1 and q3 != bar1:
                            e = e*-1

                    elif a[0] != a[1] and a[2] != a[3]:#1234
                        if q1 == bar1 or q2 == bar1 or q3 == bar1 or q4 == bar1: 
                            e = e/4*27
                        else: 
                            e = e*-1

                elif c == 6 and "=" not in a:
                    q1 = a[0]+a[1]+a[2] 
                    q2 = a[0]+a[1]+a[4]
                    q3 = a[2]+a[3]+a[0]
                    q4 = a[2]+a[3]+a[4]
                    q5 = a[4]+a[5]+a[0]
                    q6 = a[4]+a[5]+a[2]
                    if q1 == bar1 or q2 == bar1 or q3 == bar1 or q4 == bar1 or q5 == bar1 or q6 == bar1:
                        if bar1 == "665" or bar1 == "112":
                            e = e/6*55
                        else:
                            e = e/6*45
                    else: 
                        e = e*-1

                elif "=" in a:
                    ss2 = a.split("=")
                    ss4 = ss2[0]
                    ss = ss4.count("1")+ss4.count("2")+ss4.count("3")+ss4.count("4")+ss4.count("5")+ss4.count("6")
                    if ss == 1:
                        q1 = ss4[0]+ss4[0]+ss4[0]
                        if bar1 == q1:
                            e = e*160
                        elif bar1 != q1:
                            e = e*-1
                    elif ss == 2:
                        q1 = ss4[0]+ss4[0]+ss4[0]
                        q2 = ss4[1]+ss4[1]+ss4[1]
                        if bar1 == q1 or bar1 == q2:
                            e = e/2*159
                        elif bar1 != q1 or bar1 != q2:
                            e = e*-1
                    elif ss == 3:
                        q1 = ss4[0]+ss4[0]+ss4[0]
                        q2 = ss4[1]+ss4[1]+ss4[1]
                        q3 = ss4[2]+ss4[2]+ss4[2]
                        if bar1 == q1 or bar1 == q2 or bar1 == q3:
                            e = e/3*158
                        elif bar1 != q1 or bar1 != q2 or bar1 != q3:
                            e = e*-1
                    elif ss == 4:
                        q1 = ss4[0]+ss4[0]+ss4[0]
                        q2 = ss4[1]+ss4[1]+ss4[1]
                        q3 = ss4[2]+ss4[2]+ss4[2]
                        q4 = ss4[3]+ss4[3]+ss4[3]
                        if bar1 == q1 or bar1 == q2 or bar1 == q3 or bar1 == q4:
                            e = e/4*157
                        elif bar1 != q1 or bar1 != q2 or bar1 != q3 or bar1 != q4:
                            e = e*-1
                    elif ss == 5:
                        q1 = ss4[0]+ss4[0]+ss4[0]
                        q2 = ss4[1]+ss4[1]+ss4[1]
                        q3 = ss4[2]+ss4[2]+ss4[2]
                        q4 = ss4[3]+ss4[3]+ss4[3]
                        q5 = ss4[4]+ss4[4]+ss4[4]
                        if bar1 == q1 or bar1 == q2 or bar1 == q3 or bar1 == q4 or bar1 == q5:
                            e = e/5*156
                        elif bar1 != q1 or bar1 != q2 or bar1 != q3 or bar1 != q4 or bar1 != q5:
                            e = e*-1
                    elif ss == 6:
                        q1 = ss4[0]+ss4[0]+ss4[0]
                        q2 = ss4[1]+ss4[1]+ss4[1]
                        q3 = ss4[2]+ss4[2]+ss4[2]
                        q4 = ss4[3]+ss4[3]+ss4[3]
                        q5 = ss4[4]+ss4[4]+ss4[4]
                        q6 = ss4[5]+ss4[5]+ss4[5]
                        if bar1 == q1 or bar1 == q2 or bar1 == q3 or bar1 == q4 or bar1 == q5 or bar1 == q6:
                            e = e/6*155
                        elif bar1 != q1 or bar1 != q2 or bar1 != q3 or bar1 != q4 or bar1 != q5 or bar1 != q6:
                            e = e*-1
                else:
                    e = 999999
                return e
                    
                
            if "q" in bet:
                bet10 = 0
                bet11 = 0
                bet12 = 0
                bet13 = 0
                bet14 = 0
                bscv = bs[0].split("q")
                cc = bs[0].count("+")
                if cc == 0:
                    cvv1 = bscv[1]
                    c1 = cvv1.count("1")
                    c2 = cvv1.count("2")
                    c3 = cvv1.count("3")
                    c4 = cvv1.count("4")
                    c5 = cvv1.count("5")
                    c6 = cvv1.count("6")
                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        betcv = int(bs[1])
                        bet10 = scv(cvv1,cv2,betcv)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:
                        if "cvb" in bet:
                            bs1 = bs[1].split("cvb")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                            elif int(point) <=10:
                                bet10 = bet10 - betcv
                            elif int(point) >=11:
                                bet10 = bet10 + betcv

                        elif "cvs" in bet:
                            bs1 = bs[1].split("cvs")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                            elif int(point) >=11:
                                bet10 = bet10 - betcv
                            elif int(point) <=10:
                                bet10 = bet10 + betcv

                        elif "cvc" in bet:
                            bs1 = bs[1].split("cvc")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betcv
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betcv

                        elif "cv00" in bet:
                            bs1 = bs[1].split("cv00")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            y1 = int(bar) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                            elif y1 != 0:
                                bet10 = bet10 - betcv
                            elif y1 == 0:
                                bet10 = bet10 + betcv

                        elif "cv0" in bet:
                            bs1 = bs[1].split("cv0")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            y1 = int(bar) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                            elif y1 == 0:
                                bet10 = bet10 - betcv
                            elif y1 != 0:
                                bet10 = bet10 + betcv

                        elif "cv12" in bet:
                            bs1 = bs[1].split("cv12")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betcv
                            else:
                                bet10 = bet10 + betcv

                        elif "cv13" in bet:
                            bs1 = bs[1].split("cv13")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betcv
                            else:
                                bet10 = bet10 + betcv

                        elif "cv14" in bet:
                            bs1 = bs[1].split("cv14")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betcv
                            else:
                                bet10 = bet10 + betcv

                        elif "cv23" in bet:
                            bs1 = bs[1].split("cv23")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betcv
                            else:
                                bet10 = bet10 + betcv

                        elif "cv24" in bet:
                            bs1 = bs[1].split("cv24")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betcv
                            else:
                                bet10 = bet10 + betcv

                        elif "cv34" in bet:
                            bs1 = bs[1].split("cv34")
                            betcv = int(bs1[0])
                            bet10 = scv(cvv1,cv2,betcv)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betcv
                            else:
                                bet10 = bet10 + betcv
                        

                if cc == 1:
                    cv = bscv[1].split("+")
                    cvv1 = cv[0]
                    cvv2 = cv[1]
                    c1 = cvv1.count("1")
                    c2 = cvv1.count("2")
                    c3 = cvv1.count("3")
                    c4 = cvv1.count("4")
                    c5 = cvv1.count("5")
                    c6 = cvv1.count("6")
                    cc1 = cvv2.count("1")
                    cc2 = cvv2.count("2")
                    cc3 = cvv2.count("3")
                    cc4 = cvv2.count("4")
                    cc5 = cvv2.count("5")
                    cc6 = cvv2.count("6")
                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                    cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        bscvv = bs[1].split("-")
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        bet10 = scv(cvv1,cv2,betcv)
                        bet11 = scv(cvv2,cv3,betcv1)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:   
                        if "cvb" in bet:
                            bs1 = bs[1].split("cvb")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif int(point) <=10:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif int(point) >=11:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cvs" in bet:
                            bs1 = bs[1].split("cvs")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif int(point) >=11:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif int(point) <=10:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cvc" in bet:
                            bs1 = bs[1].split("cvc")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv00" in bet:
                            bs1 = bs[1].split("cv00")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            y1 = int(point) % 2
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif y1 != 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv0" in bet:
                            bs1 = bs[1].split("cv0")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            y1 = int(point) % 2
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            elif y1 == 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv12" in bet:
                            bs1 = bs[1].split("cv12")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv13" in bet:
                            bs1 = bs[1].split("cv13")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv14" in bet:
                            bs1 = bs[1].split("cv14")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv23" in bet:
                            bs1 = bs[1].split("cv23")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv24" in bet:
                            bs1 = bs[1].split("cv24")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1

                        elif "cv34" in bet:
                            bs1 = bs[1].split("cv34")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1


                if cc == 2:
                    cv = bscv[1].split("+")
                    cvv1 = cv[0]
                    cvv2 = cv[1]
                    cvv3 = cv[2]
                    c1 = cvv1.count("1")
                    c2 = cvv1.count("2")
                    c3 = cvv1.count("3")
                    c4 = cvv1.count("4")
                    c5 = cvv1.count("5")
                    c6 = cvv1.count("6")
                    cc1 = cvv2.count("1")
                    cc2 = cvv2.count("2")
                    cc3 = cvv2.count("3")
                    cc4 = cvv2.count("4")
                    cc5 = cvv2.count("5")
                    cc6 = cvv2.count("6")
                    ccc1 = cvv3.count("1")
                    ccc2 = cvv3.count("2")
                    ccc3 = cvv3.count("3")
                    ccc4 = cvv3.count("4")
                    ccc5 = cvv3.count("5")
                    ccc6 = cvv3.count("6")
                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                    cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                    cv4 = int(ccc1)+int(ccc2)+int(ccc3)+int(ccc4)+int(ccc5)+int(ccc6)
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        bscvv = bs[1].split("-")
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        betcv2 = int(bscvv[2])
                        bet10 = scv(cvv1,cv2,betcv)
                        bet11 = scv(cvv2,cv3,betcv1)
                        bet12 = scv(cvv3,cv4,betcv2)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:   
                        if "cvb" in bet:
                            bs1 = bs[1].split("cvb")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif int(point) <=10:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif int(point) >=11:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cvs" in bet:
                            bs1 = bs[1].split("cvs")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif int(point) >=11:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif int(point) <=10:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cvc" in bet:
                            bs1 = bs[1].split("cvc")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv00" in bet:
                            bs1 = bs[1].split("cv00")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            y1 = int(point) % 2
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif y1 != 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv0" in bet:
                            bs1 = bs[1].split("cv0")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            y1 = int(point) % 2
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            elif y1 == 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv12" in bet:
                            bs1 = bs[1].split("cv12")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv13" in bet:
                            bs1 = bs[1].split("cv13")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv14" in bet:
                            bs1 = bs[1].split("cv14")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv23" in bet:
                            bs1 = bs[1].split("cv23")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv24" in bet:
                            bs1 = bs[1].split("cv24")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                        elif "cv34" in bet:
                            bs1 = bs[1].split("cv34")
                            bs2 = bs1[0].split("-")
                            betcv = int(bs2[0])
                            betcv1 = int(bs2[1])
                            betcv2 = int(bs2[2])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2

                if cc == 3:
                    cv = bscv[1].split("+")
                    cvv1 = cv[0]
                    cvv2 = cv[1]
                    cvv3 = cv[2]
                    cvv4 = cv[3]
                    c1 = cvv1.count("1")
                    c2 = cvv1.count("2")
                    c3 = cvv1.count("3")
                    c4 = cvv1.count("4")
                    c5 = cvv1.count("5")
                    c6 = cvv1.count("6")
                    cc1 = cvv2.count("1")
                    cc2 = cvv2.count("2")
                    cc3 = cvv2.count("3")
                    cc4 = cvv2.count("4")
                    cc5 = cvv2.count("5")
                    cc6 = cvv2.count("6")
                    ccc1 = cvv3.count("1")
                    ccc2 = cvv3.count("2")
                    ccc3 = cvv3.count("3")
                    ccc4 = cvv3.count("4")
                    ccc5 = cvv3.count("5")
                    ccc6 = cvv3.count("6")
                    cccc1 = cvv4.count("1")
                    cccc2 = cvv4.count("2")
                    cccc3 = cvv4.count("3")
                    cccc4 = cvv4.count("4")
                    cccc5 = cvv4.count("5")
                    cccc6 = cvv4.count("6")
                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                    cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                    cv4 = int(ccc1)+int(ccc2)+int(ccc3)+int(ccc4)+int(ccc5)+int(ccc6)
                    cv5 = int(cccc1)+int(cccc2)+int(cccc3)+int(cccc4)+int(cccc5)+int(cccc6)
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        bscvv = bs[1].split("-")
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        betcv2 = int(bscvv[2])
                        betcv3 = int(bscvv[3])
                        bet10 = scv(cvv1,cv2,betcv)
                        bet11 = scv(cvv2,cv3,betcv1)
                        bet12 = scv(cvv3,cv4,betcv2)
                        bet13 = scv(cvv4,cv5,betcv3)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:   
                        if "cvb" in bet:
                            bs1 = bs[1].split("cvb")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif int(point) <=10:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif int(point) >=11:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cvs" in bet:
                            bs1 = bs[1].split("cvs")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif int(point) >=11:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif int(point) <=10:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cvc" in bet:
                            bs1 = bs[1].split("cvc")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv00" in bet:
                            bs1 = bs[1].split("cv00")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif y1 != 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv0" in bet:
                            bs1 = bs[1].split("cv0")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            elif y1 == 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv12" in bet:
                            bs1 = bs[1].split("cv12")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv13" in bet:
                            bs1 = bs[1].split("cv13")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv14" in bet:
                            bs1 = bs[1].split("cv14")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv23" in bet:
                            bs1 = bs[1].split("cv23")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv24" in bet:
                            bs1 = bs[1].split("cv24")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                        elif "cv34" in bet:
                            bs1 = bs[1].split("cv34")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3

                if cc == 4:
                    cv = bscv[1].split("+")
                    cvv1 = cv[0]
                    cvv2 = cv[1]
                    cvv3 = cv[2]
                    cvv4 = cv[3]
                    cvv5 = cv[4]
                    c1 = cvv1.count("1")
                    c2 = cvv1.count("2")
                    c3 = cvv1.count("3")
                    c4 = cvv1.count("4")
                    c5 = cvv1.count("5")
                    c6 = cvv1.count("6")
                    cc1 = cvv2.count("1")
                    cc2 = cvv2.count("2")
                    cc3 = cvv2.count("3")
                    cc4 = cvv2.count("4")
                    cc5 = cvv2.count("5")
                    cc6 = cvv2.count("6")
                    ccc1 = cvv3.count("1")
                    ccc2 = cvv3.count("2")
                    ccc3 = cvv3.count("3")
                    ccc4 = cvv3.count("4")
                    ccc5 = cvv3.count("5")
                    ccc6 = cvv3.count("6")
                    cccc1 = cvv4.count("1")
                    cccc2 = cvv4.count("2")
                    cccc3 = cvv4.count("3")
                    cccc4 = cvv4.count("4")
                    cccc5 = cvv4.count("5")
                    cccc6 = cvv4.count("6")
                    ccccc1 = cvv5.count("1")
                    ccccc2 = cvv5.count("2")
                    ccccc3 = cvv5.count("3")
                    ccccc4 = cvv5.count("4")
                    ccccc5 = cvv5.count("5")
                    ccccc6 = cvv5.count("6")
                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                    cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                    cv4 = int(ccc1)+int(ccc2)+int(ccc3)+int(ccc4)+int(ccc5)+int(ccc6)
                    cv5 = int(cccc1)+int(cccc2)+int(cccc3)+int(cccc4)+int(cccc5)+int(cccc6)
                    cv6 = int(ccccc1)+int(ccccc2)+int(ccccc3)+int(ccccc4)+int(ccccc5)+int(ccccc6)
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        bscvv = bs[1].split("-")
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        betcv2 = int(bscvv[2])
                        betcv3 = int(bscvv[3])
                        betcv4 = int(bscvv[4])
                        bet10 = scv(cvv1,cv2,betcv)
                        bet11 = scv(cvv2,cv3,betcv1)
                        bet12 = scv(cvv3,cv4,betcv2)
                        bet13 = scv(cvv4,cv5,betcv3)
                        bet14 = scv(cvv5,cv6,betcv4)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:   
                        if "cvb" in bet:
                            bs1 = bs[1].split("cvb")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif int(point) <=10:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif int(point) >=11:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cvs" in bet:
                            bs1 = bs[1].split("cvs")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif int(point) >=11:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif int(point) <=10:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cvc" in bet:
                            bs1 = bs[1].split("cvc")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv00" in bet:
                            bs1 = bs[1].split("cv00")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif y1 != 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv0" in bet:
                            bs1 = bs[1].split("cv0")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            elif y1 == 0:
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv12" in bet:
                            bs1 = bs[1].split("cv12")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv13" in bet:
                            bs1 = bs[1].split("cv13")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv14" in bet:
                            bs1 = bs[1].split("cv14")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv23" in bet:
                            bs1 = bs[1].split("cv23")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv24" in bet:
                            bs1 = bs[1].split("cv24")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                        elif "cv34" in bet:
                            bs1 = bs[1].split("cv34")
                            bscvv = bs1[0].split("-")
                            betcv = int(bscvv[0])
                            betcv1 = int(bscvv[1])
                            betcv2 = int(bscvv[2])
                            betcv3 = int(bscvv[3])
                            betcv4 = int(bscvv[4])
                            bet10 = scv(cvv1,cv2,betcv)
                            bet11 = scv(cvv2,cv3,betcv1)
                            bet12 = scv(cvv3,cv4,betcv2)
                            bet13 = scv(cvv4,cv5,betcv3)
                            bet14 = scv(cvv5,cv6,betcv4)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betcv
                                bet11 = bet11 - betcv1
                                bet12 = bet12 - betcv2
                                bet13 = bet13 - betcv3
                                bet14 = bet14 - betcv4
                            else:
                                bet10 = bet10 + betcv
                                bet11 = bet11 + betcv1
                                bet12 = bet12 + betcv2
                                bet13 = bet13 + betcv3
                                bet14 = bet14 + betcv4

                winlose = bet10+bet11+bet12+bet13+bet14


            #-----------------------------------------------
            #----------------o3输赢-------------------------
            #-----------------------------------------------

            def aa8():
                if "+" not in bet:
                    bs1 = int(bs[1])
                    winlose = bs1*3
                elif "+" in bet:
                    bs1 = bs[1].split("+")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    winlose = bs2*3+bs3*3
                return winlose

            def eat8():
                if "+" not in bet:
                    y480 = int(bs[1]) % 120
                    y340 = int(bs[1]) % 340
                    y580 = int(bs[1]) % 580
                    y100 = int(bs[1]) % 100
                    y1000 = int(bs[1]) % 1000
                    if y1000 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/1000*-1050
                    elif y480 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/120*-125
                    elif y100 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/100*-105
                    elif y340 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/340*-355
                    elif y580 == 0:
                        bs1 = int(bs[1])
                        winlose = bs1/580*-605
                    elif int(bs[1]) == 150:
                        bs1 = int(bs[1])
                        winlose = bs1/150*-155
                elif "+" in bet:
                    bs1 = bs[1].split("+")
                    bs2 = int(bs1[0])
                    bs3 = int(bs1[1])
                    winlose = bs2/100*-105+bs3/120*-125

                return winlose

            if bs[0] == "o1":
                if bar == "1":
                    winlose = aa8()
                else:
                    winlose = eat8()

            if bs[0] == "o2":
                if bar == "2":
                    winlose = aa8()
                else:
                    winlose = eat8()

            if bs[0] == "o3":
                if bar == "3":
                    winlose = aa8()
                else:
                    winlose = eat8()

            if bs[0] == "o4":
                if bar == "4":
                    winlose = aa8()
                else:
                    winlose = eat8()


            #-----------------------------------------------
            #----------------三顺-------------------------
            #-----------------------------------------------



            if "=" in bs[0] and "cv" not in bet and "q" not in bet:
                bet1 = int(bs[1])
                bs2 = bs[0]
                bs3 = bs2.split("=")
                bs4 = bs3[0]
                s1 = bs3[0].count("1")
                s2 = bs3[0].count("2")
                s3 = bs3[0].count("3")
                s4 = bs3[0].count("4")
                s5 = bs3[0].count("5")
                s6 = bs3[0].count("6")
                bs1 = int(s1)+int(s2)+int(s3)+int(s4)+int(s5)+int(s6)
                if bs1 == 1:
                    ba = bs4[0]+bs4[0]+bs4[0]
                    if bar1 == ba:
                        winlose = bet1*160
                    else:
                        winlose = bet1*-1
                elif bs1 == 2:
                    ba = bs4[0]+bs4[0]+bs4[0]
                    bb = bs4[1]+bs4[1]+bs4[1]
                    if bar1 in ba or bar1 in bb:
                        winlose = bet1/2*159
                    else:
                        winlose = bet1*-1
                elif bs1 == 3:
                    ba = bs4[0]+bs4[0]+bs4[0]
                    bb = bs4[1]+bs4[1]+bs4[1]
                    bc = bs4[2]+bs4[2]+bs4[2]
                    if bar1 in ba or bar1 in bb or bar1 in bc:
                        winlose = bet1/3*158
                    else:
                        winlose = bet1*-1
                elif bs1 == 4:
                    ba = bs4[0]+bs4[0]+bs4[0]
                    bb = bs4[1]+bs4[1]+bs4[1]
                    bc = bs4[2]+bs4[2]+bs4[2]
                    bd = bs4[3]+bs4[3]+bs4[3]
                    if bar1 in ba or bar1 in bb or bar1 in bc or bar1 in bd:
                        winlose = bet1/4*157
                    else:
                        winlose = bet1*-1
                elif bs1 == 5:
                    ba = bs4[0]+bs4[0]+bs4[0]
                    bb = bs4[1]+bs4[1]+bs4[1]
                    bc = bs4[2]+bs4[2]+bs4[2]
                    bd = bs4[3]+bs4[3]+bs4[3]
                    be = bs4[4]+bs4[4]+bs4[4]
                    if bar1 in ba or bar1 in bb or bar1 in bc or bar1 in bd or bar1 in be:
                        winlose = bet1/5*156
                    else:
                        winlose = bet1*-1
                elif bs1 == 6:
                    ba = bs4[0]+bs4[0]+bs4[0]
                    bb = bs4[1]+bs4[1]+bs4[1]
                    bc = bs4[2]+bs4[2]+bs4[2]
                    bd = bs4[3]+bs4[3]+bs4[3]
                    be = bs4[4]+bs4[4]+bs4[4]
                    bf = bs4[5]+bs4[5]+bs4[5]
                    if bar1 in ba or bar1 in bb or bar1 in bc or bar1 in bd or bar1 in be or bar1 in bf:
                        winlose = bet1/6*155
                    else:
                        winlose = bet1*-1


            #-----------------------------------------------
            #----------------大中小中-------------------------
            #-----------------------------------------------



            if bs[0] == "bc" or bs[0] == "cb":
                bs1 = int(bs[1])
                if int(point) <= 8 or bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                    winlose = bs1*-1
                elif int(point) >= 13 or int(point) == 9 or int(point) == 10 or bar1 == "333" or bar1 == "444":
                    winlose = bs1*0
                elif int(point) == 11 or 12:
                    winlose = bs1*1
                

                
            if bs[0] == "sc" or bs[0] == "cs":
                bs1 = int(bs[1])
                if int(point) >= 13 or bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                    winlose = bs1*-1
                elif int(point) <= 8 or int(point) == 11 or int(point) == 12 or bar1 == "333" or bar1 == "444":
                    winlose = bs1*0
                elif int(point) == 9 or 10:
                    winlose = bs1*1

            #-----------------------------------------------
            #----------------单双-------------------------
            #-----------------------------------------------

            if bs[0] == "00":
                bs1 = int(bs[1])
                y1 = int(point) % 2
                if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                    winlose = bs1*-1
                elif y1 == 0:
                    winlose = bs1*1
                else:
                    winlose = bs1*-1

            elif bs[0] == "0":
                bs1 = int(bs[1])
                y1 = int(point) % 2
                if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                    winlose = bs1*-1
                elif y1 != 0:
                    winlose = bs1*1
                else:
                    winlose = bs1*-1

            #-----------------------------------------------
            #----------------cv-------------------------
            #-----------------------------------------------
            if "*" in bet:
                bet2 = 0
                bet3 = 0
                bet4 = 0
                bet5 = 0
                bet6 = 0
                bet7 = 0
                bet8 = 0
                bet9 = 0
                bet10 = 0
                bet11 = 0
                bet12 = 0
                bet13 = 0
                bet14 = 0
                bet15 = 0
                bet16 = 0
                bet17 = 0
                bet18 = 0
                bet19 = 0
                cvt = 0
                bs1 = bs[0].split("*")
                bs2 = bs1[0]
                bs3 = bs1[1]
                b1 = bs2.count("1")
                b2 = bs2.count("2")
                b3 = bs2.count("3")
                b4 = bs2.count("4")
                b5 = bs2.count("5")
                b6 = bs2.count("6")
                y1 = bs3.count("1")
                y2 = bs3.count("2")
                y3 = bs3.count("3")
                y4 = bs3.count("4")
                y5 = bs3.count("5")
                y6 = bs3.count("6")
                by1 = int(b1)+int(b2)+int(b3)+int(b4)+int(b5)+int(b6)
                yy1 = int(y1)+int(y2)+int(y3)+int(y4)+int(y5)+int(y6)
                if "x" not in bet:
                    if by1 == 1 and yy1 == 1:
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y140 = (bet1-140)
                        wl = bar1.count(bs2)
                        wl1 = bar1.count(bs3)
                        wl6 = int(wl)
                        wl16 = int(wl1)
                        cvt = wl16-wl6
                        if wl16 > wl6:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet2 = bet1*1
                            else:
                                bet2 = 999999
                        if wl6 > wl16 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl6 > wl16 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl6 > wl16 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl6 > wl16 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl6 > wl16 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl6 > wl16 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl16 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl16 and y140 == 0:
                            bet4 = bet1/140*-145

                    elif by1 == 1 and yy1 == 2:
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        wl = bar1.count(bs2)
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl6 = int(wl)
                        wl16 = int(wl1)
                        wl17 = int(wl2)
                        cvt = wl17-wl6
                        if wl16 > wl6:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet2 = bet1*1
                            else:
                                bet2 = 999999
                        if wl17 > wl6:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet3 = bet1*1
                            else:
                                bet3 = 999999
                        if wl6 > wl16 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl6 > wl16 and y1000 == 0:
                            bet4 = bet1/1000*-1050 
                        elif wl6 > wl16 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl6 > wl16 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl6 > wl16 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl16 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl16 and y100 == 0: 
                            bet4 = bet1/100*-105
                        elif wl6 > wl16 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl6 > wl17 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl6 > wl17 and y1000 == 0:
                            bet5 = bet1/1000*-1050 
                        elif wl6 > wl17 and bet1 == 600:
                            bet5 = bet1/600*-630 
                        elif wl6 > wl17 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl6 > wl17 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl17 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl17 and y100 == 0: 
                            bet5 = bet1/100*-105
                        elif wl6 > wl17 and y140 == 0:
                            bet5 = bet1/140*-145

                    elif by1 == 1 and yy1 == 3:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[1])
                        wl2 = bar1.count(bs3[2])
                        wl3 = bar1.count(bs3[0])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        wl6 = int(wl)    #1
                        wl16 = int(wl1) #2
                        wl17 = int(wl2) #3
                        wl18 = int(wl3)  #4
                        cvt = wl18-wl6    
                        if wl18 > wl6:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet2 = bet1*1
                            else:
                                bet2 = 999999
                        if wl17 > wl6:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet3 = bet1*1
                            else:
                                bet3 = 999999
                        if wl16 > wl6:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet4 = bet1*1
                            else:
                                bet4 = 999999
                        if wl6 > wl16 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl6 > wl16 and y1000 == 0:
                            bet5 = bet1/1000*-1050 
                        elif wl6 > wl16 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl6 > wl16 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl6 > wl16 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl16 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl16 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl6 > wl16 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl6 > wl17 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl6 > wl17 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl6 > wl17 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl6 > wl17 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl6 > wl17 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl17 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl17 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl6 > wl17 and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl6 > wl18 and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl6 > wl18 and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl6 > wl18 and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl6 > wl18 and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl6 > wl18 and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl18 and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl18 and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl6 > wl18 and y140 == 0:
                            bet7 = bet1/140*-145

                    elif by1 == 1 and yy1 == 4:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = bet1*1
                        if wl2 > wl:
                            bet3 = bet1*1
                        if wl3 > wl:
                            bet4 = bet1*1
                        if wl4 > wl:
                            bet5 = bet1*1
                        if wl > wl1 and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl > wl1 and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl > wl1 and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl > wl1 and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl > wl1 and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl > wl1 and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl > wl1 and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl > wl1 and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl > wl2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl > wl2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl > wl2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl > wl2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl > wl2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl > wl2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl > wl2 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl > wl2 and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl > wl3 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl > wl3 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl > wl3 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl > wl3 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl > wl3 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl > wl3 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl > wl3 and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl > wl3 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl > wl4 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl > wl4 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl > wl4 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl > wl4 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl > wl4 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl > wl4 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl > wl4 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl > wl4 and y140 == 0:
                            bet5 = bet1/140*-145

                    elif by1 == 1 and yy1 == 5:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y100 = bet1 % 100
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = bet1*1
                        if wl2 > wl:
                            bet3 = bet1*1
                        if wl3 > wl:
                            bet4 = bet1*1
                        if wl4 > wl:
                            bet5 = bet1*1
                        if wl5 > wl:
                            bet6 = bet1*1
                        if wl > wl1 and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl > wl1 and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl > wl1 and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl > wl1 and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl > wl1 and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl > wl1 and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl > wl1 and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl > wl1 and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl > wl2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl > wl2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl > wl2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl > wl2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl > wl2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl > wl2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl > wl2 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl > wl2 and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl > wl3 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl > wl3 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl > wl3 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl > wl3 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl > wl3 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl > wl3 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl > wl3 and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl > wl3 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl > wl4 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl > wl4 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl > wl4 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl > wl4 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl > wl4 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl > wl4 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl > wl4 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl > wl4 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl > wl5 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl > wl5 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl > wl5 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl > wl5 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl > wl5 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl > wl5 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl > wl5 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl > wl5 and y140 == 0:
                            bet6 = bet1/140*-145

                    elif by1 == 1 and yy1 == 6:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = bet1*1
                        if wl2 > wl:
                            bet3 = bet1*1
                        if wl3 > wl:
                            bet4 = bet1*1
                        if wl4 > wl:
                            bet5 = bet1*1
                        if wl5 > wl:
                            bet6 = bet1*1
                        if wl6 > wl:
                            bet7 = bet1*1
                        if wl > wl1 and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl > wl1 and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl > wl1 and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl > wl1 and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl > wl1 and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl > wl1 and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl > wl1 and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl > wl1 and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl > wl2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl > wl2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl > wl2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl > wl2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl > wl2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl > wl2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl > wl2 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl > wl2 and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl > wl3 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl > wl3 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl > wl3 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl > wl3 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl > wl3 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl > wl3 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl > wl3 and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl > wl3 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl > wl4 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl > wl4 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl > wl4 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl > wl4 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl > wl4 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl > wl4 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl > wl4 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl > wl4 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl > wl5 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl > wl5 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl > wl5 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl > wl5 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl > wl5 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl > wl5 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl > wl5 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl > wl5 and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl > wl6 and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl > wl6 and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl > wl6 and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl > wl6 and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl > wl6 and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl > wl6 and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl > wl6 and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl > wl6 and y140 == 0:
                            bet7 = bet1/140*-145

                    elif by1 == 1 and yy1 == 7:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = bet1*1
                        if wl2 > wl:
                            bet3 = bet1*1
                        if wl3 > wl:
                            bet4 = bet1*1
                        if wl4 > wl:
                            bet5 = bet1*1
                        if wl5 > wl:
                            bet6 = bet1*1
                        if wl6 > wl:
                            bet7 = bet1*1
                        if wl7 > wl:
                            bet8 = bet1*1
                        if wl > wl1 and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl > wl1 and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl > wl1 and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl > wl1 and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl > wl1 and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl > wl1 and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl > wl1 and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl > wl1 and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl > wl2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl > wl2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl > wl2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl > wl2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl > wl2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl > wl2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl > wl2 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl > wl2 and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl > wl3 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl > wl3 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl > wl3 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl > wl3 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl > wl3 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl > wl3 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl > wl3 and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl > wl3 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl > wl4 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl > wl4 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl > wl4 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl > wl4 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl > wl4 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl > wl4 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl > wl4 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl > wl4 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl > wl5 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl > wl5 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl > wl5 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl > wl5 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl > wl5 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl > wl5 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl > wl5 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl > wl5 and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl > wl6 and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl > wl6 and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl > wl6 and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl > wl6 and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl > wl6 and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl > wl6 and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl > wl6 and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl > wl6 and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl > wl7 and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl > wl7 and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl > wl7 and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl > wl7 and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl > wl7 and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl > wl7 and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl > wl7 and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl > wl7 and y140 == 0:
                            bet8 = bet1/140*-145

                    elif by1 == 1 and yy1 == 8:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        wl8 = bar1.count(bs3[7])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = bet1*1
                        if wl2 > wl:
                            bet3 = bet1*1
                        if wl3 > wl:
                            bet4 = bet1*1
                        if wl4 > wl:
                            bet5 = bet1*1
                        if wl5 > wl:
                            bet6 = bet1*1
                        if wl6 > wl:
                            bet7 = bet1*1
                        if wl7 > wl:
                            bet8 = bet1*1
                        if wl8 > wl:
                            bet9 = bet1*1
                        if wl > wl1 and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl > wl1 and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl > wl1 and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl > wl1 and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl > wl1 and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl > wl1 and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl > wl1 and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl > wl1 and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl > wl2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl > wl2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl > wl2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl > wl2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl > wl2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl > wl2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl > wl2 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl > wl2 and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl > wl3 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl > wl3 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl > wl3 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl > wl3 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl > wl3 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl > wl3 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl > wl3 and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl > wl3 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl > wl4 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl > wl4 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl > wl4 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl > wl4 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl > wl4 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl > wl4 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl > wl4 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl > wl4 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl > wl5 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl > wl5 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl > wl5 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl > wl5 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl > wl5 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl > wl5 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl > wl5 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl > wl5 and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl > wl6 and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl > wl6 and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl > wl6 and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl > wl6 and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl > wl6 and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl > wl6 and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl > wl6 and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl > wl6 and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl > wl7 and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl > wl7 and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl > wl7 and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl > wl7 and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl > wl7 and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl > wl7 and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl > wl7 and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl > wl7 and y140 == 0:
                            bet8 = bet1/140*-145
                        if wl > wl8 and y12000 == 0:
                            bet9 = bet1/12000*-12500
                        elif wl > wl8 and y1000 == 0:
                            bet9 = bet1/1000*-1050
                        elif wl > wl8 and bet1 == 600:
                            bet9 = bet1/600*-630
                        elif wl > wl8 and y480 == 0:
                            bet9 = bet1/120*-125
                        elif wl > wl8 and y580 == 0:
                            bet9 = (((bet1-480)/100*-105)-500)
                        elif wl > wl8 and y340 == 0:
                            bet9 = (((bet1-240)/100*-105)-250)
                        elif wl > wl8 and y100 == 0:
                            bet9 = bet1/100*-105
                        elif wl > wl8 and y140 == 0:
                            bet9 = bet1/140*-145

                    elif by1 == 1 and yy1 == 9:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        wl8 = bar1.count(bs3[7])
                        wl9 = bar1.count(bs3[8])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = bet1*1
                        if wl2 > wl:
                            bet3 = bet1*1
                        if wl3 > wl:
                            bet4 = bet1*1
                        if wl4 > wl:
                            bet5 = bet1*1
                        if wl5 > wl:
                            bet6 = bet1*1
                        if wl6 > wl:
                            bet7 = bet1*1
                        if wl7 > wl:
                            bet8 = bet1*1
                        if wl8 > wl:
                            bet9 = bet1*1
                        if wl9 > wl:
                            bet10 = bet1*1
                        if wl > wl1 and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl > wl1 and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl > wl1 and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl > wl1 and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl > wl1 and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl > wl1 and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl > wl1 and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl > wl1 and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl > wl2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl > wl2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl > wl2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl > wl2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl > wl2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl > wl2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl > wl2 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl > wl2 and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl > wl3 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl > wl3 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl > wl3 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl > wl3 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl > wl3 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl > wl3 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl > wl3 and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl > wl3 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl > wl4 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl > wl4 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl > wl4 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl > wl4 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl > wl4 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl > wl4 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl > wl4 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl > wl4 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl > wl5 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl > wl5 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl > wl5 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl > wl5 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl > wl5 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl > wl5 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl > wl5 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl > wl5 and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl > wl6 and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl > wl6 and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl > wl6 and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl > wl6 and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl > wl6 and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl > wl6 and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl > wl6 and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl > wl6 and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl > wl7 and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl > wl7 and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl > wl7 and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl > wl7 and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl > wl7 and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl > wl7 and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl > wl7 and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl > wl7 and y140 == 0:
                            bet8 = bet1/140*-145
                        if wl > wl8 and y12000 == 0:
                            bet9 = bet1/12000*-12500
                        elif wl > wl8 and y1000 == 0:
                            bet9 = bet1/1000*-1050
                        elif wl > wl8 and bet1 == 600:
                            bet9 = bet1/600*-630
                        elif wl > wl8 and y480 == 0:
                            bet9 = bet1/120*-125
                        elif wl > wl8 and y580 == 0:
                            bet9 = (((bet1-480)/100*-105)-500)
                        elif wl > wl8 and y340 == 0:
                            bet9 = (((bet1-240)/100*-105)-250)
                        elif wl > wl8 and y100 == 0:
                            bet9 = bet1/100*-105
                        elif wl > wl8 and y140 == 0:
                            bet9 = bet1/140*-145
                        if wl > wl9 and y12000 == 0:
                            bet10 = bet1/12000*-12500
                        elif wl > wl9 and y1000 == 0:
                            bet10 = bet1/1000*-1050
                        elif wl > wl9 and bet1 == 600:
                            bet10 = bet1/600*-630
                        elif wl > wl9 and y480 == 0:
                            bet10 = bet1/120*-125
                        elif wl > wl9 and y580 == 0:
                            bet10 = (((bet1-480)/100*-105)-500)
                        elif wl > wl9 and y340 == 0:
                            bet10 = (((bet1-240)/100*-105)-250)
                        elif wl > wl9 and y100 == 0:
                            bet10 = bet1/100*-105
                        elif wl > wl9 and y140 == 0:
                            bet10 = bet1/140*-145

                    elif by1 == 1 and yy1 == 10:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        wl8 = bar1.count(bs3[7])
                        wl9 = bar1.count(bs3[8])
                        wl10 = bar1.count(bs3[9])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = bet1*1
                        if wl2 > wl:
                            bet3 = bet1*1
                        if wl3 > wl:
                            bet4 = bet1*1
                        if wl4 > wl:
                            bet5 = bet1*1
                        if wl5 > wl:
                            bet6 = bet1*1
                        if wl6 > wl:
                            bet7 = bet1*1
                        if wl7 > wl:
                            bet8 = bet1*1
                        if wl8 > wl:
                            bet9 = bet1*1
                        if wl9 > wl:
                            bet10 = bet1*1
                        if wl10 > wl:
                            bet11 = bet1*1
                        if wl > wl1 and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl > wl1 and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl > wl1 and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl > wl1 and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl > wl1 and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl > wl1 and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl > wl1 and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl > wl1 and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl > wl2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl > wl2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl > wl2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl > wl2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl > wl2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl > wl2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl > wl2 and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl > wl2 and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl > wl3 and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl > wl3 and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl > wl3 and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl > wl3 and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl > wl3 and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl > wl3 and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl > wl3 and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl > wl3 and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl > wl4 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl > wl4 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl > wl4 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl > wl4 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl > wl4 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl > wl4 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl > wl4 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl > wl4 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl > wl5 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl > wl5 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl > wl5 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl > wl5 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl > wl5 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl > wl5 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl > wl5 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl > wl5 and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl > wl6 and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl > wl6 and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl > wl6 and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl > wl6 and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl > wl6 and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl > wl6 and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl > wl6 and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl > wl6 and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl > wl7 and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl > wl7 and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl > wl7 and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl > wl7 and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl > wl7 and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl > wl7 and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl > wl7 and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl > wl7 and y140 == 0:
                            bet8 = bet1/140*-145
                        if wl > wl8 and y12000 == 0:
                            bet9 = bet1/12000*-12500
                        elif wl > wl8 and y1000 == 0:
                            bet9 = bet1/1000*-1050
                        elif wl > wl8 and bet1 == 600:
                            bet9 = bet1/600*-630
                        elif wl > wl8 and y480 == 0:
                            bet9 = bet1/120*-125
                        elif wl > wl8 and y580 == 0:
                            bet9 = (((bet1-480)/100*-105)-500)
                        elif wl > wl8 and y340 == 0:
                            bet9 = (((bet1-240)/100*-105)-250)
                        elif wl > wl8 and y100 == 0:
                            bet9 = bet1/100*-105
                        elif wl > wl8 and y140 == 0:
                            bet9 = bet1/140*-145
                        if wl > wl9 and y12000 == 0:
                            bet10 = bet1/12000*-12500
                        elif wl > wl9 and y1000 == 0:
                            bet10 = bet1/1000*-1050
                        elif wl > wl9 and bet1 == 600:
                            bet10 = bet1/600*-630
                        elif wl > wl9 and y480 == 0:
                            bet10 = bet1/120*-125
                        elif wl > wl9 and y580 == 0:
                            bet10 = (((bet1-480)/100*-105)-500)
                        elif wl > wl9 and y340 == 0:
                            bet10 = (((bet1-240)/100*-105)-250)
                        elif wl > wl9 and y100 == 0:
                            bet10 = bet1/100*-105
                        elif wl > wl9 and y140 == 0:
                            bet10 = bet1/140*-145
                        if wl > wl10 and y12000 == 0:
                            bet11 = bet1/12000*-12500
                        elif wl > wl10 and y1000 == 0:
                            bet11 = bet1/1000*-1050
                        elif wl > wl10 and bet1 == 600:
                            bet11 = bet1/600*-630
                        elif wl > wl10 and y480 == 0:
                            bet11 = bet1/120*-125
                        elif wl > wl10 and y580 == 0:
                            bet11 = (((bet1-480)/100*-105)-500)
                        elif wl > wl10 and y340 == 0:
                            bet11 = (((bet1-240)/100*-105)-250)
                        elif wl > wl10 and y100 == 0:
                            bet11 = bet1/100*-105
                        elif wl > wl10 and y140 == 0:
                            bet11 = bet1/140*-145

                    elif by1 == 2 and yy1 == 1:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bss1 = int(bss[0])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            y100 = bss1 % 100
                            y1000 = bss1 % 1000
                            y12000 = bss1 % 12000
                            y580 = (bss1-480) % 100
                            y340 = (bss1-240) % 100
                            y140 = (bss1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl6 = int(wl)
                            wl7 = int(wl1)
                            wl16 = int(wl2)
                            cvt = wl16-wl7
                            ys = wl6+wl7
                            ys1 = bar1[0] == bar1[1]
                            ys2 = bar1[0] == bar1[2]
                            y20 = bss2 % 20
                            ys1000 = bss2 % 1000
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = bss1*1
                                else:
                                    bet2 = 999999
                            if wl16 > wl7:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet3 = bss1*1
                                else:
                                    bet3 = 999999
                            if wl6 > wl16 and y12000 == 0:
                                bet4 = bss1/12000*-12500
                            elif wl6 > wl16 and y1000 == 0:
                                bet4 = bss1/1000*-1050
                            elif wl6 > wl16 and bss1 == 600:
                                bet4 = bss1/600*-630
                            elif wl6 > wl16 and y480 == 0:
                                bet4 = bss1/120*-125
                            elif wl6 > wl16 and y580 == 0:
                                bet4 = (((bss1-480)/100*-105)-500)
                            elif wl6 > wl16 and y340 == 0:
                                bet4 = (((bss1-240)/100*-105)-250)
                            elif wl6 > wl16 and y100 == 0: 
                                bet4 = bss1/100*-105
                            elif wl6 > wl16 and y140 == 0:
                                bet4 = bss1/140*-145
                            if wl7 > wl16 and y12000 == 0:
                                bet5 = bss1/12000*-12500
                            elif wl7 > wl16 and y1000 == 0:
                                bet5 = bss1/1000*-1050
                            elif wl7 > wl16 and bss1 == 600:
                                bet5 = bss1/600*-630
                            elif wl7 > wl16 and y480 == 0:
                                bet5 = bss1/120*-125
                            elif wl7 > wl16 and y580 == 0:
                                bet5 = (((bss1-480)/100*-105)-500)
                            elif wl7 > wl16 and y340 == 0:
                                bet5 = (((bss1-240)/100*-105)-250)
                            elif wl7 > wl16 and y100 == 0: 
                                bet5 = bss1/100*-105
                            elif wl7 > wl16 and y140 == 0:
                                bet5 = bss1/140*-145
                            if ys >= 2:
                                if ys1000 == 0:
                                    bet14 = bss2/1000*-6300
                                elif bss2 == 500:
                                    bet14 = bss2/500*-3150
                                elif y20 == 0:
                                    bet14 = bss2/20*-125
                                elif bss2 == 30:
                                    bet14 = bss2/30*-190
                                elif bss2 == 50:
                                    bet14 = bss2/50*-315
                            elif ys == 0 and ys2 is True:
                                bet14 = bss2*3
                            elif ys == 0 and ys1 is True:
                                bet14 = bss2*5
                            elif ys == 0 and ys1 is False:
                                bet14 = bss2*6
                            
                        elif "-" not in bs[1]:
                            bet1 = int(bs[1])
                            y480 = bet1 % 120
                            y100 = bet1 % 100
                            y1000 = bet1 % 1000
                            y12000 = bet1 % 12000
                            y580 = (bet1-480) % 100
                            y340 = (bet1-240) % 100
                            y140 = (bet1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl6 = int(wl)
                            wl7 = int(wl1)
                            wl16 = int(wl2)
                            cvt = wl16-wl7
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = bet1*1
                                else:
                                    bet2 = 999999
                            if wl16 > wl7:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet3 = bet1*1
                                else:
                                    bet3 = 999999
                            if wl6 > wl16 and y12000 == 0:
                                bet4 = bet1/12000*-12500
                            elif wl6 > wl16 and y1000 == 0:
                                bet4 = bet1/1000*-1050
                            elif wl6 > wl16 and bet1 == 600:
                                bet4 = bet1/600*-630
                            elif wl6 > wl16 and y480 == 0:
                                bet4 = bet1/120*-125
                            elif wl6 > wl16 and y580 == 0:
                                bet4 = (((bet1-480)/100*-105)-500)
                            elif wl6 > wl16 and y340 == 0:
                                bet4 = (((bet1-240)/100*-105)-250)
                            elif wl6 > wl16 and y100 == 0: 
                                bet4 = bet1/100*-105
                            elif wl6 > wl16 and y140 == 0:
                                bet4 = bet1/140*-145
                            if wl7 > wl16 and y12000 == 0:
                                bet5 = bet1/12000*-12500
                            elif wl7 > wl16 and y1000 == 0:
                                bet5 = bet1/1000*-1050
                            elif wl7 > wl16 and bet1 == 600:
                                bet5 = bet1/600*-630
                            elif wl7 > wl16 and y480 == 0:
                                bet5 = bet1/120*-125
                            elif wl7 > wl16 and y580 == 0:
                                bet5 = (((bet1-480)/100*-105)-500)
                            elif wl7 > wl16 and y340 == 0:
                                bet5 = (((bet1-240)/100*-105)-250)
                            elif wl7 > wl16 and y100 == 0: 
                                bet5 = bet1/100*-105
                            elif wl7 > wl16 and y140 == 0:
                                bet5 = bet1/140*-145

                    elif by1 == 3 and yy1 == 1:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs3[0])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        wl5 = int(wl)    #1
                        wl6 = int(wl1) #2
                        wl7 = int(wl2) #3
                        wl8 = int(wl3)  #4
                        cvt = wl8-wl7    
                        if wl8 > wl5:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet2 = bet1*1
                            else:
                                bet2 = 999999
                        if wl8 > wl6:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet3 = bet1*1
                            else:
                                bet3 = 999999
                        if wl8 > wl7:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet4 = bet1*1
                            else:
                                bet4 = 999999
                        if wl5 > wl8 and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl5 > wl8 and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl5 > wl8 and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl5 > wl8 and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl5 > wl8 and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl5 > wl8 and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl5 > wl8 and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl5 > wl8 and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl6 > wl8 and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl6 > wl8 and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl6 > wl8 and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl6 > wl8 and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl6 > wl8 and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl8 and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl8 and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl6 > wl8 and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl7 > wl8 and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl7 > wl8 and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl7 > wl8 and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl7 > wl8 and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl7 > wl8 and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl7 > wl8 and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl7 > wl8 and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl7 > wl8 and y140 == 0:
                            bet7 = bet1/140*-145

                    elif by1 == 4 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0    
                        if wl > wl1:
                            bet2 = bet1*1
                        if wl > wl2:
                            bet3 = bet1*1
                        if wl > wl3:
                            bet4 = bet1*1
                        if wl > wl4:
                            bet5 = bet1*1
                        if wl1 > wl and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl1 > wl and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl1 > wl and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl1 > wl and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl1 > wl and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl1 > wl and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl1 > wl and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl1 > wl and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl2 > wl and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl2 > wl and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl2 > wl and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl2 > wl and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl2 > wl and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl2 > wl and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl2 > wl and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl2 > wl and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl3 > wl and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl3 > wl and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl3 > wl and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl3 > wl and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl3 > wl and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl3 > wl and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl3 > wl and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl3 > wl and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl4 > wl and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl4 > wl and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl4 > wl and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl4 > wl and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl4 > wl and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl4 > wl and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl4 > wl and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl4 > wl and y140 == 0:
                            bet5 = bet1/140*-145

                    elif by1 == 5 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0    
                        if wl > wl1:
                            bet2 = bet1*1
                        if wl > wl2:
                            bet3 = bet1*1
                        if wl > wl3:
                            bet4 = bet1*1
                        if wl > wl4:
                            bet5 = bet1*1
                        if wl > wl5:
                            bet6 = bet1*1
                        if wl1 > wl and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl1 > wl and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl1 > wl and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl1 > wl and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl1 > wl and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl1 > wl and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl1 > wl and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl1 > wl and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl2 > wl and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl2 > wl and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl2 > wl and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl2 > wl and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl2 > wl and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl2 > wl and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl2 > wl and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl2 > wl and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl3 > wl and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl3 > wl and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl3 > wl and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl3 > wl and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl3 > wl and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl3 > wl and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl3 > wl and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl3 > wl and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl4 > wl and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl4 > wl and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl4 > wl and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl4 > wl and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl4 > wl and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl4 > wl and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl4 > wl and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl4 > wl and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl5 > wl and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl5 > wl and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl5 > wl and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl5 > wl and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl5 > wl and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl5 > wl and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl5 > wl and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl5 > wl and y140 == 0:
                            bet6 = bet1/140*-145

                    elif by1 == 6 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0    
                        if wl > wl1:
                            bet2 = bet1*1
                        if wl > wl2:
                            bet3 = bet1*1
                        if wl > wl3:
                            bet4 = bet1*1
                        if wl > wl4:
                            bet5 = bet1*1
                        if wl > wl5:
                            bet6 = bet1*1
                        if wl > wl6:
                            bet7 = bet1*1
                        if wl1 > wl and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl1 > wl and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl1 > wl and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl1 > wl and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl1 > wl and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl1 > wl and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl1 > wl and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl1 > wl and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl2 > wl and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl2 > wl and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl2 > wl and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl2 > wl and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl2 > wl and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl2 > wl and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl2 > wl and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl2 > wl and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl3 > wl and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl3 > wl and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl3 > wl and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl3 > wl and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl3 > wl and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl3 > wl and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl3 > wl and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl3 > wl and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl4 > wl and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl4 > wl and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl4 > wl and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl4 > wl and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl4 > wl and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl4 > wl and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl4 > wl and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl4 > wl and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl5 > wl and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl5 > wl and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl5 > wl and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl5 > wl and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl5 > wl and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl5 > wl and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl5 > wl and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl5 > wl and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl6 > wl and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl6 > wl and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl6 > wl and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl6 > wl and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl6 > wl and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl6 > wl and y140 == 0:
                            bet7 = bet1/140*-145

                    elif by1 == 7 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0    
                        if wl > wl1:
                            bet2 = bet1*1
                        if wl > wl2:
                            bet3 = bet1*1
                        if wl > wl3:
                            bet4 = bet1*1
                        if wl > wl4:
                            bet5 = bet1*1
                        if wl > wl5:
                            bet6 = bet1*1
                        if wl > wl6:
                            bet7 = bet1*1
                        if wl > wl7:
                            bet8 = bet1*1
                        if wl1 > wl and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl1 > wl and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl1 > wl and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl1 > wl and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl1 > wl and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl1 > wl and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl1 > wl and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl1 > wl and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl2 > wl and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl2 > wl and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl2 > wl and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl2 > wl and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl2 > wl and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl2 > wl and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl2 > wl and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl2 > wl and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl3 > wl and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl3 > wl and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl3 > wl and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl3 > wl and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl3 > wl and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl3 > wl and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl3 > wl and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl3 > wl and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl4 > wl and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl4 > wl and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl4 > wl and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl4 > wl and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl4 > wl and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl4 > wl and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl4 > wl and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl4 > wl and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl5 > wl and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl5 > wl and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl5 > wl and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl5 > wl and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl5 > wl and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl5 > wl and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl5 > wl and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl5 > wl and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl6 > wl and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl6 > wl and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl6 > wl and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl6 > wl and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl6 > wl and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl6 > wl and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl7 > wl and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl7 > wl and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl7 > wl and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl7 > wl and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl7 > wl and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl7 > wl and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl7 > wl and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl7 > wl and y140 == 0:
                            bet8 = bet1/140*-145

                    elif by1 == 8 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        wl8 = bar1.count(bs2[7])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0    
                        if wl > wl1:
                            bet2 = bet1*1
                        if wl > wl2:
                            bet3 = bet1*1
                        if wl > wl3:
                            bet4 = bet1*1
                        if wl > wl4:
                            bet5 = bet1*1
                        if wl > wl5:
                            bet6 = bet1*1
                        if wl > wl6:
                            bet7 = bet1*1
                        if wl > wl7:
                            bet8 = bet1*1
                        if wl > wl8:
                            bet9 = bet1*1
                        if wl1 > wl and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl1 > wl and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl1 > wl and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl1 > wl and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl1 > wl and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl1 > wl and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl1 > wl and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl1 > wl and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl2 > wl and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl2 > wl and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl2 > wl and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl2 > wl and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl2 > wl and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl2 > wl and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl2 > wl and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl2 > wl and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl3 > wl and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl3 > wl and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl3 > wl and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl3 > wl and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl3 > wl and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl3 > wl and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl3 > wl and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl3 > wl and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl4 > wl and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl4 > wl and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl4 > wl and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl4 > wl and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl4 > wl and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl4 > wl and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl4 > wl and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl4 > wl and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl5 > wl and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl5 > wl and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl5 > wl and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl5 > wl and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl5 > wl and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl5 > wl and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl5 > wl and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl5 > wl and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl6 > wl and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl6 > wl and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl6 > wl and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl6 > wl and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl6 > wl and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl6 > wl and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl7 > wl and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl7 > wl and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl7 > wl and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl7 > wl and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl7 > wl and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl7 > wl and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl7 > wl and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl7 > wl and y140 == 0:
                            bet8 = bet1/140*-145
                        if wl8 > wl and y12000 == 0:
                            bet9 = bet1/12000*-12500
                        elif wl8 > wl and y1000 == 0:
                            bet9 = bet1/1000*-1050
                        elif wl8 > wl and bet1 == 600:
                            bet9 = bet1/600*-630
                        elif wl8 > wl and y480 == 0:
                            bet9 = bet1/120*-125
                        elif wl8 > wl and y580 == 0:
                            bet9 = (((bet1-480)/100*-105)-500)
                        elif wl8 > wl and y340 == 0:
                            bet9 = (((bet1-240)/100*-105)-250)
                        elif wl8 > wl and y100 == 0:
                            bet9 = bet1/100*-105
                        elif wl8 > wl and y140 == 0:
                            bet9 = bet1/140*-145

                    elif by1 == 9 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        wl8 = bar1.count(bs2[7])
                        wl9 = bar1.count(bs2[8])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0    
                        if wl > wl1:
                            bet2 = bet1*1
                        if wl > wl2:
                            bet3 = bet1*1
                        if wl > wl3:
                            bet4 = bet1*1
                        if wl > wl4:
                            bet5 = bet1*1
                        if wl > wl5:
                            bet6 = bet1*1
                        if wl > wl6:
                            bet7 = bet1*1
                        if wl > wl7:
                            bet8 = bet1*1
                        if wl > wl8:
                            bet9 = bet1*1
                        if wl > wl9:
                            bet10 = bet1*1
                        if wl1 > wl and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl1 > wl and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl1 > wl and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl1 > wl and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl1 > wl and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl1 > wl and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl1 > wl and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl1 > wl and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl2 > wl and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl2 > wl and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl2 > wl and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl2 > wl and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl2 > wl and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl2 > wl and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl2 > wl and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl2 > wl and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl3 > wl and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl3 > wl and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl3 > wl and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl3 > wl and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl3 > wl and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl3 > wl and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl3 > wl and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl3 > wl and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl4 > wl and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl4 > wl and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl4 > wl and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl4 > wl and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl4 > wl and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl4 > wl and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl4 > wl and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl4 > wl and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl5 > wl and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl5 > wl and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl5 > wl and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl5 > wl and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl5 > wl and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl5 > wl and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl5 > wl and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl5 > wl and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl6 > wl and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl6 > wl and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl6 > wl and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl6 > wl and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl6 > wl and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl6 > wl and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl7 > wl and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl7 > wl and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl7 > wl and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl7 > wl and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl7 > wl and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl7 > wl and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl7 > wl and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl7 > wl and y140 == 0:
                            bet8 = bet1/140*-145
                        if wl8 > wl and y12000 == 0:
                            bet9 = bet1/12000*-12500
                        elif wl8 > wl and y1000 == 0:
                            bet9 = bet1/1000*-1050
                        elif wl8 > wl and bet1 == 600:
                            bet9 = bet1/600*-630
                        elif wl8 > wl and y480 == 0:
                            bet9 = bet1/120*-125
                        elif wl8 > wl and y580 == 0:
                            bet9 = (((bet1-480)/100*-105)-500)
                        elif wl8 > wl and y340 == 0:
                            bet9 = (((bet1-240)/100*-105)-250)
                        elif wl8 > wl and y100 == 0:
                            bet9 = bet1/100*-105
                        elif wl8 > wl and y140 == 0:
                            bet9 = bet1/140*-145
                        if wl9 > wl and y12000 == 0:
                            bet10 = bet1/12000*-12500
                        elif wl9 > wl and y1000 == 0:
                            bet10 = bet1/1000*-1050
                        elif wl9 > wl and bet1 == 600:
                            bet10 = bet1/600*-630
                        elif wl9 > wl and y480 == 0:
                            bet10 = bet1/120*-125
                        elif wl9 > wl and y580 == 0:
                            bet10 = (((bet1-480)/100*-105)-500)
                        elif wl9 > wl and y340 == 0:
                            bet10 = (((bet1-240)/100*-105)-250)
                        elif wl9 > wl and y100 == 0:
                            bet10 = bet1/100*-105
                        elif wl9 > wl and y140 == 0:
                            bet10 = bet1/140*-145

                    elif by1 == 10 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        wl8 = bar1.count(bs2[7])
                        wl9 = bar1.count(bs2[8])
                        wl10 = bar1.count(bs2[9])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        cvt = 0    
                        if wl > wl1:
                            bet2 = bet1*1
                        if wl > wl2:
                            bet3 = bet1*1
                        if wl > wl3:
                            bet4 = bet1*1
                        if wl > wl4:
                            bet5 = bet1*1
                        if wl > wl5:
                            bet6 = bet1*1
                        if wl > wl6:
                            bet7 = bet1*1
                        if wl > wl7:
                            bet8 = bet1*1
                        if wl > wl8:
                            bet9 = bet1*1
                        if wl > wl9:
                            bet10 = bet1*1
                        if wl > wl10:
                            bet11 = bet1*1
                        if wl1 > wl and y12000 == 0:
                            bet2 = bet1/12000*-12500
                        elif wl1 > wl and y1000 == 0:
                            bet2 = bet1/1000*-1050
                        elif wl1 > wl and bet1 == 600:
                            bet2 = bet1/600*-630
                        elif wl1 > wl and y480 == 0:
                            bet2 = bet1/120*-125
                        elif wl1 > wl and y580 == 0:
                            bet2 = (((bet1-480)/100*-105)-500)
                        elif wl1 > wl and y340 == 0:
                            bet2 = (((bet1-240)/100*-105)-250)
                        elif wl1 > wl and y100 == 0:
                            bet2 = bet1/100*-105
                        elif wl1 > wl and y140 == 0:
                            bet2 = bet1/140*-145
                        if wl2 > wl and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl2 > wl and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl2 > wl and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl2 > wl and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl2 > wl and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl2 > wl and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl2 > wl and y100 == 0:
                            bet3 = bet1/100*-105
                        elif wl2 > wl and y140 == 0:
                            bet3 = bet1/140*-145
                        if wl3 > wl and y12000 == 0:
                            bet4 = bet1/12000*-12500
                        elif wl3 > wl and y1000 == 0:
                            bet4 = bet1/1000*-1050
                        elif wl3 > wl and bet1 == 600:
                            bet4 = bet1/600*-630
                        elif wl3 > wl and y480 == 0:
                            bet4 = bet1/120*-125
                        elif wl3 > wl and y580 == 0:
                            bet4 = (((bet1-480)/100*-105)-500)
                        elif wl3 > wl and y340 == 0:
                            bet4 = (((bet1-240)/100*-105)-250)
                        elif wl3 > wl and y100 == 0:
                            bet4 = bet1/100*-105
                        elif wl3 > wl and y140 == 0:
                            bet4 = bet1/140*-145
                        if wl4 > wl and y12000 == 0:
                            bet5 = bet1/12000*-12500
                        elif wl4 > wl and y1000 == 0:
                            bet5 = bet1/1000*-1050
                        elif wl4 > wl and bet1 == 600:
                            bet5 = bet1/600*-630
                        elif wl4 > wl and y480 == 0:
                            bet5 = bet1/120*-125
                        elif wl4 > wl and y580 == 0:
                            bet5 = (((bet1-480)/100*-105)-500)
                        elif wl4 > wl and y340 == 0:
                            bet5 = (((bet1-240)/100*-105)-250)
                        elif wl4 > wl and y100 == 0:
                            bet5 = bet1/100*-105
                        elif wl4 > wl and y140 == 0:
                            bet5 = bet1/140*-145
                        if wl5 > wl and y12000 == 0:
                            bet6 = bet1/12000*-12500
                        elif wl5 > wl and y1000 == 0:
                            bet6 = bet1/1000*-1050
                        elif wl5 > wl and bet1 == 600:
                            bet6 = bet1/600*-630
                        elif wl5 > wl and y480 == 0:
                            bet6 = bet1/120*-125
                        elif wl5 > wl and y580 == 0:
                            bet6 = (((bet1-480)/100*-105)-500)
                        elif wl5 > wl and y340 == 0:
                            bet6 = (((bet1-240)/100*-105)-250)
                        elif wl5 > wl and y100 == 0:
                            bet6 = bet1/100*-105
                        elif wl5 > wl and y140 == 0:
                            bet6 = bet1/140*-145
                        if wl6 > wl and y12000 == 0:
                            bet7 = bet1/12000*-12500
                        elif wl6 > wl and y1000 == 0:
                            bet7 = bet1/1000*-1050
                        elif wl6 > wl and bet1 == 600:
                            bet7 = bet1/600*-630
                        elif wl6 > wl and y480 == 0:
                            bet7 = bet1/120*-125
                        elif wl6 > wl and y580 == 0:
                            bet7 = (((bet1-480)/100*-105)-500)
                        elif wl6 > wl and y340 == 0:
                            bet7 = (((bet1-240)/100*-105)-250)
                        elif wl6 > wl and y100 == 0:
                            bet7 = bet1/100*-105
                        elif wl6 > wl and y140 == 0:
                            bet7 = bet1/140*-145
                        if wl7 > wl and y12000 == 0:
                            bet8 = bet1/12000*-12500
                        elif wl7 > wl and y1000 == 0:
                            bet8 = bet1/1000*-1050
                        elif wl7 > wl and bet1 == 600:
                            bet8 = bet1/600*-630
                        elif wl7 > wl and y480 == 0:
                            bet8 = bet1/120*-125
                        elif wl7 > wl and y580 == 0:
                            bet8 = (((bet1-480)/100*-105)-500)
                        elif wl7 > wl and y340 == 0:
                            bet8 = (((bet1-240)/100*-105)-250)
                        elif wl7 > wl and y100 == 0:
                            bet8 = bet1/100*-105
                        elif wl7 > wl and y140 == 0:
                            bet8 = bet1/140*-145
                        if wl8 > wl and y12000 == 0:
                            bet9 = bet1/12000*-12500
                        elif wl8 > wl and y1000 == 0:
                            bet9 = bet1/1000*-1050
                        elif wl8 > wl and bet1 == 600:
                            bet9 = bet1/600*-630
                        elif wl8 > wl and y480 == 0:
                            bet9 = bet1/120*-125
                        elif wl8 > wl and y580 == 0:
                            bet9 = (((bet1-480)/100*-105)-500)
                        elif wl8 > wl and y340 == 0:
                            bet9 = (((bet1-240)/100*-105)-250)
                        elif wl8 > wl and y100 == 0:
                            bet9 = bet1/100*-105
                        elif wl8 > wl and y140 == 0:
                            bet9 = bet1/140*-145
                        if wl9 > wl and y12000 == 0:
                            bet10 = bet1/12000*-12500
                        elif wl9 > wl and y1000 == 0:
                            bet10 = bet1/1000*-1050
                        elif wl9 > wl and bet1 == 600:
                            bet10 = bet1/600*-630
                        elif wl9 > wl and y480 == 0:
                            bet10 = bet1/120*-125
                        elif wl9 > wl and y580 == 0:
                            bet10 = (((bet1-480)/100*-105)-500)
                        elif wl9 > wl and y340 == 0:
                            bet10 = (((bet1-240)/100*-105)-250)
                        elif wl9 > wl and y100 == 0:
                            bet10 = bet1/100*-105
                        elif wl9 > wl and y140 == 0:
                            bet10 = bet1/140*-145
                        if wl10 > wl and y12000 == 0:
                            bet11 = bet1/12000*-12500
                        elif wl10 > wl and y1000 == 0:
                            bet11 = bet1/1000*-1050
                        elif wl10 > wl and bet1 == 600:
                            bet11 = bet1/600*-630
                        elif wl10 > wl and y480 == 0:
                            bet11 = bet1/120*-125
                        elif wl10 > wl and y580 == 0:
                            bet11 = (((bet1-480)/100*-105)-500)
                        elif wl10 > wl and y340 == 0:
                            bet11 = (((bet1-240)/100*-105)-250)
                        elif wl10 > wl and y100 == 0:
                            bet11 = bet1/100*-105
                        elif wl10 > wl and y140 == 0:
                            bet11 = bet1/140*-145


                    elif by1 == 2 and yy1 == 2:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bss1 = int(bss[0])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            y100 = bss1 % 100
                            y1000 = bss1 % 1000
                            y12000 = bss1 % 12000
                            y580 = (bss1-480) % 100
                            y340 = (bss1-240) % 100
                            y140 = (bss1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            cvt = wl16-wl6
                            ys = wl6
                            ys1 = bar1[0] == bar1[1]
                            ys2 = bar1[0] == bar1[2]
                            y20 = bss2 % 20
                            ys1000 = bss2 % 1000
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = bss1*1
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y12000 == 0:
                                bet4 = bss1/12000*-12500
                            elif wl6 > wl16 and y1000 == 0:
                                bet4 = bss1/1000*-1050
                            elif wl6 > wl16 and bss1 == 600:
                                bet4 = bss1/600*-630
                            elif wl6 > wl16 and y480 == 0:
                                bet4 = bss1/120*-125
                            elif wl6 > wl16 and y580 == 0:
                                bet4 = (((bss1-480)/100*-105)-500)
                            elif wl6 > wl16 and y340 == 0:
                                bet4 = (((bss1-240)/100*-105)-250)
                            elif wl6 > wl16 and y100 == 0: 
                                bet4 = bss1/100*-105
                            elif wl6 > wl16 and y140 == 0:
                                bet4 = bss1/140*-145
                            if ys >= 2:
                                if ys1000 == 0:
                                    bet14 = bss2/1000*-6300
                                elif bss2 == 500:
                                    bet14 = bss2/500*-3150
                                elif y20 == 0:
                                    bet14 = bss2/20*-125
                                elif bss2 == 30:
                                    bet14 = bss2/30*-190
                                elif bss2 == 50:
                                    bet14 = bss2/50*-315
                            elif ys == 0 and ys2 is True:
                                bet14 = bss2*3
                            elif ys == 0 and ys1 is True:
                                bet14 = bss2*5
                            elif ys == 0 and ys1 is False:
                                bet14 = bss2*6
                            
                        elif "-" not in bs[1]:
                            bet1 = int(bs[1])
                            y480 = bet1 % 120
                            y100 = bet1 % 100
                            y1000 = bet1 % 1000
                            y12000 = bet1 % 12000
                            y580 = (bet1-480) % 100
                            y340 = (bet1-240) % 100
                            y140 = (bet1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            cvt = wl16-wl6
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = bet1*1
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y12000 == 0:
                                bet5 = bet1/12000*-12500
                            elif wl6 > wl16 and y1000 == 0:
                                bet5 = bet1/1000*-1050
                            elif wl6 > wl16 and bet1 == 600:
                                bet5 = bet1/600*-630
                            elif wl6 > wl16 and y480 == 0:
                                bet5 = bet1/120*-125
                            elif wl6 > wl16 and y580 == 0:
                                bet5 = (((bet1-480)/100*-105)-500)
                            elif wl6 > wl16 and y340 == 0:
                                bet5 = (((bet1-240)/100*-105)-250)
                            elif wl6 > wl16 and y100 == 0: 
                                bet5 = bet1/100*-105
                            elif wl6 > wl6 and y140 == 0:
                                bet5 = bet1/140*-145

                    elif by1 == 2 and yy1 == 4:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bss1 = int(bss[0])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            y100 = bss1 % 100
                            y1000 = bss1 % 1000
                            y12000 = bss1 % 12000
                            y580 = (bss1-480) % 100
                            y340 = (bss1-240) % 100
                            y140 = (bss1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            wl17 = int(wl4)+int(wl5)
                            cvt = wl17-wl6
                            ys = wl6
                            ys1 = bar1[0] == bar1[1]
                            ys2 = bar1[0] == bar1[2]
                            y20 = bss2 % 20
                            ys1000 = bss2 % 1000
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = bss1*1
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y12000 == 0:
                                bet3 = bss1/12000*-12500
                            elif wl6 > wl16 and y1000 == 0:
                                bet3 = bss1/1000*-1050
                            elif wl6 > wl16 and bss1 == 600:
                                bet3 = bss1/600*-630
                            elif wl6 > wl16 and y480 == 0:
                                bet3 = bss1/120*-125
                            elif wl6 > wl16 and y580 == 0:
                                bet3 = (((bss1-480)/100*-105)-500)
                            elif wl6 > wl16 and y340 == 0:
                                bet3 = (((bss1-240)/100*-105)-250)
                            elif wl6 > wl16 and y100 == 0: 
                                bet3 = bss1/100*-105
                            elif wl6 > wl16 and y140 == 0:
                                bet3 = bss1/140*-145
                            if wl17 > wl6:
                                bet4 = bss1*1
                            if wl6 > wl17 and y12000 == 0:
                                bet5 = bss1/12000*-12500
                            elif wl6 > wl17 and y1000 == 0:
                                bet5 = bss1/1000*-1050
                            elif wl6 > wl17 and bss1 == 600:
                                bet5 = bss1/600*-630
                            elif wl6 > wl17 and y480 == 0:
                                bet5 = bss1/120*-125
                            elif wl6 > wl17 and y580 == 0:
                                bet5 = (((bss1-480)/100*-105)-500)
                            elif wl6 > wl17 and y340 == 0:
                                bet5 = (((bss1-240)/100*-105)-250)
                            elif wl6 > wl17 and y100 == 0: 
                                bet5 = bss1/100*-105
                            elif wl6 > wl17 and y140 == 0:
                                bet5 = bss1/140*-145
                            if ys >= 2:
                                if ys1000 == 0:
                                    bet14 = bss2/1000*-6300
                                elif bss2 == 500:
                                    bet14 = bss2/500*-3150
                                elif y20 == 0:
                                    bet14 = bss2/20*-125
                                elif bss2 == 30:
                                    bet14 = bss2/30*-190
                                elif bss2 == 50:
                                    bet14 = bss2/50*-315
                            elif ys == 0 and ys2 is True:
                                bet14 = bss2*3
                            elif ys == 0 and ys1 is True:
                                bet14 = bss2*5
                            elif ys == 0 and ys1 is False:
                                bet14 = bss2*6
                            
                        elif "-" not in bs[1]:
                            bet1 = int(bs[1])
                            y480 = bet1 % 120
                            y100 = bet1 % 100
                            y1000 = bet1 % 1000
                            y12000 = bet1 % 12000
                            y580 = (bet1-480) % 100
                            y340 = (bet1-240) % 100
                            y140 = (bet1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            wl17 = int(wl4)+int(wl5)
                            cvt = wl17-wl6
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = bet1*1
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y12000 == 0:
                                bet3 = bet1/12000*-12500
                            elif wl6 > wl16 and y1000 == 0:
                                bet3 = bet1/1000*-1050
                            elif wl6 > wl16 and bet1 == 600:
                                bet3 = bet1/600*-630
                            elif wl6 > wl16 and y480 == 0:
                                bet3 = bet1/120*-125
                            elif wl6 > wl16 and y580 == 0:
                                bet3 = (((bet1-480)/100*-105)-500)
                            elif wl6 > wl16 and y340 == 0:
                                bet3 = (((bet1-240)/100*-105)-250)
                            elif wl6 > wl16 and y100 == 0: 
                                bet3 = bet1/100*-105
                            elif wl6 > wl16 and y140 == 0:
                                bet3 = bet1/140*-145
                            if wl17 > wl6:
                                bet4 = bet1*1
                            if wl6 > wl17 and y12000 == 0:
                                bet5 = bet1/12000*-12500
                            elif wl6 > wl17 and y1000 == 0:
                                bet5 = bet1/1000*-1050
                            elif wl6 > wl17 and bet1 == 600:
                                bet5 = bet1/600*-630
                            elif wl6 > wl17 and y480 == 0:
                                bet5 = bet1/120*-125
                            elif wl6 > wl17 and y580 == 0:
                                bet5 = (((bet1-480)/100*-105)-500)
                            elif wl6 > wl17 and y340 == 0:
                                bet5 = (((bet1-240)/100*-105)-250)
                            elif wl6 > wl17 and y100 == 0: 
                                bet5 = bet1/100*-105
                            elif wl6 > wl17 and y140 == 0:
                                bet5 = bet1/140*-145

                    elif by1 == 2 and yy1 == 5:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bss1 = int(bss[0])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            y100 = bss1 % 100
                            y1000 = bss1 % 1000
                            y12000 = bss1 % 12000
                            y580 = (bss1-480) % 100
                            y340 = (bss1-240) % 100
                            y140 = (bss1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = bar1.count(bs3[4])
                            if int(bs3[2]) > int(bs3[0]) and int(bs3[2]) > int(bs3[1]):
                                wl7 = int(wl)+int(wl1) 
                                wl16 = int(wl2)+int(wl3) 
                                wl17 = int(wl2)+int(wl4) 
                                wl18 = int(wl3)+int(wl4) 
                                wl19 = int(wl5)+int(wl6) 
                                cvt = 0
                                ys = wl7
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl16 > wl7:
                                    bet2 = bss1*1
                                if wl7 > wl16 and y12000 == 0:
                                    bet3 = bss1/12000*-12500
                                elif wl7 > wl16 and y1000 == 0:
                                    bet3 = bss1/1000*-1050
                                elif wl7 > wl16 and bss1 == 600:
                                    bet3 = bss1/600*-630
                                elif wl7 > wl16 and y480 == 0:
                                    bet3 = bss1/120*-125
                                elif wl7 > wl16 and y580 == 0:
                                    bet3 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl16 and y340 == 0:
                                    bet3 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl16 and y100 == 0: 
                                    bet3 = bss1/100*-105
                                elif wl7 > wl16 and y140 == 0:
                                    bet3 = bss1/140*-145
                                if wl17 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl17 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl17 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl17 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl17 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl17 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl17 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl17 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl7 > wl17 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl18 > wl7:
                                    bet6 = bss1*1
                                if wl7 > wl18 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl7 > wl18 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl7 > wl18 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl7 > wl18 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl7 > wl18 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl18 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl18 and y100 == 0: 
                                    bet7 = bss1/100*-105
                                elif wl7 > wl18 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl19 > wl7:
                                    bet8 = bss1*1
                                if wl7 > wl19 and y12000 == 0:
                                    bet9 = bss1/12000*-12500
                                elif wl7 > wl19 and y1000 == 0:
                                    bet9 = bss1/1000*-1050
                                elif wl7 > wl19 and bss1 == 600:
                                    bet9 = bss1/600*-630
                                elif wl7 > wl19 and y480 == 0:
                                    bet9 = bss1/120*-125
                                elif wl7 > wl19 and y580 == 0:
                                    bet9 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl19 and y340 == 0:
                                    bet9 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl19 and y100 == 0: 
                                    bet9 = bss1/100*-105
                                elif wl7 > wl19 and y140 == 0:
                                    bet9 = bss1/140*-145
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6

                            else:
                                wl7 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3)
                                wl17 = int(wl4)+int(wl5)
                                wl18 = int(wl4)+int(wl6)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                ys = wl7
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl16 > wl7:
                                    bet2 = bss1*1
                                if wl7 > wl16 and y12000 == 0:
                                    bet3 = bss1/12000*-12500
                                elif wl7 > wl16 and y1000 == 0:
                                    bet3 = bss1/1000*-1050
                                elif wl7 > wl16 and bss1 == 600:
                                    bet3 = bss1/600*-630
                                elif wl7 > wl16 and y480 == 0:
                                    bet3 = bss1/120*-125
                                elif wl7 > wl16 and y580 == 0:
                                    bet3 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl16 and y340 == 0:
                                    bet3 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl16 and y100 == 0: 
                                    bet3 = bss1/100*-105
                                elif wl7 > wl16 and y140 == 0:
                                    bet3 = bss1/140*-145
                                if wl17 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl17 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl17 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl17 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl17 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl17 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl17 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl17 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl7 > wl17 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl18 > wl7:
                                    bet6 = bss1*1
                                if wl7 > wl18 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl7 > wl18 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl7 > wl18 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl7 > wl18 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl7 > wl18 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl18 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl18 and y100 == 0: 
                                    bet7 = bss1/100*-105
                                elif wl7 > wl18 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl19 > wl7:
                                    bet8 = bss1*1
                                if wl7 > wl19 and y12000 == 0:
                                    bet9 = bss1/12000*-12500
                                elif wl7 > wl19 and y1000 == 0:
                                    bet9 = bss1/1000*-1050
                                elif wl7 > wl19 and bss1 == 600:
                                    bet9 = bss1/600*-630
                                elif wl7 > wl19 and y480 == 0:
                                    bet9 = bss1/120*-125
                                elif wl7 > wl19 and y580 == 0:
                                    bet9 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl19 and y340 == 0:
                                    bet9 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl19 and y100 == 0: 
                                    bet9 = bss1/100*-105
                                elif wl7 > wl19 and y140 == 0:
                                    bet9 = bss1/140*-145
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                                
                        elif "-" not in bs[1]:
                            bss1 = int(bs[1])
                            y480 = bss1 % 120
                            y100 = bss1 % 100
                            y1000 = bss1 % 1000
                            y12000 = bss1 % 12000
                            y580 = (bss1-480) % 100
                            y340 = (bss1-240) % 100
                            y140 = (bss1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = bar1.count(bs3[4])
                            if int(bs3[2]) > int(bs3[0]) and int(bs3[2]) > int(bs3[1]):
                                wl7 = int(wl)+int(wl1) 
                                wl16 = int(wl2)+int(wl3) 
                                wl17 = int(wl2)+int(wl4) 
                                wl18 = int(wl3)+int(wl4) 
                                wl19 = int(wl5)+int(wl6) 
                                cvt = 0
                                if wl16 > wl7:
                                    bet2 = bss1*1
                                if wl7 > wl16 and y12000 == 0:
                                    bet3 = bss1/12000*-12500
                                elif wl7 > wl16 and y1000 == 0:
                                    bet3 = bss1/1000*-1050
                                elif wl7 > wl16 and bss1 == 600:
                                    bet3 = bss1/600*-630
                                elif wl7 > wl16 and y480 == 0:
                                    bet3 = bss1/120*-125
                                elif wl7 > wl16 and y580 == 0:
                                    bet3 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl16 and y340 == 0:
                                    bet3 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl16 and y100 == 0: 
                                    bet3 = bss1/100*-105
                                elif wl7 > wl16 and y140 == 0:
                                    bet3 = bss1/140*-145
                                if wl17 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl17 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl17 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl17 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl17 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl17 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl17 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl17 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl7 > wl17 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl18 > wl7:
                                    bet6 = bss1*1
                                if wl7 > wl18 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl7 > wl18 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl7 > wl18 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl7 > wl18 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl7 > wl18 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl18 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl18 and y100 == 0: 
                                    bet7 = bss1/100*-105
                                elif wl7 > wl18 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl19 > wl7:
                                    bet8 = bss1*1
                                if wl7 > wl19 and y12000 == 0:
                                    bet9 = bss1/12000*-12500
                                elif wl7 > wl19 and y1000 == 0:
                                    bet9 = bss1/1000*-1050
                                elif wl7 > wl19 and bss1 == 600:
                                    bet9 = bss1/600*-630
                                elif wl7 > wl19 and y480 == 0:
                                    bet9 = bss1/120*-125
                                elif wl7 > wl19 and y580 == 0:
                                    bet9 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl19 and y340 == 0:
                                    bet9 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl19 and y100 == 0: 
                                    bet9 = bss1/100*-105
                                elif wl7 > wl19 and y140 == 0:
                                    bet9 = bss1/140*-145

                            else:
                                wl7 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3)
                                wl17 = int(wl4)+int(wl5)
                                wl18 = int(wl4)+int(wl6)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                if wl16 > wl7:
                                    bet2 = bss1*1
                                if wl7 > wl16 and y12000 == 0:
                                    bet3 = bss1/12000*-12500
                                elif wl7 > wl16 and y1000 == 0:
                                    bet3 = bss1/1000*-1050
                                elif wl7 > wl16 and bss1 == 600:
                                    bet3 = bss1/600*-630
                                elif wl7 > wl16 and y480 == 0:
                                    bet3 = bss1/120*-125
                                elif wl7 > wl16 and y580 == 0:
                                    bet3 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl16 and y340 == 0:
                                    bet3 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl16 and y100 == 0: 
                                    bet3 = bss1/100*-105
                                elif wl7 > wl16 and y140 == 0:
                                    bet3 = bss1/140*-145
                                if wl17 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl17 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl17 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl17 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl17 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl17 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl17 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl17 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl7 > wl17 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl18 > wl7:
                                    bet6 = bss1*1
                                if wl7 > wl18 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl7 > wl18 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl7 > wl18 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl7 > wl18 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl7 > wl18 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl18 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl18 and y100 == 0: 
                                    bet7 = bss1/100*-105
                                elif wl7 > wl18 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl19 > wl7:
                                    bet8 = bss1*1
                                if wl7 > wl19 and y12000 == 0:
                                    bet9 = bss1/12000*-12500
                                elif wl7 > wl19 and y1000 == 0:
                                    bet9 = bss1/1000*-1050
                                elif wl7 > wl19 and bss1 == 600:
                                    bet9 = bss1/600*-630
                                elif wl7 > wl19 and y480 == 0:
                                    bet9 = bss1/120*-125
                                elif wl7 > wl19 and y580 == 0:
                                    bet9 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl19 and y340 == 0:
                                    bet9 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl19 and y100 == 0: 
                                    bet9 = bss1/100*-105
                                elif wl7 > wl19 and y140 == 0:
                                    bet9 = bss1/140*-145


                    elif by1 == 5 and yy1 == 2:
                        if "-" not in bs[1]:
                            bss1 = int(bs[1])
                            y480 = bss1 % 120
                            y100 = bss1 % 100
                            y1000 = bss1 % 1000
                            y12000 = bss1 % 12000
                            y580 = (bss1-480) % 100
                            y340 = (bss1-240) % 100
                            y140 = (bss1-140)
                            wl = bar1.count(bs2[0])  
                            wl1 = bar1.count(bs2[1]) 
                            wl2 = bar1.count(bs2[2]) 
                            wl3 = bar1.count(bs2[3]) 
                            wl4 = bar1.count(bs2[4]) 
                            wl5 = bar1.count(bs3[0]) 
                            wl6 = bar1.count(bs3[1]) 
                            if int(bs2[2]) > int(bs2[0]) and int(bs2[2]) > int(bs2[1]):
                                wl10 = int(wl)+int(wl1)
                                wl7 = int(wl)+int(wl2)
                                wl8 = int(wl1)+int(wl2)
                                wl9 = int(wl3)+int(wl4)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                if wl19 > wl10:
                                    bet2 = bss1*1
                                if wl10 > wl19 and y12000 == 0:
                                    bet3 = bss1/12000*-12500
                                elif wl10 > wl19 and y1000 == 0:
                                    bet3 = bss1/1000*-1050
                                elif wl10 > wl19 and bss1 == 600:
                                    bet3 = bss1/600*-630
                                elif wl10 > wl19 and y480 == 0:
                                    bet3 = bss1/120*-125
                                elif wl10 > wl19 and y580 == 0:
                                    bet3 = (((bss1-480)/100*-105)-500)
                                elif wl10 > wl19 and y340 == 0:
                                    bet3 = (((bss1-240)/100*-105)-250)
                                elif wl10 > wl19 and y100 == 0: 
                                    bet3 = bss1/100*-105
                                elif wl10 > wl19 and y140 == 0:
                                    bet3 = bss1/140*-145
                                if wl19 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl19 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl19 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl19 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl19 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl19 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl19 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl19 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl7 > wl19 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl19 > wl8:
                                    bet6 = bss1*1
                                if wl8 > wl19 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl8 > wl19 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl8 > wl19 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl8 > wl19 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl8 > wl19 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl8 > wl19 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl8 > wl19 and y100 == 0: 
                                    bet7 = bss1/100*-105
                                elif wl8 > wl19 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl19 > wl9:
                                    bet8 = bss1*1
                                if wl9 > wl19 and y12000 == 0:
                                    bet9 = bss1/12000*-12500
                                elif wl9 > wl19 and y1000 == 0:
                                    bet9 = bss1/1000*-1050
                                elif wl9 > wl19 and bss1 == 600:
                                    bet9 = bss1/600*-630
                                elif wl9 > wl19 and y480 == 0:
                                    bet9 = bss1/120*-125
                                elif wl9 > wl19 and y580 == 0:
                                    bet9 = (((bss1-480)/100*-105)-500)
                                elif wl9 > wl19 and y340 == 0:
                                    bet9 = (((bss1-240)/100*-105)-250)
                                elif wl9 > wl19 and y100 == 0: 
                                    bet9 = bss1/100*-105
                                elif wl9 > wl19 and y140 == 0:
                                    bet9 = bss1/140*-145

                            else:
                                wl10 = int(wl)+int(wl1)
                                wl7 = int(wl2)+int(wl3)
                                wl8 = int(wl2)+int(wl4)
                                wl9 = int(wl3)+int(wl4)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                if wl19 > wl10:
                                    bet2 = bss1*1
                                if wl10 > wl19 and y12000 == 0:
                                    bet3 = bss1/12000*-12500
                                elif wl10 > wl19 and y1000 == 0:
                                    bet3 = bss1/1000*-1050
                                elif wl10 > wl19 and bss1 == 600:
                                    bet3 = bss1/600*-630
                                elif wl10 > wl19 and y480 == 0:
                                    bet3 = bss1/120*-125
                                elif wl10 > wl19 and y580 == 0:
                                    bet3 = (((bss1-480)/100*-105)-500)
                                elif wl10 > wl19 and y340 == 0:
                                    bet3 = (((bss1-240)/100*-105)-250)
                                elif wl10 > wl19 and y100 == 0: 
                                    bet3 = bss1/100*-105
                                elif wl10 > wl19 and y140 == 0:
                                    bet3 = bss1/140*-145
                                if wl19 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl19 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl19 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl19 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl19 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl19 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl19 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl19 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl7 > wl19 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl19 > wl8:
                                    bet6 = bss1*1
                                if wl8 > wl19 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl8 > wl19 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl8 > wl19 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl8 > wl19 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl8 > wl19 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl8 > wl19 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl8 > wl19 and y100 == 0: 
                                    bet7 = bss1/100*-105
                                elif wl8 > wl19 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl19 > wl9:
                                    bet8 = bss1*1
                                if wl9 > wl19 and y12000 == 0:
                                    bet9 = bss1/12000*-12500
                                elif wl9 > wl19 and y1000 == 0:
                                    bet9 = bss1/1000*-1050
                                elif wl9 > wl19 and bss1 == 600:
                                    bet9 = bss1/600*-630
                                elif wl9 > wl19 and y480 == 0:
                                    bet9 = bss1/120*-125
                                elif wl9 > wl19 and y580 == 0:
                                    bet9 = (((bss1-480)/100*-105)-500)
                                elif wl9 > wl19 and y340 == 0:
                                    bet9 = (((bss1-240)/100*-105)-250)
                                elif wl9 > wl19 and y100 == 0: 
                                    bet9 = bss1/100*-105
                                elif wl9 > wl19 and y140 == 0:
                                    bet9 = bss1/140*-145

                    elif by1 == 4 and yy1 == 2:   
                        if "-" not in bs[1]:
                            bet1 = int(bs[1])
                            y480 = bet1 % 120
                            y100 = bet1 % 100
                            y1000 = bet1 % 1000
                            y12000 = bet1 % 12000
                            y580 = (bet1-480) % 100
                            y340 = (bet1-240) % 100
                            y140 = (bet1-140)
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs2[2])
                            wl3 = bar1.count(bs2[3])
                            wl4 = bar1.count(bs3[0])
                            wl5 = bar1.count(bs3[1])
                            wl6 = int(wl)+int(wl1)
                            wl7 = int(wl2)+int(wl3)
                            wl16 = int(wl4)+int(wl5)
                            cvt = wl16-wl7
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = bet1*1
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y12000 == 0:
                                bet3 = bet1/12000*-12500
                            elif wl6 > wl16 and y1000 == 0:
                                bet3 = bet1/1000*-1050
                            elif wl6 > wl16 and bet1 == 600:
                                bet3 = bet1/600*-630
                            elif wl6 > wl16 and y480 == 0:
                                bet3 = bet1/120*-125
                            elif wl6 > wl16 and y580 == 0:
                                bet3 = (((bet1-480)/100*-105)-500)
                            elif wl6 > wl16 and y340 == 0:
                                bet3 = (((bet1-240)/100*-105)-250)
                            elif wl6 > wl16 and y100 == 0: 
                                bet3 = bet1/100*-105
                            elif wl6 > wl16 and y140 == 0:
                                bet3 = bet1/140*-145
                            if wl16 > wl7:
                                bet4 = bet1*1
                            if wl7 > wl16 and y12000 == 0:
                                bet5 = bet1/12000*-12500
                            elif wl7 > wl16 and y1000 == 0:
                                bet5 = bet1/1000*-1050
                            elif wl7 > wl16 and bet1 == 600:
                                bet5 = bet1/600*-630
                            elif wl7 > wl16 and y480 == 0:
                                bet5 = bet1/120*-125
                            elif wl7 > wl16 and y580 == 0:
                                bet5 = (((bet1-480)/100*-105)-500)
                            elif wl7 > wl16 and y340 == 0:
                                bet5 = (((bet1-240)/100*-105)-250)
                            elif wl7 > wl16 and y100 == 0: 
                                bet5 = bet1/100*-105
                            elif wl7 > wl16 and y140 == 0:
                                bet5 = bet1/140*-145

                        elif "-" in bs[1]:
                            bet5 = 999999


                    elif by1 == 2 and yy1 == 3:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs3[0])
                        wl3 = bar1.count(bs3[1])
                        wl4 = bar1.count(bs3[2])
                        if bs3[2] != bs3[0] and bs3[2] != bs3[1]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bss1 = int(bss[0])
                                bss2 = int(bss[1])
                                y480 = bss1 % 120
                                y100 = bss1 % 100
                                y1000 = bss1 % 1000
                                y12000 = bss1 % 12000
                                y580 = (bss1-480) % 100
                                y340 = (bss1-240) % 100
                                y140 = (bss1-140)
                                wl6 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3) #12 13 23
                                wl17 = int(wl2)+int(wl4)
                                wl18 = int(wl3)+int(wl4)
                                cvt = (wl16+wl17+wl18)-3
                                ys = wl6
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl16 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet2 = bss1*1
                                    else:
                                        bet2 = 999999
                                if wl17 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet3 = bss1*1
                                    else:
                                        bet3 = 999999
                                if wl18 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet4 = bss1*1
                                    else:
                                        bet4 = 999999
                                if wl6 > wl16 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl6 > wl16 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl6 > wl16 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl6 > wl16 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl6 > wl16 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl16 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl16 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl6 > wl16 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl6 > wl17 and y12000 == 0:
                                    bet6 = bss1/12000*-12500
                                elif wl6 > wl17 and y1000 == 0:
                                    bet6 = bss1/1000*-1050
                                elif wl6 > wl17 and bss1 == 600:
                                    bet6 = bss1/600*-630
                                elif wl6 > wl17 and y480 == 0:
                                    bet6 = bss1/120*-125
                                elif wl6 > wl17 and y580 == 0:
                                    bet6 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl17 and y340 == 0:
                                    bet6 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl17 and y100 == 0: 
                                    bet6 = bss1/100*-105
                                elif wl6 > wl17 and y140 == 0:
                                    bet6 = bss1/140*-145
                                if wl6 > wl18 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl6 > wl18 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl6 > wl18 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl6 > wl18 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl6 > wl18 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl18 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl18 and y100 == 0: 
                                    bet7 = bss1/100*-105  
                                elif wl6 > wl18 and y140 == 0:
                                    bet7 = bss1/140*-145     
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                                        
                            elif "-" not in bs[1]:
                                bet1 = int(bs[1])
                                y480 = bet1 % 120
                                y100 = bet1 % 100
                                y1000 = bet1 % 1000
                                y12000 = bet1 % 12000
                                y580 = (bet1-480) % 100
                                y340 = (bet1-240) % 100
                                y140 = (bet1-140)
                                wl6 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3)
                                wl17 = int(wl2)+int(wl4)
                                wl18 = int(wl3)+int(wl4)
                                cvt = (wl16+wl17+wl18)-3
                                if wl16 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet2 = bet1*1
                                    else:
                                        bet2 = 999999
                                if wl17 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet3 = bet1*1
                                    else:
                                        bet3 = 999999
                                if wl18 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet4 = bet1*1
                                    else:
                                        bet4 = 999999
                                if wl6 > wl16 and y12000 == 0:
                                    bet5 = bet1/12000*-12500
                                elif wl6 > wl16 and y1000 == 0:
                                    bet5 = bet1/1000*-1050
                                elif wl6 > wl16 and bet1 == 600:
                                    bet5 = bet1/600*-630
                                elif wl6 > wl16 and y480 == 0:
                                    bet5 = bet1/120*-125
                                elif wl6 > wl16 and y580 == 0:
                                    bet5 = (((bet1-480)/100*-105)-500)
                                elif wl6 > wl16 and y340 == 0:
                                    bet5 = (((bet1-240)/100*-105)-250)
                                elif wl6 > wl16 and y100 == 0: 
                                    bet5 = bet1/100*-105
                                elif wl6 > wl16 and y140 == 0:
                                    bet5 = bet1/140*-145
                                if wl6 > wl17 and y12000 == 0:
                                    bet6 = bet1/12000*-12500
                                elif wl6 > wl17 and y1000 == 0:
                                    bet6 = bet1/1000*-1050
                                elif wl6 > wl17 and bet1 == 600:
                                    bet6 = bet1/600*-630
                                elif wl6 > wl17 and y480 == 0:
                                    bet6 = bet1/120*-125
                                elif wl6 > wl17 and y580 == 0:
                                    bet6 = (((bet1-480)/100*-105)-500)
                                elif wl6 > wl17 and y340 == 0:
                                    bet6 = (((bet1-240)/100*-105)-250)
                                elif wl6 > wl17 and y100 == 0: 
                                    bet6 = bet1/100*-105
                                elif wl6 > wl17 and y140 == 0:
                                    bet6 = bet1/140*-145
                                if wl6 > wl18 and y12000 == 0:
                                    bet7 = bet1/12000*-12500
                                elif wl6 > wl18 and y1000 == 0:
                                    bet7 = bet1/1000*-1050
                                elif wl6 > wl18 and bet1 == 600:
                                    bet7 = bet1/600*-630
                                elif wl6 > wl18 and y480 == 0:
                                    bet7 = bet1/120*-125
                                elif wl6 > wl18 and y580 == 0:
                                    bet7 = (((bet1-480)/100*-105)-500)
                                elif wl6 > wl18 and y340 == 0:
                                    bet7 = (((bet1-240)/100*-105)-250)
                                elif wl6 > wl18 and y100 == 0: 
                                    bet7 = bet1/100*-105    
                                elif wl6 > wl18 and y140 == 0:
                                    bet7 = bet1/140*-145

                        elif bs3[2] == bs3[0] or bs3[2] == bs3[1]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bss1 = int(bss[0])
                                bss2 = int(bss[1])
                                y480 = bss1 % 120
                                y100 = bss1 % 100
                                y1000 = bss1 % 1000
                                y12000 = bss1 % 12000
                                y580 = (bss1-480) % 100
                                y340 = (bss1-240) % 100
                                y140 = (bss1-140)
                                wl6 = int(wl)+int(wl1)    #12
                                wl7 = int(wl) #1
                                wl8 = int(wl1) #2
                                wl9 = int(wl2)+int(wl3)   #34
                                wl10 = int(wl4)   #3
                                cvt = wl8-wl6
                                ys = wl6
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl9 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet2 = bss1*1
                                    else:
                                        bet2 = 999999
                                if wl10 > wl7:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet3 = bss1*1
                                    else:
                                        bet3 = 999999
                                if wl10 > wl8:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet4 = bss1*1
                                    else:
                                        bet4 = 999999
                                if wl6 > wl9 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl6 > wl9 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl6 > wl9 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl6 > wl9 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl6 > wl9 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl9 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl9 and y100 == 0: 
                                    bet5 = bss1/100*-105
                                elif wl6 > wl9 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl7 > wl10 and y12000 == 0:
                                    bet6 = bss1/12000*-12500
                                elif wl7 > wl10 and y1000 == 0:
                                    bet6 = bss1/1000*-1050
                                elif wl7 > wl10 and bss1 == 600:
                                    bet6 = bss1/600*-630
                                elif wl7 > wl10 and y480 == 0:
                                    bet6 = bss1/120*-125
                                elif wl7 > wl10 and y580 == 0:
                                    bet6 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl10 and y340 == 0:
                                    bet6 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl10 and y100 == 0: 
                                    bet6 = bss1/100*-105
                                elif wl7 > wl10 and y140 == 0:
                                    bet6 = bss1/140*-145
                                if wl8 > wl10 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl8 > wl10 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl8 > wl10 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl8 > wl10 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl8 > wl10 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl8 > wl10 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl8 > wl10 and y100 == 0: 
                                    bet7 = bss1/100*-105   
                                elif wl8 > wl10 and y140 == 0:
                                    bet7 = bss1/140*-145    
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6

                            elif "-" not in bs[1]:
                                bet1 = int(bs[1])
                                y480 = bet1 % 120
                                y100 = bet1 % 100
                                y1000 = bet1 % 1000
                                y12000 = bet1 % 12000
                                y580 = (bet1-480) % 100
                                y340 = (bet1-240) % 100
                                y140 = (bet1-140)
                                wl6 = int(wl)+int(wl1)    #12
                                wl7 = int(wl) #1
                                wl8 = int(wl1) #2
                                wl9 = int(wl2)+int(wl3)   #34
                                wl10 = int(wl4)   #3
                                cvt = wl8-wl6
                                if wl9 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet2 = bet1*1
                                    else:
                                        bet2 = 999999
                                if wl10 > wl7:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet3 = bet1*1
                                    else:
                                        bet3 = 999999
                                if wl10 > wl8:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet4 = bet1*1
                                    else:
                                        bet4 = 999999
                                if wl6 > wl9 and y12000 == 0:
                                    bet5 = bet1/12000*-12500
                                elif wl6 > wl9 and y1000 == 0:
                                    bet5 = bet1/1000*-1050
                                elif wl6 > wl9 and bet1 == 600:
                                    bet5 = bet1/600*-630
                                elif wl6 > wl9 and y480 == 0:
                                    bet5 = bet1/120*-125
                                elif wl6 > wl9 and y580 == 0:
                                    bet5 = (((bet1-480)/100*-105)-500)
                                elif wl6 > wl9 and y340 == 0:
                                    bet5 = (((bet1-240)/100*-105)-250)
                                elif wl6 > wl9 and y100 == 0: 
                                    bet5 = bet1/100*-105
                                elif wl6 > wl9 and y140 == 0:
                                    bet5 = bet1/140*-145
                                if wl7 > wl10 and y12000 == 0:
                                    bet6 = bet1/12000*-12500
                                elif wl7 > wl10 and y1000 == 0:
                                    bet6 = bet1/1000*-1050
                                elif wl7 > wl10 and bet1 == 600:
                                    bet6 = bet1/600*-630
                                elif wl7 > wl10 and y480 == 0:
                                    bet6 = bet1/120*-125
                                elif wl7 > wl10 and y580 == 0:
                                    bet6 = (((bet1-480)/100*-105)-500)
                                elif wl7 > wl10 and y340 == 0:
                                    bet6 = (((bet1-240)/100*-105)-250)
                                elif wl7 > wl10 and y100 == 0: 
                                    bet6 = bet1/100*-105
                                elif wl7 > wl10 and y140 == 0:
                                    bet6 = bet1/140*-145
                                if wl8 > wl10 and y12000 == 0:
                                    bet7 = bet1/12000*-12500
                                elif wl8 > wl10 and y1000 == 0:
                                    bet7 = bet1/1000*-1050
                                elif wl8 > wl10 and bet1 == 600:
                                    bet7 = bet1/600*-630
                                elif wl8 > wl10 and y480 == 0:
                                    bet7 = bet1/120*-125
                                elif wl8 > wl10 and y580 == 0:
                                    bet7 = (((bet1-480)/100*-105)-500)
                                elif wl8 > wl10 and y340 == 0:
                                    bet7 = (((bet1-240)/100*-105)-250)
                                elif wl8 > wl10 and y100 == 0: 
                                    bet7 = bet1/100*-105   
                                elif wl8 > wl10 and y140 == 0:
                                    bet7 = bet1/140*-145 

                    elif by1 == 3 and yy1 == 2:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs3[0])
                        wl4 = bar1.count(bs3[1])
                        if bs2[0] == bs2[1] or bs2[0] == bs2[2]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bss1 = int(bss[0]) #960
                                bss2 = int(bss[1]) #80
                                bet1 = int(bss1)
                                y480 = bet1 % 120
                                y100 = bet1 % 100
                                y1000 = bet1 % 1000
                                y12000 = bet1 % 12000
                                y580 = (bet1-480) % 100
                                y340 = (bet1-240) % 100
                                y140 = (bet1-140)
                                wl5 = int(wl)    #1
                                wl6 = int(wl1)+int(wl2)
                                wl7 = int(wl3)+int(wl4)
                                wl8 = int(wl3)  #4 
                                wl9 = int(wl4) #5
                                cvt = wl7-wl6
                                ys = wl6
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl7 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet2 = bss1*1
                                    else:
                                        bet2 = 999999
                                if wl8 > wl5:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet3 = bss1*1
                                    else:
                                        bet3 = 999999
                                if wl9 > wl5:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet4 = bss1*1
                                    else:
                                        bet4 = 999999
                                if wl6 > wl7 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl6 > wl7 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl6 > wl7 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl6 > wl7 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl6 > wl7 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl7 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl7 and y100 == 0:
                                    bet5 = bss1/100*-105
                                elif wl6 > wl7 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl5 > wl8 and y12000 == 0:
                                    bet6 = bss1/12000*-12500
                                elif wl5 > wl8 and y1000 == 0:
                                    bet6 = bss1/1000*-1050
                                elif wl5 > wl8 and bss1 == 600:
                                    bet6 = bss1/600*-630
                                elif wl5 > wl8 and y480 == 0:
                                    bet6 = bss1/120*-125
                                elif wl5 > wl8 and y580 == 0:
                                    bet6 = (((bss1-480)/100*-105)-500)
                                elif wl5 > wl8 and y340 == 0:
                                    bet6 = (((bss1-240)/100*-105)-250)
                                elif wl5 > wl8 and y100 == 0:
                                    bet6 = bss1/100*-105
                                elif wl5 > wl8 and y140 == 0:
                                    bet6 = bss1/140*-145
                                if wl5 > wl9 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl5 > wl9 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl5 > wl9 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl5 > wl9 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl5 > wl9 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl5 > wl9 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl5 > wl9 and y100 == 0:
                                    bet7 = bss1/100*-105
                                elif wl5 > wl9 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                            elif "-" not in bs[1]:
                                bet1 = int(bs[1])
                                y480 = bet1 % 120
                                y100 = bet1 % 100
                                y1000 = bet1 % 1000
                                y12000 = bet1 % 12000
                                y580 = (bet1-480) % 100
                                y340 = (bet1-240) % 100
                                y140 = (bet1-140)
                                wl5 = int(wl)    #1
                                wl6 = int(wl1)+int(wl2) #12
                                wl7 = int(wl3)+int(wl4) #34
                                wl8 = int(wl3)  #3
                                wl9 = int(wl4) #4
                                cvt = wl7-wl6
                                if wl7 > wl6:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet2 = bet1*1
                                    else:
                                        bet2 = 999999
                                if wl8 > wl5:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet3 = bet1*1
                                    else:
                                        bet3 = 999999
                                if wl9 > wl5:
                                    if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                        bet4 = bet1*1
                                    else:
                                        bet4 = 999999
                                if wl6 > wl7 and y12000 == 0:
                                    bet5 = bet1/12000*-12500
                                elif wl6 > wl7 and y1000 == 0:
                                    bet5 = bet1/1000*-1050
                                elif wl6 > wl7 and bet1 == 600:
                                    bet5 = bet1/600*-630
                                elif wl6 > wl7 and y480 == 0:
                                    bet5 = bet1/120*-125
                                elif wl6 > wl7 and y580 == 0:
                                    bet5 = (((bet1-480)/100*-105)-500)
                                elif wl6 > wl7 and y340 == 0:
                                    bet5 = (((bet1-240)/100*-105)-250)
                                elif wl6 > wl7 and y100 == 0:
                                    bet5 = bet1/100*-105
                                elif wl6 > wl7 and y140 == 0:
                                    bet5 = bet1/140*-145
                                if wl5 > wl8 and y12000 == 0:
                                    bet6 = bet1/12000*-12500
                                elif wl5 > wl8 and y1000 == 0:
                                    bet6 = bet1/1000*-1050
                                elif wl5 > wl8 and bet1 == 600:
                                    bet6 = bet1/600*-630
                                elif wl5 > wl8 and y480 == 0:
                                    bet6 = bet1/120*-125
                                elif wl5 > wl8 and y580 == 0:
                                    bet6 = (((bet1-480)/100*-105)-500)
                                elif wl5 > wl8 and y340 == 0:
                                    bet6 = (((bet1-240)/100*-105)-250)
                                elif wl5 > wl8 and y100 == 0:
                                    bet6 = bet1/100*-105
                                elif wl5 > wl8 and y140 == 0:
                                    bet6 = bet1/140*-145
                                if wl5 > wl9 and y12000 == 0:
                                    bet7 = bet1/12000*-12500
                                elif wl5 > wl9 and y1000 == 0:
                                    bet7 = bet1/1000*-1050
                                elif wl5 > wl9 and bet1 == 600:
                                    bet7 = bet1/600*-630
                                elif wl5 > wl9 and y480 == 0:
                                    bet7 = bet1/120*-125
                                elif wl5 > wl9 and y580 == 0:
                                    bet7 = (((bet1-480)/100*-105)-500)
                                elif wl5 > wl9 and y340 == 0:
                                    bet7 = (((bet1-240)/100*-105)-250)
                                elif wl5 > wl9 and y100 == 0:
                                    bet7 = bet1/100*-105
                                elif wl5 > wl9 and y140 == 0:
                                    bet7 = bet1/140*-145
                        else:
                            bet1 = int(bs[1])
                            y480 = bet1 % 120
                            y100 = bet1 % 100
                            y1000 = bet1 % 1000
                            y12000 = bet1 % 12000
                            y580 = (bet1-480) % 100
                            y340 = (bet1-240) % 100
                            y140 = (bet1-140)
                            wl5 = int(wl)+int(wl1)   #12
                            wl6 = int(wl)+int(wl2) #13
                            wl7 = int(wl1)+int(wl2) #23
                            wl8 = int(wl3)+int(wl4) #45
                            cvt = 0
                            if wl8 > wl5:
                                bet2 = bet1*1
                            if wl8 > wl6:
                                bet3 = bet1*1
                            if wl8 > wl7:
                                bet4 = bet1*1
                            if wl5 > wl8 and y12000 == 0:
                                bet5 = bet1/12000*-12500
                            elif wl5 > wl8 and y1000 == 0:
                                bet5 = bet1/1000*-1050
                            elif wl5 > wl8 and bet1 == 600:
                                bet5 = bet1/600*-630
                            elif wl5 > wl8 and y480 == 0:
                                bet5 = bet1/120*-125
                            elif wl5 > wl8 and y580 == 0:
                                bet5 = (((bet1-480)/100*-105)-500)
                            elif wl5 > wl8 and y340 == 0:
                                bet5 = (((bet1-240)/100*-105)-250)
                            elif wl5 > wl8 and y100 == 0:
                                bet5 = bet1/100*-105   
                            elif wl5 > wl8 and y140 == 0:
                                bet5 = bet1/140*-145
                            if wl6 > wl8 and y12000 == 0:
                                bet6 = bet1/12000*-12500
                            elif wl6 > wl8 and y1000 == 0:
                                bet6 = bet1/1000*-1050
                            elif wl6 > wl8 and bet1 == 600:
                                bet6 = bet1/600*-630
                            elif wl6 > wl8 and y480 == 0:
                                bet6 = bet1/120*-125
                            elif wl6 > wl8 and y580 == 0:
                                bet6 = (((bet1-480)/100*-105)-500)
                            elif wl6 > wl8 and y340 == 0:
                                bet6 = (((bet1-240)/100*-105)-250)
                            elif wl6 > wl8 and y100 == 0:
                                bet6 = bet1/100*-105  
                            elif wl6 > wl8 and y140 == 0:
                                bet6 = bet1/140*-145
                            if wl7 > wl8 and y12000 == 0:
                                bet7 = bet1/12000*-12500
                            elif wl7 > wl8 and y1000 == 0:
                                bet7 = bet1/1000*-1050
                            elif wl7 > wl8 and bet1 == 600:
                                bet7 = bet1/600*-630
                            elif wl7 > wl8 and y480 == 0:
                                bet7 = bet1/120*-125
                            elif wl7 > wl8 and y580 == 0:
                                bet7 = (((bet1-480)/100*-105)-500)
                            elif wl7 > wl8 and y340 == 0:
                                bet7 = (((bet1-240)/100*-105)-250)
                            elif wl7 > wl8 and y100 == 0:
                                bet7 = bet1/100*-105  
                            elif wl7 > wl8 and y140 == 0:
                                bet7 = bet1/140*-145

                    elif by1 == 3 and yy1 == 3:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs3[0])
                        wl4 = bar1.count(bs3[1])
                        wl5 = bar1.count(bs3[2])
                        if bs2[0] == bs2[1] or bs2[0] == bs2[2]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bss1 = int(bss[0]) #960
                                bss2 = int(bss[1]) #80
                                bet1 = int(bss1)
                                y480 = bet1 % 120
                                y100 = bet1 % 100
                                y1000 = bet1 % 1000
                                y12000 = bet1 % 12000
                                y580 = (bet1-480) % 100
                                y340 = (bet1-240) % 100
                                y140 = (bet1-140)
                                wl6 = int(wl)    #1
                                wl7 = int(wl1)+int(wl2)
                                wl8 = int(wl3)+int(wl4)
                                wl9 = int(wl3)+int(wl5)
                                wl10 = int(wl4)+int(wl5)
                                wl11 = int(wl3)
                                wl12 = int(wl4)
                                wl13 = int(wl5)
                                cvt = 0
                                ys = wl7
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl8 > wl7:
                                    bet2 = bss1*1
                                if wl9 > wl7:
                                    bet3 = bss1*1
                                if wl10 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl8 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl8 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl8 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl8 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl8 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl8 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl8 and y100 == 0:
                                    bet5 = bss1/100*-105
                                elif wl7 > wl8 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl7 > wl9 and y12000 == 0:
                                    bet6 = bss1/12000*-12500
                                elif wl7 > wl9 and y1000 == 0:
                                    bet6 = bss1/1000*-1050
                                elif wl7 > wl9 and bss1 == 600:
                                    bet6 = bss1/600*-630
                                elif wl7 > wl9 and y480 == 0:
                                    bet6 = bss1/120*-125
                                elif wl7 > wl9 and y580 == 0:
                                    bet6 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl9 and y340 == 0:
                                    bet6 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl9 and y100 == 0:
                                    bet6 = bss1/100*-105
                                elif wl7 > wl9 and y140 == 0:
                                    bet6 = bss1/140*-145
                                if wl7 > wl10 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl7 > wl10 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl7 > wl10 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl7 > wl10 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl7 > wl10 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl10 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl10 and y100 == 0:
                                    bet7 = bss1/100*-105
                                elif wl7 > wl10 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl11 > wl6:
                                    bet8 = bss1*1
                                if wl12 > wl6:
                                    bet9 = bss1*1
                                if wl13 > wl6:
                                    bet10 = bss1*1
                                if wl6 > wl11 and y12000 == 0:
                                    bet11 = bss1/12000*-12500
                                elif wl6 > wl11 and y1000 == 0:
                                    bet11 = bss1/1000*-1050
                                elif wl6 > wl11 and bss1 == 600:
                                    bet11 = bss1/600*-630
                                elif wl6 > wl11 and y480 == 0:
                                    bet11 = bss1/120*-125
                                elif wl6 > wl11 and y580 == 0:
                                    bet11 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl11 and y340 == 0:
                                    bet11 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl11 and y100 == 0:
                                    bet11 = bss1/100*-105
                                elif wl6 > wl11 and y140 == 0:
                                    bet11 = bss1/140*-145
                                if wl6 > wl12 and y12000 == 0:
                                    bet12 = bss1/12000*-12500
                                elif wl6 > wl12 and y1000 == 0:
                                    bet12 = bss1/1000*-1050
                                elif wl6 > wl12 and bss1 == 600:
                                    bet12 = bss1/600*-630
                                elif wl6 > wl12 and y480 == 0:
                                    bet12 = bss1/120*-125
                                elif wl6 > wl12 and y580 == 0:
                                    bet12 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl12 and y340 == 0:
                                    bet12 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl12 and y100 == 0:
                                    bet12 = bss1/100*-105
                                elif wl6 > wl12 and y140 == 0:
                                    bet12 = bss1/140*-145
                                if wl6 > wl13 and y12000 == 0:
                                    bet13 = bss1/12000*-12500
                                elif wl6 > wl13 and y1000 == 0:
                                    bet13 = bss1/1000*-1050
                                elif wl6 > wl13 and bss1 == 600:
                                    bet13 = bss1/600*-630
                                elif wl6 > wl13 and y480 == 0:
                                    bet13 = bss1/120*-125
                                elif wl6 > wl13 and y580 == 0:
                                    bet13 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl13 and y340 == 0:
                                    bet13 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl13 and y100 == 0:
                                    bet13 = bss1/100*-105
                                elif wl6 > wl13 and y140 == 0:
                                    bet13 = bss1/140*-145
                                
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                            elif "-" not in bs[1]:
                                bss1 = int(bs[1]) #960
                                bet1 = int(bss1)
                                y480 = bet1 % 120
                                y100 = bet1 % 100
                                y1000 = bet1 % 1000
                                y12000 = bet1 % 12000
                                y580 = (bet1-480) % 100
                                y340 = (bet1-240) % 100
                                y140 = (bet1-140)
                                wl6 = int(wl)    #1
                                wl7 = int(wl1)+int(wl2)
                                wl8 = int(wl3)+int(wl4)
                                wl9 = int(wl3)+int(wl5)
                                wl10 = int(wl4)+int(wl5)
                                wl11 = int(wl3)
                                wl12 = int(wl4)
                                wl13 = int(wl5)
                                cvt = 0
                                if wl8 > wl7:
                                    bet2 = bss1*1
                                if wl9 > wl7:
                                    bet3 = bss1*1
                                if wl10 > wl7:
                                    bet4 = bss1*1
                                if wl7 > wl8 and y12000 == 0:
                                    bet5 = bss1/12000*-12500
                                elif wl7 > wl8 and y1000 == 0:
                                    bet5 = bss1/1000*-1050
                                elif wl7 > wl8 and bss1 == 600:
                                    bet5 = bss1/600*-630
                                elif wl7 > wl8 and y480 == 0:
                                    bet5 = bss1/120*-125
                                elif wl7 > wl8 and y580 == 0:
                                    bet5 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl8 and y340 == 0:
                                    bet5 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl8 and y100 == 0:
                                    bet5 = bss1/100*-105
                                elif wl7 > wl8 and y140 == 0:
                                    bet5 = bss1/140*-145
                                if wl7 > wl9 and y12000 == 0:
                                    bet6 = bss1/12000*-12500
                                elif wl7 > wl9 and y1000 == 0:
                                    bet6 = bss1/1000*-1050
                                elif wl7 > wl9 and bss1 == 600:
                                    bet6 = bss1/600*-630
                                elif wl7 > wl9 and y480 == 0:
                                    bet6 = bss1/120*-125
                                elif wl7 > wl9 and y580 == 0:
                                    bet6 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl9 and y340 == 0:
                                    bet6 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl9 and y100 == 0:
                                    bet6 = bss1/100*-105
                                elif wl7 > wl9 and y140 == 0:
                                    bet6 = bss1/140*-145
                                if wl7 > wl10 and y12000 == 0:
                                    bet7 = bss1/12000*-12500
                                elif wl7 > wl10 and y1000 == 0:
                                    bet7 = bss1/1000*-1050
                                elif wl7 > wl10 and bss1 == 600:
                                    bet7 = bss1/600*-630
                                elif wl7 > wl10 and y480 == 0:
                                    bet7 = bss1/120*-125
                                elif wl7 > wl10 and y580 == 0:
                                    bet7 = (((bss1-480)/100*-105)-500)
                                elif wl7 > wl10 and y340 == 0:
                                    bet7 = (((bss1-240)/100*-105)-250)
                                elif wl7 > wl10 and y100 == 0:
                                    bet7 = bss1/100*-105
                                elif wl7 > wl10 and y140 == 0:
                                    bet7 = bss1/140*-145
                                if wl11 > wl6:
                                    bet8 = bss1*1
                                if wl12 > wl6:
                                    bet9 = bss1*1
                                if wl13 > wl6:
                                    bet10 = bss1*1
                                if wl6 > wl11 and y12000 == 0:
                                    bet11 = bss1/12000*-12500
                                elif wl6 > wl11 and y1000 == 0:
                                    bet11 = bss1/1000*-1050
                                elif wl6 > wl11 and bss1 == 600:
                                    bet11 = bss1/600*-630
                                elif wl6 > wl11 and y480 == 0:
                                    bet11 = bss1/120*-125
                                elif wl6 > wl11 and y580 == 0:
                                    bet11 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl11 and y340 == 0:
                                    bet11 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl11 and y100 == 0:
                                    bet11 = bss1/100*-105
                                elif wl6 > wl11 and y140 == 0:
                                    bet11 = bss1/140*-145
                                if wl6 > wl12 and y1000 == 0:
                                    bet12 = bss1/1000*-1050
                                elif wl6 > wl12 and bss1 == 600:
                                    bet12 = bss1/600*-630
                                elif wl6 > wl12 and y12000 == 0:
                                    bet12 = bss1/12000*-12500
                                elif wl6 > wl12 and y480 == 0:
                                    bet12 = bss1/120*-125
                                elif wl6 > wl12 and y580 == 0:
                                    bet12 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl12 and y340 == 0:
                                    bet12 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl12 and y100 == 0:
                                    bet12 = bss1/100*-105
                                elif wl6 > wl12 and y140 == 0:
                                    bet12 = bss1/140*-145
                                if wl6 > wl13 and y12000 == 0:
                                    bet13 = bss1/12000*-12500
                                elif wl6 > wl13 and y1000 == 0:
                                    bet13 = bss1/1000*-1050
                                elif wl6 > wl13 and bss1 == 600:
                                    bet13 = bss1/600*-630
                                elif wl6 > wl13 and y480 == 0:
                                    bet13 = bss1/120*-125
                                elif wl6 > wl13 and y580 == 0:
                                    bet13 = (((bss1-480)/100*-105)-500)
                                elif wl6 > wl13 and y340 == 0:
                                    bet13 = (((bss1-240)/100*-105)-250)
                                elif wl6 > wl13 and y100 == 0:
                                    bet13 = bss1/100*-105
                                elif wl6 > wl13 and y140 == 0:
                                    bet13 = bss1/140*-145
                        elif bs3[2] == bs3[0] or bs3[2] == bs3[1]:
                            bss1 = int(bs[1]) #960
                            bet1 = int(bss1)
                            y480 = bet1 % 120
                            y100 = bet1 % 100 
                            y1000 = bet1 % 1000
                            y12000 = bet1 % 12000
                            y580 = (bet1-480) % 100   
                            y340 = (bet1-240) % 100   
                            y140 = (bet1-140)
                            wl6 = int(wl)+int(wl1)
                            wl7 = int(wl)+int(wl2)
                            wl8 = int(wl1)+int(wl2)
                            wl9 = int(wl3)+int(wl4)
                            wl10 = int(wl5)
                            wl11 = int(wl)
                            wl12 = int(wl1)
                            wl13 = int(wl2)
                            cvt = 0
                            if wl9 > wl6:
                                bet2 = bss1*1
                            if wl9 > wl7:
                                bet3 = bss1*1
                            if wl9 > wl8:
                                bet4 = bss1*1
                            if wl6 > wl9 and y12000 == 0:
                                bet5 = bss1/12000*-12500
                            elif wl6 > wl9 and y1000 == 0:
                                bet5 = bss1/1000*-1050
                            elif wl6 > wl9 and bss1 == 600:
                                bet5 = bss1/600*-630
                            elif wl6 > wl9 and y480 == 0:
                                bet5 = bss1/120*-125
                            elif wl6 > wl9 and y580 == 0:
                                bet5 = (((bss1-480)/100*-105)-500)
                            elif wl6 > wl9 and y340 == 0:
                                bet5 = (((bss1-240)/100*-105)-250)
                            elif wl6 > wl9 and y100 == 0:
                                bet5 = bss1/100*-105
                            elif wl6 > wl9 and y140 == 0:
                                bet5 = bss1/140*-145
                            if wl7 > wl9 and y12000 == 0:
                                bet6 = bss1/12000*-12500
                            elif wl7 > wl9 and y1000 == 0:
                                bet6 = bss1/1000*-1050
                            elif wl7 > wl9 and bss1 == 600:
                                bet6 = bss1/600*-630
                            elif wl7 > wl9 and y480 == 0:
                                bet6 = bss1/120*-125
                            elif wl7 > wl9 and y580 == 0:
                                bet6 = (((bss1-480)/100*-105)-500)
                            elif wl7 > wl9 and y340 == 0:
                                bet6 = (((bss1-240)/100*-105)-250)
                            elif wl7 > wl9 and y100 == 0:
                                bet6 = bss1/100*-105
                            elif wl7 > wl9 and y140 == 0:
                                bet6 = bss1/140*-145
                            if wl8 > wl9 and y12000 == 0:
                                bet7 = bss1/12000*-12500
                            elif wl8 > wl9 and y1000 == 0:
                                bet7 = bss1/1000*-1050
                            elif wl8 > wl9 and bss1 == 600:
                                bet7 = bss1/600*-630
                            elif wl8 > wl9 and y480 == 0:
                                bet7 = bss1/120*-125
                            elif wl8 > wl9 and y580 == 0:
                                bet7 = (((bss1-480)/100*-105)-500)
                            elif wl8 > wl9 and y340 == 0:
                                bet7 = (((bss1-240)/100*-105)-250)
                            elif wl8 > wl9 and y100 == 0:
                                bet7 = bss1/100*-105
                            elif wl8 > wl9 and y140 == 0:
                                bet7 = bss1/140*-145
                            if wl10 > wl11:
                                bet8 = bss1*1
                            if wl10 > wl12:
                                bet9 = bss1*1
                            if wl10 > wl13:
                                bet10 = bss1*1
                            if wl11 > wl10 and y12000 == 0:
                                bet11 = bss1/12000*-12500
                            elif wl11 > wl10 and y1000 == 0:
                                bet11 = bss1/1000*-1050
                            elif wl11 > wl10 and bss1 == 600:
                                bet11 = bss1/600*-630
                            elif wl11 > wl10 and y480 == 0:
                                bet11 = bss1/120*-125
                            elif wl11 > wl10 and y580 == 0:
                                bet11 = (((bss1-480)/100*-105)-500)
                            elif wl11 > wl10 and y340 == 0:
                                bet11 = (((bss1-240)/100*-105)-250)
                            elif wl11 > wl10 and y100 == 0:
                                bet11 = bss1/100*-105
                            elif wl11 > wl10 and y140 == 0:
                                bet11 = bss1/140*-145
                            if wl12 > wl10 and y12000 == 0:
                                bet12 = bss1/12000*-12500
                            elif wl12 > wl10 and y1000 == 0:
                                bet12 = bss1/1000*-1050
                            elif wl12 > wl10 and bss1 == 600:
                                bet12 = bss1/600*-630
                            elif wl12 > wl10 and y480 == 0:
                                bet12 = bss1/120*-125
                            elif wl12 > wl10 and y580 == 0:
                                bet12 = (((bss1-480)/100*-105)-500)
                            elif wl12 > wl10 and y340 == 0:
                                bet12 = (((bss1-240)/100*-105)-250)
                            elif wl12 > wl10 and y100 == 0:
                                bet12 = bss1/100*-105
                            elif wl12 > wl10 and y140 == 0:
                                bet12 = bss1/140*-145
                            if wl13 > wl10 and y12000 == 0:
                                bet13 = bss1/12000*-12500
                            elif wl13 > wl10 and y1000 == 0:
                                bet13 = bss1/1000*-1050
                            elif wl13 > wl10 and bss1 == 600:
                                bet13 = bss1/600*-630
                            elif wl13 > wl10 and y480 == 0:
                                bet13 = bss1/120*-125
                            elif wl13 > wl10 and y580 == 0:
                                bet13 = (((bss1-480)/100*-105)-500)
                            elif wl13 > wl10 and y340 == 0:
                                bet13 = (((bss1-240)/100*-105)-250)
                            elif wl13 > wl10 and y100 == 0:
                                bet13 = bss1/100*-105
                            elif wl13 > wl10 and y140 == 0:
                                bet13 = bss1/140*-145

                    elif by1 == 3 and yy1 == 0:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100   
                        y340 = (bet1-240) % 100   
                        y140 = (bet1-140)
                        wl5 = int(wl)+int(wl1)+int(wl2)  #12
                        cvt = (((int(wl)+int(wl1)+int(wl)+int(wl2)+int(wl1)+int(wl2))*-1)+3) #test
                        if wl5 <= 1:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet2 = bet1*1
                            else:
                                bet2 = 999999
                        elif wl5 >= 2 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl5 >= 2 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl5 >= 2 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl5 >= 2 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl5 >= 2 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl5 >= 2 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl5 >= 2 and y100 == 0:
                            bet3 = bet1/100*-105  
                        elif wl5 >= 2 and y140 == 0:
                            bet3 = bet1/140*-145 
                    
                    elif by1 == 0 and yy1 == 3:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs3[1])
                        wl2 = bar1.count(bs3[2])
                        bet1 = int(bs[1])
                        y480 = bet1 % 120
                        y100 = bet1 % 100
                        y1000 = bet1 % 1000
                        y12000 = bet1 % 12000
                        y580 = (bet1-480) % 100
                        y340 = (bet1-240) % 100
                        y140 = (bet1-140)
                        wl5 = int(wl)+int(wl1)+int(wl2)  #12
                        cvt = ((int(wl)+int(wl1)+int(wl)+int(wl2)+int(wl1)+int(wl2))-3) #test
                        if wl5 >= 2:
                            if y480 == 0 or y100 == 0 or y1000 == 0 or y12000 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                bet2 = bet1*1
                            else:
                                bet2 = 999999
                        elif wl5 <= 1 and y12000 == 0:
                            bet3 = bet1/12000*-12500
                        elif wl5 <= 1 and y1000 == 0:
                            bet3 = bet1/1000*-1050
                        elif wl5 <= 1 and bet1 == 600:
                            bet3 = bet1/600*-630
                        elif wl5 <= 1 and y480 == 0:
                            bet3 = bet1/120*-125
                        elif wl5 <= 1 and y580 == 0:
                            bet3 = (((bet1-480)/100*-105)-500)
                        elif wl5 <= 1 and y340 == 0:
                            bet3 = (((bet1-240)/100*-105)-250)
                        elif wl5 <= 1 and y100 == 0:
                            bet3 = bet1/100*-105   
                        elif wl5 <= 2 and y140 == 0:
                            bet3 = bet1/140*-145 

                    elif by1 == 2 and yy1 == 0:
                        bet1 = int(bs[1])
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        ys = int(wl)+int(wl1)
                        ys1 = bar1[0] == bar1[1]
                        ys2 = bar1[0] == bar1[2]
                        y20 = bet1 % 20
                        ys1000 = bet1 % 1000
                        if ys >= 2:
                            if ys1000 == 0:
                                bet2 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet2 = bet1/500*-3150
                            elif y20 == 0:
                                bet2 = bet1/20*-125
                            elif bet1 == 30:
                                bet2 = bet1/30*-190
                            elif bet1 == 50:
                                bet2 = bet1/50*-315
                        elif ys == 0 and ys2 is True:
                            bet3 = bet1*3
                        elif ys == 0 and ys1 is True:
                            bet4 = bet1*5
                        elif ys == 0 and ys1 is False:
                            bet5 = bet1*6

                    elif by1 == 4 and yy1 == 0:
                        bet1 = int(bs[1])
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs2[3])
                        ys = int(wl)+int(wl1)
                        yss = int(wl2)+int(wl3)
                        ys1 = bar1[0] == bar1[1]
                        ys2 = bar1[0] == bar1[2]
                        y20 = bet1 % 20
                        ys1000 = bet1 % 1000
                        if ys >= 2:
                            if ys1000 == 0:
                                bet2 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet2 = bet1/500*-3150
                            elif y20 == 0:
                                bet2 = bet1/20*-125
                            elif bet1 == 30:
                                bet2 = bet1/30*-190
                            elif bet1 == 50:
                                bet2 = bet1/50*-315
                        elif ys == 0 and ys2 is True:
                            bet3 = bet1*3
                        elif ys == 0 and ys1 is True:
                            bet4 = bet1*5
                        elif ys == 0 and ys1 is False:
                            bet5 = bet1*6
                        if yss >= 2:
                            if ys1000 == 0:
                                bet6 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet6 = bet1/500*-3150
                            elif y20 == 0:
                                bet6 = bet1/20*-125
                            elif bet1 == 30:
                                bet6 = bet1/30*-190
                            elif bet1 == 50:
                                bet6 = bet1/50*-315
                        elif yss == 0 and ys2 is True:
                            bet7 = bet1*3
                        elif yss == 0 and ys1 is True:
                            bet8 = bet1*5
                        elif yss == 0 and ys1 is False:
                            bet9 = bet1*6

                    elif by1 == 0 and yy1 == 2:
                        bet1 = int(bs[1])
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs3[1])
                        wl6 = int(wl)+int(wl1)
                        ys = wl6
                        ys1 = bar1[0] == bar1[1]
                        ys2 = bar1[0] == bar1[2]
                        y120 = bet1 % 120
                        y20 = bet1 % 20
                        ys1000 = bet1 % 1000
                        if ys >= 2:
                            bet2 = bet1*6
                        elif ys == 0 and ys2 is True:
                            if ys1000 == 0:
                                bet3 = bet1/1000*-3150
                            elif bet1 == 380:
                                bet3 = bet1/380*-1195
                            elif bet1 == 340:
                                bet3 = bet1/340*-1070
                            elif bet1 == 300:
                                bet3 = bet1/300*-945
                            elif bet1 == 500:
                                bet3 = bet1/500*-1550
                            elif bet1 == 260:
                                bet3 = bet1/260*-815
                            elif bet1 == 220:
                                bet3 = bet1/220*-690
                            elif bet1 == 180:
                                bet3 = bet1/180*-565
                            elif bet1 == 140:
                                bet3 = bet1/140*-440
                            elif bet1 == 100:
                                bet3 = bet1/100*-315
                            elif bet1 == 60:
                                bet3 = bet1/60*-190
                            elif bet1 == 20:
                                bet3 = bet1/20*-60
                            elif y20 == 0:
                                bet3 = bet1/20*-62.5
                            elif bet1 == 30:
                                bet3 = bet1/30*-95
                            elif bet1 == 50:
                                bet3 = bet1/50*-155
                        elif ys == 0 and ys1 is True:
                            if ys1000 == 0:
                                bet3 = bet1/1000*-5250
                            elif bet1 == 300:
                                bet3 = bet1/300*-1550
                            elif bet1 == 500:
                                bet3 = bet1/500*-2600
                            elif y20 == 0:
                                bet3 = bet1/20*-105
                            elif bet1 == 30:
                                bet3 = bet1/30*-155
                            elif bet1 == 50:
                                bet3 = bet1/50*-260
                        elif ys == 0 and ys1 is False:
                            if ys1000 == 0:
                                bet4 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet4 = bet1/500*-3150
                            elif y20 == 0:
                                bet4 = bet1/20*-125
                            elif bet1 == 30:
                                bet4 = bet1/30*-190
                            elif bet1 == 50:
                                bet4 = bet1/50*-315

                elif "x" in bet:
                    if by1 == 1 and yy1 == 1:
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        wl = bar1.count(bs2)
                        wl1 = bar1.count(bs3)
                        wl6 = int(wl)
                        wl16 = int(wl1)
                        cvt = wl16-wl6
                        if wl16 > wl6:
                            if y480 == 0:
                                bet2 = (bet1*1)*betx
                            else:
                                bet2 = 999999
                        if wl6 > wl16 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 2:
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        wl = bar1.count(bs2)
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl6 = int(wl)
                        wl16 = int(wl1)
                        wl17 = int(wl2)
                        cvt = wl17-wl6
                        if wl16 > wl6:
                            if y480 == 0:
                                bet2 = (bet1*1)*betx
                            else:
                                bet2 = 999999
                        if wl17 > wl6:
                            if y480 == 0:
                                bet3 = (bet1*1)*betx
                            else:
                                bet3 = 999999
                        if wl6 > wl16 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl6 > wl17 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 3:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[1])
                        wl2 = bar1.count(bs3[2])
                        wl3 = bar1.count(bs3[0])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        wl6 = int(wl)    #1
                        wl16 = int(wl1) #2
                        wl17 = int(wl2) #3
                        wl18 = int(wl3)  #4
                        cvt = wl18-wl6    
                        if wl18 > wl6:
                            if y480 == 0:
                                bet2 = (bet1*1)*betx
                            else:
                                bet2 = 999999
                        if wl17 > wl6:
                            if y480 == 0:
                                bet3 = (bet1*1)*betx
                            else:
                                bet3 = 999999
                        if wl16 > wl6:
                            if y480 == 0:
                                bet4 = (bet1*1)*betx
                            else:
                                bet4 = 999999
                        if wl6 > wl16 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl6 > wl17 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl6 > wl18 and y480 == 0:
                            bet7 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 4:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = (bet1*1)*betx
                        if wl2 > wl:
                            bet3 = (bet1*1)*betx
                        if wl3 > wl:
                            bet4 = (bet1*1)*betx
                        if wl4 > wl:
                            bet5 = (bet1*1)*betx
                        if wl > wl1 and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl > wl2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl > wl3 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl > wl4 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 5:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = (bet1*1)*betx
                        if wl2 > wl:
                            bet3 = (bet1*1)*betx
                        if wl3 > wl:
                            bet4 = (bet1*1)*betx
                        if wl4 > wl:
                            bet5 = (bet1*1)*betx
                        if wl5 > wl:
                            bet6 = (bet1*1)*betx
                        if wl > wl1 and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl > wl2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl > wl3 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl > wl4 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl > wl5 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 6:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = (bet1*1)*betx
                        if wl2 > wl:
                            bet3 = (bet1*1)*betx
                        if wl3 > wl:
                            bet4 = (bet1*1)*betx
                        if wl4 > wl:
                            bet5 = (bet1*1)*betx
                        if wl5 > wl:
                            bet6 = (bet1*1)*betx
                        if wl6 > wl:
                            bet7 = (bet1*1)*betx
                        if wl > wl1 and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl > wl2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl > wl3 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl > wl4 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl > wl5 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl > wl6 and y480 == 0:
                            bet7 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 7:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = (bet1*1)*betx
                        if wl2 > wl:
                            bet3 = (bet1*1)*betx
                        if wl3 > wl:
                            bet4 = (bet1*1)*betx
                        if wl4 > wl:
                            bet5 = (bet1*1)*betx
                        if wl5 > wl:
                            bet6 = (bet1*1)*betx
                        if wl6 > wl:
                            bet7 = (bet1*1)*betx
                        if wl7 > wl:
                            bet8 = (bet1*1)*betx
                        if wl > wl1 and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl > wl2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl > wl3 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl > wl4 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl > wl5 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl > wl6 and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl > wl7 and y480 == 0:
                            bet8 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 8:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        wl8 = bar1.count(bs3[7])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = (bet1*1)*betx
                        if wl2 > wl:
                            bet3 = (bet1*1)*betx
                        if wl3 > wl:
                            bet4 = (bet1*1)*betx
                        if wl4 > wl:
                            bet5 = (bet1*1)*betx
                        if wl5 > wl:
                            bet6 = (bet1*1)*betx
                        if wl6 > wl:
                            bet7 = (bet1*1)*betx
                        if wl7 > wl:
                            bet8 = (bet1*1)*betx
                        if wl8 > wl:
                            bet9 = (bet1*1)*betx
                        if wl > wl1 and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl > wl2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl > wl3 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl > wl4 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl > wl5 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl > wl6 and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl > wl7 and y480 == 0:
                            bet8 = (bet1/120*-125)*betx
                        if wl > wl8 and y480 == 0:
                            bet9 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 9:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        wl8 = bar1.count(bs3[7])
                        wl9 = bar1.count(bs3[8])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = (bet1*1)*betx
                        if wl2 > wl:
                            bet3 = (bet1*1)*betx
                        if wl3 > wl:
                            bet4 = (bet1*1)*betx
                        if wl4 > wl:
                            bet5 = (bet1*1)*betx
                        if wl5 > wl:
                            bet6 = (bet1*1)*betx
                        if wl6 > wl:
                            bet7 = (bet1*1)*betx
                        if wl7 > wl:
                            bet8 = (bet1*1)*betx
                        if wl8 > wl:
                            bet9 = (bet1*1)*betx
                        if wl9 > wl:
                            bet10 = (bet1*1)*betx
                        if wl > wl1 and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl > wl2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl > wl3 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl > wl4 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl > wl5 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl > wl6 and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl > wl7 and y480 == 0:
                            bet8 = (bet1/120*-125)*betx
                        if wl > wl8 and y480 == 0:
                            bet9 = (bet1/120*-125)*betx
                        if wl > wl9 and y480 == 0:
                            bet10 = (bet1/120*-125)*betx

                    elif by1 == 1 and yy1 == 10:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs3[0])
                        wl2 = bar1.count(bs3[1])
                        wl3 = bar1.count(bs3[2])
                        wl4 = bar1.count(bs3[3])
                        wl5 = bar1.count(bs3[4])
                        wl6 = bar1.count(bs3[5])
                        wl7 = bar1.count(bs3[6])
                        wl8 = bar1.count(bs3[7])
                        wl9 = bar1.count(bs3[8])
                        wl10 = bar1.count(bs3[9])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0 
                        if wl1 > wl:
                            bet2 = (bet1*1)*betx
                        if wl2 > wl:
                            bet3 = (bet1*1)*betx
                        if wl3 > wl:
                            bet4 = (bet1*1)*betx
                        if wl4 > wl:
                            bet5 = (bet1*1)*betx
                        if wl5 > wl:
                            bet6 = (bet1*1)*betx
                        if wl6 > wl:
                            bet7 = (bet1*1)*betx
                        if wl7 > wl:
                            bet8 = (bet1*1)*betx
                        if wl8 > wl:
                            bet9 = (bet1*1)*betx
                        if wl9 > wl:
                            bet10 = (bet1*1)*betx
                        if wl10 > wl:
                            bet11 = (bet1*1)*betx
                        if wl > wl1 and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl > wl2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl > wl3 and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl > wl4 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl > wl5 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl > wl6 and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl > wl7 and y480 == 0:
                            bet8 = (bet1/120*-125)*betx
                        if wl > wl8 and y480 == 0:
                            bet9 = (bet1/120*-125)*betx
                        if wl > wl9 and y480 == 0:
                            bet10 = (bet1/120*-125)*betx
                        if wl > wl10 and y480 == 0:
                            bet11 = (bet1/120*-125)*betx

                    elif by1 == 2 and yy1 == 1:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bsx = bss[0].split("x")
                            bss1 = int(bsx[0])
                            betx = int(bsx[1])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl6 = int(wl)
                            wl7 = int(wl1)
                            wl16 = int(wl2)
                            cvt = wl16-wl7
                            ys = wl6+wl7
                            ys1 = bar1[0] == bar1[1]
                            ys2 = bar1[0] == bar1[2]
                            y20 = bss2 % 20
                            ys1000 = bss2 % 1000
                            if wl16 > wl6:
                                if y480 == 0:
                                    bet2 = (bss1*1)*betx
                                else:
                                    bet2 = 999999
                            if wl16 > wl7:
                                if y480 == 0:
                                    bet3 = (bss1*1)*betx
                                else:
                                    bet3 = 999999
                            if wl6 > wl16 and y480 == 0:
                                bet4 = (bss1/120*-125)*betx
                            if wl7 > wl16 and y480 == 0:
                                bet5 = (bss1/120*-125)*betx
                            if ys >= 2:
                                if ys1000 == 0:
                                    bet14 = bss2/1000*-6300
                                elif bss2 == 500:
                                    bet14 = bss2/500*-3150
                                elif y20 == 0:
                                    bet14 = bss2/20*-125
                                elif bss2 == 30:
                                    bet14 = bss2/30*-190
                                elif bss2 == 50:
                                    bet14 = bss2/50*-315
                            elif ys == 0 and ys2 is True:
                                bet14 = bss2*3
                            elif ys == 0 and ys1 is True:
                                bet14 = bss2*5
                            elif ys == 0 and ys1 is False:
                                bet14 = bss2*6
                            
                        elif "-" not in bs[1]:
                            bsx = bs[1].split("x")
                            bet1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bet1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl6 = int(wl)
                            wl7 = int(wl1)
                            wl16 = int(wl2)
                            cvt = wl16-wl7
                            if wl16 > wl6:
                                if y480 == 0:
                                    bet2 = (bet1*1)*betx
                                else:
                                    bet2 = 999999
                            if wl16 > wl7:
                                if y480 == 0:
                                    bet3 = (bet1*1)*betx
                                else:
                                    bet3 = 999999
                            if wl6 > wl16 and y480 == 0:
                                bet4 = (bet1/120*-125)*betx
                            if wl7 > wl16 and y480 == 0:
                                bet5 = (bet1/120*-125)*betx

                    elif by1 == 3 and yy1 == 1:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs3[0])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        wl5 = int(wl)    #1
                        wl6 = int(wl1) #2
                        wl7 = int(wl2) #3
                        wl8 = int(wl3)  #4
                        cvt = wl8-wl7    
                        if wl8 > wl5:
                            if y480 == 0:
                                bet2 = (bet1*1)*betx
                            else:
                                bet2 = 999999
                        if wl8 > wl6:
                            if y480 == 0:
                                bet3 = (bet1*1)*betx
                            else:
                                bet3 = 999999
                        if wl8 > wl7:
                            if y480 == 0:
                                bet4 = (bet1*1)*betx
                            else:
                                bet4 = 999999
                        if wl5 > wl8 and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl6 > wl8 and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl7 > wl8 and y480 == 0:
                            bet7 = (bet1/120*-125)*betx

                    elif by1 == 4 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0    
                        if wl > wl1:
                            bet2 = (bet1*1)*betx
                        if wl > wl2:
                            bet3 = (bet1*1)*betx
                        if wl > wl3:
                            bet4 = (bet1*1)*betx
                        if wl > wl4:
                            bet5 = (bet1*1)*betx
                        if wl1 > wl and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl2 > wl and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl3 > wl and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl4 > wl and y480 == 0:
                            bet5 = (bet1/120*-125)*betx

                    elif by1 == 5 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0    
                        if wl > wl1:
                            bet2 = (bet1*1)*betx
                        if wl > wl2:
                            bet3 = (bet1*1)*betx
                        if wl > wl3:
                            bet4 = (bet1*1)*betx
                        if wl > wl4:
                            bet5 = (bet1*1)*betx
                        if wl > wl5:
                            bet6 = (bet1*1)*betx
                        if wl1 > wl and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl2 > wl and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl3 > wl and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl4 > wl and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl5 > wl and y480 == 0:
                            bet6 = (bet1/120*-125)*betx

                    elif by1 == 6 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0    
                        if wl > wl1:
                            bet2 = (bet1*1)*betx
                        if wl > wl2:
                            bet3 = (bet1*1)*betx
                        if wl > wl3:
                            bet4 = (bet1*1)*betx
                        if wl > wl4:
                            bet5 = (bet1*1)*betx
                        if wl > wl5:
                            bet6 = (bet1*1)*betx
                        if wl > wl6:
                            bet7 = (bet1*1)*betx
                        if wl1 > wl and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl2 > wl and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl3 > wl and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl4 > wl and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl5 > wl and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl6 > wl and y480 == 0:
                            bet7 = (bet1/120*-125)*betx

                    elif by1 == 7 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0    
                        if wl > wl1:
                            bet2 = (bet1*1)*betx
                        if wl > wl2:
                            bet3 = (bet1*1)*betx
                        if wl > wl3:
                            bet4 = (bet1*1)*betx
                        if wl > wl4:
                            bet5 = (bet1*1)*betx
                        if wl > wl5:
                            bet6 = (bet1*1)*betx
                        if wl > wl6:
                            bet7 = (bet1*1)*betx
                        if wl > wl7:
                            bet8 = (bet1*1)*betx
                        if wl1 > wl and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl2 > wl and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl3 > wl and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl4 > wl and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl5 > wl and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl6 > wl and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl7 > wl and y480 == 0:
                            bet8 = (bet1/120*-125)*betx

                    elif by1 == 8 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        wl8 = bar1.count(bs2[7])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0    
                        if wl > wl1:
                            bet2 = (bet1*1)*betx
                        if wl > wl2:
                            bet3 = (bet1*1)*betx
                        if wl > wl3:
                            bet4 = (bet1*1)*betx
                        if wl > wl4:
                            bet5 = (bet1*1)*betx
                        if wl > wl5:
                            bet6 = (bet1*1)*betx
                        if wl > wl6:
                            bet7 = (bet1*1)*betx
                        if wl > wl7:
                            bet8 = (bet1*1)*betx
                        if wl > wl8:
                            bet9 = (bet1*1)*betx
                        if wl1 > wl and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl2 > wl and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl3 > wl and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl4 > wl and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl5 > wl and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl6 > wl and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl7 > wl and y480 == 0:
                            bet8 = (bet1/120*-125)*betx
                        if wl8 > wl and y480 == 0:
                            bet9 = (bet1/120*-125)*betx

                    elif by1 == 9 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        wl8 = bar1.count(bs2[7])
                        wl9 = bar1.count(bs2[8])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0    
                        if wl > wl1:
                            bet2 = (bet1*1)*betx
                        if wl > wl2:
                            bet3 = (bet1*1)*betx
                        if wl > wl3:
                            bet4 = (bet1*1)*betx
                        if wl > wl4:
                            bet5 = (bet1*1)*betx
                        if wl > wl5:
                            bet6 = (bet1*1)*betx
                        if wl > wl6:
                            bet7 = (bet1*1)*betx
                        if wl > wl7:
                            bet8 = (bet1*1)*betx
                        if wl > wl8:
                            bet9 = (bet1*1)*betx
                        if wl > wl9:
                            bet10 = (bet1*1)*betx
                        if wl1 > wl and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl2 > wl and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl3 > wl and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl4 > wl and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl5 > wl and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl6 > wl and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl7 > wl and y480 == 0:
                            bet8 = (bet1/120*-125)*betx
                        if wl8 > wl and y480 == 0:
                            bet9 = (bet1/120*-125)*betx
                        if wl9 > wl and y480 == 0:
                            bet10 = (bet1/120*-125)*betx

                    elif by1 == 10 and yy1 == 1:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs2[0])
                        wl2 = bar1.count(bs2[1])
                        wl3 = bar1.count(bs2[2])
                        wl4 = bar1.count(bs2[3])
                        wl5 = bar1.count(bs2[4])
                        wl6 = bar1.count(bs2[5])
                        wl7 = bar1.count(bs2[6])
                        wl8 = bar1.count(bs2[7])
                        wl9 = bar1.count(bs2[8])
                        wl10 = bar1.count(bs2[9])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        cvt = 0    
                        if wl > wl1:
                            bet2 = (bet1*1)*betx
                        if wl > wl2:
                            bet3 = (bet1*1)*betx
                        if wl > wl3:
                            bet4 = (bet1*1)*betx
                        if wl > wl4:
                            bet5 = (bet1*1)*betx
                        if wl > wl5:
                            bet6 = (bet1*1)*betx
                        if wl > wl6:
                            bet7 = (bet1*1)*betx
                        if wl > wl7:
                            bet8 = (bet1*1)*betx
                        if wl > wl8:
                            bet9 = (bet1*1)*betx
                        if wl > wl9:
                            bet10 = (bet1*1)*betx
                        if wl > wl10:
                            bet11 = (bet1*1)*betx
                        if wl1 > wl and y480 == 0:
                            bet2 = (bet1/120*-125)*betx
                        if wl2 > wl and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                        if wl3 > wl and y480 == 0:
                            bet4 = (bet1/120*-125)*betx
                        if wl4 > wl and y480 == 0:
                            bet5 = (bet1/120*-125)*betx
                        if wl5 > wl and y480 == 0:
                            bet6 = (bet1/120*-125)*betx
                        if wl6 > wl and y480 == 0:
                            bet7 = (bet1/120*-125)*betx
                        if wl7 > wl and y480 == 0:
                            bet8 = (bet1/120*-125)*betx
                        if wl8 > wl and y480 == 0:
                            bet9 = (bet1/120*-125)*betx
                        if wl9 > wl and y480 == 0:
                            bet10 = (bet1/120*-125)*betx
                        if wl10 > wl and y480 == 0:
                            bet11 = (bet1/120*-125)*betx


                    elif by1 == 2 and yy1 == 2:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bsx = bss[0].split("x")
                            bss1 = int(bsx[0])
                            betx = int(bsx[1])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            cvt = wl16-wl6
                            ys = wl6
                            ys1 = bar1[0] == bar1[1]
                            ys2 = bar1[0] == bar1[2]
                            y20 = bss2 % 20
                            ys1000 = bss2 % 1000
                            if wl16 > wl6:
                                if y480 == 0 or y100 == 0 or y1000 == 0 or y480 == 0 or y580 == 0 or y340 == 0 or y140 == 0:
                                    bet2 = (bss1*1)*betx
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y480 == 0:
                                bet4 = (bss1/120*-125)*betx
                            if ys >= 2:
                                if ys1000 == 0:
                                    bet14 = bss2/1000*-6300
                                elif bss2 == 500:
                                    bet14 = bss2/500*-3150
                                elif y20 == 0:
                                    bet14 = bss2/20*-125
                                elif bss2 == 30:
                                    bet14 = bss2/30*-190
                                elif bss2 == 50:
                                    bet14 = bss2/50*-315
                            elif ys == 0 and ys2 is True:
                                bet14 = bss2*3
                            elif ys == 0 and ys1 is True:
                                bet14 = bss2*5
                            elif ys == 0 and ys1 is False:
                                bet14 = bss2*6
                            
                        elif "-" not in bs[1]:
                            bsx = bs[1].split("x")
                            bet1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bet1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            cvt = wl16-wl6
                            if wl16 > wl6:
                                if y480 == 0:
                                    bet2 = (bet1*1)*betx
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y480 == 0:
                                bet5 = (bet1/120*-125)*betx

                    elif by1 == 2 and yy1 == 4:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bsx = bss[0].split("x")
                            bss1 = int(bsx[0])
                            betx = int(bsx[1])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            wl17 = int(wl4)+int(wl5)
                            cvt = wl17-wl6
                            ys = wl6
                            ys1 = bar1[0] == bar1[1]
                            ys2 = bar1[0] == bar1[2]
                            y20 = bss2 % 20
                            ys1000 = bss2 % 1000
                            if wl16 > wl6:
                                if y480 == 0:
                                    bet2 = (bss1*1)*betx
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y480 == 0:
                                bet3 = (bss1/120*-125)*betx
                            if wl17 > wl6:
                                bet4 = (bss1*1)*betx
                            if wl6 > wl17 and y480 == 0:
                                bet5 = (bss1/120*-125)*betx
                            if ys >= 2:
                                if ys1000 == 0:
                                    bet14 = bss2/1000*-6300
                                elif bss2 == 500:
                                    bet14 = bss2/500*-3150
                                elif y20 == 0:
                                    bet14 = bss2/20*-125
                                elif bss2 == 30:
                                    bet14 = bss2/30*-190
                                elif bss2 == 50:
                                    bet14 = bss2/50*-315
                            elif ys == 0 and ys2 is True:
                                bet14 = bss2*3
                            elif ys == 0 and ys1 is True:
                                bet14 = bss2*5
                            elif ys == 0 and ys1 is False:
                                bet14 = bss2*6
                            
                        elif "-" not in bs[1]:
                            bsx = bs[1].split("x")
                            bet1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bet1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = int(wl)+int(wl1)
                            wl16 = int(wl2)+int(wl3)
                            wl17 = int(wl4)+int(wl5)
                            cvt = wl17-wl6
                            if wl16 > wl6:
                                if y480 == 0:
                                    bet2 = (bet1*1)*betx
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y480 == 0:
                                bet3 = (bet1/120*-125)*betx
                            if wl17 > wl6:
                                bet4 = (bet1*1)*betx
                            if wl6 > wl17 and y480 == 0:
                                bet5 = (bet1/120*-125)*betx

                    elif by1 == 2 and yy1 == 5:
                        if "-" in bs[1]:
                            bss = bs[1].split("-")
                            bsx = bss[0].split("x")
                            bss1 = int(bsx[0])
                            betx = int(bsx[1])
                            bss2 = int(bss[1])
                            y480 = bss1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = bar1.count(bs3[4])
                            if int(bs3[2]) > int(bs3[0]) and int(bs3[2]) > int(bs3[1]):
                                wl7 = int(wl)+int(wl1) 
                                wl16 = int(wl2)+int(wl3) 
                                wl17 = int(wl2)+int(wl4) 
                                wl18 = int(wl3)+int(wl4) 
                                wl19 = int(wl5)+int(wl6) 
                                cvt = 0
                                ys = wl7
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl16 > wl7:
                                    bet2 = (bss1*1)*betx
                                if wl7 > wl16 and y480 == 0:
                                    bet3 = (bss1/120*-125)*betx
                                if wl17 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl17 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl18 > wl7:
                                    bet6 = (bss1*1)*betx
                                if wl7 > wl18 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl19 > wl7:
                                    bet8 = (bss1*1)*betx
                                if wl7 > wl19 and y480 == 0:
                                    bet9 = (bss1/120*-125)*betx
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6

                            else:
                                wl7 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3)
                                wl17 = int(wl4)+int(wl5)
                                wl18 = int(wl4)+int(wl6)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                ys = wl7
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl16 > wl7:
                                    bet2 = (bss1*1)*betx
                                if wl7 > wl16 and y480 == 0:
                                    bet3 = (bss1/120*-125)*betx
                                if wl17 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl17 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl18 > wl7:
                                    bet6 = (bss1*1)*betx
                                if wl7 > wl18 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl19 > wl7:
                                    bet8 = (bss1*1)*betx
                                if wl7 > wl19 and y480 == 0:
                                    bet9 = (bss1/120*-125)*betx
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                                
                        elif "-" not in bs[1]:
                            bsx = bs[1].split("x")
                            bss1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bss1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs3[0])
                            wl3 = bar1.count(bs3[1])
                            wl4 = bar1.count(bs3[2])
                            wl5 = bar1.count(bs3[3])
                            wl6 = bar1.count(bs3[4])
                            if int(bs3[2]) > int(bs3[0]) and int(bs3[2]) > int(bs3[1]):
                                wl7 = int(wl)+int(wl1) 
                                wl16 = int(wl2)+int(wl3) 
                                wl17 = int(wl2)+int(wl4) 
                                wl18 = int(wl3)+int(wl4) 
                                wl19 = int(wl5)+int(wl6) 
                                cvt = 0
                                if wl16 > wl7:
                                    bet2 = (bss1*1)*betx
                                if wl7 > wl16 and y480 == 0:
                                    bet3 = (bss1/120*-125)*betx
                                if wl17 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl17 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl18 > wl7:
                                    bet6 = (bss1*1)*betx
                                if wl7 > wl18 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl19 > wl7:
                                    bet8 = (bss1*1)*betx
                                if wl7 > wl19 and y480 == 0:
                                    bet9 = (bss1/120*-125)*betx

                            else:
                                wl7 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3)
                                wl17 = int(wl4)+int(wl5)
                                wl18 = int(wl4)+int(wl6)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                if wl16 > wl7:
                                    bet2 = (bss1*1)*betx
                                if wl7 > wl16 and y480 == 0:
                                    bet3 = (bss1/120*-125)*betx
                                if wl17 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl17 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl18 > wl7:
                                    bet6 = (bss1*1)*betx
                                if wl7 > wl18 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl19 > wl7:
                                    bet8 = (bss1*1)*betx
                                if wl7 > wl19 and y480 == 0:
                                    bet9 = (bss1/120*-125)*betx


                    elif by1 == 5 and yy1 == 2:
                        if "-" not in bs[1]:
                            bsx = bs[1].split("x")
                            bss1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bss1 % 120
                            wl = bar1.count(bs2[0])  
                            wl1 = bar1.count(bs2[1]) 
                            wl2 = bar1.count(bs2[2]) 
                            wl3 = bar1.count(bs2[3]) 
                            wl4 = bar1.count(bs2[4]) 
                            wl5 = bar1.count(bs3[0]) 
                            wl6 = bar1.count(bs3[1]) 
                            if int(bs2[2]) > int(bs2[0]) and int(bs2[2]) > int(bs2[1]):
                                wl10 = int(wl)+int(wl1)
                                wl7 = int(wl)+int(wl2)
                                wl8 = int(wl1)+int(wl2)
                                wl9 = int(wl3)+int(wl4)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                if wl19 > wl10:
                                    bet2 = (bss1*1)*betx
                                if wl10 > wl19 and y480 == 0:
                                    bet3 = (bss1/120*-125)*betx
                                if wl19 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl19 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl19 > wl8:
                                    bet6 = (bss1*1)*betx
                                if wl8 > wl19 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl19 > wl9:
                                    bet8 = (bss1*1)*betx
                                if wl9 > wl19 and y480 == 0:
                                    bet9 = (bss1/120*-125)*betx

                            else:
                                wl10 = int(wl)+int(wl1)
                                wl7 = int(wl2)+int(wl3)
                                wl8 = int(wl2)+int(wl4)
                                wl9 = int(wl3)+int(wl4)
                                wl19 = int(wl5)+int(wl6)
                                cvt = 0
                                if wl19 > wl10:
                                    bet2 = (bss1*1)*betx
                                if wl10 > wl19 and y480 == 0:
                                    bet3 = (bss1/120*-125)*betx
                                if wl19 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl19 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl19 > wl8:
                                    bet6 = (bss1*1)*betx
                                if wl8 > wl19 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl19 > wl9:
                                    bet8 = (bss1*1)*betx
                                if wl9 > wl19 and y480 == 0:
                                    bet9 = (bss1/120*-125)*betx

                    elif by1 == 4 and yy1 == 2:   
                        if "-" not in bs[1]:
                            bsx = bs[1].split("x")
                            bet1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bet1 % 120
                            wl = bar1.count(bs2[0])
                            wl1 = bar1.count(bs2[1])
                            wl2 = bar1.count(bs2[2])
                            wl3 = bar1.count(bs2[3])
                            wl4 = bar1.count(bs3[0])
                            wl5 = bar1.count(bs3[1])
                            wl6 = int(wl)+int(wl1)
                            wl7 = int(wl2)+int(wl3)
                            wl16 = int(wl4)+int(wl5)
                            cvt = wl16-wl7
                            if wl16 > wl6:
                                if y480 == 0:
                                    bet2 = (bet1*1)*betx
                                else:
                                    bet2 = 999999
                            if wl6 > wl16 and y480 == 0:
                                bet3 = (bet1/120*-125)*betx
                            if wl16 > wl7:
                                bet4 = (bet1*1)*betx
                            if wl7 > wl16 and y480 == 0:
                                bet5 = (bet1/120*-125)*betx


                    elif by1 == 2 and yy1 == 3:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs3[0])
                        wl3 = bar1.count(bs3[1])
                        wl4 = bar1.count(bs3[2])
                        if bs3[2] != bs3[0] and bs3[2] != bs3[1]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bsx = bss[0].split("x")
                                bss1 = int(bsx[0])
                                betx = int(bsx[1])
                                bss2 = int(bss[1])
                                y480 = bss1 % 120
                                wl6 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3) #12 13 23
                                wl17 = int(wl2)+int(wl4)
                                wl18 = int(wl3)+int(wl4)
                                cvt = (wl16+wl17+wl18)-3
                                ys = wl6
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl16 > wl6:
                                    if y480 == 0:
                                        bet2 = (bss1*1)*betx
                                    else:
                                        bet2 = 999999
                                if wl17 > wl6:
                                    if y480 == 0:
                                        bet3 = (bss1*1)*betx
                                    else:
                                        bet3 = 999999
                                if wl18 > wl6:
                                    if y480 == 0:
                                        bet4 = (bss1*1)*betx
                                    else:
                                        bet4 = 999999
                                if wl6 > wl16 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl6 > wl17 and y480 == 0:
                                    bet6 = (bss1/120*-125)*betx
                                if wl6 > wl18 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                                        
                            elif "-" not in bs[1]:
                                bsx = bs[1].split("x")
                                bet1 = int(bsx[0])
                                betx = int(bsx[1])
                                y480 = bet1 % 120
                                wl6 = int(wl)+int(wl1)
                                wl16 = int(wl2)+int(wl3)
                                wl17 = int(wl2)+int(wl4)
                                wl18 = int(wl3)+int(wl4)
                                cvt = (wl16+wl17+wl18)-3
                                if wl16 > wl6:
                                    if y480 == 0:
                                        bet2 = (bet1*1)*betx
                                    else:
                                        bet2 = 999999
                                if wl17 > wl6:
                                    if y480 == 0:
                                        bet3 = (bet1*1)*betx
                                    else:
                                        bet3 = 999999
                                if wl18 > wl6:
                                    if y480 == 0:
                                        bet4 = (bet1*1)*betx
                                    else:
                                        bet4 = 999999
                                if wl6 > wl16 and y480 == 0:
                                    bet5 = (bet1/120*-125)*betx
                                if wl6 > wl17 and y480 == 0:
                                    bet6 = (bet1/120*-125)*betx
                                if wl6 > wl18 and y480 == 0:
                                    bet7 = (bet1/120*-125)*betx

                        elif bs3[2] == bs3[0] or bs3[2] == bs3[1]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bsx = bss[0].split("x")
                                bss1 = int(bsx[0])
                                betx = int(bsx[1])
                                bss2 = int(bss[1])
                                y480 = bss1 % 120
                                wl6 = int(wl)+int(wl1)    #12
                                wl7 = int(wl) #1
                                wl8 = int(wl1) #2
                                wl9 = int(wl2)+int(wl3)   #34
                                wl10 = int(wl4)   #3
                                cvt = wl8-wl6
                                ys = wl6
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl9 > wl6:
                                    if y480 == 0:
                                        bet2 = (bss1*1)*betx
                                    else:
                                        bet2 = 999999
                                if wl10 > wl7:
                                    if y480 == 0:
                                        bet3 = (bss1*1)*betx
                                    else:
                                        bet3 = 999999
                                if wl10 > wl8:
                                    if y480 == 0:
                                        bet4 = (bss1*1)*betx
                                    else:
                                        bet4 = 999999
                                if wl6 > wl9 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl7 > wl10 and y480 == 0:
                                    bet6 = (bss1/120*-125)*betx
                                if wl8 > wl10 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6

                            elif "-" not in bs[1]:
                                bsx = bs[1].split("x")
                                bet1 = int(bsx[0])
                                betx = int(bsx[1])
                                y480 = bet1 % 120
                                wl6 = int(wl)+int(wl1)    #12
                                wl7 = int(wl) #1
                                wl8 = int(wl1) #2
                                wl9 = int(wl2)+int(wl3)   #34
                                wl10 = int(wl4)   #3
                                cvt = wl8-wl6
                                if wl9 > wl6:
                                    if y480 == 0:
                                        bet2 = (bet1*1)*betx
                                    else:
                                        bet2 = 999999
                                if wl10 > wl7:
                                    if y480 == 0:
                                        bet3 = (bet1*1)*betx
                                    else:
                                        bet3 = 999999
                                if wl10 > wl8:
                                    if y480 == 0:
                                        bet4 = (bet1*1)*betx
                                    else:
                                        bet4 = 999999
                                if wl6 > wl9 and y480 == 0:
                                    bet5 = (bet1/120*-125)*betx
                                if wl7 > wl10 and y480 == 0:
                                    bet6 = (bet1/120*-125)*betx
                                if wl8 > wl10 and y480 == 0:
                                    bet7 = (bet1/120*-125)*betx

                    elif by1 == 3 and yy1 == 2:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs3[0])
                        wl4 = bar1.count(bs3[1])
                        if bs2[0] == bs2[1] or bs2[0] == bs2[2]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bsx = bss[0].split("x")
                                bss1 = int(bsx[0])
                                betx = int(bsx[1])
                                bss2 = int(bss[1]) #80
                                y480 = bss1 % 120
                                wl5 = int(wl)    #1
                                wl6 = int(wl1)+int(wl2)
                                wl7 = int(wl3)+int(wl4)
                                wl8 = int(wl3)  #4 
                                wl9 = int(wl4) #5
                                cvt = wl7-wl6
                                ys = wl6
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl7 > wl6:
                                    if y480 == 0:
                                        bet2 = (bss1*1)*betx
                                    else:
                                        bet2 = 999999
                                if wl8 > wl5:
                                    if y480 == 0:
                                        bet3 = (bss1*1)*betx
                                    else:
                                        bet3 = 999999
                                if wl9 > wl5:
                                    if y480 == 0:
                                        bet4 = (bss1*1)*betx
                                    else:
                                        bet4 = 999999
                                if wl6 > wl7 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl5 > wl8 and y480 == 0:
                                    bet6 = (bss1/120*-125)*betx
                                if wl5 > wl9 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                            elif "-" not in bs[1]:
                                bsx = bs[1].split("x")
                                bet1 = int(bsx[0])
                                betx = int(bsx[1])
                                y480 = bet1 % 120
                                wl5 = int(wl)    #1
                                wl6 = int(wl1)+int(wl2) #12
                                wl7 = int(wl3)+int(wl4) #34
                                wl8 = int(wl3)  #3
                                wl9 = int(wl4) #4
                                cvt = wl7-wl6
                                if wl7 > wl6:
                                    if y480 == 0:
                                        bet2 = (bet1*1)*betx
                                    else:
                                        bet2 = 999999
                                if wl8 > wl5:
                                    if y480 == 0:
                                        bet3 = (bet1*1)*betx
                                    else:
                                        bet3 = 999999
                                if wl9 > wl5:
                                    if y480 == 0:
                                        bet4 = (bet1*1)*betx
                                    else:
                                        bet4 = 999999
                                if wl6 > wl7 and y480 == 0:
                                    bet5 = (bet1/120*-125)*betx
                                if wl5 > wl8 and y480 == 0:
                                    bet6 = (bet1/120*-125)*betx
                                if wl5 > wl9 and y480 == 0:
                                    bet7 = (bet1/120*-125)*betx

                        else:
                            bsx = bs[1].split("x")
                            bet1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bet1 % 120
                            wl5 = int(wl)+int(wl1)   #12
                            wl6 = int(wl)+int(wl2) #13
                            wl7 = int(wl1)+int(wl2) #23
                            wl8 = int(wl3)+int(wl4) #45
                            cvt = 0
                            if wl8 > wl5:
                                bet2 = (bet1*1)*betx
                            if wl8 > wl6:
                                bet3 = (bet1*1)*betx
                            if wl8 > wl7:
                                bet4 = (bet1*1)*betx
                            if wl5 > wl8 and y480 == 0:
                                bet5 = (bet1/120*-125)*betx
                            if wl6 > wl8 and y480 == 0:
                                bet6 = (bet1/120*-125)*betx
                            if wl7 > wl8 and y480 == 0:
                                bet7 = (bet1/120*-125)*betx

                    elif by1 == 3 and yy1 == 3:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs3[0])
                        wl4 = bar1.count(bs3[1])
                        wl5 = bar1.count(bs3[2])
                        if bs2[0] == bs2[1] or bs2[0] == bs2[2]:
                            if "-" in bs[1]:
                                bss = bs[1].split("-")
                                bsx = bss[0].split("x")
                                bss1 = int(bsx[0])
                                betx = int(bsx[1])
                                bss2 = int(bss[1]) #80
                                y480 = bet1 % 120
                                wl6 = int(wl)    #1
                                wl7 = int(wl1)+int(wl2)
                                wl8 = int(wl3)+int(wl4)
                                wl9 = int(wl3)+int(wl5)
                                wl10 = int(wl4)+int(wl5)
                                wl11 = int(wl3)
                                wl12 = int(wl4)
                                wl13 = int(wl5)
                                cvt = 0
                                ys = wl7
                                ys1 = bar1[0] == bar1[1]
                                ys2 = bar1[0] == bar1[2]
                                y20 = bss2 % 20
                                ys1000 = bss2 % 1000
                                if wl8 > wl7:
                                    bet2 = (bss1*1)*betx
                                if wl9 > wl7:
                                    bet3 = (bss1*1)*betx
                                if wl10 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl8 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl7 > wl9 and y480 == 0:
                                    bet6 = (bss1/120*-125)*betx
                                if wl7 > wl10 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl11 > wl6:
                                    bet8 = (bss1*1)*betx
                                if wl12 > wl6:
                                    bet9 = (bss1*1)*betx
                                if wl13 > wl6:
                                    bet10 = (bss1*1)*betx
                                if wl6 > wl11 and y480 == 0:
                                    bet11 = (bss1/120*-125)*betx
                                if wl6 > wl12 and y480 == 0:
                                    bet12 = (bss1/120*-125)*betx
                                if wl6 > wl13 and y480 == 0:
                                    bet13 = (bss1/120*-125)*betx
                                
                                if ys >= 2:
                                    if ys1000 == 0:
                                        bet14 = bss2/1000*-6300
                                    elif bss2 == 500:
                                        bet14 = bss2/500*-3150
                                    elif y20 == 0:
                                        bet14 = bss2/20*-125
                                    elif bss2 == 30:
                                        bet14 = bss2/30*-190
                                    elif bss2 == 50:
                                        bet14 = bss2/50*-315
                                elif ys == 0 and ys2 is True:
                                    bet14 = bss2*3
                                elif ys == 0 and ys1 is True:
                                    bet14 = bss2*5
                                elif ys == 0 and ys1 is False:
                                    bet14 = bss2*6
                            elif "-" not in bs[1]:
                                bsx = bs[1].split("x")
                                bss1 = int(bsx[0])
                                betx = int(bsx[1])
                                y480 = bet1 % 120
                                wl6 = int(wl)    #1
                                wl7 = int(wl1)+int(wl2)
                                wl8 = int(wl3)+int(wl4)
                                wl9 = int(wl3)+int(wl5)
                                wl10 = int(wl4)+int(wl5)
                                wl11 = int(wl3)
                                wl12 = int(wl4)
                                wl13 = int(wl5)
                                cvt = 0
                                if wl8 > wl7:
                                    bet2 = (bss1*1)*betx
                                if wl9 > wl7:
                                    bet3 = (bss1*1)*betx
                                if wl10 > wl7:
                                    bet4 = (bss1*1)*betx
                                if wl7 > wl8 and y480 == 0:
                                    bet5 = (bss1/120*-125)*betx
                                if wl7 > wl9 and y480 == 0:
                                    bet6 = (bss1/120*-125)*betx
                                if wl7 > wl10 and y480 == 0:
                                    bet7 = (bss1/120*-125)*betx
                                if wl11 > wl6:
                                    bet8 = (bss1*1)*betx
                                if wl12 > wl6:
                                    bet9 = (bss1*1)*betx
                                if wl13 > wl6:
                                    bet10 = (bss1*1)*betx
                                if wl6 > wl11 and y480 == 0:
                                    bet11 = (bss1/120*-125)*betx
                                if wl6 > wl12 and y1000 == 0:
                                    bet12 = bss1/1000*-1050
                                if wl6 > wl13 and y480 == 0:
                                    bet13 = (bss1/120*-125)*betx
                        elif bs3[2] == bs3[0] or bs3[2] == bs3[1]:
                            bsx = bs[1].split("x")
                            bss1 = int(bsx[0])
                            betx = int(bsx[1])
                            y480 = bet1 % 120
                            wl6 = int(wl)+int(wl1)
                            wl7 = int(wl)+int(wl2)
                            wl8 = int(wl1)+int(wl2)
                            wl9 = int(wl3)+int(wl4)
                            wl10 = int(wl5)
                            wl11 = int(wl)
                            wl12 = int(wl1)
                            wl13 = int(wl2)
                            cvt = 0
                            if wl9 > wl6:
                                bet2 = (bss1*1)*betx
                            if wl9 > wl7:
                                bet3 = (bss1*1)*betx
                            if wl9 > wl8:
                                bet4 = (bss1*1)*betx
                            if wl6 > wl9 and y480 == 0:
                                bet5 = (bss1/120*-125)*betx
                            if wl7 > wl9 and y480 == 0:
                                bet6 = (bss1/120*-125)*betx
                            if wl8 > wl9 and y480 == 0:
                                bet7 = (bss1/120*-125)*betx
                            if wl10 > wl11:
                                bet8 = (bss1*1)*betx
                            if wl10 > wl12:
                                bet9 = (bss1*1)*betx
                            if wl10 > wl13:
                                bet10 = (bss1*1)*betx
                            if wl11 > wl10 and y480 == 0:
                                bet11 = (bss1/120*-125)*betx
                            if wl12 > wl10 and y480 == 0:
                                bet12 = (bss1/120*-125)*betx
                            if wl13 > wl10 and y480 == 0:
                                bet13 = (bss1/120*-125)*betx

                    elif by1 == 3 and yy1 == 0:
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        wl5 = int(wl)+int(wl1)+int(wl2)  #12
                        cvt = (((int(wl)+int(wl1)+int(wl)+int(wl2)+int(wl1)+int(wl2))*-1)+3) #test
                        if wl5 <= 1:
                            if y480 == 0:
                                bet2 = (bet1*1)*betx
                            else:
                                bet2 = 999999
                        elif wl5 >= 2 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx
                    
                    elif by1 == 0 and yy1 == 3:
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs3[1])
                        wl2 = bar1.count(bs3[2])
                        bsx = bs[1].split("x")
                        bet1 = int(bsx[0])
                        betx = int(bsx[1])
                        y480 = bet1 % 120
                        wl5 = int(wl)+int(wl1)+int(wl2)  #12
                        cvt = ((int(wl)+int(wl1)+int(wl)+int(wl2)+int(wl1)+int(wl2))-3) #test
                        if wl5 >= 2:
                            if y480 == 0:
                                bet2 = (bet1*1)*betx
                            else:
                                bet2 = 999999
                        if wl5 <= 1 and y480 == 0:
                            bet3 = (bet1/120*-125)*betx

                    elif by1 == 2 and yy1 == 0:
                        bet1 = int(bs[1])
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        ys = int(wl)+int(wl1)
                        ys1 = bar1[0] == bar1[1]
                        ys2 = bar1[0] == bar1[2]
                        y20 = bet1 % 20
                        ys1000 = bet1 % 1000
                        if ys >= 2:
                            if ys1000 == 0:
                                bet2 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet2 = bet1/500*-3150
                            elif y20 == 0:
                                bet2 = bet1/20*-125
                            elif bet1 == 30:
                                bet2 = bet1/30*-190
                            elif bet1 == 50:
                                bet2 = bet1/50*-315
                        elif ys == 0 and ys2 is True:
                            bet3 = bet1*3
                        elif ys == 0 and ys1 is True:
                            bet4 = bet1*5
                        elif ys == 0 and ys1 is False:
                            bet5 = bet1*6

                    elif by1 == 4 and yy1 == 0:
                        bet1 = int(bs[1])
                        wl = bar1.count(bs2[0])
                        wl1 = bar1.count(bs2[1])
                        wl2 = bar1.count(bs2[2])
                        wl3 = bar1.count(bs2[3])
                        ys = int(wl)+int(wl1)
                        yss = int(wl2)+int(wl3)
                        ys1 = bar1[0] == bar1[1]
                        ys2 = bar1[0] == bar1[2]
                        y20 = bet1 % 20
                        ys1000 = bet1 % 1000
                        if ys >= 2:
                            if ys1000 == 0:
                                bet2 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet2 = bet1/500*-3150
                            elif y20 == 0:
                                bet2 = bet1/20*-125
                            elif bet1 == 30:
                                bet2 = bet1/30*-190
                            elif bet1 == 50:
                                bet2 = bet1/50*-315
                        elif ys == 0 and ys2 is True:
                            bet3 = bet1*3
                        elif ys == 0 and ys1 is True:
                            bet4 = bet1*5
                        elif ys == 0 and ys1 is False:
                            bet5 = bet1*6
                        if yss >= 2:
                            if ys1000 == 0:
                                bet6 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet6 = bet1/500*-3150
                            elif y20 == 0:
                                bet6 = bet1/20*-125
                            elif bet1 == 30:
                                bet6 = bet1/30*-190
                            elif bet1 == 50:
                                bet6 = bet1/50*-315
                        elif yss == 0 and ys2 is True:
                            bet7 = bet1*3
                        elif yss == 0 and ys1 is True:
                            bet8 = bet1*5
                        elif yss == 0 and ys1 is False:
                            bet9 = bet1*6

                    elif by1 == 0 and yy1 == 2:
                        bet1 = int(bs[1])
                        wl = bar1.count(bs3[0])
                        wl1 = bar1.count(bs3[1])
                        wl6 = int(wl)+int(wl1)
                        ys = wl6
                        ys1 = bar1[0] == bar1[1]
                        ys2 = bar1[0] == bar1[2]
                        y480 = bet1 % 120
                        y20 = bet1 % 20
                        ys1000 = bet1 % 1000
                        if ys >= 2:
                            bet2 = bet1*6
                        elif ys == 0 and ys2 is True:
                            if ys1000 == 0:
                                bet3 = bet1/1000*-3150
                            elif bet1 == 380:
                                bet3 = bet1/380*-1195
                            elif bet1 == 340:
                                bet3 = bet1/340*-1070
                            elif bet1 == 300:
                                bet3 = bet1/300*-945
                            elif bet1 == 500:
                                bet3 = bet1/500*-1550
                            elif bet1 == 260:
                                bet3 = bet1/260*-815
                            elif bet1 == 220:
                                bet3 = bet1/220*-690
                            elif bet1 == 180:
                                bet3 = bet1/180*-565
                            elif bet1 == 140:
                                bet3 = bet1/140*-440
                            elif bet1 == 100:
                                bet3 = bet1/100*-315
                            elif bet1 == 60:
                                bet3 = bet1/60*-190
                            elif bet1 == 20:
                                bet3 = bet1/20*-60
                            elif y20 == 0:
                                bet3 = bet1/20*-62.5
                            elif bet1 == 30:
                                bet3 = bet1/30*-95
                            elif bet1 == 50:
                                bet3 = bet1/50*-155
                        elif ys == 0 and ys1 is True:
                            if ys1000 == 0:
                                bet3 = bet1/1000*-5250
                            elif bet1 == 300:
                                bet3 = bet1/300*-1550
                            elif bet1 == 500:
                                bet3 = bet1/500*-2600
                            elif y20 == 0:
                                bet3 = bet1/20*-105
                            elif bet1 == 30:
                                bet3 = bet1/30*-155
                            elif bet1 == 50:
                                bet3 = bet1/50*-260
                        elif ys == 0 and ys1 is False:
                            if ys1000 == 0:
                                bet4 = bet1/1000*-6300
                            elif bet1 == 500:
                                bet4 = bet1/500*-3150
                            elif y20 == 0:
                                bet4 = bet1/20*-125
                            elif bet1 == 30:
                                bet4 = bet1/30*-190
                            elif bet1 == 50:
                                bet4 = bet1/50*-315

                def scv(a,c,e):
                    if c == 3 and "=" not in a:
                        bcv1 = bar1.count(a[0])
                        bcv2 = bar1.count(a[1])
                        bcv3 = bar1.count(a[2])
                        bcv5 = int(bcv1)+int(bcv2)+int(bcv3)
                        if a[0] == a[1]:
                            if bcv5 == 5 and cvt > 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e*61
                                else:
                                    e = e*51
                            elif bcv5 == 5 and cvt == 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e*60
                                else:
                                    e = e*50
                            elif bcv5 == 5 and cvt < 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e*59
                                else:
                                    e = e*49
                            elif bcv5 != 5 and cvt > 0:
                                e = e*0
                            elif bcv5 != 5 and cvt == 0:
                                e = e*-1
                            elif bcv5 != 5 and cvt < 0:
                                e = e*-2
                        elif a[0] != a[1]:
                            if a == bar1 and cvt > 0:
                                e = e*31
                            elif a == bar1 and cvt == 0:
                                e = e*30
                            elif a == bar1 and cvt < 0:
                                e = e*29
                            elif a != bar1 and cvt > 0:
                                e = e*0
                            elif a != bar1 and cvt == 0:
                                e = e*-1
                            elif a != bar1 and cvt < 0:
                                e = e*-2
                    elif c == 4 and "=" not in a:
                        bcv1 = bar1.count(a[0])
                        bcv2 = bar1.count(a[1])
                        bcv3 = bar1.count(a[2])
                        bcv4 = bar1.count(a[3])
                        bcv5 = int(bcv1)+int(bcv2)+int(bcv3)+int(bcv4)
                        q1 = a[0]+a[1]+a[2]
                        q2 = a[0]+a[1]+a[3]
                        q3 = a[0]+a[2]+a[3]
                        q4 = a[1]+a[2]+a[3]
                        if a[0] == a[1] and a[2] == a[3]: #5566
                            if bcv5 == 6 and bar1[0] == bar1[2]:
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2
                            elif bcv5 == 6 and cvt > 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*61
                                else:
                                    e = e/2*51
                            elif bcv5 == 6 and cvt == 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*59
                                else:
                                    e = e/2*49
                            elif bcv5 == 6 and cvt < 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*57
                                else:
                                    e = e/2*47
                            elif bcv5 != 6 and cvt > 0:                   
                                e = e*0
                            elif bcv5 != 6 and cvt == 0:
                                e = e*-1
                            elif bcv5 != 6 and cvt < 0:
                                e = e*-2
                        
                        elif a[0] == a[1] and a[2] != a[3] and a[0] == a[2]:#4443
                            q1 = a[0]+a[1]+a[2] #444 
                            q2 = a[1]+a[2]+a[3] #443
                            if q1 == bar1:
                                if cvt > 0:
                                    e = e/2*161
                                elif cvt == 0:
                                    e = e/2*159
                                elif cvt < 0:
                                    e = e/2*157
                            elif q2 == bar1 and cvt > 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*61
                                else:
                                    e = e/2*51
                            elif q2 == bar1 and cvt == 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*59
                                else:
                                    e = e/2*49
                            elif q2 == bar1 and cvt < 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*57
                                else:
                                    e = e/2*47
                            elif q1 != bar1 and q2 != bar1 and cvt > 0:                   
                                e = e*0
                            elif q1 != bar1 and q2 != bar1 and cvt == 0:
                                e = e*-1
                            elif q1 != bar1 and q2 != bar1 and cvt < 0:
                                e = e*-2

                        elif a[1] == a[2] and a[0] != a[1] and a[1] == a[3]:#3444
                            q1 = a[1]+a[2]+a[3] #444 
                            q2 = a[1]+a[2]+a[0] #443
                            if q1 == bar1:
                                if cvt > 0:
                                    e = e/2*161
                                elif cvt == 0:
                                    e = e/2*159
                                elif cvt < 0:
                                    e = e/2*157
                            elif q2 == bar1 and cvt > 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*61
                                else:
                                    e = e/2*51
                            elif q2 == bar1 and cvt == 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*59
                                else:
                                    e = e/2*49
                            elif q2 == bar1 and cvt < 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/2*57
                                else:
                                    e = e/2*47
                            elif q1 != bar1 and q2 != bar1 and cvt > 0:                   
                                e = e*0
                            elif q1 != bar1 and q2 != bar1 and cvt == 0:
                                e = e*-1
                            elif q1 != bar1 and q2 != bar1 and cvt < 0:
                                e = e*-2
                        
                        elif a[0] == a[1] and a[2] != a[3] and a[0] != a[2]:#1123
                            q1 = a[0]+a[1]+a[2] #112
                            q2 = a[0]+a[1]+a[3] #113
                            q3 = a[1]+a[2]+a[3] #123
                            if q3 == bar1:
                                if cvt > 0:
                                    e = e/3*31
                                elif cvt == 0:
                                    e = e/3*28
                                elif cvt < 0:
                                    e = e/3*25
                            elif q1 == bar1 or q2 == bar1:
                                if cvt > 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*61
                                    else:
                                        e = e/3*51
                                elif cvt == 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*58
                                    else:
                                        e = e/3*48
                                elif cvt < 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*55
                                    else:
                                        e = e/3*45
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt > 0:                   
                                e = e*0
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt == 0:
                                e = e*-1
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt < 0:
                                e = e*-2

                        elif a[0] != a[1] and a[2] != a[3] and a[1] == a[2]:#1223
                            q1 = a[1]+a[2]+a[3] #223
                            q2 = a[1]+a[2]+a[0] #221
                            q3 = a[0]+a[2]+a[3] #123
                            if q3 == bar1:
                                if cvt > 0:
                                    e = e/3*31
                                elif cvt == 0:
                                    e = e/3*28
                                elif cvt < 0:
                                    e = e/3*25
                            elif q1 == bar1 or q2 == bar1:
                                if cvt > 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*61
                                    else:
                                        e = e/3*51
                                elif cvt == 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*58
                                    else:
                                        e = e/3*48
                                elif cvt < 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*55
                                    else:
                                        e = e/3*45
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt > 0:                   
                                e = e*0
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt == 0:
                                e = e*-1
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt < 0:
                                e = e*-2

                        elif a[0] != a[1] and a[2] == a[3] and a[1] != a[2]:#1233
                            q1 = a[2]+a[3]+a[0] #331
                            q2 = a[2]+a[3]+a[1] #332
                            q3 = a[0]+a[1]+a[2] #123
                            if q3 == bar1:
                                if cvt > 0:
                                    e = e/3*31
                                elif cvt == 0:
                                    e = e/3*28
                                elif cvt < 0:
                                    e = e/3*25
                            elif q1 == bar1 or q2 == bar1:
                                if cvt > 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*61
                                    else:
                                        e = e/3*51
                                elif cvt == 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*58
                                    else:
                                        e = e/3*48
                                elif cvt < 0:
                                    if bar1 == "665" or bar1 == "112":
                                        e = e/3*55
                                    else:
                                        e = e/3*45
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt > 0:                   
                                e = e*0
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt == 0:
                                e = e*-1
                            elif q1 != bar1 and q2 != bar1 and q3 != bar1 and cvt < 0:
                                e = e*-2

                        elif a[0] != a[1] and a[2] != a[3]:#1234
                            if q1 == bar1 or q2 == bar1 or q3 == bar1 or q4 == bar1: 
                                if cvt > 0:
                                    e = e/4*31
                                elif cvt == 0:
                                    e = e/4*27
                                elif cvt < 0:
                                    e = e/4*23
                            else: 
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2

                    elif c == 6 and "=" not in a:
                        q1 = a[0]+a[1]+a[2] 
                        q2 = a[0]+a[1]+a[4]
                        q3 = a[2]+a[3]+a[0]
                        q4 = a[2]+a[3]+a[4]
                        q5 = a[4]+a[5]+a[0]
                        q6 = a[4]+a[5]+a[2]
                        if q1 == bar1 or q2 == bar1 or q3 == bar1 or q4 == bar1 or q5 == bar1 or q6 == bar1:
                            if cvt > 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/6*61
                                else:
                                    e = e/6*51
                            elif cvt == 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/6*55
                                else:
                                    e = e/6*45
                            elif cvt < 0:
                                if bar1 == "665" or bar1 == "112":
                                    e = e/6*49
                                else:
                                    e = e/6*39
                        elif q1 != bar1 and q2 != bar1 and q3 != bar1 and q4 != bar1 and q5 != bar1 and q6 != bar1:
                            if cvt > 0:                   
                                e = e*0
                            elif cvt == 0:
                                e = e*-1
                            elif cvt < 0:
                                e = e*-2

                    elif "=" in a:
                        ss2 = a.split("=")
                        ss4 = ss2[0]
                        ss = ss4.count("1")+ss4.count("2")+ss4.count("3")+ss4.count("4")+ss4.count("5")+ss4.count("6")
                        if ss == 1:
                            q1 = ss4[0]+ss4[0]+ss4[0]
                            if bar1 == q1:
                                if cvt > 0:
                                    e = e*161
                                elif cvt == 0:
                                    e = e*160
                                elif cvt < 0:
                                    e = e*159
                            elif bar1 != q1:
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2
                        elif ss == 2:
                            q1 = ss4[0]+ss4[0]+ss4[0]
                            q2 = ss4[1]+ss4[1]+ss4[1]
                            if bar1 == q1 or bar1 == q2:
                                if cvt > 0:
                                    e = e/2*161
                                elif cvt == 0:
                                    e = e/2*159
                                elif cvt < 0:
                                    e = e/2*157
                            elif bar1 != q1 or bar1 != q2:
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2
                        elif ss == 3:
                            q1 = ss4[0]+ss4[0]+ss4[0]
                            q2 = ss4[1]+ss4[1]+ss4[1]
                            q3 = ss4[2]+ss4[2]+ss4[2]
                            if bar1 == q1 or bar1 == q2 or bar1 == q3:
                                if cvt > 0:
                                    e = e/3*161
                                elif cvt == 0:
                                    e = e/3*158
                                elif cvt < 0:
                                    e = e/3*155
                            elif bar1 != q1 or bar1 != q2 or bar1 != q3:
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2
                        elif ss == 4:
                            q1 = ss4[0]+ss4[0]+ss4[0]
                            q2 = ss4[1]+ss4[1]+ss4[1]
                            q3 = ss4[2]+ss4[2]+ss4[2]
                            q4 = ss4[3]+ss4[3]+ss4[3]
                            if bar1 == q1 or bar1 == q2 or bar1 == q3 or bar1 == q4:
                                if cvt > 0:
                                    e = e/4*161
                                elif cvt == 0:
                                    e = e/4*157
                                elif cvt < 0:
                                    e = e/4*153
                            elif bar1 != q1 or bar1 != q2 or bar1 != q3 or bar1 != q4:
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2
                        elif ss == 5:
                            q1 = ss4[0]+ss4[0]+ss4[0]
                            q2 = ss4[1]+ss4[1]+ss4[1]
                            q3 = ss4[2]+ss4[2]+ss4[2]
                            q4 = ss4[3]+ss4[3]+ss4[3]
                            q5 = ss4[4]+ss4[4]+ss4[4]
                            if bar1 == q1 or bar1 == q2 or bar1 == q3 or bar1 == q4 or bar1 == q5:
                                if cvt > 0:
                                    e = e/5*161
                                elif cvt == 0:
                                    e = e/5*156
                                elif cvt < 0:
                                    e = e/5*151
                            elif bar1 != q1 or bar1 != q2 or bar1 != q3 or bar1 != q4 or bar1 != q5:
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2
                        elif ss == 6:
                            q1 = ss4[0]+ss4[0]+ss4[0]
                            q2 = ss4[1]+ss4[1]+ss4[1]
                            q3 = ss4[2]+ss4[2]+ss4[2]
                            q4 = ss4[3]+ss4[3]+ss4[3]
                            q5 = ss4[4]+ss4[4]+ss4[4]
                            q6 = ss4[5]+ss4[5]+ss4[5]
                            if bar1 == q1 or bar1 == q2 or bar1 == q3 or bar1 == q4 or bar1 == q5 or bar1 == q6:
                                if cvt > 0:
                                    e = e/5*161
                                elif cvt == 0:
                                    e = e/5*156
                                elif cvt < 0:
                                    e = e/5*151
                            elif bar1 != q1 or bar1 != q2 or bar1 != q3 or bar1 != q4 or bar1 != q5 or bar1 != q6:
                                if cvt > 0:
                                    e = e*0
                                elif cvt == 0:
                                    e = e*-1
                                elif cvt < 0:
                                    e = e*-2                  

                    return e

                def ds(a,b):
                    if a == point:
                        if point == "3":
                            if cvt > 0:
                                b = b*161
                            elif cvt == 0:
                                b = b*160
                            elif cvt < 0:
                                b = b*159
                        elif point == "4":
                            if cvt > 0:
                                b = b*61
                            elif cvt == 0:
                                b = b*60
                            elif cvt < 0:
                                b = b*59
                        elif point == "5":
                            if cvt > 0:
                                b = b*31
                            elif cvt == 0:
                                b = b*30
                            elif cvt < 0:
                                b = b*29
                        elif point == "6":
                            if cvt > 0:
                                b = b*19
                            elif cvt == 0:
                                b = b*18
                            elif cvt < 0:
                                b = b*17
                        elif point == "7":
                            if cvt > 0:
                                b = b*13
                            elif cvt == 0:
                                b = b*12
                            elif cvt < 0:
                                b = b*11
                        elif point == "8":
                            if cvt > 0:
                                b = b*9
                            elif cvt == 0:
                                b = b*8
                            elif cvt < 0:
                                b = b*7
                        elif point == "9":
                            if cvt > 0:
                                b = b*8
                            elif cvt == 0:
                                b = b*7
                            elif cvt < 0:
                                b = b*6
                        elif point == "10":
                            if cvt > 0:
                                b = b*8
                            elif cvt == 0:
                                b = b*7
                            elif cvt < 0:
                                b = b*6
                        elif point == "11":
                            if cvt > 0:
                                b = b*8
                            elif cvt == 0:
                                b = b*7
                            elif cvt < 0:
                                b = b*6
                        elif point == "12":
                            if cvt > 0:
                                b = b*8
                            elif cvt == 0:
                                b = b*7
                            elif cvt < 0:
                                b = b*6
                        elif point == "13":
                            if cvt > 0:
                                b = b*9
                            elif cvt == 0:
                                b = b*8
                            elif cvt < 0:
                                b = b*7
                        elif point == "14":
                            if cvt > 0:
                                b = b*13
                            elif cvt == 0:
                                b = b*12
                            elif cvt < 0:
                                b = b*11
                        elif point == "15":
                            if cvt > 0:
                                b = b*19
                            elif cvt == 0:
                                b = b*18
                            elif cvt < 0:
                                b = b*17
                        elif point == "16":
                            if cvt > 0:
                                b = b*31
                            elif cvt == 0:
                                b = b*30
                            elif cvt < 0:
                                b = b*29
                        elif point == "17":
                            if cvt > 0:
                                b = b*61
                            elif cvt == 0:
                                b = b*60
                            elif cvt < 0:
                                b = b*59
                        elif point == "18":
                            if cvt > 0:
                                b = b*161
                            elif cvt == 0:
                                b = b*160
                            elif cvt < 0:
                                b = b*159
                    else:
                        if cvt > 0:
                            b = b*0
                        elif cvt == 0:
                            b = b*-1
                        elif cvt < 0:
                            b = b*-2

                    return b
                    


                if "cv" in bet:
                    cc = bs[2].count("+")
                    if cc == 0:
                        if "cv" in bs[2]:
                            cb = bs[2].count("-")
                            qz = bs[0].split("*")
                            cvv = qz[1]
                            a1 = cvv.count("1")
                            a2 = cvv.count("2")
                            a3 = cvv.count("3")
                            a4 = cvv.count("4")
                            a5 = cvv.count("5")
                            a6 = cvv.count("6")
                            qz1 = int(a1)+int(a2)+int(a3)+int(a4)+int(a5)+int(a6)
                            if cb == 0:
                                if qz1 == 2:
                                    bscv = bs[2].split("cv")
                                    betcv = int(bscv[0])
                                    cvv1 = cvv[0]+cvv[0]+cvv[1]+cvv[1]
                                    c1 = cvv1.count("1")
                                    c2 = cvv1.count("2")
                                    c3 = cvv1.count("3")
                                    c4 = cvv1.count("4")
                                    c5 = cvv1.count("5")
                                    c6 = cvv1.count("6")
                                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                                    #cv1[0] #cv1[1] #cv2 #bet10 #betcv
                                    bet15 = scv(cvv1,cv2,betcv)
                                elif qz1 == 3:
                                    bscv = bs[2].split("cv")
                                    betcv = int(bscv[0])
                                    cvv1 = cvv[0]+cvv[0]+cvv[1]+cvv[1]+cvv[2]+cvv[2]
                                    c1 = cvv1.count("1")
                                    c2 = cvv1.count("2")
                                    c3 = cvv1.count("3")
                                    c4 = cvv1.count("4")
                                    c5 = cvv1.count("5")
                                    c6 = cvv1.count("6")
                                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                                    #cv1[0] #cv1[1] #cv2 #bet10 #betcv
                                    bet15 = scv(cvv1,cv2,betcv)
                            if cb == 1:
                                if qz1 == 2:
                                    bscv = bs[2].split("cv")
                                    bscvv = bscv[0].split("-")
                                    betcv = int(bscvv[0])
                                    betcv1 = int(bscvv[1])
                                    cvv1 = cvv[0]+cvv[0]+cvv[1]+cvv[1]
                                    cvv2 = cvv[0]+cvv[1]+"="
                                    c1 = cvv1.count("1")
                                    c2 = cvv1.count("2")
                                    c3 = cvv1.count("3")
                                    c4 = cvv1.count("4")
                                    c5 = cvv1.count("5")
                                    c6 = cvv1.count("6")
                                    cc1 = cvv2.count("1")
                                    cc2 = cvv2.count("2")
                                    cc3 = cvv2.count("3")
                                    cc4 = cvv2.count("4")
                                    cc5 = cvv2.count("5")
                                    cc6 = cvv2.count("6")
                                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                                    cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                                    bet15 = scv(cvv1,cv2,betcv)
                                    bet16 = scv(cvv2,cv3,betcv1)
                                elif qz1 == 3:
                                    bscv = bs[2].split("cv")
                                    bscvv = bscv[0].split("-")
                                    betcv = int(bscvv[0])
                                    betcv1 = int(bscvv[1])
                                    cvv1 = cvv[0]+cvv[0]+cvv[1]+cvv[1]+cvv[2]+cvv[2]
                                    cvv2 = cvv[0]+cvv[1]+cvv[2]+"="
                                    c1 = cvv1.count("1")
                                    c2 = cvv1.count("2")
                                    c3 = cvv1.count("3")
                                    c4 = cvv1.count("4")
                                    c5 = cvv1.count("5")
                                    c6 = cvv1.count("6")
                                    cc1 = cvv2.count("1")
                                    cc2 = cvv2.count("2")
                                    cc3 = cvv2.count("3")
                                    cc4 = cvv2.count("4")
                                    cc5 = cvv2.count("5")
                                    cc6 = cvv2.count("6")
                                    cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                                    cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                                    bet15 = scv(cvv1,cv2,betcv)
                                    bet16 = scv(cvv2,cv3,betcv1)
                        else:
                            bscv = bs[3].split("cv")
                            betcv = int(bscv[0])
                            cvv1 = bs[2]
                            c1 = cvv1.count("1")
                            c2 = cvv1.count("2")
                            c3 = cvv1.count("3")
                            c4 = cvv1.count("4")
                            c5 = cvv1.count("5")
                            c6 = cvv1.count("6")
                            cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                            #cv1[0] #cv1[1] #cv2 #bet10 #betcv
                            bet15 = scv(cvv1,cv2,betcv)
                        

                    if cc == 1:
                        cv = bs[2].split("+")
                        bscv = bs[3].split("cv")
                        bscvv = bscv[0].split("-")
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        cvv1 = cv[0]
                        cvv2 = cv[1]
                        c1 = cvv1.count("1")
                        c2 = cvv1.count("2")
                        c3 = cvv1.count("3")
                        c4 = cvv1.count("4")
                        c5 = cvv1.count("5")
                        c6 = cvv1.count("6")
                        cc1 = cvv2.count("1")
                        cc2 = cvv2.count("2")
                        cc3 = cvv2.count("3")
                        cc4 = cvv2.count("4")
                        cc5 = cvv2.count("5")
                        cc6 = cvv2.count("6")
                        cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                        cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                        bet15 = scv(cvv1,cv2,betcv)
                        bet16 = scv(cvv2,cv3,betcv1)
                    
                    if cc == 2:
                        cv = bs[2].split("+")
                        bscv = bs[3].split("cv")
                        bscvv = bscv[0].split("-")
                        betcv2 = int(bscvv[2])
                        cvv3 = cv[2]
                        ccc1 = cvv3.count("1")
                        ccc2 = cvv3.count("2")
                        ccc3 = cvv3.count("3")
                        ccc4 = cvv3.count("4")
                        ccc5 = cvv3.count("5")
                        ccc6 = cvv3.count("6")
                        cv4 = int(ccc1)+int(ccc2)+int(ccc3)+int(ccc4)+int(ccc5)+int(ccc6)
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        cvv1 = cv[0]
                        cvv2 = cv[1]
                        c1 = cvv1.count("1")
                        c2 = cvv1.count("2")
                        c3 = cvv1.count("3")
                        c4 = cvv1.count("4")
                        c5 = cvv1.count("5")
                        c6 = cvv1.count("6")
                        cc1 = cvv2.count("1")
                        cc2 = cvv2.count("2")
                        cc3 = cvv2.count("3")
                        cc4 = cvv2.count("4")
                        cc5 = cvv2.count("5")
                        cc6 = cvv2.count("6")
                        cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                        cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                        bet15 = scv(cvv1,cv2,betcv)
                        bet16 = scv(cvv2,cv3,betcv1)
                        bet17 = scv(cvv3,cv4,betcv2)

                    if cc == 3:
                        cv = bs[2].split("+")
                        bscv = bs[3].split("cv")
                        bscvv = bscv[0].split("-")
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        betcv2 = int(bscvv[2])
                        betcv3 = int(bscvv[3])
                        cvv1 = cv[0]
                        cvv2 = cv[1]
                        cvv3 = cv[2]
                        cvv4 = cv[3]
                        c1 = cvv1.count("1")
                        c2 = cvv1.count("2")
                        c3 = cvv1.count("3")
                        c4 = cvv1.count("4")
                        c5 = cvv1.count("5")
                        c6 = cvv1.count("6")
                        cc1 = cvv2.count("1")
                        cc2 = cvv2.count("2")
                        cc3 = cvv2.count("3")
                        cc4 = cvv2.count("4")
                        cc5 = cvv2.count("5")
                        cc6 = cvv2.count("6")
                        ccc1 = cvv3.count("1")
                        ccc2 = cvv3.count("2")
                        ccc3 = cvv3.count("3")
                        ccc4 = cvv3.count("4")
                        ccc5 = cvv3.count("5")
                        ccc6 = cvv3.count("6")
                        cccc1 = cvv4.count("1")
                        cccc2 = cvv4.count("2")
                        cccc3 = cvv4.count("3")
                        cccc4 = cvv4.count("4")
                        cccc5 = cvv4.count("5")
                        cccc6 = cvv4.count("6")
                        cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                        cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                        cv4 = int(ccc1)+int(ccc2)+int(ccc3)+int(ccc4)+int(ccc5)+int(ccc6)
                        cv5 = int(cccc1)+int(cccc2)+int(cccc3)+int(cccc4)+int(cccc5)+int(cccc6)
                        bet15 = scv(cvv1,cv2,betcv)
                        bet16 = scv(cvv2,cv3,betcv1)
                        bet17 = scv(cvv3,cv4,betcv2)
                        bet18 = scv(cvv4,cv5,betcv3)

                    if cc == 4:
                        cv = bs[2].split("+")
                        bscv = bs[3].split("cv")
                        bscvv = bscv[0].split("-")
                        betcv = int(bscvv[0])
                        betcv1 = int(bscvv[1])
                        betcv2 = int(bscvv[2])
                        betcv3 = int(bscvv[3])
                        betcv4 = int(bscvv[4])
                        cvv1 = cv[0]
                        cvv2 = cv[1]
                        cvv3 = cv[2]
                        cvv4 = cv[3]
                        cvv5 = cv[4]
                        c1 = cvv1.count("1")
                        c2 = cvv1.count("2")
                        c3 = cvv1.count("3")
                        c4 = cvv1.count("4")
                        c5 = cvv1.count("5")
                        c6 = cvv1.count("6")
                        cc1 = cvv2.count("1")
                        cc2 = cvv2.count("2")
                        cc3 = cvv2.count("3")
                        cc4 = cvv2.count("4")
                        cc5 = cvv2.count("5")
                        cc6 = cvv2.count("6")
                        ccc1 = cvv3.count("1")
                        ccc2 = cvv3.count("2")
                        ccc3 = cvv3.count("3")
                        ccc4 = cvv3.count("4")
                        ccc5 = cvv3.count("5")
                        ccc6 = cvv3.count("6")
                        cccc1 = cvv4.count("1")
                        cccc2 = cvv4.count("2")
                        cccc3 = cvv4.count("3")
                        cccc4 = cvv4.count("4")
                        cccc5 = cvv4.count("5")
                        cccc6 = cvv4.count("6")
                        ccccc1 = cvv5.count("1")
                        ccccc2 = cvv5.count("2")
                        ccccc3 = cvv5.count("3")
                        ccccc4 = cvv5.count("4")
                        ccccc5 = cvv5.count("5")
                        ccccc6 = cvv5.count("6")
                        cv2 = int(c1)+int(c2)+int(c3)+int(c4)+int(c5)+int(c6)
                        cv3 = int(cc1)+int(cc2)+int(cc3)+int(cc4)+int(cc5)+int(cc6)
                        cv4 = int(ccc1)+int(ccc2)+int(ccc3)+int(ccc4)+int(ccc5)+int(ccc6)
                        cv5 = int(cccc1)+int(cccc2)+int(cccc3)+int(cccc4)+int(cccc5)+int(cccc6)
                        cv6 = int(ccccc1)+int(ccccc2)+int(ccccc3)+int(ccccc4)+int(ccccc5)+int(ccccc6)
                        bet15 = scv(cvv1,cv2,betcv)
                        bet16 = scv(cvv2,cv3,betcv1)
                        bet17 = scv(cvv3,cv4,betcv2)
                        bet18 = scv(cvv4,cv5,betcv3)
                        bet19 = scv(cvv5,cv6,betcv4)

                if "cv" in bet and "-" in bs[2] and "cv" not in bs[2]:
                    cc = bs[2].count("+")
                    bs1 = bs[2].split("-")
                    bet10 = 0
                    bet11 = 0
                    bet12 = 0
                    if cc == 0:
                        dss1 = bs1[1]
                        betd = bs[3].split("cv")
                        betds1 = int(betd[0])
                        bet15 = ds(dss1,betds1)
                    elif cc == 1:
                        ds1 = bs1[1].split("+")
                        betd = bs[3].split("cv")
                        betds = betd[0].split("-")
                        dss1 = ds1[0]
                        dss2 = ds1[1]
                        betds1 = int(betds[0])
                        betds2 = int(betds[1])
                        bet15 = ds(dss1,betds1)
                        bet16 = ds(dss2,betds2)
                    elif cc == 2:
                        ds1 = bs1[1].split("+")
                        betd = bs[3].split("cv")
                        betds = betd[0].split("-")
                        dss1 = ds1[0]
                        dss2 = ds1[1]
                        dss3 = ds1[2]
                        betds1 = int(betds[0])
                        betds2 = int(betds[1])
                        betds3 = int(betds[2])
                        bet15 = ds(dss1,betds1)
                        bet16 = ds(dss2,betds2)
                        bet17 = ds(dss3,betds3)
                
                winlose = bet2+bet3+bet4+bet5+bet6+bet7+bet8+bet9+bet10+bet11+bet12+bet13+bet14+bet15+bet16+bet17+bet18+bet19

            if "w" in bs[0]:
                ws = bs[0].split("w")
                wl1 = ws[0].count("1")
                wl2 = ws[0].count("2")
                wl3 = ws[0].count("3")
                wl4 = ws[0].count("4")
                wl5 = ws[0].count("5")
                wl6 = ws[0].count("6")
                wt = wl1+wl2+wl3+wl4+wl5+wl6
                if wt == 0:
                    bet1 = int(bs[1])
                    y480 = bet1 % 120
                    y100 = bet1 % 100 
                    y1000 = bet1 % 1000 
                    y580 = (bet1-480) % 100 
                    y340 = (bet1-240) % 100 
                    wl7 = bar1.count(ws[1])
                    ys1 = bar1[0] == bar1[1]
                    ys2 = bar1[0] == bar1[2]
                    if wl7 == 1:
                        winlose = bet1*3
                    elif wl7 >= 2:
                        winlose = bet1*5
                    elif wl7 == 0 and ys2 is True and y1000 == 0:
                        winlose = bet1/1000*-1050
                    elif wl7 == 0 and ys2 is True and y480 == 0:
                        winlose = bet1/120*-125
                    elif wl7 == 0 and ys2 is True and y580 == 0:
                        winlose = (((bet1-480)/100*-105)-500)
                    elif wl7 == 0 and ys2 is True and y340 == 0:
                        winlose = (((bet1-240)/100*-105)-250)
                    elif wl7 == 0 and ys2 is True and y100 == 0:
                        winlose = bet1/100*-105    
                    elif wl7 == 0 and ys1 is True and y1000 == 0:
                        winlose = bet1/1000*-2100
                    elif wl7 == 0 and ys1 is True and y480 == 0:
                        winlose = bet1/120*-250
                    elif wl7 == 0 and ys1 is True and y580 == 0:
                        winlose = (((bet1-480)/100*-105)-500)*2
                    elif wl7 == 0 and ys1 is True and y340 == 0:
                        winlose = (((bet1-240)/100*-105)-250)*2
                    elif wl7 == 0 and ys1 is True and y100 == 0:
                        winlose = bet1/100*-210
                    elif wl7 == 0 and ys2 is False and ys1 is False and y1000 == 0:
                        winlose = bet1/1000*-3150
                    elif wl7 == 0 and ys2 is False and ys1 is False and y480 == 0:
                        winlose = bet1/120*-375
                    elif wl7 == 0 and ys2 is False and ys1 is False and y580 == 0:
                        winlose = (((bet1-480)/100*-105)-500)*3
                    elif wl7 == 0 and ys2 is False and ys1 is False and y340 == 0:
                        winlose = (((bet1-240)/100*-105)-250)*3
                    elif wl7 == 0 and ys2 is False and ys1 is False and y100 == 0:
                        winlose = bet1/100*-315    
                elif wt != 0:
                    bet1 = int(bs[1])
                    y480 = bet1 % 120
                    y100 = bet1 % 100 
                    y1000 = bet1 % 1000
                    y580 = (bet1-480) % 100  
                    y340 = (bet1-240) % 100 
                    wl7 = bar1.count(ws[0])
                    ys1 = bar1[0] == bar1[1]
                    ys2 = bar1[0] == bar1[2]
                    if wl7 == 1 and y1000 == 0:
                        winlose = bet1/1000*-3150
                    elif wl7 == 1 and y480 == 0:
                        winlose = bet1/120*-375
                    elif wl7 == 1 and y580 == 0:
                        winlose = (((bet1-480)/100*-105)-500)*3
                    elif wl7 == 1 and y340 == 0:
                        winlose = (((bet1-240)/100*-105)-250)*3
                    elif wl7 == 1 and y100 == 0:
                        winlose = bet1/100*-315
                    elif wl7 >= 2 and y1000 == 0:
                        winlose = bet1/1000*-5250
                    elif wl7 >= 2 and y480 == 0:
                        winlose = bet1/120*-625
                    elif wl7 >= 2 and y580 == 0:
                        winlose = (((bet1-480)/100*-105)-500)*5
                    elif wl7 >= 2 and y340 == 0:
                        winlose = (((bet1-240)/100*-105)-250)*5
                    elif wl7 >= 2 and y100 == 0:
                        winlose = bet1/100*-525
                    elif wl7 == 0 and ys2 is True:
                        winlose = bet1*1
                    elif wl7 == 0 and ys1 is True:
                        winlose = bet1*2     
                    elif wl7 == 0 and ys2 is False and ys1 is False:
                        winlose = bet1*3 
            #-----------------------------------------------
            #----------------ds-------------------------
            #-----------------------------------------------

            def ds(a,b):
                if a == point:
                    if point == "3":
                        b = b*160
                    elif point == "4":
                        b = b*60
                    elif point == "5":
                        b = b*30
                    elif point == "6":
                        b = b*18
                    elif point == "7":
                        b = b*12
                    elif point == "8":
                        b = b*8
                    elif point == "9":
                        b = b*7
                    elif point == "10":
                        b = b*7
                    elif point == "11":
                        b = b*7
                    elif point == "12":
                        b = b*7
                    elif point == "13":
                        b = b*8
                    elif point == "14":
                        b = b*12
                    elif point == "15":
                        b = b*18
                    elif point == "16":
                        b = b*30
                    elif point == "17":
                        b = b*60
                    elif point == "18":
                        b = b*160
                else:
                    b = b*-1

                return b

            if "-" in bs[0]:
                cc = bs[0].count("+")
                bs1 = bs[0].split("-")
                bet10 = 0
                bet11 = 0
                bet12 = 0
                bet13 = 0
                bet14 = 0
                if cc == 0:
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        betds1 = int(bs[1])
                        dss1 = bs1[1]
                        bet10 = ds(dss1,betds1)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:
                        if "cvb" in bet:
                            betd = bs[1].split("cvb")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                            elif int(point) <=10:
                                bet10 = bet10 - betds1
                            elif int(point) >=11:
                                bet10 = bet10 + betds1

                        elif "cvs" in bet:
                            betd = bs[1].split("cvs")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                            elif int(point) >=11:
                                bet10 = bet10 - betds1
                            elif int(point) <=10:
                                bet10 = bet10 + betds1

                        elif "cvc" in bet:
                            betd = bs[1].split("cvc")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betds1
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betds1

                        elif "cv00" in bet:
                            betd = bs[1].split("cv00")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            y1 = int(bar) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                            elif y1 != 0:
                                bet10 = bet10 - betds1
                            elif y1 == 0:
                                bet10 = bet10 + betds1

                        elif "cv0" in bet:
                            betd = bs[1].split("cv0")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            y1 = int(bar) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                            elif y1 == 0:
                                bet10 = bet10 - betds1
                            elif y1 != 0:
                                bet10 = bet10 + betds1

                        elif "cv12" in bet:
                            betd = bs[1].split("cv12")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betds1
                            else:
                                bet10 = bet10 + betds1

                        elif "cv13" in bet:
                            betd = bs[1].split("cv13")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betds1
                            else:
                                bet10 = bet10 + betds1

                        elif "cv14" in bet:
                            betd = bs[1].split("cv14")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betds1
                            else:
                                bet10 = bet10 + betds1

                        elif "cv23" in bet:
                            betd = bs[1].split("cv23")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betds1
                            else:
                                bet10 = bet10 + betds1

                        elif "cv24" in bet:
                            betd = bs[1].split("cv24")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betds1
                            else:
                                bet10 = bet10 + betds1

                        elif "cv34" in bet:
                            betd = bs[1].split("cv34")
                            betds1 = int(betd[0])
                            dss1 = bs1[1]
                            bet10 = ds(dss1,betds1)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betds1
                            else:
                                bet10 = bet10 + betds1
                elif cc == 1:
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        ds1 = bs1[1].split("+")
                        betds = bs[1].split("-")
                        dss1 = ds1[0]
                        dss2 = ds1[1]
                        betds1 = int(betds[0])
                        betds2 = int(betds[1])
                        bet10 = ds(dss1,betds1)
                        bet11 = ds(dss2,betds2)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:
                        if "cvb" in bet:
                            bs2 = bs[1].split("cvb")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif int(point) <=10:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif int(point) >=11:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cvs" in bet:
                            bs2 = bs[1].split("cvs")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif int(point) >=11:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif int(point) <=10:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cvc" in bet:
                            bs2 = bs[1].split("cvc")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv00" in bet:
                            bs2 = bs[1].split("cv00")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            y1 = int(point) % 2
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif y1 != 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv0" in bet:
                            bs2 = bs[1].split("cv0")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            y1 = int(point) % 2
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            elif y1 == 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv12" in bet:
                            bs2 = bs[1].split("cv12")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv13" in bet:
                            bs2 = bs[1].split("cv13")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv14" in bet:
                            bs2 = bs[1].split("cv14")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv23" in bet:
                            bs2 = bs[1].split("cv23")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv24" in bet:
                            bs2 = bs[1].split("cv24")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2

                        elif "cv34" in bet:
                            bs2 = bs[1].split("cv34")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2


                elif cc == 2:
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        ds1 = bs1[1].split("+")
                        betds = bs[1].split("-")
                        dss1 = ds1[0]
                        dss2 = ds1[1]
                        dss3 = ds1[2]
                        betds1 = int(betds[0])
                        betds2 = int(betds[1])
                        betds3 = int(betds[2])
                        bet10 = ds(dss1,betds1)
                        bet11 = ds(dss2,betds2)
                        bet12 = ds(dss3,betds3)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:
                        if "cvb" in bet:
                            bs2 = bs[1].split("cvb")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif int(point) <=10:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif int(point) >=11:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cvs" in bet:
                            bs2 = bs[1].split("cvs")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif int(point) >=11:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif int(point) <=10:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cvc" in bet:
                            bs2 = bs[1].split("cvc")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv00" in bet:
                            bs2 = bs[1].split("cv00")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            y1 = int(point) % 2
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif y1 != 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv0" in bet:
                            bs2 = bs[1].split("cv0")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            y1 = int(point) % 2
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            elif y1 == 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv12" in bet:
                            bs2 = bs[1].split("cv12")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv13" in bet:
                            bs2 = bs[1].split("cv13")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv14" in bet:
                            bs2 = bs[1].split("cv14")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv23" in bet:
                            bs2 = bs[1].split("cv23")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv24" in bet:
                            bs2 = bs[1].split("cv24")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                        elif "cv34" in bet:
                            bs2 = bs[1].split("cv34")
                            ds1 = bs1[1].split("+")
                            betds = bs2[0].split("-")
                            dss1 = ds1[0]
                            dss2 = ds1[1]
                            dss3 = ds1[2]
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3

                elif cc == 3:
                    ds1 = bs1[1].split("+")
                    dss1 = ds1[0]
                    dss2 = ds1[1]
                    dss3 = ds1[2]
                    dss4 = ds1[3]
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        betds = bs[1].split("-")
                        betds1 = int(betds[0])
                        betds2 = int(betds[1])
                        betds3 = int(betds[2])
                        betds4 = int(betds[3])
                        bet10 = ds(dss1,betds1)
                        bet11 = ds(dss2,betds2)
                        bet12 = ds(dss3,betds3)
                        bet13 = ds(dss4,betds4)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:
                        if "cvb" in bet:
                            bs2 = bs[1].split("cvb")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif int(point) <=10:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif int(point) >=11:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cvs" in bet:
                            bs2 = bs[1].split("cvs")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif int(point) >=11:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif int(point) <=10:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cvc" in bet:
                            bs2 = bs[1].split("cvc")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv00" in bet:
                            bs2 = bs[1].split("cv00")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif y1 != 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv0" in bet:
                            bs2 = bs[1].split("cv0")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            elif y1 == 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv12" in bet:
                            bs2 = bs[1].split("cv12")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv13" in bet:
                            bs2 = bs[1].split("cv13")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv14" in bet:
                            bs2 = bs[1].split("cv14")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv23" in bet:
                            bs2 = bs[1].split("cv23")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv24" in bet:
                            bs2 = bs[1].split("cv24")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4

                        elif "cv34" in bet:
                            bs2 = bs[1].split("cv34")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                
                elif cc == 4:
                    ds1 = bs1[1].split("+")
                    dss1 = ds1[0]
                    dss2 = ds1[1]
                    dss3 = ds1[2]
                    dss4 = ds1[3]
                    dss5 = ds1[4]
                    if "cvb" not in bet and "cvs" not in bet and "cvc" not in bet and "cv0" not in bet and "cv00" not in bet and "cv12" not in bet and "cv13" not in bet and "cv14" not in bet and "cv23" not in bet and "cv24" not in bet and "cv34" not in bet:
                        betds = bs[1].split("-")
                        betds1 = int(betds[0])
                        betds2 = int(betds[1])
                        betds3 = int(betds[2])
                        betds4 = int(betds[3])
                        betds5 = int(betds[4])
                        bet10 = ds(dss1,betds1)
                        bet11 = ds(dss2,betds2)
                        bet12 = ds(dss3,betds3)
                        bet13 = ds(dss4,betds4)
                        bet14 = ds(dss5,betds5)
                    elif "cvb" in bet or "cvs" in bet or "cvc" in bet or "cv0" in bet or "cv00" in bet in bet or "cv12" in bet or "cv13" in bet or "cv14" in bet or "cv23" in bet or "cv24" in bet or "cv34" in bet:
                        if "cvb" in bet:
                            bs2 = bs[1].split("cvb")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif int(point) <=10:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif int(point) >=11:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cvs" in bet:
                            bs2 = bs[1].split("cvs")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif int(point) >=11:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif int(point) <=10:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cvc" in bet:
                            bs2 = bs[1].split("cvc")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar1 == "111" or bar1 == "222" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif int(point) >= 13 or int(point) <= 8:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif 9<= int(point) <=12:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv00" in bet:
                            bs2 = bs[1].split("cv00")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif y1 != 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv0" in bet:
                            bs2 = bs[1].split("cv0")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            y1 = int(point) % 2
                            if bar1 == "111" or bar1 == "222" or bar1 == "333" or bar1 == "444" or bar1 == "555" or bar1 == "666":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            elif y1 == 0:
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv12" in bet:
                            bs2 = bs[1].split("cv12")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar == "3" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv13" in bet:
                            bs2 = bs[1].split("cv13")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar == "2" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv14" in bet:
                            bs2 = bs[1].split("cv14")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar == "2" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv23" in bet:
                            bs2 = bs[1].split("cv23")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar == "1" or bar == "4":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv24" in bet:
                            bs2 = bs[1].split("cv24")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar == "1" or bar == "3":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5

                        elif "cv34" in bet:
                            bs2 = bs[1].split("cv34")
                            betds = bs2[0].split("-")
                            betds1 = int(betds[0])
                            betds2 = int(betds[1])
                            betds3 = int(betds[2])
                            betds4 = int(betds[3])
                            betds5 = int(betds[4])
                            bet10 = ds(dss1,betds1)
                            bet11 = ds(dss2,betds2)
                            bet12 = ds(dss3,betds3)
                            bet13 = ds(dss4,betds4)
                            bet14 = ds(dss5,betds5)
                            if bar == "1" or bar == "2":
                                bet10 = bet10 - betds1
                                bet11 = bet11 - betds2
                                bet12 = bet12 - betds3
                                bet13 = bet13 - betds4
                                bet14 = bet14 - betds5
                            else:
                                bet10 = bet10 + betds1
                                bet11 = bet11 + betds2
                                bet12 = bet12 + betds3
                                bet13 = bet13 + betds4
                                bet14 = bet14 + betds5
                winlose = bet10+bet11+bet12+bet13+bet14

            def fc1():
                bs1 = bs[0].split("-")
                bet01 = int(bs[1])
                if bs1[0] in bar1 and bs1[1] in bar1:
                    if bar1[0] == bar1[1]:
                        winlose = bet01*7
                    elif bar1[0] != bar1[1]:
                        winlose = bet01*5
                else:
                    winlose = bet01*-1
                return winlose

            def fc2():
                bet01 = int(bs[1])
                bs1 = bs[0].split("-")
                if bs1[0] == bar1[0] and bs1[1] == bar1[1]:
                    winlose = bet01*11
                else:
                    winlose = bet01*-1
                return winlose

            if bs[0] == "1-2":
                winlose = fc1()

            elif bs[0] == "1-3":
                winlose = fc1()

            elif bs[0] == "1-4":
                winlose = fc1()

            elif bs[0] == "1-5":
                winlose = fc1()

            elif bs[0] == "1-6":
                winlose = fc1()

            elif bs[0] == "2-3":
                winlose = fc1()

            elif bs[0] == "2-4":
                winlose = fc1()

            elif bs[0] == "2-5":
                winlose = fc1()

            elif bs[0] == "2-6":
                winlose = fc1()

            elif bs[0] == "3-4":
                winlose = fc1()

            elif bs[0] == "3-5":
                winlose = fc1()

            elif bs[0] == "3-6":
                winlose = fc1()

            elif bs[0] == "4-5":
                winlose = fc1()

            elif bs[0] == "4-6":
                winlose = fc1()

            elif bs[0] == "5-6":
                winlose = fc1()

            elif bs[0] == "1-1":
                winlose = fc2()

            elif bs[0] == "2-2":
                winlose = fc2()

            elif bs[0] == "3-3":
                winlose = fc2()

            elif bs[0] == "4-4":
                winlose = fc2()

            elif bs[0] == "5-5":
                winlose = fc2()

            elif bs[0] == "6-6":
                winlose = fc2()

            if "d" in bs[0]:
                bs1 = bs[0].split("d")
                bet1 = int(bs[1])
                bs2 = bar1.count(bs1[1])
                if bs2 == 3:
                    winlose = bet1*3
                elif bs2 == 2:
                    winlose = bet1*2
                elif bs2 == 1:
                    winlose = bet1*1
                else:
                    winlose = bet1*-1

            if bs[0] == "yy":
                winlose = int(bs[1])*1
                
            if bs[0] == "ss":
                winlose = int(bs[1])*-1

        except:
            winlose = 888888

    return winlose
