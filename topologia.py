from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel
class CustomTopo(Topo):
  def build(self):
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    s4 = self.addSwitch('s4')

    h1 = self.addHost('h1')
    h2 = self.addHost('h2')
    h3 = self.addHost('h3')
    h4 = self.addHost('h4')
    h5 = self.addHost('h5')
    ht6 = self.addHsot('h6')

    self.addLink(h1,s1)
    self.addLink(h2,s1)
    self.addLink(h3,s2)
    self.addLink(h4,s2)
    self.addLink(h5,s3)
    self.addLink(h6,s4)

    self.addLink(s1,s2)
    self.addLink(s2,s3)
    self.addLink(s3,s4)
    self.addLink(s4,s1)

def runCustomTopo():
  setLogLevel('info')

  topo = CustomTopo()
  net = Mininet(topo=topo)
  net.start()

  CLI(net)

  net.stop()

if __name__ == '__main__':
  runCustomTopo()
