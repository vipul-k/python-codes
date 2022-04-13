# -*- coding: utf-8 -*-
import unittest
import graph

class test_graph(unittest.TestCase):
    
    def test_add_edge(self):
        graph.add_edge((4,6))
        self.assertTrue(6 in graph and 4 in graph)
        self.assertFalse(6 not in graph or 4 not in graph)
        
    def test_add_node(self):
        graph.add_edge(6)
        self.assertTrue(6 in graph)
        self.assertFalse(6 not in graph)
        
    def test_in(self):
        self.assertTrue(1 in graph)
        self.assertFalse(1 not in graph)
        
    def test_subscript(self):
        self.assertEqual(graph[1],[2,5])
        
    def test_distance(self):
        self.assertEqual(graph.distance(1,3),2)

