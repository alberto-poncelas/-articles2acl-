
import os
from os import listdir


#get Proceedings pdf
main_pdf = [f for f in listdir(".") if f[-4:]==".pdf"][0]


#load the file with the index of the papers
f = open("list", "r")
lines=f.readlines()



#load the metadata of the first and last (real) pages
os.system("pdftk "+main_pdf+" dump_data_utf8| grep -e ^BookmarkPageNumber | head -1 > meta_pages")
os.system("pdftk "+main_pdf+" dump_data_utf8| grep -e ^BookmarkPageNumber | tail -1 >> meta_pages")

params_file = open("meta_pages", "r")
params=params_file.readlines()
first_page=int(params[0].strip().split(" ")[-1])
last_page=int(params[1].strip().split(" ")[-1])


#load metadata
meta_file = open("meta", "r")
meta=meta_file.readlines()
meta_parameters=dict([x.strip().split(" ", 1) for x in meta])
abbrev=meta_parameters["abbrev"]
year=meta_parameters["year"]



print("Metadata: ")
print("main_pdf "+str(main_pdf))
print("abbrev "+str(abbrev))
print("year "+str(year))
print("first page "+str(first_page))
print("last page "+str(last_page))



f_accepted = open("accepted", "w")
f_submission = open("submissions", "w")


dist=first_page-int(lines[0].split("\t")[2].strip())
pages_ini=[int(p.split("\t")[2].strip())+dist for p in lines]
pages_fin=[x-1 for x in pages_ini[1:]+[last_page]]


os.system("rm -r pdf")
os.system("mkdir pdf")


meta_command="cp "+main_pdf+" pdf/"+abbrev+"_"+year+".pdf"
os.system(meta_command)



cut_command="pdftk "+main_pdf+" cat "+str(1)+"-"+str(first_page-1)+"  output pdf/"+abbrev+"_"+year+"_frontmatter.pdf"
os.system(cut_command)


i=0
for row in lines:
	i=i+1
	paper_number=str(i)
	row_splited=row.strip().split("\t")
	authors=row_splited[0]
	title=row_splited[1]
	page_in= pages_ini[i-1] #i has been increased already
	page_fin= pages_fin[i-1]
	cut_command="pdftk "+main_pdf+" cat "+str(page_in)+"-"+str(page_fin)+"  output pdf/"+abbrev+"_"+year+"_paper_"+paper_number+".pdf"
	os.system(cut_command)
	print (cut_command)
	accepted_row=paper_number+"\t"+title+"\t"+"SCORE"+"\t"+"ACCEPT"+"\n"
	submission_row=paper_number+"\t"+authors+"\t"+title+"\t"+"OK"+"\t"+"DATE"+"\n"
	f_accepted.write(accepted_row)
	f_submission.write(submission_row)

f_accepted.close()
f_submission.close()

