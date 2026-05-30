class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        my_dic = Counter(tasks)
        steps = 0
        while my_dic:
            top = my_dic.most_common(n + 1)
            #size_top = len(top)
            for i in range(n+1):
                if top:
                    task, _ = top.pop(0)
                    my_dic[task] -= 1
                    steps +=1
                    if my_dic[task] == 0:
                        del my_dic[task]
                elif my_dic: 
                    steps += (n + 1- i)
                    break
                elif top and my_dic:
                    break

        return steps