import os
import qtawesome as qta

_resource = {
    'directory': os.path.join(os.path.dirname(os.path.realpath(__file__)), '../fonts'),
    'loaded': False,
}

_qtaargs = {
    'log':                     [('fa.file-text-o',), {}],
    'configure':               [('fa.wrench',), {}],
    'bold':                    [('fa.bold',), {}],
    'italic':                  [('fa.italic',), {}],
    'genprefs':                [('fa.cogs',), {}],
    'exit':                    [('fa.power-off',), {}],
    'run_small':               [('fa.play',), {'color':'green'}],
    'stop':                    [('fa.stop',), {}],
    'syspath':                 [('fa.cogs',), {}],
    'font':                    [('fa.font',), {}],
    'tooloptions':             [('fa.cog',), {}],
    'edit24':                  [('fa.edit',), {}],
    'edit':                    [('fa.edit',), {}],
    'filenew':                 [(['fa.file-o', 'fa.plus'],), {'options': [{}, {'scale_factor': 0.5, 'offset': (0.0, 0.1)}]}],
    'fileopen':                [('fa.folder-open',), {}],
    'revert':                  [('fa.undo',), {}],
    'filesave':                [('fa.save',), {}],
    'save_all':                [(['fa.save', 'fa.save'],), {'options': [{'offset': (-0.2, -0.2), 'scale_factor': 0.6}, {'offset': (0.2, 0.2), 'scale_factor': 0.6}]}],
    'filesaveas':              [(['fa.save', 'fa.pencil'],), {'options': [{'offset': (-0.2, -0.2), 'scale_factor': 0.6}, {'offset': (0.2, 0.2), 'scale_factor': 0.6}]}],
    'print':                   [('fa.print',), {}],
    'fileclose':               [('fa.close',), {}],
    'filecloseall':            [(['fa.close', 'fa.close', 'fa.close'],), {'options': [{'scale_factor': 0.6, 'offset': (0.3, -0.3)},  {'scale_factor': 0.6, 'offset': (-0.3, -0.3)}, {'scale_factor': 0.6, 'offset': (0.3, 0.3)}]}],
    'breakpoint_big':          [('fa.circle',), {'color': 'darkred'} ],
    'breakpoint_cond_big':     [('fa.question-circle',), {'color':  'darkred'},],
    'debug':                   [('spyder.debug',), {'color': '#3775a9'}],
    'arrow-step-over':         [('spyder.step-forward',), {'color': '#3775a9'}],
    'arrow-continue':          [('spyder.continue',), {'color': '#3775a9'}],
    'arrow-step-in':           [('spyder.step-into',), {'color': '#3775a9'}],
    'arrow-step-out':          [('spyder.step-out',), {'color': '#3775a9'}],
    'stop_debug':              [('spyder.stop',), {'color': '#3775a9'}],
    'run':                     [('spyder.run',), {'color': 'green'}],
    'run_settings':            [(['fa.wrench', 'spyder.run'],), {'options': [{'offset':(-0.1, -0.1), 'scale_factor': 0.75}, {'offset': (0.0, 0.125), 'color': 'green','scale_factor': 0.75}]}],
    'run_again':               [(['fa.repeat', 'spyder.run'],), {'options': [{'offset':(-0.1, -0.1), 'scale_factor': 0.75}, {'offset':(0.1, 0.125), 'color': 'green', 'scale_factor': 0.75}]}],
    'run_selection':           [('spyder.run-selection',), {}],
    'run_cell':                [(['fa.th-list', 'spyder.run-one-inplace'],), {'options': [{'color': '#AAAAAA'}, {'color':'green'}]}],
    'run_cell_advance':        [(['fa.th-list', 'spyder.run-one'],), {'options': [{'color': '#AAAAAA'}, {'color':'green'}]}],
    'todo_list':               [(['fa.th-list', 'fa.check'],), {'options': [{'color': '#3775a9'}, {'offset': (0.0, 0.2), 'color': 'orange', 'color_disabled': '#face7e'}]}],
    'wng_list':                [(['fa.th-list', 'fa.warning'],), {'options': [{'color': '#3775a9'}, {'offset': (0.0, 0.2), 'scale_factor': 0.75, 'color': 'orange', 'color_disabled': '#face7e'}]}],
    'prev_wng':                [(['fa.arrow-left', 'fa.warning'],), {'options': [{'color': '#3775a9'}, {'offset': (0.0, 0.2), 'scale_factor': 0.75, 'color': 'orange', 'color_disabled': '#face7e'}]}],
    'next_wng':                [(['fa.arrow-right', 'fa.warning'],), {'options': [{'color': '#3775a9'}, {'offset': (0.0, 0.2), 'scale_factor': 0.75, 'color': 'orange', 'color_disabled': '#face7e'}]}],
    'last_edit_location':      [('fa.caret-up',), {}],
    'prev_cursor':             [('fa.hand-o-left',), {}],
    'next_cursor':             [('fa.hand-o-right',), {}],
    'comment':                 [('fa.comment',), {}],
    'indent':                  [('fa.indent',), {}],
    'unindent':                [('fa.outdent',), {}],
    'gotoline':                [('fa.sort-numeric-asc',), {}],
    'error':                   [('fa.times-circle',), {}],
    'warning':                 [('fa.warning',), {}],
    'todo':                    [('fa.check',), {'color':'#3775a9'}],
    'ipython_console':         [('spyder.ipython-logo',), {}],
    'ipython_console_t':       [('spyder.ipython-logo',), {'color':'gray'}],
    'python':                  [(['spyder.python-logo-up', 'spyder.python-logo-down'],), {'options': [{'color': '#3775a9'}, {'color': '#ffd444'}]}],
    'python_t':                [('spyder.python-logo',), {'color':'gray'}],
    'terminated':              [('fa.circle',), {}],
    'cmdprompt':               [('fa.terminal',), {}],
    'cmdprompt_t':             [('fa.terminal',), {'color':'gray'}],
    'console':                 [('fa.terminal',), {}],
    'findf':                   [(['fa.file-o', 'fa.search'],), {'options': [{'scale_factor': 1.0}, {'scale_factor': 0.6}]}],
    'history24':               [('fa.history',), {}],
    'history':                 [('fa.history',), {}],
    'inspector':               [('fa.search',), {}],
    'lock':                    [('fa.lock',), {}],
    'lock_open':               [('fa.unlock-alt',), {}],
    'outline_explorer':        [('spyder.treeview',), {}],
    'project_expanded':        [('fa.plus',), {}],
    'dictedit':                [('fa.th-list',), {}],
    'previous':                [('fa.arrow-left',), {}],
    'next':                    [('fa.arrow-right',), {}],
    'set_workdir':             [('fa.check',), {}],
    'up':                      [('fa.arrow-up',), {}],
    'down':                    [('fa.arrow-down',), {}],
    'filesaveas2':             [(['fa.save', 'fa.close'],), {'options': [{'scale_factor': 0.8, 'offset': (-0.1, -0.1)}, {'offset': (0.2, 0.2)}]}],   # save_session_action
    'spyder_light':            [(['spyder.spyder-logo-background', 'spyder.spyder-logo-web'],), {'options': [{'color': '#414141'}, {'color': '#fafafa'}]}],
    'spyder':                  [(['spyder.spyder-logo-background', 'spyder.spyder-logo-web', 'spyder.spyder-logo-snake'],),  {'options': [{'color': '#414141'}, {'color': '#fafafa'}, {'color': '#ee0000'}]}],
    'find':                    [('fa.search',), {}],
    'findnext':                [(['fa.search', 'fa.long-arrow-down'],), {'options':[{'scale_factor': 0.6, 'offset': (0.3, 0.0)}, {'offset': (-0.3, 0.0)}]}],
    'findprevious':            [(['fa.search', 'fa.long-arrow-up'],), {'options':[{'scale_factor': 0.6, 'offset': (0.3, 0.0)}, {'offset': (-0.3, 0.0)}]}],
    'replace':                 [('fa.retweet',), {}],
    'undo':                    [('fa.undo',), {}],
    'redo':                    [('fa.repeat',), {}],
    'restart':                 [('fa.repeat',), {}],
    'editcopy':                [('fa.copy',), {}],
    'editcut':                 [('fa.scissors',), {}],
    'editpaste':               [('fa.clipboard',), {}],
    'editdelete':              [('fa.eraser',), {}],
    'editclear':               [('fa.times',), {}],
    'selectall':               [('spyder.text-select-all',), {}],
    'pythonpath_mgr':          [(['spyder.python-logo-up', 'spyder.python-logo-down'],), {'options': [{'color': '#3775a9'}, {'color': '#ffd444'}]}],
    'exit':                    [('fa.power-off',), {}],
    'advanced':                [('fa.gear',), {}],
    'bug':                     [('fa.bug',), {}],
    'maximize':                [('spyder.maximize-pane',), {}],
    'unmaximize':              [('spyder.minimize-pane',), {}],
    'window_nofullscreen':     [('spyder.inward',), {}],
    'window_fullscreen':       [('fa.arrows-alt',), {}],
    'MessageBoxWarning':       [('fa.warning',), {}],
    'arredit':                 [('fa.table',), {}],
    'zoom_out':                [('fa.search-minus',), {}],
    'zoom_in':                 [('fa.search-plus',), {}],
    'home':                    [('fa.home',), {}],
    'find':                    [('fa.search',), {}],
    'plot':                    [('fa.line-chart',), {}],
    'hist':                    [('fa.bar-chart',), {}],
    'imshow':                  [('fa.image',), {}],
    'insert':                  [('fa.sign-in',), {}],
    'rename':                  [('fa.pencil',), {}],
    'edit_add':                [('fa.plus',), {}],
    'edit_remove':             [('fa.minus',), {}],
    'browse_tab':              [('fa.folder-o',), {}],
    'filelist':                [('fa.list',), {}],
    'newwindow':               [('spyder.window',), {}],
    'versplit':                [('spyder.rows',), {}],
    'horsplit':                [('fa.columns',), {}],
    'close_panel':             [('fa.close',), {}],
    'class':                   [('spyder.circle-letter-c',), {'color':'#3775a9'}],
    'private2':                [('fa.minus-circle',), {'color':'#7ea67e'}],
    'private1':                [('fa.minus-circle',), {'color':'#7ea67e'}],
    'method':                  [('spyder.circle-letter-m',), {'color':'green'}],
    'function':                [('spyder.circle-letter-f',), {'color':'orange'}],
    'blockcomment':            [('spyder.circle-hash',), {'color':'grey'}],
    'cell':                    [('spyder.circle-percent',), {'color':'red'}],
    'fromcursor':              [('fa.hand-o-right',), {}],
    'filter':                  [('fa.filter',), {}],
    'folder_new':              [(['fa.folder-o', 'fa.plus'],), {'options': [{}, {'scale_factor': 0.5, 'offset': (0.0, 0.1)}]}],
    'package_new':             [(['fa.folder-o', 'spyder.python-logo'],), {'options': [{'offset': (0.0, -0.125)}, {'offset': (0.0, 0.125)}]}],
    'vcs_commit':              [('fa.check',), {'color': 'green'}],
    'vcs_browse':              [('fa.search',), {'color': 'green'}],
    'ArrowUp':                 [('fa.arrow-circle-up',), {}],
    'kill':                    [('fa.warning',), {}],
    'reload':                  [('fa.repeat',), {}],
    'auto_reload':             [(['fa.repeat', 'fa.clock-o'],), {'options': [{'scale_factor': 0.75, 'offset': (-0.1, -0.1)}, {'scale_factor': 0.5, 'offset': (0.25, 0.25)}]}],
    'profiler':                [('fa.clock-o',), {}],
    'fileimport':              [('fa.download',), {}],
    'environ':                 [('fa.th-list',), {}],
    'options_less':            [('fa.minus-square',), {}],
    'options_more':            [('fa.plus-square',), {}],
    'ArrowBack':               [('fa.arrow-circle-left',), {}],
    'ArrowForward':            [('fa.arrow-circle-right',), {}],
    'DialogApplyButton':       [('fa.check',), {}],
    'DialogCloseButton':       [('fa.close',), {}],
    'DialogHelpButton':        [('fa.question',), {}],
    'DirClosedIcon':           [('fa.folder-o',), {}],
    'DialogHelpButton':        [('fa.life-ring',), {}],
    'MessageBoxInformation':   [('fa.info',), {}],
    'DirOpenIcon':             [('fa.folder-open',), {}],
    'FileIcon2':               [('fa.file-o',), {}],   # QtHelper
    'DriveHDIcon':             [('fa.hdd-o',), {}],
    'arrow':                   [('fa.arrow-right',), {}],
    'collapse':                [('spyder.inward',), {}],
    'expand':                  [('fa.arrows-alt',), {}],
    'restore':                 [('fa.level-up',), {}],
    'collapse_selection':      [('fa.minus-square-o',), {}],
    'expand_selection':        [('fa.plus-square-o',), {}],
    'copywop':                 [('fa.terminal',), {}],
    'editpaste':               [('fa.paste',), {}],
    'editcopy':                [('fa.copy',), {}],
    'edit':                    [('fa.edit',), {}],
    'convention':              [('spyder.circle-letter-c',), {'color':'#3775a9'}],
    'refactor':                [('spyder.circle-letter-r',), {'color':'#3775a9'}],
    '2uparrow':                [('fa.angle-double-up',), {}],
    '1uparrow':                [('fa.angle-up',), {}],
    '2downarrow':              [('fa.angle-double-down',), {}],
    '1downarrow':              [('fa.angle-down',), {}],
}

def icon(name):
    if not _resource['loaded']:
        qta.load_font('spyder', 'spyder.ttf', 'spyder-charmap.json', directory=_resource['directory'])
        _resource['loaded'] = True
    args, kwargs = _qtaargs[name]
    return qta.icon(*args, **kwargs)
