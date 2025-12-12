from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
        n = numberOfUsers
        mentions = [0] * n
        online = [0] * n
        for event_type, time, mention_str in events:
            if event_type == "OFFLINE":
                idx = int(mention_str)
                online[idx] = int(time) + 60
                continue

            if mention_str == "ALL":
                for i in range(n):
                    mentions[i] += 1
            elif mention_str == "HERE":
                t = int(time)
                for i in range(n):
                    if online[i] <= t:
                        mentions[i] += 1
            else:
                for mention in mention_str.split():
                    idx = int(mention[2:])
                    mentions[idx] += 1

        return mentions
