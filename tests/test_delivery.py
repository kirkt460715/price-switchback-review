"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        plan = read_table("plan.json")
        paid = read_table("orders.json")
        self.assertTrue({r["window"] for r in paid} <= {r["window"] for r in plan})
        self.assertTrue({r["order"] for r in read_table("refunds.json")} <= {r["id"] for r in paid})
        hits = {r["pair"] for r in plan if r["window"] in
                {e["window"] for e in read_table("exposure.json") if e["register_down"]}}
        self.assertEqual(len([r for r in plan if r["pair"] in hits]), 2)
