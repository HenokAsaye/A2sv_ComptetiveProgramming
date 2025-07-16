# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        email_to_index = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(i, email_to_index[email])
                email_to_index[email] = i
        index_to_emails = defaultdict(set)
        for email, idx in email_to_index.items():
            root = find(idx)
            index_to_emails[root].add(email)
        result = []
        for idx, emails in index_to_emails.items():
            name = accounts[idx][0]
            result.append([name] + sorted(emails))

        return result
