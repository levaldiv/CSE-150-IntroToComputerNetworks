# Luis Valdivia
# Lab 3 Skeleton
# Based on of_tutorial by James McCauley

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Firewall (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_firewall (self, packet, packet_in):
    # The code in here will be executed for every packet.
    #insatlling a table entry
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)

    #initializing som variables
    ipv4 = packet.find('ipv4')
    proto_arp = packet.find('arp')
    proto_icmp = packet.find('icmp')
    tcp = packet.find('tcp')

    #show couple of dump flow entries by setting idle and hard timeout
    msg.idle_timeout = 1000   # flow expires after n sec of inactivity
    msg.hard_timeout = 3000   # flow expiers after n sec even with activity
    msg.priority

    if (ipv4 and tcp):    #creating the rule from the pdf to allow TCP/ARP connections but other traffic dropped
      msg.data = packet_in
      msg.priority = 50
      msg.match.dl_type = 0x0800
      msg.nw_proto = 6    # for tcp
      action = of.ofp_action_output(port = of.OFPP_ALL)
      msg.actions.append(action)
      self.connection.send(msg)
    elif (proto_arp is not None):
        msg.data = packet_in
        msg.priority = 45
        msg.match.dl_type = 0x0806 # for arp
        action = of.ofp_action_output(port = of.OFPP_ALL)
        msg.actions.append(action)
        self.connection.send(msg)

    else:   # if not arp/tcp&ipv4 then drop
        msg.data = packet_in
        self.connection.send(msg)

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_firewall(packet, packet_in)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
