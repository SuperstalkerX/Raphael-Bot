from discord import Embed
from discord.ext.commands import Context


def make_embed(
    title: str = None,
    description: str = None,
    ctx: Context = None,
    color="dark_theme",
    image_url: str = None,
    author: bool = True,
) -> Embed:
    """General embed template

    Args:
        title (str, optional): Title of your embed. Defaults to None.
        description (str, optional): Secondary text of your embed. Defaults to None.
        ctx (Context, optional): Discord context object, needed for author and timestamps. Defaults to None.
        color (str, optional): Use a predefined name or use a hex color value. Defaults to 'dark_theme'.
        image_url (str, optional): URL for the side image of embed. Defaults to None.
        author (bool, optional): Whether or not you wish to set the author of embed. Defaults to True.

    Returns:
        Embed: discord embed object
    """

    colors = dict(
        default=0,
        teal=0x1ABC9C,
        dark_teal=0x11806A,
        green=0x2ECC71,
        dark_green=0x1F8B4C,
        blue=0x3498DB,
        dark_blue=0x206694,
        purple=0x9B59B6,
        dark_purple=0x71368A,
        magenta=0xE91E63,
        dark_magenta=0xAD1457,
        gold=0xF1C40F,
        dark_gold=0xC27C0E,
        orange=0xE67E22,
        dark_orange=0xA84300,
        red=0xE74C3C,
        dark_red=0x992D22,
        lighter_grey=0x95A5A6,
        dark_grey=0x607D8B,
        light_grey=0x979C9F,
        darker_grey=0x546E7A,
        blurple=0x7289DA,
        greyple=0x99AAB5,
        dark_theme=0x36393F,
        # Reddit colors:
        reddit=0xFF5700,
        orange_red=0xFF450,
        upvote=0xFF8B60,
        neutral=0xC6C6C6,
        downvote=0x9494FF,
        light_bg=0xEFF7FF,
        header=0xCEE3F8,
        ui_text=0x336699,
    )

    if isinstance(color, str) and color.lower() in colors:
        embed = Embed(color=colors[color.lower()], title=title, description=description)
    else:
        embed = Embed(color=color, title=title, description=description)

    # Setting the author field and setting their profile pic as the image.
    if author and ctx is not None:
        embed.set_author(icon_url=ctx.author.avatar.url, name=str(ctx.author))

    # Setting the embed side image if a url was given.
    if image_url:
        embed.set_thumbnail(url=image_url)

    # Adding Timestamp for ease of tracking when embeds are posted.
    if ctx:
        # Treated_at value is not always at the same location.
        try:
            embed.timestamp = ctx.message.created_at
        except AttributeError:
            embed.timestamp = ctx.created_at

    return embed


async def error_message(description: str, ctx: Context, author: bool = True):
    """Send basic error message

    Note:
        You must await this function

    Args:
        description (str): Error description.
        ctx (Context): Discord context object, needed for author and timestamps.
        author (bool, optional): Whether or not you wish to set the author of embed. Defaults to True.
    """
    await ctx.send(
        embed=make_embed(
            title="ERROR",
            description=f"📢 **{description}**",
            ctx=ctx,
            color="dark_red",
            author=author,
        ),
        delete_after=30,
    )


def error_embed(
    title: str, description: str, ctx: Context, author: bool = True
) -> Embed:
    """Make a basic Error message embed

    Args:
        title (str): Name of error.
        description (str): Error description.
        ctx (Context): Discord context object, needed for author and timestamps.
        author (bool, optional): Whether or not you wish to set the author of embed. Defaults to True.

    Returns:
        Embed: discord embed object.
    """
    return make_embed(
        title=f"ERROR: {title}",
        description=f"📢 **{description}**",
        ctx=ctx,
        color="dark_red",
        author=author,
    )


async def warning_message(ctx: Context, description: str, author: bool = True):
    """Send a basic warning message

    Note:
        You must await this function

    Args:
        description (str): Warning description
        ctx (Context): Discord context object, needed for author and timestamps.
        author (bool, optional): Whether or not you wish to set the author of embed. Defaults to True.
    """
    await ctx.send(
        embed=make_embed(
            title="WARNING",
            description=f"📢 **{description}**",
            ctx=ctx,
            color="dark_gold",
            author=author,
        ),
        delete_after=30,
    )


def files_and_links_only(ctx: Context) -> Embed:
    """Standard messsage for when files or links are only used in the channel

    Args:
        ctx (Context): Discord context object, needed for author and timestamps.

    Returns:
        Embed: discord embed object.
    """

    embed = make_embed(
        description="This channel is for submissions only! "
        "All messages that do not contain an image or a link are automatically removed.",
        ctx=ctx,
        color="reddit",
    )
    embed.set_footer(text="This message will self-destruct in 10 seconds.")
    return embed
