import pymysql
from show_scenery_rank.utils import logUtil

class operateDB():
    # 初始化,构造函数
    def __init__(self):
        self.__dbName = 'qunarnew'
        self.__user = 'root'
        self.__password = '123456'
        self.__host = 'localhost'
        self.__char = 'utf8'
        self.logger = logUtil.getLogger(0)

# 显示区
    # 查询城市
    # 参数：城市名
    # 返回：成功一个城市信息的二维元组，失败false
    def searchCity(self,city_name):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT city_number FROM city_table WHERE city_name = '%s';" % (city_name)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error(city_name + "：城市景点查找失败")
            return False
        finally:
            db.close()

    # 查询旅游景点个数
    # 参数：城市编码，景点名
    # 返回：成功景点个数，失败false
    def countScenery(self, city_number, scnery_name):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        if scnery_name == '':
            sql = "SELECT count(*) FROM scenery_table WHERE city_number = '%d';" % (city_number)
        else:
            sql = "SELECT count(*) FROM scenery_table WHERE city_number = '%d' and scenery_name LIKE '%%%s%%';" % (
            city_number, scnery_name)
        try:
            cs.execute(sql)
            result = cs.fetchall()[0][0]
            return result
        except:
            db.rollback()
            self.logger.error(city_number + "：城市景点查找失败")
            return False
        finally:
            db.close()

    # 计算有评论的景点数量
    # 参数：城市编码
    # 返回：成功景点个数，失败false
    def countSceneryHave(self, city_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT count(*) FROM scenery_table WHERE city_number = '%d';" % (city_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()[0][0]
            return result
        except:
            db.rollback()
            self.logger.error(city_number + "：城市景点查找失败")
            return False
        finally:
            db.close()

    # 查询旅游景点信息
    # 参数：景点名字，页码号
    # 返回：成功相应的景点一个二维元组，失败false
    def searchScenery(self,scenery_name, num):
        num *= 13
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        if scenery_name == '':
            sql = "SELECT * FROM scenery_table order by count DESC LIMIT %d,14;" % (num)
        else:
            sql = "SELECT * FROM scenery_table WHERE scenery_name LIKE '%%%s%%' order by count DESC LIMIT %d,13;" % (
            scenery_name, num)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error(scenery_name + "：城市景点查找失败")
            return False
        finally:
            db.close()

    # 查询评论
    # 参数：景点编号
    # 返回：成功评论一个二维元组，失败false
    def searchComment(self,scenery_number):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT * FROM comment_table WHERE scenery_number = '%s' ;" % (scenery_number)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error(scenery_number + "：景点评论查找失败")
            return False
        finally:
            db.close()

    # 查找所有景点名
    # 参数：景点名
    # 返回：成功景点编号以及景点名称的一个二维元组，失败false
    def getAllscenery(self,scenery_name):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        if scenery_name == '':
            sql = "SELECT scenery_number,scenery_name FROM scenery_table WHERE 1;"
        else:
            sql = "SELECT scenery_number,scenery_name FROM scenery_table WHERE scenery_name LIKE '%%%s%%';" % (
                scenery_name)
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error(scenery_name + "：景点查找失败")
            return False
        finally:
            db.close()

    # 查找所有有评论的景点信息
    # 参数：无
    # 返回：成功景点信息的二维元组，失败false
    def getAllSceneryMsgs(self):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT scenery_table.* FROM scenery_table, scenery_weight WHERE scenery_weight.scenery_number = scenery_table.scenery_number and scenery_table.scenery_name not LIKE '%大学%' order by scenery_weight.weight DESC;"
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error("景点查找失败")
            return False
        finally:
            db.close()

    # 统计权重表是否有值
    # 参数：无
    # 返回：成功一个数字，失败false
    def countSceneryWeight(self):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT count(*) FROM scenery_weight WHERE 1"
        try:
            cs.execute(sql)
            result = cs.fetchall()[0][0]
            return result
        except:
            db.rollback()
            self.logger.error("权重表查找失败")
            return False
        finally:
            db.close()

# 存入区
    # 插入权重
    # 参数：景点编号，权重
    def insertWeight(self,scenery_number, weight):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "INSERT INTO scenery_weight(scenery_number, weight) VALUES('%s','%s');" % (scenery_number, weight)
        try:
            cs.execute(sql)
            db.commit()
        except:
            db.rollback()
            self.logger.error(scenery_number + ":景点权重插入失败")
        finally:
            db.close()

    # 查找所有有评论的景点编号
    # 返回：成功景点编号以及等级二维元组，失败false
    def searchSceneryNum(self):
        db = pymysql.connect(self.__host, self.__user, self.__password, self.__dbName, charset=self.__char)
        cs = db.cursor()
        sql = "SELECT scenery_number, grade FROM scenery_table WHERE count != 0 ;"
        try:
            cs.execute(sql)
            result = cs.fetchall()
            return result
        except:
            db.rollback()
            self.logger.error("评论查找失败")
            return False
        finally:
            db.close()