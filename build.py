print("building static site generator")

top_template = open('./templates/top.html').read()

bottom_template = open('./templates/bottom.html').read()

middle_content = open('./content/index.html').read() 
combined_index = top_template + middle_content + bottom_template 
open('./docs/index.html', 'w+').write(combined_index)


middle_content = open('./content/resume.html').read()
combined_resume = top_template + middle_content + bottom_template 
open('./docs/resume.html', 'w+').write(combined_resume)

middle_content = open('./content/projects.html').read()
combined_projects = top_template + middle_content + bottom_template 
open('./docs/projects.html', 'w+').write(combined_projects)