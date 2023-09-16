import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel
import asyncio


class Reports(commands.Cog):
    """
    Easy report system right here!
    """

    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def report(self, ctx):
        """
        Report a player.
        """
        try:
       
     message.channel.send("<a:check:742680789262663710> | Shift announcement has been edited and the shift has ended!")
        except discord.ext.commands.CommandOnCooldown:
            print("cooldown")


async def setup(bot):
    await bot.add_cog(Reports(bot))
