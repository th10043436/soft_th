import  xlrd
import  os
#打开文件
class Class_Xlrd(object):

    def __init__(self,path):

        self.data=xlrd.open_workbook(path)
        self.table=self.data.sheet_by_name('1')
        #获取总行数
        print('总行数 %d'%self.table.nrows)
        #获取总列数
        print('总列数 %d'%self.table.ncols)

        #获取第一行
        # t1=table.row_values(0)
        # # print(t1)
        # #获取第一列
        # t2=table.col_values(0)
        # print(t2)

    def dict_data(self):
        list=[]
        #获取第一行
        key=self.table.row_values(0)
        #print(key)
        for i in range(self.table.nrows-1):
            print(i)
            dict={}
            #获取第二行数据
            cells=self.table.row_values(i+1)
            print(cells)
            for j in  range(len(cells)):
                dict[key[j]]=cells[j]
            list.append(dict)
        return list

if __name__ == '__main__':
        #获取当前路径
        curr=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        print(curr)
        # 绝对路径
        path='D:\\soft\\github\\web_soft\\config_c\\ceshi.xlsx'
        # 相对路径
        path1='../config_c/ceshi.xlsx'
        XLRD=Class_Xlrd(path1)
        list=XLRD.dict_data()
        print(list)
