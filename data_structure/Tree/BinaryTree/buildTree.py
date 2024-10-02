class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def build_tree(nums: list) -> TreeNode:
    if not nums:
        return None

    # 使用队列来辅助构建二叉树,队列中存放的是这颗二叉树的一个个节点
    queue = []
    root = TreeNode(nums[0])
    queue.append(root)
    i = 1

    while i < len(nums):  # 当i遍历完nums，构造完成
        current_node = queue.pop(0)

        # 构建左子节点
        if nums[i] is not None:
            current_node.left = TreeNode(nums[i])
            queue.append(current_node.left)  # 将构造好的左子节点加入队列，等待后续对其子树部分的构造
        i += 1

        # 构建右子节点
        if i < len(nums) and nums[i] is not None:  # 这里多了一个i的判断是因为第25行处对i进行了自加一，这时i是有可能超出nums的索引范围的
            current_node.right = TreeNode(nums[i])
            queue.append(current_node.right)
        i += 1

    return root


class Traverse:
    def __init__(self):
        self.level_res = []
        self.DLR_recur_res = []
        self.LDR_recur_res = []
        self.LRD_recur_res = []

    # 层序遍历, 使用广度优先探索
    def level_traverse(self, root: TreeNode) -> list:
        if not root:
            return None

        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                else:
                    level.append(None)
                    continue
                queue.append(node.left)
                queue.append(node.right)

            self.level_res.append(level)

        return self.level_res[:-1]

    # 前序遍历, 递归
    def DLR_recursion(self, root: TreeNode) -> None:
        if not root:
            return

        self.DLR_recur_res.append(root.val)
        self.DLR_recursion(root.left)
        self.DLR_recursion(root.right)

    # 前序遍历, 迭代
    def DLR_iteration(self, root: TreeNode) -> list:
        stk = [root]  # 根节点入栈，利用栈实现前序遍历
        res = []  # 用于存放遍历结果的数组

        while stk:  # 栈为空时遍历结束
            node = stk.pop()  # 弹出栈顶的节点
            if not node:  # 如果该节点为None, 说明这个子树探索到头了，需要返回上一个节点，上一个节点还在栈的内部等待弹出
                continue
            res.append(node.val)  # 因为是前序遍历，所以一旦访问到子树的根节点就把它对应的值存入数组中

            """核心环节: 前序遍历本该是按照中左右的顺序遍历, 而这里入栈顺序是先右后左.
            道理也很简单, 因为栈是后进先出, 所以后进的左子节点会在下一次循环中先被弹出, 也即先被遍历到"""
            stk.append(node.right)
            stk.append(node.left)

        return res

    # 中序遍历, 递归
    def LDR_recursion(self, root: TreeNode) -> None:
        if not root:
            return

        self.LDR_recursion(root.left)
        self.LDR_recur_res.append(root.val)
        self.LDR_recursion(root.right)

    # 中序遍历, 迭代
    def LDR_iteration(self, root: TreeNode) -> list:
        cur = root
        stack = []
        res = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res

    # 后序遍历, 递归
    def LRD_recursion(self, root: TreeNode) -> None:
        if not root:
            return

        self.LRD_recursion(root.left)
        self.LRD_recursion(root.right)
        self.LRD_recur_res.append(root.val)

    # 后序遍历, 迭代
    def LRD_iteration(self, root: TreeNode) -> list:
        stack = []
        cur, pre = root, None
        res = []

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if (not cur.right) or cur.right == pre:
                    res.append(cur.val)
                    pre, cur = cur, None
                else:
                    stack.append(cur)
                    cur = cur.right

        return res


if __name__ == "__main__":
    # 示例使用：
    nums1, nums2 = [1, 2, 3, 4, 5, None, 7, None, None, 8], list(range(1, 16))
    root1, root2 = build_tree(nums1), build_tree(nums2)
    '''       1                                        1
             *  *                                  *       *
            2    3                               2           3
          *  *    *                           *   *         *   *
        4     5    7                        4      5       6      7
             *                            *  *   *  *     *  *   *  *
            8                           8    9  10  11   12  13 14   15

        *** Results ***

        level_traverse:     	[1],[2, 3],[4, 5, None, 7],[None, None, 8, None, None, None]	[1],[2, 3],[4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14, 15]

        Preorder-recursion: 	1, 2, 4, 5, 8, 3, 7 	1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15
        Preorder-iteration: 	1, 2, 4, 5, 8, 3, 7 	1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15

        Inorder-recursion:  	4, 2, 8, 5, 1, 3, 7 	8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15
        Inorder-iteration:  	4, 2, 8, 5, 1, 3, 7 	8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15

        Postorder-recursion: 	4, 8, 5, 2, 7, 3, 1 	8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1
        Postorder-iteration: 	4, 8, 5, 2, 7, 3, 1 	8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1
    '''
    # 层序遍历结果
    print("{0:<20}\t{1:<20}\t{2:<20}".format("level_traverse:", ",".join(str(i) for i in Traverse().level_traverse(root1)), ",".join(str(i) for i in Traverse().level_traverse(root2))))

    # 前序遍历-递归 结果
    res1, res2 = Traverse(), Traverse()
    res1.DLR_recursion(root1), res2.DLR_recursion(root2)
    print("\n{0:<20}\t{1:<20}\t{2:<20}".format("Preorder-recursion: ", ", ".join(str(i) for i in res1.DLR_recur_res), ", ".join(str(i) for i in res2.DLR_recur_res)))

    # 前序遍历-迭代 结果
    print("{0:<20}\t{1:<20}\t{2:<20}".format("Preorder-iteration: ", ", ".join(str(i) for i in Traverse().DLR_iteration(root1)), ", ".join(str(i) for i in Traverse().DLR_iteration(root2))))

    # 中序遍历-递归 结果
    res3, res4 = Traverse(), Traverse()
    res3.LDR_recursion(root1), res4.LDR_recursion(root2)
    print("\n{0:<20}\t{1:<20}\t{2:<20}".format("Inorder-recursion: ", ", ".join(str(i) for i in res3.LDR_recur_res), ", ".join(str(i) for i in res4.LDR_recur_res)))

    # 中序遍历-迭代 结果
    print("{0:<20}\t{1:<20}\t{2:<20}".format("Inorder-iteration: ", ", ".join(str(i) for i in Traverse().LDR_iteration(root1)), ", ".join(str(i) for i in Traverse().LDR_iteration(root2))))

    # 后序遍历-递归 结果
    res5, res6 = Traverse(), Traverse()
    res5.LRD_recursion(root1), res6.LRD_recursion(root2)
    print("\n{0:<20}\t{1:<20}\t{2:<20}".format("Postorder-recursion: ", ", ".join(str(i) for i in res5.LRD_recur_res), ", ".join(str(i) for i in res6.LRD_recur_res)))

    # 后序遍历-迭代 结果
    print("{0:<20}\t{1:<20}\t{2:<20}".format("Postorder-iteration: ", ", ".join(str(i) for i in Traverse().LRD_iteration(root1)), ", ".join(str(i) for i in Traverse().LRD_iteration(root2))))
