from snownlp import SnowNLP
import pylab as pl
from show_scenery_rank.DAL import DB
import threading

operate = DB.operateDB()

# 创建一个绘图的线程
class getThread(threading.Thread):
    def __init__(self,scenery_name,scenery_number):
        threading.Thread.__init__(self)
        self.scenery_name = scenery_name
        self.scenery_number = scenery_number

    # 运行线程
    def run(self):
        if self.scenery_number == '':
            self.getSearch(self.scenery_name)
        else:
            self.analyzeMsg(self.scenery_name, self.scenery_number)

    # 绘制单个景点图（在界面调用）
    # 参数：景点名，景点编号
    def analyzeMsg(self, scenery_name,scenery_number):
        sent1 = []
        sent2 = []
        senti_score1 = []
        senti_score2 = []
        i = 0
        result = operate.searchComment(scenery_number)
        for rows in result:
            msgs = rows[2].decode('gbk')
            suggestion = rows[4].decode('gbk')
            sent1.append(msgs)
            sent2.append(suggestion)
            senti_score1.append(SnowNLP(msgs).sentiments)
            if suggestion in '没有建议':
                senti_score2.append(0.5)
            else:
                senti_score2.append(SnowNLP(suggestion).sentiments)
            i += 1
        self.Painting(senti_score1, senti_score2, range(i), scenery_name)

    # 绘制总图（在界面调用）
    # 参数：景点名
    def getSearch(self,scenery_name):
        senti_score1 = []
        senti_score2 = []
        result_0 = operate.searchAllScenery(scenery_name)
        name_list = []
        for rows in result_0:
            result_1 = operate.searchComment(rows[0])
            name_list.append(rows[1])
            score1 = 0
            score2 = 0
            for row in result_1:
                try:
                    msgs = row[2].decode('gbk')
                    suggestion = row[4].decode('gbk')
                    score1 += SnowNLP(msgs).sentiments
                    score2 += SnowNLP(suggestion).sentiments
                except:
                    score1 += 0.5
                    score2 += 0.5
                    print(row, '文本分析出错')
            if len(result_1) == 0:
                senti_score1.append(0.5)
                senti_score2.append(0.5)
            else:
                senti_score1.append(float(score1 / len(result_1)))
                senti_score2.append(float(score2 / len(result_1)))
        self.Painting(senti_score1, senti_score2, name_list, scenery_name)

    # 画折线图图显示数据
    # 参数：评论情感度列表，建议情感度列表，景点名列表，标题名
    def Painting(self,senti_score1, senti_score2, name_list, name):
        num = len(name_list)
        if num == 0:
            print('该景区没有评论')
        else:
            x = name_list
            pl.close()
            pl.mpl.rcParams['font.sans-serif'] = ['SimHei']
            if num < 9:
                pl.plot(x, senti_score1, marker='o', label=u'评论分析')
                pl.plot(x, senti_score2, marker='*', label=u'建议分析')
            else:
                pl.plot(x, senti_score1, label=u'评论分析')
                pl.plot(x, senti_score2, label=u'建议分析')
            pl.title(name)
            pl.xlabel(u'评论用户')
            pl.ylabel(u'情感程度')
            pl.legend()
            pl.show()