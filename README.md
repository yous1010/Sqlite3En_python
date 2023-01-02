# Sqlite3En_python
Installtion

Needed packages before install Sqlite3En package:

First you need to install cryptography package 
	
	pip install cryptography

Then you can  install Sqlite3En package 

	pip install Sqlite3En

Sqlite3En has been tested only on python 2.7 

It works only on an existing DB that you want to encrypt 

Usage or how to use Sqlite3En ?

Importing: 

	from Sqlite3En import Sqlite3En

To encrypt an existing DB you can use this function :

	Sqlite3En.Encrypt_existing_DB_By_Password (Exist_DB_Path , Exist_DB_Name ,Exist_Table_Name , password = 'password' )

Exist_DB_Path : is DB path which you want to encrypr |example('BDfolder\\')

Exist_DB_Name : is the name of DB you want to encrypr |example('test.db')

Exist_Table_Name : is the name of the table inside the DB you want to encrypt |examole('TableTest')

password : is the password which will be used to encrypt DB |example('password')

It is important to make folder that contain only one DB which you want to encrypt 
so if you have more than one DB  you want to encrypt you have to make folders for every single
DB and then encrypt them all one by one

for example if you have 2 DBs First.db and Sec.db and you want to encrypt both of them 
you have to add Firsr.db in a folder and Sec.db in a other folder : 

	DBfile1/First.db
	DBfile2/Sec.db
	
Then you have to encrypt them one by one.

Example :

	Sqlite3En.Encrypt_existing_DB_By_Password ('DBfile1\\' , 'First.db' ,'Table_Name' , password = 'password' )
	Sqlite3En.Encrypt_existing_DB_By_Password ('DBfile2\\' , 'Sec.db' ,'Table_Name' , password = 'password' )
	
And it is important in each folder to have just the DB inside it without any other files or folders.

The result files of encryption are (.Kn files).

For example :

	First.db after encrypt it the result files are
		First1.Kn
		First2.Kn
		First3.Kn and so on 

	Sec.db result files are
		Sec1.Kn
		Sec2.Kn
		Sec3.Kn
		Sec4.Kn and so on


To open an encrypt DB you can use the function:

	Sqlite3En.Open_Encrypted_DB_By_Password (Encryp_DB_Path_Name,Orgenal_DB_Name,Orgenal_DB_Table_Name,Memory_conn , password = 'password' )

Encryp_DB_Path_Name : is the path where (.Kn files) are.

Orgenal_DB_Name : is the name of DB befor encrypt.

Orgenal_DB_Table_Name : is the name of DB's table befor encrypt.

Memory_conn : is a sqlite3 connection to in :memory: (will talk about it later).

password : is the password which used to encrypt the DB .

It is important DB path or folder to have only the encrypted DB files you want to open (.Kn files).

Do not mix more than one encrypted DB files (.Kn files)  together into one folder
and do not mix (.Kn files) with any kind of other files or folders into one folder or the same folder. 

Before using Open_Encrypted_DB_By_Password function
you have to make a connect to in :memory: db 
using this function :

	Memory_conn = sqlite3.connect(":memory:")
 

You can add more than one DB to that connection(in :memory: - Memory_conn) as new table and use it, by using this function :

	Sqlite3En.Add_Encrypted_DB_By_Password (Encryp_DB_Path_Name,Orgenal_DB_Name,Orgenal_DB_Table_Name,Memory_conn,Trg1,Trg2,Trg3, password = 'password' )


Encryp_DB_Path_Name : is the path where (.Kn files) are

Orgenal_DB_Name : is the name of DB befor encrypt

Orgenal_DB_Table_Name : is the name of DB's table befor encrypt

Memory_conn : is a sqlite3 connection to in :memory: (will talk about it later)

Trg1 , Trg2 and Trg3 : are table TRIGGERS names , you can use any 3 difrent Names |example('t1','t2','t3').

Be careful that if you add more than 2 DBs you have to use diferent TRIGGERS names every time |example fist add TRIGGERS ('t1','t2','t3') ,secend add TRIGGERS ('t4','t5','t6')

password : is the password which used to encrypt the DB 

Save changes 

3 kinds of operation on an encrypted DB can be saved 

insert

update

and delete 

So when you do any of that operation on DB you have to use this function:

	Sqlite3En.Save_Change_On_EnDB_By_Password(Memory_conn,Orgenal_DB_Name,Orgenal_DB_Table_Name,DB_Path,password = 'password' ,salt = 'a48detSckiYod67f')

Memory_conn: is a sqlite3 connection to in :memory:

Orgenal_DB_Name : is the name of DB befor encrypt

Orgenal_DB_Table_Name : is the name of DB's table befor encrypt

