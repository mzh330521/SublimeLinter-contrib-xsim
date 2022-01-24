# SublimeLinter-contrib-xsim

[![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/mzh330521/SublimeLinter-contrib-xsim?style=flat-square&logo=github)](https://github.com/mzh330521/SublimeLinter-contrib-xsim/tags)
[![Project license](https://img.shields.io/github/license/mzh330521/SublimeLinter-contrib-xsim?style=flat-square&logo=github)](https://github.com/mzh330521/SublimeLinter-contrib-xsim/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/mzh330521/SublimeLinter-contrib-xsim?style=flat-square&logo=github)](https://github.com/mzh330521/SublimeLinter-contrib-xsim/stargazers)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to `xvlog`/`xvhdl` - Verilog/SystemVerilog/VHDL compilers provided with [Vivado Simulator](https://www.xilinx.com/support/documentation-navigation/design-hubs/dh0010-vivado-simulation-hub.html) (XSim). `xvlog` will be used with "Verilog" and "SystemVerilog" files , `xvhdl` with "VHDL" files.

## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `xvlog`/`xvhdl` are installed on your system. Once you install [Vivado Design Suite](https://www.xilinx.com/products/design-tools/vivado.html), they will be in the directory `PATH_TO_VIVADO/VIVADO_VERSION/bin`.

In order for `xvlog`/`xvhdl` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

Verilog/SystemVerilog/VHDL syntax highlight is not natively supplied by Sublime Text.
You may install [Sublime Text Verilog](https://packagecontrol.io/packages/Verilog), [Sublime Text SystemVerilog](https://packagecontrol.io/packages/SystemVerilog) and [Sublime Text VHDL Mode](https://packagecontrol.io/packages/VHDL%20Mode) to do the job.

## Settings

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

### Passing arguments to `xvlog`/`xvhdl`

Arguments can be passed in a [linter settings](http://www.sublimelinter.com/en/stable/linter_settings.html#args) file or set in a [project settings](http://www.sublimelinter.com/en/stable/settings.html#project-settings) file:

- Using linter settings file:

   ```javascript
   // SublimeLinter Settings - User
   {
       "linters": {
           "xvlog": {
               "args": ["--relax"],
               "working_dir": "${TEMP:${project_path:${folder:$file_path}}}",
           },
           "xvlog_sv": {
               "args": ["--relax"],
               "working_dir": "${TEMP:${project_path:${folder:$file_path}}}",
           },
           "xvhdl": {
               "args": ["--relax"],
               "working_dir": "${TEMP:${project_path:${folder:$file_path}}}",
           }
       },
   }
   ```

- Using Project specific settings:

    ```javascript
    // .sublime-project
    {
        "folders":
        [
            {
                "path": "."
            }
        ],
        "settings": {
            // SublimeLinter-contrib-xsim
            "SublimeLinter.linters.xvlog.args":[
                "-i", "$project_path/PATH_TO_HEADER_0",
                "-i", "$project_path/PATH_TO_HEADER_1",
                "--relax"
            ],
            "SublimeLinter.linters.xvlog_sv.args":[
                "-i", "$project_path/PATH_TO_HEADER_0",
                "-i", "$project_path/PATH_TO_HEADER_1",
                "--relax"
            ],
            "SublimeLinter.linters.xvhdl.args":[
                "--relax"
            ]
        }
    }
    ```
    
    It is recommended to use project specific settings when using `xvlog` with `-i [include] <directory_name>` command option.

## Demo

`xvlog` for Verilog file:

![xvlog](https://user-images.githubusercontent.com/34703459/150652581-72f74c25-d3cc-4b88-b523-981cf0b403b3.png)

`xvlog` for SystemVerilog file

![xvlog_sv](https://user-images.githubusercontent.com/34703459/150648542-219eafe0-e747-48a7-a6e6-10f35e8836c3.png)

`xvhdl` for VHDL file

![xvhdl](https://user-images.githubusercontent.com/34703459/150648545-7b157dff-81e1-4397-a5fd-b1c1d43212c2.png)

## Acknowledgment

- [SublimeLinter-contrib-modelsim](https://github.com/jevogel/SublimeLinter-contrib-modelsim)

- [SublimeLinter-contrib-iverilog](https://github.com/jfcherng-sublime/SublimeLinter-contrib-iverilog)

