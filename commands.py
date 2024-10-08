import discord

from core import command, Plugin, utils, Server
from discord import app_commands
from services import DCSServerBot


class JTF111(Plugin):
    
    # This command should only run on servers that are in the state RUNNING, PAUSED or STOPPED.
    @command(description='This is a sample command.')
    @app_commands.guild_only()
    @utils.app_has_role('DCS')
    async def sample(self, interaction: discord.Interaction,
                     server: app_commands.Transform[Server, utils.ServerTransformer], text: str):
        await interaction.response.defer(thinking=True, ephemeral=True)
        # do something that takes some time
        await interaction.followup.send(f"I did something on server {server.name} using text {text}.")
        