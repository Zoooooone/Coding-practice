import unittest
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        """初始化链表，避免在每个测试函数中重复创建"""
        self.dll = DoublyLinkedList()

    def test_empty_list(self):
        """测试空链表的遍历"""
        self.assertEqual(self.dll.head, None)
        self.assertEqual(self.dll.tail, None)
        self.dll.displayForward()  # Expected output: "The list is empty."
        self.dll.displayBackward()  # Expected output: "The list is empty."

    def test_create_list(self):
        """测试创建链表"""
        self.dll.create([1, 2, 3, 4, 5])
        self.assertEqual(self.dll.head.val, 1)
        self.assertEqual(self.dll.tail.val, 5)
        self.dll.displayForward()  # Expected output: 1 2 3 4 5
        self.dll.displayBackward()  # Expected output: 5 4 3 2 1

    def test_insert_front(self):
        """测试前端插入"""
        self.dll.create([1, 2, 3])
        self.dll.insertFront(0)
        self.assertEqual(self.dll.head.val, 0)
        self.assertEqual(self.dll.head.next.val, 1)

    def test_insert_rear(self):
        """测试后端插入"""
        self.dll.create([1, 2, 3])
        self.dll.insertRear(4)
        self.assertEqual(self.dll.tail.val, 4)
        self.assertEqual(self.dll.tail.prev.val, 3)

    def test_delete_front(self):
        """测试前端删除"""
        self.dll.create([1, 2, 3])
        self.dll.deleteFront()
        self.assertEqual(self.dll.head.val, 2)
        self.dll.deleteFront()
        self.dll.deleteFront()
        self.assertEqual(self.dll.head, None)
        self.assertEqual(self.dll.tail, None)

    def test_delete_rear(self):
        """测试后端删除"""
        self.dll.create([1, 2, 3])
        self.dll.deleteRear()
        self.assertEqual(self.dll.tail.val, 2)
        self.dll.deleteRear()
        self.dll.deleteRear()
        self.assertEqual(self.dll.head, None)
        self.assertEqual(self.dll.tail, None)

    def test_delete_empty(self):
        """测试从空链表删除元素"""
        self.assertFalse(self.dll.deleteFront())
        self.assertFalse(self.dll.deleteRear())

    def test_single_element(self):
        """测试仅有一个元素的情况"""
        self.dll.insertFront(10)
        self.assertEqual(self.dll.head.val, 10)
        self.assertTrue(self.dll.deleteFront())
        self.assertIsNone(self.dll.head)

        self.dll.insertRear(20)
        self.assertEqual(self.dll.tail.val, 20)
        self.assertTrue(self.dll.deleteRear())
        self.assertIsNone(self.dll.tail)


if __name__ == "__main__":
    unittest.main()
