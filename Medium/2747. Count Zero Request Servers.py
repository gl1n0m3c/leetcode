# URL: https://leetcode.com/problems/count-zero-request-servers/description/

class Solution(object):
    def countServers(self, n, logs, x, queries):
        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()
        print(queries)
        logs = sorted(logs, key=lambda y: y[1])
        ans = [0] * len(queries)
        servers = []
        server_counter = [0]*n
        finish = queries[0][0]
        start = finish - x
        for i in range(len(logs)):
            if start <= logs[i][1] <= finish:
                server_counter[logs[i][0] - 1] += 1
                servers.append(logs[i])
            if logs[i][1] > finish:  # time
                 break
        count = 0
        for t in server_counter:
            if t == 0:
                count += 1
        ans[0] = count
        servers = sorted(servers, key=lambda y: y[1])
        for finish, j in queries:
            while i < len(logs) and logs[i][1] <= finish:
                if server_counter[logs[i][0] - 1] == 0:
                     count -= 1
                servers.append(logs[i])
                server_counter[logs[i][0] - 1] += 1
                i += 1
            while len(servers) > 0 and servers[0][1] < finish - x:
                server_counter[servers[0][0] - 1] -= 1
                if server_counter[servers[0][0] - 1] == 0:
                    count += 1
                servers.pop(0)
            ans[j] = count
        return ans