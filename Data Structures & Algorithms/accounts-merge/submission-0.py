from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_ids = {} # email -> email_id
        emails = [] # all distinct emails
        email_to_acc = {} # email -> acc_id

        m = 0
        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                email = acc[j]
                if email in email_ids:
                    continue
                emails.append(email)
                email_ids[email] = m
                email_to_acc[m] = i
                m += 1 
        
        adj = [[] for _ in range(m)] # email_id -> all it's neihbours

        for acc in accounts:
            for j in range(2, len(acc)):
                id_1 = email_ids[acc[j]]
                id_2 = email_ids[acc[j-1]]
                adj[id_1].append(id_2)
                adj[id_2].append(id_1)

        email_group = defaultdict(list) # acc_id -> emails list
        visited = [False]*m

        def dfs(email_id, account):
            visited[email_id] = True
            email_group[account].append(emails[email_id])
            for m_id in adj[email_id]:
                if not visited[m_id]:
                    dfs(m_id, account)

        for i in range(m):
            if not visited[i]:
                dfs(i, email_to_acc[i])
        
        res = []
        for i in email_group:
            acc_name = accounts[i][0]
            res.append([acc_name] + sorted(email_group[i]))

        return res