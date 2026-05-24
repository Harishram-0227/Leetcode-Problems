from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = deque()
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.appendleft(level)

        return list(res)