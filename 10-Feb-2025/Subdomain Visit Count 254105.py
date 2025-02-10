# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domains=Counter()
        for cpdomain in cpdomains:
            rep=int(cpdomain.split()[0])
            sub=cpdomain.split()[1]
            domain=sub.split(".")
            for i in range(len(domain)):
                subdomain=".".join(domain[i:])
                domains[subdomain]+=rep
        res=[str(count)+" "+domain for domain, count in domains.items()]
        return res
                

