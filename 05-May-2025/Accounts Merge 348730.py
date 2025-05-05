# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts)+1)]
        rank = [0 for _ in range(len(accounts) + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                elif rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                else:
                    parent[rooty] = rootx
                    rank[rootx] += 1
        email_to_index = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(i,email_to_index[email])
                else:
                    email_to_index[email] = i
        index_to_emails = defaultdict(list)
        for email,idx in email_to_index.items():
            root = find(idx)
            index_to_emails[root].append(email)
        result = []
        for root_index,email_list in index_to_emails.items():
            name = accounts[root_index][0]
            result.append([name] + sorted(email_list))
        return result

                    
         

        