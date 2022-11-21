

def countItems(items, ruleKey, ruleValue):
    ruleKeys = {"type":0, "color":1, "name":2}
    count =0
    for item in items:
        if item[ruleKeys[ruleKey]] == ruleValue:
            count +=1
    return count

print(countItems(items = [["phone","blue","pixel"],
                          ["computer","silver","lenovo"],
                          ["phone","gold","iphone"]], 
                 ruleKey = "color", ruleValue = "silver"))