import re
from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        n = len(code)
        category = set(["electronics", "grocery", "pharmacy", "restaurant"])
        result = []
        for i in range(n):
            c, bl, a = code[i], businessLine[i], isActive[i]
            if not c:
                continue

            if not re.match(r"^[a-zA-z0-9_]+$", c):
                continue

            if bl not in category:
                continue

            if not a:
                continue

            obj = {"code": c, "businessLine": bl, "isActive": a}
            result.append(obj)

        result.sort(key=lambda x: (x["businessLine"], x["code"]))

        return [obj["code"] for obj in result]
