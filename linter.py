from SublimeLinter.lint import Linter

class xvlog(Linter):
    name = 'xvlog'
    cmd = ['xvlog', '${args}', '${temp_file}']
    tempfile_suffix = 'verilog'
    multiline = False
    on_stderr = None

    defaults = {
        'selector': 'source.verilog',
        '-i +': [],
    }

    regex = (
        r'((?P<error>ERROR)|(?P<warning>WARNING)): '
        r'(?P<message>([^"\'\n]*(?P<quote>["\'])(?P<near>[^"\']+)(?P=quote))?.*)'
        r'\[(?P<file>.*):'
        r'(?P<line>\d+)\]'
    )

class xvlog_sv(Linter):
    name = 'xvlog_sv'
    cmd = ['xvlog', '${args}', '--sv', '${temp_file}']
    tempfile_suffix = 'systemverilog'
    multiline = False
    on_stderr = None

    defaults = {
        'selector': 'source.systemverilog',
        '-i +': [],
    }

    regex = (
        r'((?P<error>ERROR)|(?P<warning>WARNING)): '
        r'(?P<message>([^"\'\n]*(?P<quote>["\'])(?P<near>[^"\']+)(?P=quote))?.*)'
        r'\[(?P<file>.*):'
        r'(?P<line>\d+)\]'
    )

class xvhdl(Linter):
    name = 'xvhdl'
    cmd = ['xvhdl', '${args}', '${temp_file}']
    tempfile_suffix = 'vhdl'
    multiline = False
    on_stderr = None

    defaults = {
        'selector': 'source.vhdl'
    }

    regex = (
        r'((?P<error>ERROR)|(?P<warning>WARNING)): '
        r'(?P<message>([^"\'\n]*(?P<quote>["\'])(?P<near>[^"\']+)(?P=quote))?.*)'
        r'\[(?P<file>.*):'
        r'(?P<line>\d+)\]'
    )
