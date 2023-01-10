# SublimeLinter-contrib-xsim

[![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/mzh330521/SublimeLinter-contrib-xsim?style=flat-square&logo=github)](https://github.com/mzh330521/SublimeLinter-contrib-xsim/tags)
[![Project license](https://img.shields.io/github/license/mzh330521/SublimeLinter-contrib-xsim?style=flat-square&logo=github)](https://github.com/mzh330521/SublimeLinter-contrib-xsim/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/mzh330521/SublimeLinter-contrib-xsim?style=flat-square&logo=github)](https://github.com/mzh330521/SublimeLinter-contrib-xsim/stargazers)

[English](./README.md) | [简体中文](./README.ch.md)

这是一个 [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) 的子插件, 提供了 `xvlog`/`xvhdl` 的接口. `xvlog`/`xvhdl` 由 [Vivado Simulator](https://www.xilinx.com/support/documentation-navigation/design-hubs/dh0010-vivado-simulation-hub.html) (XSim) 提供. `xvlog` 被用于 "Verilog" 和 "SystemVerilog" 文件 , `xvhdl` 被用于 "VHDL" 文件.

## 安装

在安装该插件前需要先安装 SublimeLinter. 

请使用 [Package Control](https://packagecontrol.io) 安装该插件.

使用该插件前, 需要保证 `xvlog`/`xvhdl` 已经安装在系统中. 当你安装了 [Vivado Design Suite](https://www.xilinx.com/products/design-tools/vivado.html) 后, 他们将出现在 Vivado 安装目录下 `PATH_TO_VIVADO/VIVADO_VERSION/bin`.

为了 `xvlog`/`xvhdl` 能被 SublimeLinter 正确执行, 你必须确保 SublimeLinter 能够找到他们的路径. 你可以在环境变量中配置 PATH, 也可以在  SublimeLinter 中设置, 详见 [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

Sublime 不支持 Verilog/SystemVerilog/VHDL 语法高亮.
你需要安装 [Sublime Text Verilog](https://packagecontrol.io/packages/Verilog), [Sublime Text SystemVerilog](https://packagecontrol.io/packages/SystemVerilog) 和 [Sublime Text VHDL Mode](https://packagecontrol.io/packages/VHDL%20Mode) 插件来实现.

## 设置

- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

### `xvlog`/`xvlog_sv`/`xvhdl` 参数设置

参数可以在 [linter settings](http://www.sublimelinter.com/en/stable/linter_settings.html#args) 文件或 [project settings](http://www.sublimelinter.com/en/stable/settings.html#project-settings) 文件中进行设置:

- 使用 linter settings:

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

- 使用 Project settings (会覆盖 linter setttings 的同名参数):

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
    
    在使用 `xvlog` 的 `-i [include] <directory_name>` 选项等与工程相关的选项时, 建议各个工程各自使用 Project settings; 其他选项建议使用全局的 linter settings.

- 备注

    - `xvlog_sv` 等价于带 `--sv` 选项的 `xvlog`, 专门为 SystemVerilog 打造.

    - `args` 为传递给 `xvlog/xvhdl` 的参数
        - `--relax`: 放松语法检查规则, Vivado 中默认开启该选项
        - `-i`: 指定 `` `include`` 语句的检索目录, 对多个目录需分别设置
        - 更多选项请查看 [UG900](https://www.xilinx.com/support/documentation-navigation/design-hubs/dh0010-vivado-simulation-hub.html), 或在命令行中使用 `xvlog/xvhdl --help`.

    - `work_dir` 为 `xvlog/xvhdl` 的运行目录
        - 由于运行目录下会生成 `.dir` `.log` `.pb` 等目录或文件, 故上述参考设置中将其优先设为 `$TEMP`, 即操作系统临时文件夹, 当 `TEMP` 不存在时 (对于 Windows, 这是系统自带的环境变量), 才会依次选择后续目录.


## 示例

`xvlog` for Verilog file:

![xvlog](https://user-images.githubusercontent.com/34703459/150652581-72f74c25-d3cc-4b88-b523-981cf0b403b3.png)

`xvlog_sv` for SystemVerilog file

![xvlog_sv](https://user-images.githubusercontent.com/34703459/150648542-219eafe0-e747-48a7-a6e6-10f35e8836c3.png)

`xvhdl` for VHDL file

![xvhdl](https://user-images.githubusercontent.com/34703459/150648545-7b157dff-81e1-4397-a5fd-b1c1d43212c2.png)

## 致谢

- [SublimeLinter-contrib-modelsim](https://github.com/jevogel/SublimeLinter-contrib-modelsim)

- [SublimeLinter-contrib-iverilog](https://github.com/jfcherng-sublime/SublimeLinter-contrib-iverilog)

