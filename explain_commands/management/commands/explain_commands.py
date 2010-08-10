from django.core.management import base, get_commands

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
    for provider in sorted(grouped.keys()):
        print "%s =>" % provider
        for command in grouped[provider]:
            print "\t%s" % command

def explain_commands():
    print_commands(group_commands())

class Command(base.NoArgsCommand):
    help = "Explain where each command coming from"

    def handle_noargs(self, **options):
        explain_commands()
