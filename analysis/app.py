import warnings
import pymongo
import functions as fn


# myclient = pymongo.MongoClient("mongodb://mongo:27017/") # production
myclient = pymongo.MongoClient("mongodb://localhost:27017/") # development

# specifying the db and column
# mydb = myclient["project6db"] # production
mydb = myclient["testdb"] # development


col = mydb["product"]

# reading example
 
# x = col.find()

dir = "raw_data"

warnings.filterwarnings("ignore")
print('Making files readable: ')
fn.make_all_readable(dir)
print('making imports from csv :')
x = fn.import_dataframes(dir)
print('making correct dates :')
x = fn.fix_date_time(x)
print('making df into tree 1 :')
x = fn.df_to_tree(x)
print('making tree 1 into tree 2 :')
x = fn.tree_add_date_branches(x)
print('making analysis :')
x = fn.analyze_logs(x)
print('making export dictionary :')
x = fn.export_dict(x)
print('Writing to DataBase :')
col.insert_one(x)
print('Deleting generated file : ')
fn.remove_files(dir)
print('Done!')



