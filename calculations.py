
import sqlite3

print "Opened database successfully";

def Add_New_Entry(Entry_Date,Account_No,Account_Name,Debit,Credit,Account_No2,Account_Name2,Debit2,Credit2,Description,):#اضافة قيد جديد لدفتر اليومية
    connCalcu = sqlite3.connect('calculations.db')
    cursorCalcu = connCalcu.execute(" SELECT   Entry_No FROM    Journals WHERE Entry_No = (SELECT MAX(Entry_No)  FROM Journals);") #لاختيار آخر قيمة في قاعدة البيانات
    Last_Entry_No = 0 
    for s in cursorCalcu:
        try :
            Last_Entry_No = s[0]
        except:
            Last_Entry_No = 0
    New_Entry_No = str(int(Last_Entry_No) + 1)
    
    #Enty_Balance_Test
    if float(Debit) == float(Credit2) and float(Credit) == float(Debit2) :
        connCalcu.execute("INSERT INTO Journals (Date,Entry_No,Account_No,Account_Name,Debit,Credit,Description) \
                                        VALUES (?,?,?,?,?,?,?)",(Entry_Date,New_Entry_No,Account_No,Account_Name,Debit,Credit,Description,))
        connCalcu.execute("INSERT INTO Journals (Date,Entry_No,Account_No,Account_Name,Debit,Credit,Description) \
                                        VALUES (?,?,?,?,?,?,?)",(Entry_Date,New_Entry_No,Account_No2,Account_Name2,Debit2,Credit2,Description,))
        connCalcu.commit()
        connCalcu.close()
        return True
    else :
        return "NOT_BALANCE_ENTRY"

def Edit_Entry(Entry_Date,Entry_No,Account_No,Account_Name,Debit,Credit,Account_No2,Account_Name2,Debit2,Credit2,Description,):#اضافة قيد جديد لدفتر اليومية
    connCalcu = sqlite3.connect('calculations.db')

    #Enty_Balance_Test
    if float(Debit) == float(Credit2) and float(Credit) == float(Debit2) :
        connCalcu.execute('''UPDATE Journals SET Date = ? ,
                                               Account_Name=?,
                                               Debit=?,
                                               Credit=?,
                                               Description=? where Entry_No = ? and Account_No = ?''',(Entry_Date,Account_Name,Debit,Credit,Description,Entry_No,Account_No))
        connCalcu.execute('''UPDATE Journals SET Date = ? ,
                                               Account_Name=?,
                                               Debit=?,
                                               Credit=?,
                                               Description=? where Entry_No = ? and Account_No = ?''',(Entry_Date,Account_Name2,Debit2,Credit2,Description,Entry_No,Account_No2))
        connCalcu.commit()
        connCalcu.close()
        return True
    else :
        return "NOT_BALANCE_ENTRY"
#print Add_New_Entry("6/6/2022","6658","Acount Test","7000","0","22456","Acounttest2","0","7000","This is test")
print Edit_Entry("6/6/2022","1","6658","Acount Test","5000","0","22456","Acounttest2","0","5000","This is test")
