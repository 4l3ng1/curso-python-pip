import csv
import pprint

def read_csv(path):
    with open(path,'r') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        header=next(reader)
        data_dict={}
        for row in reader:
            iterable=zip(header,row)
            data_dict={key: value for key,value in iterable}
        return list(data_dict)


if __name__=='__main__':
    #pprint.pprint(read_csv('data.csv'))
    data=read_csv('data.csv')      
    filtered=list(filter(lambda item: item['Country/Territory']=='Argentina',data))
    print(filtered)
    
https://mega.nz/file/IrEWQJKD#kw0d1-Jhyv-X56xbpheurnzG0UI58dYbYad-yjAf36E