# 资源管理

# pyqt都用qrc文件来管理软件内部的资源文件（如图标文件，翻译文件等）。
#
# qrc文件的编写格式如下：
    <!DOCTYPE RCC><RCC version="1.0">
    <qresource>
        <file>images/copy.png</file>
    </qresource>
    </RCC>

#　qrc的编写还是很简单的，完全可以手工编写之。
# 上面代码第三行的images/copy.png的意思就是qrc文件所在目录下的images文件夹，里面的copy.png文件。

# qrc文件编写好了你需要运行如下命令

    pyrcc5  wise.qrc  -o  wise_rc.py

# 这样将会输出一个wise_rc.py文件，你如果要使用里面的资源，首先

# import  wise_rc

# 然后引用路径如下 ' :/images/copy.png ' ，这样就可以使用该图标文件了。

# 上面是pyqt5的情况，对于pyqt4类似的有：

    pyrcc4  wise.qrc  -o  wise_rc.py

# 值得一提的是pyrcc4还有一个额外的选项 -py3 ，用于生成python3的代码。

# 推荐一个项目里面所有的资源文件都用一个qrc文件来管理。
