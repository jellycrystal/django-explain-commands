from django.core.management import base, get_commands, color
from django.utils import termcolors

def color_style():
    style = color.color_style()
    style.PROVIDER = termcolors.make_style(fg='green', opts=('bold',))
    style.COMMAND = termcolors.make_style(opts=('bold',))
    style.UNKNOWN = termcolors.make_style(fg='red')
    return style

def group_commands():
    grouped = {}
    for command, provider in get_commands().items():
        if isinstance(provider, basestring):
            key = provider
        elif isinstance(provider, base.BaseCommand):
            mod = provider.__module__
            idx = mod.find('management') - 1
            key = mod[:idx]
        else:
            key = '?unknown'
        grouped[key] = sorted(grouped.get(key, []) + [command])
    return grouped


def print_commands(grouped):
    style = color_style()
    for provider in sorted(grouped.keys()):
        if provider.startswith('?'):
            pstyle = style.UNKNOWN
        else:
            pstyle = style.PROVIDER
        print pstyle(provider) + " =>"
        for command in grouped[provider]:
            print "\t" + style.COMMAND(command)

def explain_commands():
    print_commands(group_commands())

class Command(base.NoArgsCommand):
    help = "Explain where each command coming from"

    def handle_noargs(self, **options):
        explain_commands()
