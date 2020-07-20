#!/usr/bin/python


from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.cli import CLI

class MyTopology(Topo):
    """
    A basic topology
    """
    def __init__(self):
      Topo.__init__(self)

        # Set Up Topology Here
      switch = self.addSwitch('s1') ## Adds a Switch
          
      host1 = self.addHost('h1')    ## Adds a Host
      host2 = self.addHost('h2')	## Adds second Host
      host3 = self.addHost('h3')	## Adds third Host
      host4 = self.addHost('h4')	## Adds fourth Host
          
      self.addLink(host1, switch)   ## Adds a link
      self.addLink(host2, switch)	## Adds link b/w S1 & H2
      self.addLink(host3, switch)	## Adds link b/w S1 & H3
      self.addLink(host4, switch)	## Adds link b/w S1 & H4


if __name__ == '__main__': 
  """
  If this script is run as an executable (by chmod +x), this is what it will do
  """

  topo = MyTopology()   ## Creates the topology
  net = Mininet( topo=topo ) ## Loads the topology
  net.start()   ## Starts Mininet

# Commands here will run on the simulated topology


CLI(net)

net.stop() ## Stops Mininet
