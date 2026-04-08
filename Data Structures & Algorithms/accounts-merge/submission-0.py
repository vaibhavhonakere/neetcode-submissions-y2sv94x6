class DSU:
    
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*(n)

    def find(self, n1):
        res = n1
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res
    
    def union(self, n1, n2):
        par_1 = self.find(n1)
        par_2 = self.find(n2)

        if(par_1 == par_2):
            return False

        if(self.rank[par_1] > self.rank[par_2]):
            self.rank[par_1] += self.rank[par_2]
            self.par[par_2] = par_1
        else:
            self.rank[par_2] += self.rank[par_1]
            self.par[par_1] = par_2
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = DSU(n)

        emailToAcc = {}  # email -> index of acc

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if(email in emailToAcc):
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i
        
        # print(uf.par)
        # print(uf.rank)

        email_group = defaultdict(list) # {account_index: emails_associated}

        for e, i in emailToAcc.items():
            account_index = uf.find(i)
            email_group[account_index].append(e)
        
        ret = []
        for idx, emails in email_group.items():
            tmp = []
            tmp.append(accounts[idx][0])
            emails.sort()
            tmp += emails
            ret.append(tmp)
        
        return ret














        