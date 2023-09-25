from mininet.topo import Topo  
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.node import CPULimitedHost, RemoteController
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller
from mininet.cli import CLI


def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller,link=TCLink )

    print( '*** Adding controller\n' )
    net.addController( 'c0' )

    Host1 = net.addHost( 'h1' )
    Host2 = net.addHost( 'h2' )
    Host3 = net.addHost( 'h3' )
    Host4 = net.addHost( 'h4' )
    Switch1 = net.addSwitch('s1')
    Switch2 = net.addSwitch('s2')
    Switch3 = net.addSwitch('s3')
    Switch4 = net.addSwitch('s4')
        # Add links
    net.addLink( Host1, Switch1 )
    net.addLink( Host2, Switch1 )
    net.addLink( Host3, Switch3 )
    net.addLink( Host4, Switch4 )
    net.addLink( Switch1, Switch2 )
    net.addLink( Switch2, Switch3, bw=5, delay='20ms',loss=10)
    net.addLink( Switch3, Switch4, bw=15, delay='40ms',loss=2)

    print( '*** Starting network\n')
    net.start()

    print( '*** Running CLI\n' )
    CLI( net )

    print( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()