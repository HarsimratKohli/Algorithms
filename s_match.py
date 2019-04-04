import random
# Stable Match Problem
def stable_match(men,women):
    marriage = []

    # Len marriage should be according to len of pref list
    while len(marriage) <= len(women.get(1)["Pref"]):

        # print(women.get(1)["Pref"])
        # print(len(women.get(1)["Pref"]))
        # break
        for man_id ,man_info in men.items():

            #if man is un-engaged
            if man_id not in [x[0] for x in marriage]:

                # engage him with a woman of his highest Pref if not already Proposed
                pref =men[man_id]['Pref'] # Man's Preference List
                status =men[man_id]['Proposed'] # Status Of The women in pref list (i.e proposed)


                # iterate over men's preference list
                for i in range(len(pref)):

                    # check is he has not proposed that woman
                    if not status[i]:

                        # Checking woman's preference
                        w_pref=women[pref[i]]['Pref']

                        #if woman is engaged , look for better man
                        if any(pref[i] == x[1] for x in marriage):
                            married_men,married_women = zip(*marriage)
                            married_man = married_men[married_women.index(pref[i])] # Id of the man married to the current woman


                            # Man inside women pref
                            if man_id in w_pref:

                                # if married man not in women's pref
                                if married_man not in w_pref:
                                    marriage.append([man_id, pref[i]])
                                    status[i] = True
                                    break

                                #if marriage is not stable
                                elif w_pref.index(man_id) < w_pref.index(married_man):
                                     marriage[list(married_men).index(married_man)][0] = man_id
                                     status[i]=True
                                     break

                                # if the marriage Is stable
                                else:
                                    continue

                            # When man not in woman's pref list
                            else:
                                continue

                        #if the woman is not engaged
                        else:
                            if man_id in w_pref:
                                marriage.append([man_id,pref[i]])
                                status[i]=True
                                break

    return marriage

def gen_inputs(n):
    men = {}
    women = {}
    # print("Men:",n)
    for i in range(1,n+1):
        men[i] ={}
        women[i] ={}

        men[i]["Pref"]=random.sample(range(1,n), int(n/2))
        men[i]["Proposed"] = [False for i in range(int(n/2))]
    for i in range(1, n + 1):
        women[i]["Pref"]=random.sample(range(1,n), int(n/2))

    # print(men.values())
    # print(women.values())
    return men,women

# men = {1:{'Pref':[1,3],'Proposed':[False,False]},
#        2:{'Pref':[2,3],'Proposed':[False,False]},
#        3:{'Pref':[2,3],'Proposed':[False,False]},
#        4:{'Pref':[1,3],'Proposed':[False,False]},
#        }
#
# women = {1:{'Pref':[1,2]},
#          2:{'Pref':[2,1]},
#          3:{'Pref':[1,3]},
#          4:{'Pref':[2,3]},
#         }

men_avg=0
women_avg=0
men,women = gen_inputs(500)
married_list = stable_match(men,women)
# print("Marriage List:",married_list)
print("No. of Matches:",len(married_list))

for man_id,woman_id in married_list:
    man_pref = men[man_id]['Pref'].index(woman_id)+1
    woman_pref =women[woman_id]['Pref'].index(man_id)+1
    men_avg += man_pref
    women_avg += woman_pref
    # print("Man :",man_id,"got Preference:",man_pref,
    # "\t Woman :",woman_id,"got Preference:",woman_pref)
print("Average Preference - Men:",men_avg/len(men),"Women:",women_avg/len(women))
