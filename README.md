---

**将数据库的评论分析后展示排名**
---
入口函数：main.py

包说明：

BLL：存放将评论进行情感分析并进行绘图

DAL：访问数据库

UI：界面展示

logs：存放错误日记

utils：存放一些工具

---
**技术栈**
---

python(python3.7 x64)：有python的一定基础，https://www.runoob.com/python/python-tutorial.html

PyQt5：用于显示客户端界面，http://code.py40.com/pyqt5/

snownlp：https://www.cnblogs.com/zhiyong-ITNote/p/6938931.html

pylab：https://www.cnblogs.com/coser/archive/2013/06/20/3146022.html

pymysql：https://www.runoob.com/python3/python3-mysql.html

---
**包的层次结构**
---

show_scenery_rank ---- BLL ---- chartAnalysis.py

                           ---- saveWeight.py
                  
                  ---- DAL ---- DB.py
                  
                  ---- logs ---- data_log.log
                  
                            ---- DB_log.log
                            
                  ---- UI ---- showScenery.py
                  
                  ---- utils ---- logUtil.py
                  
                  ---- main.py
                  
                  ----README.md
       
---
**依赖包**
---

PyQt5：用于界面实现和展示

snownlp:用于情感分析

pylab：用于绘图

pymysql：用于python连接数据库