DB_Path : is the path where (.Kn files) are

password : is the password which used to encrypt the DB 

Some examples:

If you want to open 2 encrypted DBs (First.db and Sec.db) :
files of First.db after encrypted  will be :

	First1.Kn
	First2.Kn
	First3.Kn and so on 

All this files must be in one folder alone

	DBfile1/First1.Kn
	DBfile1/First2.Kn
	DBfile1/First3.Kn

Sec.db encrypted files must be in other folder alone too : 

	DBfile2/Sec1.Kn
	DBfile2/Sec2.Kn
	DBfile2/Sec3.Kn
	DBfile2/Sec4.Kn

To open this 2 encrypted DBs :

	Memory_conn = sqlite3.connect(":memory:")
	Sqlite3En.Open_Encrypted_DB_By_Password ('DBfile1\\','First.db','Table_Name1',Memory_conn , password = 'password' )
	Sqlite3En.Add_Encrypted_DB_By_Password ('DBfile2\\','Sec.db','Table_Name2',Memory_conn,'t1','t2','t3', password = 'password' )
	
To insert new value in first DB:

	Memory_conn.execute("INSERT INTO Table_Name1 (ID,NAME,AGE) VALUES (1, 'sam', 35)");
	Memory_conn.commit()

After that you have to save that insert : 

	Sqlite3En.Save_Change_On_EnDB_By_Password(Memory_conn,'First.db','Table_Name1','DBfile1\\',password = 'password' )

To insert value in Sec DB :

	Memory_conn.execute("INSERT INTO Table_Name2 (ID,NAME,AGE) VALUES (1, 'yous', 29)");
	Memory_conn.commit()
	Sqlite3En.Save_Change_On_EnDB_By_Password(Memory_conn,'Sec.db','Table_Name2','DBfile2\\',password = 'password' )


To update value in First DB :

	Memory_conn.execute("UPDATE Table_Name1 set AGE = 36 where ID = 1")
	Memory_conn.commit()
	Sqlite3En.Save_Change_On_EnDB_By_Password(Memory_conn,'First.db','Table_Name1','DBfile1\\',password = 'password' )

To update value in Sec DB :

	Memory_conn.execute("UPDATE Table_Name2 set AGE = 30 where ID = 1")
	Memory_conn.commit()
	Sqlite3En.Save_Change_On_EnDB_By_Password(Memory_conn,'Sec.db','Table_Name2','DBfile2\\',password = 'password' )

To delete value in First DB:

	Memory_conn.execute('DELETE FROM Table_Name1 WHERE ID =1')
	Memory_conn.commit()
	Sqlite3En.Save_Change_On_EnDB_By_Password(Memory_conn,'First.db','Table_Name1','DBfile1\\',password = 'password' )

To delete value in Sec DB :

	Memory_conn.execute('DELETE FROM Table_Name2 WHERE ID =1')
	Memory_conn.commit()
	Sqlite3En.Save_Change_On_EnDB_By_Password(Memory_conn,'Sec.db','Table_Name2','DBfile2\\',password = 'password' )


Notes:
1- Do not close Memory_conn while your program is runing if you close Memory_conn then 
all opened DBs (by Open_Encrypted_DB_By_Password function and Add_Encrypted_DB_By_Password function) 
will be closed too.

2- If you have one DB contain more than one table and you want to encrypt it you have to encrypt each table alone.

For example :

If you want to encrypt DB named MultyTable.db
Which have 2 tables F1Table and F2Table .

To encrypt it copy MultyTable.db into 2 folders:

	F1folder/MultyTable.db
	F2folder/MultyTable.db
	
Rename one of them (here will rename MultyTable.db which is into F2folder) :

	F1folder/MultyTable.db
	F2folder/MultyTableC.db

Then encrypt each table alone:

	Sqlite3En.Encrypt_existing_DB_By_Password ('F1folder\\' , 'MultyTable.db' ,'F1Table' , password = 'password' )
	Sqlite3En.Encrypt_existing_DB_By_Password ('F2folder\\' , 'MultyTableC.db' ,'F2Table' , password = 'password' )

To open:

Remove MultyTable.db and MultyTable2.db from their folders (you have to remember not to mix (.Kn files) with any kind of other files or folders). 

Then:

	Memory_conn = sqlite3.connect(":memory:")
	Sqlite3En.Open_Encrypted_DB_By_Password ('F1folder\\','MultyTable.db','F1Table',Memory_conn , password = 'password' )
	Sqlite3En.Add_Encrypted_DB_By_Password ('F2folder\\','MultyTableC.db','F2Table',Memory_conn,'t1','t2','t3', password = 'password' )

