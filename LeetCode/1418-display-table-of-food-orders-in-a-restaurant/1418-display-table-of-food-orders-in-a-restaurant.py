class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_info = {}
        for _, table, food in orders:
            if table in table_info:
                table_info[table][food] += 1
            else:
                table_info[table] = defaultdict(int)
                table_info[table][food] = 1
        
        menu_set = set()
        for _, v in table_info.items():
            for menu_name in v.keys():
                menu_set.add(menu_name)
        
        menu_list = sorted(list(menu_set))
        idx_info = {menu:i+1 for i, menu in enumerate(menu_list)}
        first = ["Table"] + menu_list
        result = [first]

        for _, v in table_info.items():
            for menu_name in v.keys():
                menu_set.add(menu_name)
        
        table_details = []
        for k, v in table_info.items():
            temp = [str(k)] + ["0"]*len(idx_info)
            for menu, cnt in v.items():
                temp[idx_info[menu]] = str(cnt)

            table_details.append(temp)
            
        table_details.sort(key=lambda x: int(x[0]))
        for detail in table_details:
            result.append(detail)
        
        return result

