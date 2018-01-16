import nbformat as nbf
import glob
import shutil
import nb2html

retrieve_name_from_cell = lambda cell_source: cell_source.replace('#','').strip()

def retrieve_name_from_fname(fname):
    nb = nbf.read(open(fname),nbf.current_nbformat)
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            return  retrieve_name_from_cell(cell['source'])
    return 'ERROR'

def get_manual_configuration():
    import yaml
    return yaml.load(open('notebooks/config.yml'))

def get_configuration():
    configuration = []
    for chapter_folder in sorted(glob.glob("notebooks/Chapter_*")):
        all_section_fnames = sorted(glob.glob("%s/*.ipynb"%chapter_folder))
        all_section_info = [
                dict(
                    file_name=fname.rpartition('/')[2],
                    section_name=retrieve_name_from_fname(fname)
                )
            for fname in all_section_fnames]

        chapter_name = all_section_info[0]['section_name']
        configuration.append(dict(
            chapter_name=chapter_name,
            folder_name=chapter_folder[10:],
            sections=all_section_info,
                        ))
    return configuration


#
#
# A function which makes the markdown file for a section
#
#

outline = """{}
------

{{% include "../notebooks-html/{}" %}}
"""

def make_md_file(title,ipynb_name,cold=False):
    filled_outline = outline.format(title,ipynb_name.replace('ipynb','html'))
    if cold:
        print(filled_outline)
        return
    with open('notebooks-md/%s'%(ipynb_name.replace('ipynb','md')),'w') as f:
        f.write(filled_outline)




#
#
# In this section
#  - python notebooks (.ipynb) are moved to "notebooks-flat"
#  - markdown files (.md) are generated for each section in "notebooks-md"
#
#

def copy_into_flat_directory(configuration,cold=False):
    shutil.copy2('notebooks/To_the_Student.ipynb','notebooks-flat/To_the_Student.ipynb')
    make_md_file('To The Student','To_the_Student.ipynb')


    for n,chapter in zip(range(1,len(configuration)+1),configuration):
        for section in chapter['sections']:
            src = ('notebooks/%s/%s'%(chapter['folder_name'],section['file_name']))
            dest = ('notebooks-flat/%d_%s'%(n,section['file_name']))

            ipynb_file = '%d_%s'%(n,section['file_name'])
            make_md_file(section['section_name'],ipynb_file,cold=cold)
            if cold:
                print("Copying from %s to %s"%(src,dest))
            else:
                shutil.copy2(src,dest)

#
#
# In this section
#  - The summary file (SUMMARY.md) is generated
#
#
def generate_summary(configuration,cold=False):
    SUMMARY_head = """
# Summary

* [Authors and License](README.md)
* [To the Student](notebooks-md/To_the_Student.md)

    """

    chapter_summaries = [SUMMARY_head]

    for n,chapter in zip(range(1,len(configuration)+1),configuration):
        chapter_intro_md = chapter['sections'][0]['file_name'].replace('ipynb','md')
        entries = ['* [Chapter %d: %s](notebooks-md/%d_%s)'%(n,chapter['chapter_name'],n,chapter_intro_md)]
        for i,section in list(enumerate(chapter['sections']))[1:]:
            section_md = section['file_name'].replace ('ipynb','md')
            section_entry = ('\t* [%d.%d %s](notebooks-md/%d_%s)'%(n,i,section['section_name'],n,section_md))
            entries.append(section_entry)
        chapter_summaries.append('\n'.join(entries)+'\n')

    SUMMARY_md ="\n".join(chapter_summaries)
    if cold:
        print(SUMMARY_md)
    else:
        with open("SUMMARY.md","w") as f:
            f.write(SUMMARY_md)

if __name__ == "__main__":
    configuration = get_configuration()
    copy_into_flat_directory(configuration,cold=False)
    generate_summary(configuration,cold=False)
    notebook_paths = glob.glob('notebooks-flat/*.ipynb')
    nb2html.convert_notebooks_to_html_partial(notebook_paths)
    print(open("SUMMARY.md",'r').read())
