import yaml
import glob
import shutil
import nb2html


configuration = yaml.load(open('notebooks/config.yml'))
configuration[0]


#
#
# A function which makes the markdown file for a section
#
#

outline = """{}
------

{{% include "../notebooks-html/{}" %}}
"""

def make_md_file(title,ipynb_name):
    filled_outline = outline.format(title,ipynb_name.replace('ipynb','html'))
    with open('notebooks-md/%s'%(ipynb_name.replace('ipynb','md')),'w') as f:
        f.write(filled_outline)




#
#
# In this section
#  - python notebooks (.ipynb) are moved to "notebooks-flat"
#  - markdown files (.md) are generated for each section in "notebooks-md"
#
#


shutil.copy2('notebooks/To_the_Student.ipynb','notebooks-flat/To_the_Student.ipynb')
make_md_file('To The Student','To_the_Student.ipynb')


for n,chapter in zip(range(1,len(configuration)+1),configuration):
    for i,section in enumerate(chapter['sections']):
        src = ('notebooks/%s/%s'%(chapter['folder'],section))
        dest = ('notebooks-flat/%d_%d_%s'%(n,i,section))
        ipynb_file = dest.rpartition('/')[2]
        make_md_file(section[:-6].replace('_',' '),ipynb_file)
        shutil.copy2(src,dest)



#
#
# In this section
#  - The summary file (SUMMARY.md) is generated
#
#

SUMMARY_head = """
# Summary

* [To the Student](notebooks-md/To_the_Student.md)

"""

chapter_summaries = [SUMMARY_head]

for n,chapter in zip(range(1,len(configuration)+1),configuration):
    entries = ['* [Chapter %d: %s](notebooks-md/%d_0_%s)'%(n,chapter['name'],n,chapter['sections'][0].replace('ipynb','md'))]
    for i,section in list(enumerate(chapter['sections']))[1:]:
        section_name = section.partition('.')[0].replace('_',' ')
        section_md = section.replace ('ipynb','md')
        section_entry = ('\t* [%d.%d %s](notebooks-md/%d_%d_%s)'%(n,i,section_name,n,i,section_md))
        entries.append(section_entry)
    chapter_summaries.append('\n'.join(entries)+'\n')

SUMMARY_md ="\n".join(chapter_summaries)
with open("SUMMARY.md","w") as f:
    f.write(SUMMARY_md)

#
#
# In this section
#  - basic html files are generated from "notebooks-flat", and placed in "notebooks-html"
#
#

notebook_paths = glob.glob('notebooks-flat/*.ipynb')
nb2html.convert_notebooks_to_html_partial(notebook_paths)

