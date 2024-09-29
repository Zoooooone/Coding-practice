import unittest
from LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """初始化链表，避免在每个测试函数中重复创建"""
        self.ll = LinkedList()

    def test_empty_list(self):
        """测试空链表"""
        self.assertEqual(self.ll.head, None)
        self.assertEqual(self.ll.length(), 0)

    def test_create_list(self):
        """测试创建非空链表"""
        self.ll.create([1, 2, 3, 4, 5])
        self.assertEqual(self.ll.length(), 5)
        self.assertEqual(self.ll.head.val, 1)
        self.assertEqual(self.ll.getVal(4), 5)

    def test_find(self):
        """测试查找节点"""
        self.ll.create([1, 2, 3])
        node = self.ll.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.val, 2)

        node = self.ll.find(4)
        self.assertIsNone(node)

    def test_getVal(self):
        """测试获取节点值"""
        self.ll.create([1, 2, 3])
        self.assertEqual(self.ll.getVal(1), 2)
        self.assertEqual(self.ll.getVal(5), "Error")
        self.assertEqual(self.ll.getVal(-1), "Error")

    def test_insertFront(self):
        """测试前端插入"""
        self.ll.create([1, 2, 3])
        self.ll.insertFront(0)
        self.assertEqual(self.ll.head.val, 0)

    def test_insertRear(self):
        """测试后端插入"""
        self.ll.create([1, 2, 3])
        self.ll.insertRear(4)
        self.assertEqual(self.ll.getVal(3), 4)

    def test_insertInside(self):
        """测试中间插入"""
        self.ll.create([1, 2, 4])
        self.ll.insertInside(2, 3)
        self.assertEqual(self.ll.getVal(2), 3)

    def test_update(self):
        """测试更新节点"""
        self.ll.create([1, 2, 3])
        self.ll.update(1, 20)
        self.assertEqual(self.ll.getVal(1), 20)

        result = self.ll.update(5, 50)
        self.assertEqual(result, "Error")

    def test_deleteFront(self):
        """测试前端删除"""
        self.ll.create([1, 2, 3])
        self.ll.deleteFront()
        self.assertEqual(self.ll.head.val, 2)
        self.ll.deleteFront()
        self.ll.deleteFront()
        self.assertIsNone(self.ll.head)

    def test_deleteRear(self):
        """测试后端删除"""
        self.ll.create([1, 2, 3])
        self.ll.deleteRear()
        self.assertEqual(self.ll.getVal(1), 2)
        self.ll.deleteRear()
        self.ll.deleteRear()
        self.assertIsNone(self.ll.head)

    def test_deleteInside(self):
        """测试中间删除"""
        self.ll.create([1, 2, 3, 4])
        self.ll.deleteInside(1)
        self.assertEqual(self.ll.getVal(1), 3)

        result = self.ll.deleteInside(0)
        self.assertEqual(result, "Error")

        result = self.ll.deleteInside(5)
        self.assertEqual(result, "Error")


if __name__ == "__main__":
    unittest.main()
