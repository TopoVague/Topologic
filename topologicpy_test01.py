import  topologicpy 
print(topologicpy.__version__)

from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Topology import Topology
from topologicpy.Graph import Graph
from topologicpy.Dictionary import Dictionary
from topologicpy.Plotly import Plotly

#create some geometry
#TO figure out how to import
p = CellComplex.Prism(width=2, uSides=5, vSides=4, placement ="bottom")
c = Cell.Prism(width=0.8, height=1.2, placement="bottom")
p=Topology.Impose(p,c)
c=Cell.Prism(width=0.8, height=1.2, placement="bottom")
p =Topology.Merge (p,c)

Topology.Show(p)