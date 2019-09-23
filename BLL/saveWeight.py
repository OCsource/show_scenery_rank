from show_scenery_rank.DAL import DB
from snownlp import SnowNLP

operate = DB.operateDB()

# 计算所有景点评论的综合权重
def calAffection():
    result = operate.searchSceneryNum()
    AHP = [91, 61, 61, 37, 98]      # 调查问卷数据
    for r in result:
        tempList = []               #存取所有指标
        scenery_number = r[0]
        senti_comment = []          #指标一,用户对景点的评论分析度
        senti_Suggest = []          #指标二,用户对景点的建议分析度
        star_list = []              #指标三,用户对景点的评分
        grade = int(r[1][:-1])      #指标四,景点的排名
        recommend = 0               # 指标五,用户对景点的推荐度（）
        msgs = operate.searchComment(scenery_number)
        for rows in msgs:
            suggestion = rows[0].decode('gbk')
            comment = rows[1].decode('gbk')
            star = int(rows[2])
            if '没有评论' in comment or '' in comment or None in comment:
                # senti_Suggest.append(0.5)
                pass
            else:
                senti_comment.append(SnowNLP(comment).sentiments)
            if '没有建议' in suggestion or '' in suggestion or None in suggestion:
                # senti_Suggest.append(0.5)
                pass
            else:
                senti_Suggest.append(SnowNLP(suggestion).sentiments)
            if star != 0:
                star = star / 5
                star_list.append(star)
        tempList.append(calAverage(senti_comment))
        tempList.append(calAverage(senti_Suggest))
        tempList.append(calAverage(star_list))
        tempList.append(grade/100)
        tempList.append(calAverage(star_list))
        weight = useAHP(AHP,tempList)
        operate.insertWeight(scenery_number,weight)

# 计算情感度平均值
# 参数：一个数字的列表
# 返回：一个平均数
def calAverage(ls):
    all = 0
    if len(ls) == 0:
        return 0.5
    else:
        for l in ls:
            all += l
        return (all/len(ls))

# 计算综合权重
# 参数：权重指标，数值列表
# 返回：综合权重
def useAHP(AHP, ls):
    weight = 0
    for i in range(len(AHP)):
        weight += (AHP[i] / sum(AHP)) * ls[i]
    return weight