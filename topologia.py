from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class MyTopo(Topo):
  def build(self):
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    s4 = self.addSwitch('s4')

    h1 = self.addHost('h1', ip='10.0.0.1/24')
    h2 = self.addHost('h2', ip='10.0.0.2/24')
    h3 = self.addHost('h3', ip='10.0.0.3/24')
    h4 = self.addHost('h4', ip='10.0.0.4/24')
    h5 = self.addHost('h5', ip='10.0.0.5/24')
    h6 = self.addHsot('h6', ip='10.0.0.6/24')

    self.addLink(h1, s1, bw=1, delay='14ms')
    self.addLink(h2, s1, bw=1, delay='14ms')
    self.addLink(h3, s4, bw=1, delay='14ms')
    self.addLink(h4, s2, bw=1, delay='14ms')
    self.addLink(h5, s4, bw=1, delay='14ms')
    self.addLink(h6, s3, bw=1, delay='14ms')

    self.addLink(s1, s2, bw=10, delay='14ms')
    self.addLink(s1, s3, bw=10, delay='14ms')
    self.addLink(s2, s4, bw=10, delay='14ms')
    self.addLink(s3, s4, bw=10, delay='14ms')

topos = { 'mytopo' : (lambda: MyTopo() ) }
