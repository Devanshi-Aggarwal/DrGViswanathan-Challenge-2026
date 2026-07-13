class Solution(object):
    def averageOfLevels(self, root):
        ans = []
        queue = [root]
        while queue:
            cur_sum = 0
            cur_cnt = len(queue)
            for _ in range(cur_cnt):
                cur_node = queue.pop(0)
                cur_sum += cur_node.val
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            ans.append(cur_sum / float(cur_cnt))
        return ans
        
