from piemc.plugin.PluginBase import PLuginBase
from piemc.plugin.Terminal import Terminal

class Main(PluginBase):
  def on_enable(self):
    self.logger.info(Terminal.green("[Example] enabling..."))
