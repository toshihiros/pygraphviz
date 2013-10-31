# -*- coding: utf-8 -*-
from nose.tools import *
import pygraphviz as pgv

def test_subgraph_cluster():
    G = pgv.AGraph(label='foo')
    s = G.subgraph('cluster_a', label='<Hello<BR/>World>')
    s.add_node('sa')
    G.add_node('a')
    assert_equal(G.string().expandtabs(2),
"""strict graph {
  graph [label=foo];
  {
    graph [label=<Hello<BR/>World>];
    sa;
  }
  a;
}
""")

def test_subgraph_cluster_attribute():
    G = pgv.AGraph()
    s = G.subgraph(name='cluster_a')
    s.node_attr['foo']='bar'
    G.add_node('a')
    G.node_attr['foo']='baz'
    assert_equal(G.string().expandtabs(2),
"""strict graph {
  node [foo=baz];
  subgraph cluster_a {
    graph [foo=bar];
  }
  a;
}
""")
