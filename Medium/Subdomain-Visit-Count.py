# Problem description
# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, 
# we have "com", at the next level, we have "leetcode.com" and at the lowest level, 
# "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", 
# we will also visit the parent domains "leetcode.com" and "com" implicitly.

# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" 
# or "rep d1.d2" where rep is the number of visits to the domain and d1.d2.d3 is 
# the domain itself.

# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates 
# that discuss.leetcode.com was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired 
# domains of each subdomain in the input. You may return the answer in any order.

# EXAMPLE:
# Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: ["901 mail.com","50 yahoo.com","900 google.mail.com",
#               "5 wiki.org","5 org","1 intel.mail.com","951 com"]

# Explanation: We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" 
# once and "wiki.org" 5 times.
# For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, 
# and "org" 5 times.

from __future__ import annotations
from collections import defaultdict
from typing import List

def subdomainVisits(cpdomains: List[str]) -> List[str]:
    res = []

    for s in cpdomains:
        # split the cpdomain into rep and domain
        rep, domain = s.split()
        
        # splitting the domain at '.'
        d_split = domain.split('.')

        # making sub cpdomains
        for i in range(len(d_split)):
            sub_cp_domain = rep+" "+d_split[i]+"."+".".join(d_split[i+1:])
            res.append(sub_cp_domain)
            
        # removing the '.' from the last sub cpdomain in list
        res[-1] = res[-1].removesuffix('.')

    # creating a default dictionary of lists
    dd = defaultdict(list)
    
    # for going through each sub cpdomains
    for d in res:
        # splitting
        split = d.split()
        
        # mapping the domain with the list of its count
        dd[split[1]].append(int(split[0]))
    
    # an empty list to store final results
    output = []
    for x in dd:
        # summing up the lists and converting into list to make cpdomains
        output.append(str(sum(dd[x]))+" "+x)
        
    # return the final list of outputs
    return output